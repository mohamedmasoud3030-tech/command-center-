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


    def test_pr_api_denial_is_visible_in_markdown_not_empty_success(self):
        def denied_pr_list(url, headers):
            if "/pulls?" in url:
                raise HTTPError(url, 403, "rate limited", {}, None)
            return self.fake_fetch(url, headers)

        result = portfolio.project_snapshot("example", "Example", "example", {}, denied_pr_list)
        rendered = portfolio.render_markdown({"checked_at": "2026-11-04T00:00:00Z", "projects": [result]})
        self.assertEqual(result["state"], "verified")
        self.assertEqual(result["pr_observation"]["state"], "not-verified")
        self.assertIn("PRs NOT VERIFIED", rendered)
        self.assertNotIn("none observed", rendered)

    def test_branch_api_denial_is_visible_in_markdown(self):
        def denied_branch(url, headers):
            if "/branches/" in url:
                raise HTTPError(url, 403, "rate limited", {}, None)
            if "/pulls?" in url:
                return []
            return self.fake_fetch(url, headers)

        result = portfolio.project_snapshot("example", "Example", "example", {}, denied_branch)
        rendered = portfolio.render_markdown({"checked_at": "2026-11-04T00:00:00Z", "projects": [result]})
        self.assertEqual(result["branch_observation"]["state"], "not-verified")
        self.assertIn("HEAD NOT VERIFIED", rendered)
        self.assertIn("none observed", rendered)  # PR list was independently verified.

    def test_first_page_of_hundred_prs_is_marked_partial(self):
        def first_page(url, headers):
            if "/pulls?" in url:
                return [
                    {"number": i, "title": "Open", "draft": False, "state": "open",
                     "head": {"sha": "head", "ref": "work"}, "base": {"ref": "main"},
                     "updated_at": "now", "html_url": f"https://github.com/owner/pr/{i}"}
                    for i in range(1, 101)
                ]
            if "/check-runs?" in url:
                return {"check_runs": []}
            return self.fake_fetch(url, headers)

        result = portfolio.project_snapshot("example", "Example", "example", {}, first_page)
        rendered = portfolio.render_markdown({"checked_at": "2026-11-04T00:00:00Z", "projects": [result]})
        self.assertEqual(len(result["open_prs"]), 100)
        self.assertEqual(result["pr_observation"]["state"], "partial")
        self.assertIn("PARTIAL", rendered)

    def test_empty_verified_pr_list_is_allowed_to_say_none_observed(self):
        def no_prs(url, headers):
            if "/pulls?" in url:
                return []
            return self.fake_fetch(url, headers)

        result = portfolio.project_snapshot("example", "Example", "example", {}, no_prs)
        rendered = portfolio.render_markdown({"checked_at": "2026-11-04T00:00:00Z", "projects": [result]})
        self.assertEqual(result["pr_observation"]["state"], "verified")
        self.assertIn("none observed", rendered)

if __name__ == "__main__":
    unittest.main()
