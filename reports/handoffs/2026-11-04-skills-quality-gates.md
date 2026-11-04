# Skill quality gates — handoff — 2026-11-04

Scope: canonical `command-center-` skills governance only. Baseline `main@0587041fc8f3a3b2d87f8df71b40e6823f64228f`. Independent repository-local change to project-specific `kiyyal/.agents/skills/ui-ux-pro-max/SKILL.md` is proposed in its own PR, not mixed with this center PR.

- Implemented a read-only, stdlib-only skill quality gate and 10 unit tests.
- Added 26 authored canary prompts (positive and near-miss for each of the 13 canonical skills). This validates *case specifications*, **not live agent activation**.
- Defined the three-tier protocol: structural, live activation and outcome comparison; clarified required RTL skill versus project UI augmentation.
- Added a PR-time CI proposal, routing documentation, and PR evidence fields. No merge, production deploy or project-code mutation.
- Local verification on an isolated 13-skill **fixture**: `python3 tools/skill_gate.py --root /mnt/data/skills_work` PASS (26 cases), `python3 -m unittest discover -s /mnt/data/skills_work/tools -p 'test_*.py'` 10/10 PASS. Fixture checks do not prove integration against the remote canonical repo.
- The new GitHub workflow and structural validation against the *entire checked-out repository* still require a hosted CI run on this PR; do not call them green until GitHub reports success.
- Overlap warning: center PR #4 also edits registry/handoff files and remains draft; reconcile before any merge.

Next: review PR diffs, await actual GitHub CI, run live agent canaries in a real harness, then decide whether to merge or roll out to additional projects. No auto-merge authorized.
