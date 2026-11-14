import json
import subprocess
import sys
import tempfile
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_external_links import check_link, collect_links, report_markdown
class TestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/canonical", "/changed"):
            self.send_response(302)
            self.send_header("Location", "/canonical/" if self.path == "/canonical" else "/ok")
        elif self.path in ("/ok", "/ok/", "/canonical/"):
            self.send_response(200)
        elif self.path == "/limited":
            self.send_response(403)
        else:
            self.send_response(404)
        self.end_headers()
    def log_message(self, format, *args):
        pass
class ExternalLinkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), TestHandler)
        cls.thread = Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"
    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()
    def test_generated_html_collection_and_deduplication(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "index.html").write_text(f'<a href="{self.base}/ok#one">One</a><a href="{self.base}/ok#two">Two</a><a href="https://site.example/contact/">Internal</a><a href="mailto:x@example.org">Email</a>', encoding="utf-8")
            refs, pages = collect_links(root, "https://site.example")
            self.assertEqual(pages, 1)
            self.assertEqual(dict(refs), {self.base + "/ok": {"/"}})
    def test_http_outcomes_and_redirects(self):
        outcomes = {path: check_link((self.base + path, {"/history/"})) for path in ("/ok", "/missing", "/limited", "/canonical", "/changed")}
        self.assertEqual(outcomes["/ok"]["outcome"], "OK")
        self.assertEqual(outcomes["/missing"]["outcome"], "Not found")
        self.assertEqual(outcomes["/limited"]["outcome"], "Access limited")
        self.assertFalse(outcomes["/canonical"]["unexpected_redirect"])
        self.assertTrue(outcomes["/changed"]["unexpected_redirect"])
        report = report_markdown(list(outcomes.values()), 2, "2026-11-14 00:00 UTC")
        self.assertIn("References requiring review: 3", report)
        self.assertIn("No website references were changed", report)
        self.assertIn("/history/", report)
    def test_cli_writes_markdown_and_json(self):
        with tempfile.TemporaryDirectory() as temp:
            site = Path(temp) / "site"
            output = Path(temp) / "report"
            site.mkdir()
            (site / "index.html").write_text(f'<a href="{self.base}/missing">Citation</a>', encoding="utf-8")
            subprocess.run([sys.executable, str(Path(__file__).resolve().parents[1] / "scripts" / "check_external_links.py"), str(site), str(output), "https://site.example"], check=True, capture_output=True, text=True)
            self.assertIn("Not found", (output / "report.md").read_text(encoding="utf-8"))
            data = json.loads((output / "report.json").read_text(encoding="utf-8"))
            self.assertEqual(data["links"][0]["pages"], ["/"])
if __name__ == "__main__":
    unittest.main()
