#!/usr/bin/env python3
"""Read-only live portfolio/PR snapshot from GitHub's public API.

This tool is deliberately a reporter, not a second status database. It uses
the canonical repository map documented in PROJECTS.md and prints fresh facts;
it never edits files, branches, PRs, or hosted data. A 404/403 is reported as NOT VERIFIED,
never as proof that a project or repository does not exist.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
import sys
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

OWNER = "mohamedmasoud3030-tech"
API_ROOT = "https://api.github.com"

# This is the canonical portfolio map used by the human registry. The output is
# a live observation, not a copy of project status. Private/unlisted slugs stay
# visible as NOT VERIFIED until the owner supplies access or corrects the slug.
PROJECTS = (
    ("lena-beauty", "LenaBeauty", "larabeauty-"),
    ("lena-dress-roomshow", "LENA Dress Roomshow", "carmen-gallery-"),
    ("lena-supply", "LENA SUPPLY", "Lenastore"),
    ("digital-house", "LENA Digital House", "platform"),
    ("nile-systems", "Nile Systems", "nilesys"),
    ("malek", "MALEK", "malek"),
    ("terranex", "Terranex", "Terranex"),
    ("hospitality", "Hospitality Ops", "starting"),
    ("kiyyal", "Kiyyal", "kiyyal"),
    ("mosaid", "Mosaid", "mosaid"),
    ("command-center", "Command Center", "command-center-"),
)

Json = dict[str, Any]
Fetcher = Callable[[str, dict[str, str]], Any]


def api_url(path: str) -> str:
    return f"{API_ROOT}/repos/{OWNER}/{path.lstrip('/')}"


def fetch_json(url: str, headers: dict[str, str]) -> Any:
    request = Request(url, headers=headers)
    with urlopen(request, timeout=20) as response:  # noqa: S310 - fixed GitHub API host
        return json.loads(response.read().decode("utf-8"))


def observed_get(url: str, headers: dict[str, str], fetch: Fetcher = fetch_json) -> tuple[Json | None, Json]:
    try:
        payload = fetch(url, headers)
        if not isinstance(payload, dict):
            raise ValueError("expected an object")
        return payload, {"state": "verified", "source": url}
    except HTTPError as error:
        return None, {
            "state": "not-verified",
            "source": url,
            "reason": f"GitHub API returned HTTP {error.code}; repository may be private, renamed, or inaccessible",
        }
    except (OSError, URLError, TimeoutError, ValueError) as error:
        return None, {"state": "not-verified", "source": url, "reason": str(error)}


def project_snapshot(key: str, label: str, slug: str, headers: dict[str, str], fetch: Fetcher = fetch_json) -> Json:
    repo = f"{OWNER}/{slug}"
    repo_url = api_url(slug)
    data, meta = observed_get(repo_url, headers, fetch)
    result: Json = {"key": key, "label": label, "repository": repo, **meta}
    if data is None:
        result["open_prs"] = []
        return result

    default_branch = data.get("default_branch")
    result.update({
        "default_branch": default_branch,
        "visibility": data.get("visibility"),
        "archived": data.get("archived"),
        "updated_at": data.get("updated_at"),
        "pushed_at": data.get("pushed_at"),
    })
    if isinstance(default_branch, str) and default_branch:
        branch_url = api_url(f"{slug}/branches/{default_branch}")
        branch, branch_meta = observed_get(branch_url, headers, fetch)
        result["default_sha"] = branch.get("commit", {}).get("sha") if branch else None
        result["branch_observation"] = branch_meta

    prs_url = api_url(f"{slug}/pulls?state=open&per_page=100")
    try:
        raw_prs = fetch(prs_url, headers)
        if not isinstance(raw_prs, list):
            raise ValueError("expected a PR array")
        result["open_prs"] = [
            {
                "number": pr.get("number"),
                "title": pr.get("title"),
                "draft": pr.get("draft"),
                "state": pr.get("state"),
                "head": pr.get("head", {}).get("sha"),
                "branch": pr.get("head", {}).get("ref"),
                "base": pr.get("base", {}).get("ref"),
                "updated_at": pr.get("updated_at"),
                "url": pr.get("html_url"),
                "checks": [],
            }
            for pr in raw_prs
        ]
        for pr_item in result["open_prs"]:
            head = pr_item.get("head")
            if not head:
                continue
            checks_url = api_url(f"{slug}/commits/{head}/check-runs?per_page=100")
            try:
                checks_payload = fetch(checks_url, headers)
                if not isinstance(checks_payload, dict):
                    raise ValueError("expected a check-runs object")
                pr_item["checks"] = [
                    {
                        "name": check.get("name"),
                        "status": check.get("status"),
                        "conclusion": check.get("conclusion"),
                        "completed_at": check.get("completed_at"),
                        "url": check.get("details_url") or check.get("html_url"),
                    }
                    for check in checks_payload.get("check_runs", [])
                ]
            except (HTTPError, OSError, URLError, TimeoutError, ValueError, AttributeError) as error:
                pr_item["checks_observation"] = {
                    "state": "not-verified", "source": checks_url, "reason": str(error)
                }
    except (HTTPError, OSError, URLError, TimeoutError, ValueError, AttributeError) as error:
        result["open_prs"] = []
        result["pr_observation"] = {"state": "not-verified", "source": prs_url, "reason": str(error)}
    return result


def snapshot(headers: dict[str, str], fetch: Fetcher = fetch_json) -> Json:
    checked_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    return {
        "schema": "command-center-portfolio-live-v1",
        "checked_at": checked_at,
        "source": API_ROOT,
        "read_only": True,
        "projects": [project_snapshot(*project, headers, fetch) for project in PROJECTS],
    }


def render_markdown(data: Json) -> str:
    lines = [
        "# Live portfolio snapshot",
        "",
        f"> Checked at `{data['checked_at']}` from GitHub API. This is an observation, not a committed status database.",
        "> `NOT VERIFIED` means the API did not prove the fact; it is not a claim that the repository is absent.",
        "",
        "| Project | Repository | Default branch/SHA | Open PRs | State |",
        "|---|---|---|---|---|",
    ]
    for item in data["projects"]:
        if item["state"] != "verified":
            lines.append(f"| {item['label']} | `{item['repository']}` | — | — | **NOT VERIFIED** — {item['reason']} |")
            continue
        branch = item.get("default_branch", "—")
        sha = str(item.get("default_sha") or "—")[:12]
        prs = item.get("open_prs", [])
        pr_parts = []
        for pr in prs:
            checks = pr.get("checks", [])
            check_text = ""
            if checks:
                check_text = " [" + ", ".join(
                    f"{check['name']}={check['conclusion'] or check['status']}" for check in checks
                ) + "]"
            elif "checks_observation" in pr:
                check_text = " [checks NOT VERIFIED]"
            pr_parts.append(f"[#{pr['number']}]({pr['url']}){' draft' if pr['draft'] else ''}{check_text}")
        pr_text = ", ".join(pr_parts) or "none observed"
        lines.append(f"| {item['label']} | `{item['repository']}` | `{branch}@{sha}` | {pr_text} | verified at API |")
    lines.extend([
        "",
        "## Operating interpretation",
        "",
        "- GitHub is the live source for branch/PR state; this output does not overwrite `PROJECTS.md`.",
        "- A draft/open PR is unfinished work, not an active session reservation.",
        "- A skipped check, inaccessible repository, or missing credential remains unverified.",
    ])
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit JSON instead of the human report")
    parser.add_argument("--token-env", default="GITHUB_TOKEN", help="environment variable for an optional API token")
    args = parser.parse_args(argv)
    token = os.environ.get(args.token_env)
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "command-center-portfolio-report"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    data = snapshot(headers)
    sys.stdout.write(json.dumps(data, ensure_ascii=False, indent=2) + "\n" if args.json else render_markdown(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
