# AGENTS.md — Command Center

This repository is the entry point for the portfolio of `mohamedmasoud3030-tech`.
Owner communication: simple Egyptian Arabic; explain technical terms in one line.

## 1. Start here — every session

1. Read this file, [PROJECTS.md](PROJECTS.md), the current session registry in
   [README.md](README.md), and [handoffs](reports/handoffs/INDEX.md).
2. Read [skill routing](skills/README.md), select the relevant skills, read their
   complete SKILL.md files, and announce: `المهارة المستخدمة: <names>`.
3. Check the target repository's default branch and open PRs through GitHub.
   Record the exact base SHA. Fetch a clean checkout; do not trust an old clone.
4. Read the target's AGENTS.md, declared canonical status, relevant decisions,
   and applicable local skills. Read nested instructions before changing files.
   MALEK uses its Canonical Pack; mosaid has its own agent system. Do not impose
   a parallel STATUS.md or AGENTS.md on those exceptions.
5. State in five lines: objective, current evidence, scope, checks, next action.
   Use [the start prompt](prompts/START-HERE.md).

## 2. Authority and evidence

- Explicit current owner instructions govern task scope and supersede stale
  session reservations. Do not infer permission to merge/deploy from permission
  to prepare a change.
- PROJECTS.md owns project cards; README.md owns session reservations and owner
  decisions. The target repository owns its detailed current technical state.
- Reports, inventory snapshots and handoffs are dated evidence, not live state.
  This includes legacy `reports/README.md` and `reports/PROJECTS.md`.
- For current claims record source link, checked-at date/time, and commit SHA
  when applicable. Say "reported", "verified", "stale", or "not verified".
- Distinguish implemented, checked, merged, deployed and real-user validated.
  An HTTP 200, green unit tests, or a merged PR alone does not prove readiness.
- Never present no checks, skipped checks, or missing access as a pass. Inspect
  failures before attributing them to artifact quota or an environment issue.

## 3. Ownership and concurrency

The single session registry is in README.md. On 2026-10-24 the owner explicitly
confirmed there are no parallel sessions; old reservations are historical.
Open PRs still preserve unfinished work and are not automatically abandoned.

Before writing, inspect current upstream changes and PRs in the affected scope.
Reserve this session's repository, branch, paths and purpose in its PR and in
README.md. Do not change another session's row. If new overlapping work appears,
stop overlapping writes and coordinate; independent authorized work may continue.
Recheck the base before publishing. Never force-push or silently overwrite work.
A timestamp expiring does not transfer ownership; record an explicit handoff.

## 4. Skills: canonical source and usable local copies

- `skills/` here is the canonical shared library. Discover the count from the
  filesystem; do not maintain counts in multiple documents.
- Shared skills needed by a project must be available locally in
  `.agents/skills/` (or its documented native path). A link alone is insufficient.
- Copy the complete required skill directory, including referenced resources.
  Record source repository, source commit, copied paths and verification in the
  sync PR. Preserve project-specific skills and instructions.
- On drift, review the difference against the canonical version and prepare a
  project-scoped sync PR. Do not silently overwrite local additions.
- Do not assume an agent automatically loaded a skill. Name the actual file read
  and include the evidence required by that skill in delivery.
- UI work requires `frontend-rtl-design`; money requires
  `financial-correctness`; database/RLS work requires `database-postgres-rls`.
- Skill changes require `skill-engineering`; completion claims require
  `verification-before-completion`; merging/releasing requires `release-readiness`.

## 5. Authorized execution

Owner requests to improve/fix a defined scope authorize preparing reversible
changes and a reviewable PR in that scope. Do not repeatedly ask for the same
authorization. Ask for a decision only when scope or a material choice is missing.

Use a task branch and a small reviewable PR. No direct main writes.
Do not merge, deploy, change hosted data, rotate credentials, remove branches,
change CI/release configuration, or broaden into product code without authorization
for that action. Never commit secrets, delete documents/history, or force-push.

Plan multi-file work before edits; reuse existing tools. Test behavior changes
with meaningful failing cases before implementation. Keep documentation changes
proportionate; do not add frameworks or duplicate status systems.

## 6. Delivery gate

For changes to this center, run from the repository root:

```bash
python3 -m unittest discover -s tools -p 'test_*.py'
python3 tools/validate-center.py --base-ref <reviewed-base-sha>
git diff --check
```

The validator is local and read-only. It checks required entry documents, inline
relative file links in active documentation, skill metadata, and missing documents
relative to the supplied base. It does not verify external URLs, anchor fragments,
GitHub branch protection, product tests, or downstream skill synchronization.

Before delivery:
- Review the diff for requirements, correctness and scope.
- Update README.md / PROJECTS.md only where reality changed.
- Add a dated handoff using [the template](templates/HANDOFF.md); index it.
- Report changed files, exact checks/results, PR link, remaining gaps and the
  first next action. Say "PR prepared" until GitHub confirms merged.
- End with real owner decisions and a recommendation; if none, say none.

