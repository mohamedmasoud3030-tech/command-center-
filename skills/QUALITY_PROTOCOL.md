# Skill quality protocol — portfolio-wide

This document governs **how to evaluate skills**, not product business rules. The canonical skill bodies live in `skills/*/SKILL.md`; project-local copies remain governed by their repository instructions. No new parallel status ledger is created.

## 1. Before a task: choose the smallest applicable set

1. Read the project's `AGENTS.md`, active decisions and the central routing table in [README.md](README.md).
2. Match the task to skill `description` triggers. Read the **full local** `SKILL.md` for each selected skill, including referenced material only when applicable; never infer that auto-discovery loaded it.
3. State each loaded skill's **actual path** and one-line trigger. Note relevant skills that are intentionally not loaded and why. Tool-specific paths must be verified in the current workspace; never copy an environment-dependent example blindly.
4. If instructions conflict, follow the project's accepted business/architecture decisions and the portfolio governance hierarchy. Escalate consequential conflicts; do not silently drop either requirement.

## 2. During and after: evidence, not skill-name theatre

Use a compact section in the PR body/handoff; do **not** create a per-task report file:

```text
Skill evidence (commit: <exact SHA>)
- Loaded: <skill> — <actual SKILL.md path> — because <trigger>
- Applied: <concrete action/decision caused by skill>
- Proof: <test command + outcome / browser scenario / diff / review finding>
- Not run / blocked: <what, why; never claim PASS>
```

For code, record the exact commit, tests and exit codes. For UI, include route/device, screenshots and business persistence. For money/security/DB, attach the relevant invariant tests. Keep secrets and private data out of logs and PRs. A declared skill without evidence is **unverified**, not automatically failed or passed.

## 3. Three different quality tiers

- **Tier 0 — structural (automatable):** `python3 tools/skill_gate.py` checks central metadata and the canary **specification**. Run `--downstream path/to/project/.agents/skills` to detect drift in **present** shared copies, and `--require name` when a local skill is mandatory for the task. Missing optional skills are not errors. The existing `tools/validate-center.py` checks center documents and links. The workflow on PRs runs these checks.
- **Tier 1 — activation (requires an actual agent run):** use [activation-cases.json](activation-cases.json) in fresh sessions. For each positive case, check that the target skill was read and used; for near-miss cases, check that it was not activated unnecessarily. Record tool/agent version, prompt ID, selected skills, evidence and verdict. The JSON validator does **not** execute an agent.
- **Tier 2 — outcome (requires real work):** compare an appropriate before/after task with and without the skill, using the same codebase and acceptance checks. Record behavioral improvements and overhead; do not claim causal benefit from file parity or a green build alone.

## 4. UI skill overlap policy

`frontend-rtl-design` is **mandatory** for portfolio user-facing work and controls RTL, accessibility, operational workflows and verification expectations. A project-specific skill such as `ui-ux-pro-max` can supplement component and aesthetic decisions, but cannot override approved design tokens, product rules or `frontend-rtl-design`. Read only relevant reference datasets; do not execute a command containing an unsupported environment variable or stale plugin path.

## 5. Change management

Before adding another skill, use `skill-engineering`: KEEP/MODIFY/MERGE/DELETE/MISSING, demonstrate the gap, check positive and negative canaries, then compare output quality. Update the canonical master first; synchronize *only needed* downstream copies by independent PR with master SHA and byte parity. Preserve project-specific skills and avoid overlapping open PRs. Do not merge or deploy automatically.

For a new agent capability, test one actual repository workflow on a draft PR before broad rollout. Add a handoff entry to the existing index and update the central session registry only when a session changes ownership.
