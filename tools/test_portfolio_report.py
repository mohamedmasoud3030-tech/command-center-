import importlib.util
from pathlib import Path
import unittest
from urllib.error import HTTPError


SPEC = importlib.util.spec_from_file_location("portfolio_report", Path(__file__).with_name("portfolio_report.py"))
portfolio = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(portfolio)


class PortfolioReportTests(unittest.TestCase):
    def fake_fetch(self, url, _headers):
        if url.endswith("/repos/mohamedmasoud3030-tech/example"):
            return {"default_branch": "main", "visibility": "public", "archived": False, "updated_at": "now", "pushed_at": "now"}
        if url.endswith("/repos/mohamedmasoud3030-tech/example/branches/main"):
            return {"commit": {"sha": "abc123"}}
        if "/pulls?" in url:
            return [{
                "number": 7,
                "title": "Draft work",
                "draft": True,
                "state": "open",
                "head": {"sha": "def456", "ref": "task/example"},
                "base": {"ref": "main"},
                "updated_at": "now",
                "html_url": "https://github.com/example/pr/7",
            }]
        if "/check-runs?" in url:
            return {"check_runs": [{
                "name": "tests", "status": "completed", "conclusion": "success",
                "completed_at": "now", "html_url": "https://github.com/example/checks/1",
            }]}
        raise AssertionError(f"unexpected URL: {url}")

    def test_verified_repository_includes_branch_and_open_pr(self):
        result = portfolio.project_snapshot(
            "example", "Example", "example", {}, self.fake_fetch
        )
        self.assertEqual(result["state"], "verified")
        self.assertEqual(result["default_sha"], "abc123")
        self.assertEqual(result["open_prs"][0]["number"], 7)
        self.assertTrue(result["open_prs"][0]["draft"])
        self.assertEqual(result["open_prs"][0]["checks"][0]["conclusion"], "success")

    def test_inaccessible_repository_is_not_called_missing(self):
        def denied(url, _headers):
            raise HTTPError(url, 404, "not found", {}, None)

        result = portfolio.project_snapshot("private", "Private", "private", {}, denied)
        self.assertEqual(result["state"], "not-verified")
        self.assertIn("may be private", result["reason"])
        self.assertEqual(result["open_prs"], [])

    def test_markdown_preserves_not_verified_state(self):
        data = {
            "checked_at": "2026-11-04T00:00:00Z",
            "projects": [{
                "label": "Private", "repository": "owner/private", "state": "not-verified",
                "reason": "HTTP 404; may be private",
            }],
        }
        output = portfolio.render_markdown(data)
        self.assertIn("NOT VERIFIED", output)
        self.assertNotIn("verified at API", output)


if __name__ == "__main__":
    unittest.main()
