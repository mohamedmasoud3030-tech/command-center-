#!/usr/bin/env python3
"""Portfolio skill contract gate (stdlib only; not an agent-behaviour test).

Checks canonical metadata, manually curated positive/near-miss canary definitions,
and optional byte-for-byte parity of downstream shared skill copies.
"""
import argparse
import json
from pathlib import Path
import re

NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", re.S)


def metadata(contents):
    match = FRONTMATTER.match(contents)
    if not match:
        raise ValueError("missing YAML frontmatter")
    result = {}
    for key in ("name", "description"):
        line = re.search(rf"^{key}:[ \t]*(.+)$", match.group(1), re.M)
        if not line:
            raise ValueError(f"missing {key}")
        value = line.group(1).strip().strip('"\'')
        if not value or value in ("|", ">"):
            raise ValueError(f"empty or unsupported multiline {key}")
        result[key] = value
    return result


def audit(root, cases_path=None, downstream=None, required=()):
    root = Path(root)
    errors, notices = [], []
    master = root / "skills"
    skills = sorted(master.glob("*/SKILL.md"))
    if not skills:
        return ["no skills/*/SKILL.md found"], [], 0

    names = set()
    for path in skills:
        name = path.parent.name
        names.add(name)
        label = path.relative_to(root)
        try:
            content = path.read_text(encoding="utf-8")
            info = metadata(content)
        except (OSError, ValueError) as exc:
            errors.append(f"{label}: {exc}")
            continue
        if not NAME.fullmatch(name) or info["name"] != name:
            errors.append(f"{label}: invalid or mismatched name")
        if len(info["description"]) > 1024:
            errors.append(f"{label}: description exceeds 1024 characters")
        if len(content.splitlines()) >= 500:
            errors.append(f"{label}: SKILL.md must be < 500 lines")
        if (path.parent / "README.md").exists():
            errors.append(f"{label}: README.md inside a skill folder")
    if cases_path is not None:
        try:
            cases = json.loads(Path(cases_path).read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            errors.append(f"canary cases unreadable: {exc}")
            cases = []
        if not isinstance(cases, list):
            errors.append("canary cases must be a JSON array")
            cases = []
        positive, negative, seen, seen_ids = set(), set(), set(), set()
        for index, case in enumerate(cases, 1):
            if not isinstance(case, dict):
                errors.append(f"case {index}: must be an object")
                continue
            ident = case.get("id")
            if not isinstance(ident, str) or not NAME.fullmatch(ident):
                errors.append(f"case {index}: invalid id")
            elif ident in seen_ids:
                errors.append(f"case {index}: duplicate id")
            seen_ids.add(ident)
            prompt = case.get("prompt")
            expected, excluded = case.get("expected"), case.get("excluded")
            if not isinstance(prompt, str) or len(prompt.strip()) < 8:
                errors.append(f"case {index}: prompt too short")
                continue
            if prompt in seen:
                errors.append(f"case {index}: duplicate prompt")
            seen.add(prompt)
            if not isinstance(expected, list) or not isinstance(excluded, list) or not expected and not excluded:
                errors.append(f"case {index}: expected/excluded lists required")
                continue
            for group, bucket in ((expected, positive), (excluded, negative)):
                if any(not isinstance(n, str) or n not in names for n in group):
                    errors.append(f"case {index}: references an unknown skill")
                bucket.update(n for n in group if isinstance(n, str) and n in names)
            if set(expected) & set(excluded):
                errors.append(f"case {index}: expected and excluded overlap")
        for name in sorted(names):
            if name not in positive:
                errors.append(f"{name}: missing positive canary")
            if name not in negative:
                errors.append(f"{name}: missing near-miss negative canary")
        notices.append(f"{len(cases)} authored canary cases validated; agent activation NOT executed")

    if downstream is not None:
        dest = Path(downstream)
        if not dest.exists():
            errors.append(f"downstream not found: {dest}")
        else:
            found = 0
            for name in sorted(names):
                target = dest / name / "SKILL.md"
                if not target.is_file():
                    if name in required:
                        errors.append(f"required downstream skill missing: {name}")
                    continue
                found += 1
                try:
                    if target.read_bytes() != (master / name / "SKILL.md").read_bytes():
                        errors.append(f"downstream drift: {name}")
                except OSError as exc:
                    errors.append(f"downstream read failed for {name}: {exc}")
            notices.append(f"{found} downstream shared skill copies compared byte-for-byte")
    for name in required:
        if name not in names:
            errors.append(f"unknown required master skill: {name}")
    return errors, notices, len(skills)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--cases", type=Path, default=None, help="authored canary JSON")
    parser.add_argument("--downstream", type=Path, help="path to project's .agents/skills folder")
    parser.add_argument("--require", action="append", default=[], help="required local shared skill")
    args = parser.parse_args()
    cases = args.cases or args.root / "skills" / "activation-cases.json"
    errors, notices, count = audit(args.root, cases, args.downstream, args.require)
    for message in notices:
        print("INFO:", message)
    for message in errors:
        print("FAIL:", message)
    if errors:
        return 1
    print(f"PASS: {count} canonical skills; structural/canary-spec checks only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
