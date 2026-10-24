#!/usr/bin/env python3
"""Read-only structural checks. No network, credentials or third-party packages."""
import argparse
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit

REQUIRED = ('AGENTS.md', 'PROJECTS.md', 'README.md', 'skills/README.md',
            'prompts/START-HERE.md', 'reports/handoffs/INDEX.md')
DOC_SUFFIXES = {'.md', '.mdx', '.txt', '.rst'}


def validate(root, base_ref=None):
    root = Path(root).resolve()
    errors = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f'missing required document: {name}')
    active = list(root.glob('*.md'))
    for directory in ('skills', 'prompts', 'templates', 'tools', '.github'):
        active.extend((root / directory).rglob('*.md'))
    active.append(root / 'reports/handoffs/INDEX.md')
    for path in sorted(set(active)):
        if not path.is_file():
            continue
        text = path.read_text(encoding='utf-8')
        # Inline links only; fenced examples are not live navigation.
        text = re.sub(r'(?ms)^```[^\n]*\n.*?^```[^\n]*$', '', text)
        for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
            parts = urlsplit(target.strip('<>'))
            if parts.scheme or parts.netloc or not parts.path:
                continue
            dest = (path.parent / unquote(parts.path)).resolve()
            if not dest.is_relative_to(root) or not dest.exists():
                errors.append(f'{path.relative_to(root)}: broken local link: {target}')
    skills = sorted((root / 'skills').glob('*/SKILL.md'))
    if not skills:
        errors.append('skills: no SKILL.md files found')
    for path in skills:
        text = path.read_text(encoding='utf-8')
        header = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
        label = str(path.relative_to(root))
        if not header:
            errors.append(f'{label}: missing frontmatter')
            continue
        name = re.search(r'^name:\s*([^\n]+)', header[1], re.M)
        desc = re.search(r'^description:[ \t]*([^\n]+)', header[1], re.M)
        if not name or name[1].strip().strip('\"\'') != path.parent.name:
            errors.append(f'{label}: name must match directory')
        if not desc or not desc[1].strip().strip('\"\''):
            errors.append(f'{label}: description is empty')
        if len(text.splitlines()) >= 500:
            errors.append(f'{label}: skill must be under 500 lines')
    if base_ref:
        try:
            result = subprocess.run(['git', '-C', str(root), 'ls-tree', '-rz',
                                     '--name-only', base_ref, '--'],
                                    check=True, capture_output=True, text=True)
            for name in result.stdout.split('\0'):
                if name and Path(name).suffix.lower() in DOC_SUFFIXES:
                    if not (root / name).is_file():
                        errors.append(f'document removed since base {base_ref}: {name}')
        except (OSError, subprocess.CalledProcessError):
            errors.append(f'cannot inspect base ref: {base_ref}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--base-ref', help='Reviewed commit available locally; enables no-document-deletion check')
    args = parser.parse_args()
    errors = validate(args.root, args.base_ref)
    for error in errors:
        print(f'FAIL: {error}')
    if errors:
        return 1
    print('PASS: required documents, active inline local links, skill metadata')
    print('PASS: no document paths removed' if args.base_ref else 'NOT CHECKED: document deletion (supply --base-ref)')
    print('NOT CHECKED: external URLs, anchors, product readiness, downstream skills, branch protection')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
