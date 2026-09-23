import copy
import importlib.util
from pathlib import Path
import unittest
import tempfile
import contextlib
import io
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("sync", Path(__file__).resolve().parents[1] / "scripts/sync_notion_indicadores.py")
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.row = dict(title="Recurso", authors="Autora", publisher=None, date=None,
                        tags=["México"], url="https://example.org/recurso", notion_page_url=None,
                        source="Notion", status="activo", last_updated="2026-01-01")

    def test_preserves_local_enrichment_and_reports_clearing(self):
        local = dict(self.row, publisher="Edición curada", notes="Conservar")
        remote = dict(self.row, authors=None, tags=[])
        rows, report = sync.merge([local], [remote], "2026-09-23")
        self.assertEqual(rows, [local])
        self.assertEqual({c["field"] for c in report["conflicts"]}, {"authors", "publisher", "tags"})

    def test_missing_records_are_kept(self):
        rows, report = sync.merge([self.row], [], "2026-09-23")
        self.assertEqual(rows, [self.row])
        self.assertEqual(report["missing"], ["Recurso"])

    def test_fill_and_repeat_is_idempotent(self):
        remote = dict(self.row, publisher="Editorial", notion_page_url="https://www.notion.so/" + "a" * 32)
        rows, report = sync.merge([self.row], [remote], "2026-09-23")
        self.assertEqual(rows[0]["publisher"], "Editorial")
        self.assertEqual(rows[0]["last_updated"], "2026-09-23")
        repeated, report = sync.merge(rows, [remote], "2026-09-24")
        self.assertEqual(rows, repeated)
        self.assertEqual(report["updated"], [])

    def test_page_identity_preserves_changed_url(self):
        local = dict(self.row, notion_page_url="https://www.notion.so/" + "a" * 32)
        remote = dict(local, url="https://example.org/new")
        rows, report = sync.merge([local], [remote], "2026-09-23")
        self.assertEqual(rows, [local])
        self.assertEqual(report["conflicts"][0]["field"], "url")

    def test_duplicate_and_unsafe_urls_fail(self):
        with self.assertRaises(ValueError):
            sync.merge([], [self.row, copy.deepcopy(self.row)], "2026-09-23")
        with self.assertRaises(ValueError):
            sync.merge([], [dict(self.row, url="javascript:alert(1)")], "2026-09-23")

    def test_pagination(self):
        source = "a" * 32
        with patch.object(sync, "request_notion", side_effect=[
            {"data_sources": [{"id": source}]},
            {"results": [{"id": "one"}], "has_more": True, "next_cursor": "next"},
            {"results": [{"id": "two"}], "has_more": False},
        ]) as request:
            self.assertEqual(len(sync.query_notion("secret", "b" * 32)), 2)
            self.assertEqual(request.call_args.args[2]["start_cursor"], "next")

    def test_ambiguous_sources_fail(self):
        with patch.object(sync, "request_notion", return_value={"data_sources": [{"id": "a" * 32}, {"id": "b" * 32}]}):
            with self.assertRaises(ValueError):
                sync.query_notion("secret", "c" * 32)

    def test_property_mapping(self):
        page = {"id": "a" * 32, "last_edited_time": "2026-09-22T00:00:00Z", "properties": {
            "Artículo": {"type": "title", "title": [{"plain_text": "Título"}]},
            "Tags": {"type": "multi_select", "multi_select": [{"name": "México"}]},
            "URL": {"type": "url", "url": "https://example.org"}}}
        row = sync.from_page(page)
        self.assertEqual(row["title"], "Título")
        self.assertEqual(row["tags"], ["México"])
        self.assertEqual(row["authors"], None)
        sync.validate([row])

    def test_dry_run_and_invalid_input_leave_file_unchanged(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "catalog.yml"
            output.write_text(sync.yaml.safe_dump({"resources": [self.row]}), encoding="utf-8")
            before = output.read_bytes()
            with patch.dict(sync.os.environ, {"NOTION_TOKEN": "test", "NOTION_DATABASE_ID": "a" * 32}), patch.object(sync, "query_notion", return_value=[{}]), patch.object(sync, "from_page", return_value=dict(self.row, publisher="Nueva")), patch.object(sync.sys, "argv", ["sync", "--output", str(output), "--dry-run"]), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(sync.main(), 0)
            self.assertEqual(before, output.read_bytes())
            with patch.dict(sync.os.environ, {"NOTION_TOKEN": "test", "NOTION_DATABASE_ID": "a" * 32}), patch.object(sync, "query_notion", side_effect=ValueError("Consulta fallida")), patch.object(sync.sys, "argv", ["sync", "--output", str(output)]), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(sync.main(), 1)
            self.assertEqual(before, output.read_bytes())


if __name__ == "__main__":
    unittest.main()
