#!/usr/bin/env python3
"""
ماسح جرد المحفظة (read-only) — يعيد بناء صورة الواقع في أي وقت.
الاستخدام:
  export GH_TOKEN=...      # مفتاح قراءة GitHub
  python3 tools/inventory-scan.py
الناتج: data/inventory-<تاريخ>.json + ملخص في الطرفية.
لا يغيّر أي شيء في المستودعات — قراءة فقط.
"""
import json, os, sys, time, hashlib, urllib.request, urllib.parse
from collections import Counter

OWNER = os.environ.get("PORTFOLIO_OWNER", "mohamedmasoud3030-tech")
T = os.environ.get("GH_TOKEN", "").strip()
if not T:
    sys.exit("ضع GH_TOKEN في البيئة أولاً (مفتاح قراءة فقط يكفي)")

def gh(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": "portfolio-inventory", "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {T}"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read()

SKIP = ("node_modules/","vendor/",".git/","dist/","build/",".next/","coverage/","out/",
        "target/",".venv/","__pycache__/",".turbo/",".cache/")
DOC_EXT = (".md", ".mdx", ".txt", ".rst")
AGENT_HINTS = ("agents.md","claude.md","gemini.md","copilot-instructions.md",".cursorrules",
               ".cursor/",".claude/",".agents/",".github/instructions/","skill")

today = time.strftime("%Y-%m-%d")
inv = {"generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "repos": []}

repos = json.loads(gh(f"https://api.github.com/user/repos?per_page=100&sort=pushed&affiliation=owner"))
repos = [r for r in repos if isinstance(r, dict) and r["full_name"].startswith(OWNER + "/") and r["name"] != "command-center-"]

for r in repos:
    full, br = r["full_name"], r.get("default_branch", "main")
    it = {"full_name": full, "visibility": r["visibility"], "description": r.get("description"),
          "language": r.get("language"), "pushed_at": r.get("pushed_at"), "default_branch": br}
    try:
        tree = json.loads(gh(f"https://api.github.com/repos/{full}/git/trees/{urllib.parse.quote(br)}?recursive=1"))
        files = [e for e in tree.get("tree", []) if e.get("type") == "blob"
                 and not any(s in e["path"].lower() for s in SKIP)]
        it.update({
            "files_total": len(files),
            "docs": [{"path": e["path"], "size": e.get("size", 0)} for e in files if e["path"].lower().endswith(DOC_EXT)],
            "agent_files": sorted({e["path"] for e in files if any(h in e["path"].lower() for h in AGENT_HINTS)}),
            "skills": sorted({e["path"].split("/")[-2] for e in files if e["path"].endswith("/SKILL.md")}),
            "env_files": [e["path"] for e in files if e["path"].split("/")[-1].startswith(".env")],
            "workflows": [e["path"] for e in files if e["path"].startswith(".github/workflows/")],
            "tree_truncated": tree.get("truncated", False)})
    except Exception as ex:
        it["error"] = str(ex)
    inv["repos"].append(it)
    print("scanned", full, file=sys.stderr)

out = os.path.join(os.path.dirname(__file__), "..", "data", f"inventory-{today}.json")
json.dump(inv, open(out, "w"), ensure_ascii=False, indent=1)
print(f"\n✅ saved {out}")
for it in inv["repos"]:
    print(f"  {it['full_name']:45s} docs={len(it.get('docs', [])):3d} skills={len(it.get('skills', [])):2d} env={len(it.get('env_files', []))}")
