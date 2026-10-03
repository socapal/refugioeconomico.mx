#!/usr/bin/env python3
"""Importación conservadora de recursos de vivienda. No ejecuta operaciones Git."""
import argparse
import copy
import csv
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import time
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
from uuid import UUID

import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE_URL = "https://app.notion.com/p/928c729a501f4bb6b2f810dce59e1cf1?pvs=21"
FIELDS = {"title": "Artículo", "authors": "Autoría", "publisher": "Casa editora",
          "date": "Date", "tags": "Tags", "url": "URL",
          "source": "source", "status": "status", "last_updated": "last_updated"}


def request_notion(token, path, payload=None):
    request = Request("https://api.notion.com/v1/" + path,
                      data=json.dumps(payload).encode() if payload is not None else None,
                      headers={"Authorization": "Bearer " + token,
                               "Notion-Version": "2025-09-03",
                               "Content-Type": "application/json"})
    for attempt in range(4):
        try:
            with urlopen(request, timeout=30) as response:
                return json.load(response)
        except HTTPError as error:
            if (error.code == 429 or error.code >= 500) and attempt < 3:
                time.sleep(min(float(error.headers.get("Retry-After", 2 ** attempt)), 30))
                continue
            raise ValueError(f"Notion HTTP {error.code}; revise permisos, ID y token.") from None


def query_notion(token, database_id, data_source_id=None):
    database_id = str(UUID(database_id))
    database = request_notion(token, "databases/" + database_id)
    sources = database.get("data_sources", [])
    if data_source_id:
        data_source_id = str(UUID(data_source_id))
        if data_source_id not in [str(UUID(s["id"])) for s in sources]:
            raise ValueError("NOTION_DATA_SOURCE_ID no pertenece a la base indicada.")
    elif len(sources) == 1:
        data_source_id = sources[0]["id"]
    else:
        raise ValueError("La base no tiene una única fuente; configure NOTION_DATA_SOURCE_ID.")
    pages, cursor, seen = [], None, set()
    while True:
        payload = {"page_size": 100}
        if cursor:
            payload["start_cursor"] = cursor
        batch = request_notion(token, f"data_sources/{data_source_id}/query", payload)
        pages.extend(batch["results"])
        if not batch.get("has_more"):
            return pages
        cursor = batch.get("next_cursor")
        if not cursor or cursor in seen:
            raise ValueError("Paginación incompleta; no se escribirá el YAML.")
        seen.add(cursor)


def property_value(prop):
    kind = prop.get("type")
    value = prop.get(kind)
    if kind in ("title", "rich_text"):
        return "".join(v.get("plain_text", v.get("text", {}).get("content", "")) for v in value)
    if kind == "multi_select":
        return [v["name"] for v in value]
    if kind in ("select", "status"):
        return value["name"] if value else None
    if kind == "date":
        return value["start"] if value else None
    if kind == "people":
        return "; ".join(v.get("name", "") for v in value)
    if kind in ("url", "last_edited_time", "created_time"):
        return value
    raise ValueError(f"Tipo de propiedad no soportado: {kind}; adapte el mapeo antes de importar.")


def from_page(page):
    props = page["properties"]
    row = {}
    for field, label in FIELDS.items():
        prop = props.get(label, props.get(field))
        row[field] = property_value(prop) if prop else None
    if isinstance(row["tags"], str):
        row["tags"] = [t.strip() for t in row["tags"].split(",") if t.strip()]
    row["tags"] = row["tags"] or []
    row["notion_page_url"] = page.get("url") or "https://www.notion.so/" + page["id"].replace("-", "")
    row["source"] = row["source"] or "Notion"
    row["status"] = row["status"] or "activo"
    # Fecha de modificación del catálogo, no la fecha editorial del recurso.
    row["last_updated"] = row["last_updated"] or page.get("last_edited_time", "")[:10] or None
    return row


def from_csv(path):
    months = {name: i + 1 for i, name in enumerate(
        "January February March April May June July August September October November December".split())}
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not set(list(FIELDS.values())[:6]).issubset(reader.fieldnames or []):
            raise ValueError("El CSV no contiene las seis columnas esperadas.")
        rows = []
        for raw in reader:
            row = {field: raw[label].strip() or None for field, label in list(FIELDS.items())[:6]}
            if row["date"]:
                month, day, year = row["date"].replace(",", "").split()
                row["date"] = datetime(int(year), months[month], int(day)).date().isoformat()
            row["title"] = " ".join((row["title"] or "").split())
            row["tags"] = [t.strip() for t in (row["tags"] or "").split(",") if t.strip()]
            row.update(notion_page_url=None, source="Notion (exportación CSV)", status="activo", last_updated=None)
            rows.append(row)
        return rows


def page_id(url):
    match = re.search(r"([0-9a-f]{32})$", urlsplit(url or "").path.replace("-", ""), re.I)
    return match[1].lower() if match else None


def validate(rows):
    if not isinstance(rows, list):
        raise ValueError("resources debe ser una lista.")
    ids, urls = set(), set()
    for row in rows:
        if not isinstance(row, dict) or not row.get("title") or not row.get("url"):
            raise ValueError("Cada recurso requiere title y url; no se escribirá el YAML.")
        for field in ("url", "notion_page_url"):
            if row.get(field):
                parsed = urlsplit(row[field])
                if parsed.scheme not in ("http", "https") or not parsed.netloc:
                    raise ValueError(f"Enlace inválido en {field}: {row['title']}")
        if not isinstance(row.get("tags"), list):
            raise ValueError("tags debe ser una lista.")
        identity = page_id(row.get("notion_page_url"))
        if row["url"] in urls or (identity and identity in ids):
            raise ValueError("Identidad o URL duplicada; revise los registros antes de importar.")
        urls.add(row["url"])
        if identity:
            ids.add(identity)


def merge(existing, incoming, today):
    validate(existing)
    validate(incoming)
    result = copy.deepcopy(existing)
    report = {"added": [], "updated": [], "conflicts": [], "missing": []}
    seen = set()
    for new in incoming:
        identity = page_id(new.get("notion_page_url"))
        matches = [i for i, old in enumerate(existing)
                   if (identity and page_id(old.get("notion_page_url")) == identity)
                   or old["url"] == new["url"]]
        if len(matches) > 1 or (matches and matches[0] in seen):
            raise ValueError("Coincidencia ambigua; resuelva las identidades manualmente.")
        if not matches:
            new = copy.deepcopy(new)
            new["last_updated"] = today
            result.append(new)
            report["added"].append(new["title"])
            continue
        index = matches[0]
        seen.add(index)
        old = result[index]
        changed = []
        for field, value in new.items():
            if field == "last_updated":
                continue
            if old.get(field) in (None, "", []):
                if value not in (None, "", []):
                    old[field] = value
                    changed.append(field)
            elif old[field] != value:
                report["conflicts"].append({"title": old["title"], "field": field,
                                            "kept": old[field], "notion": value})
        if changed:
            old["last_updated"] = today
            report["updated"].append({"title": old["title"], "fields": changed})
    report["missing"] = [r["title"] for i, r in enumerate(existing) if i not in seen]
    validate(result)
    return result, report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, help="Importación inicial sin credenciales")
    parser.add_argument("--output", type=Path, default=ROOT / "_data/indicadores_vivienda.yml")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--summary", type=Path, help="Resumen JSON de cambios y advertencias")
    args = parser.parse_args()
    today = datetime.now(timezone.utc).date().isoformat()
    try:
        if args.csv:
            incoming = from_csv(args.csv)
        else:
            token, database_id = os.getenv("NOTION_TOKEN"), os.getenv("NOTION_DATABASE_ID")
            if not token or not database_id:
                raise ValueError("Defina NOTION_TOKEN y NOTION_DATABASE_ID en el entorno.")
            incoming = [from_page(p) for p in query_notion(token, database_id, os.getenv("NOTION_DATA_SOURCE_ID"))
                        if not p.get("archived") and not p.get("in_trash")]
        document = yaml.safe_load(args.output.read_text(encoding="utf-8")) if args.output.exists() else {
            "title": "Indicadores e informes sobre la vivienda", "source_url": SOURCE_URL,
            "last_updated": today, "resources": []}
        if not isinstance(document, dict) or "resources" not in document:
            raise ValueError("Estructura YAML inválida.")
        rows, report = merge(document["resources"], incoming, today)
        changed = rows != document["resources"]
        if changed:
            document["resources"] = rows
            document["last_updated"] = today
        report["dry_run"] = args.dry_run
        print(json.dumps(report, ensure_ascii=False, indent=2))
        if report["conflicts"] or report["missing"]:
            print("ADVERTENCIA: se conservaron valores locales y registros ausentes; revise el resumen.", file=sys.stderr)
        if args.summary:
            args.summary.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if changed and not args.dry_run:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            # Reemplazo atómico únicamente después de validar toda la respuesta.
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=args.output.parent,
                                             delete=False, suffix=".tmp") as stream:
                yaml.safe_dump(document, stream, allow_unicode=True, sort_keys=False, width=110)
                temp = Path(stream.name)
            try:
                temp.replace(args.output)
            finally:
                temp.unlink(missing_ok=True)
        return 0
    except (ValueError, KeyError, TypeError, OSError, yaml.YAMLError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
