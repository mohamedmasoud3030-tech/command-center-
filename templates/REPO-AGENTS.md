# AGENTS.md — {اسم المشروع}

> Instruction file for AI coding agents working in this repository (AGENTS.md open standard).
> Portfolio-level rules: see the `mohamedmasoud3030-tech/command-center-` repository `AGENTS.md` — it takes precedence on governance.
> Owner communication: always in simple Egyptian Arabic (مصري بسيط); owner is non-technical.

## 1) Product in one paragraph

{What this product does, for whom, in which market. Write so a newcomer understands in 30 seconds.}

## 2) Tech stack (exact)

- Frontend: {framework + version}
- Backend/DB: {e.g. Supabase Postgres + RLS + RPC}
- Package manager: {npm/pnpm + version}
- Runtime: {Node version}
- Key libs: {list}

## 3) Commands (copy-paste ready)

```bash
# install
{command}
# dev server
{command}
# tests
{command}
# typecheck / lint
{command}
# build
{command}
```

## 4) Repository map

| Path | What lives there |
|---|---|
| `src/` | |
| `docs/` | |
| `supabase/` (if any) | |

## 5) Canonical documents (read in this order)

1. {canonical status path declared by this project} — the ONE live status source; use `docs/STATUS.md` only when the project adopts it.
2. `README.md` — product overview
3. `docs/decisions/` or `docs/adr/` — immutable decisions
4. Anything under `docs/archive/` — frozen history, read-only context

## 6) Hard rules for this repo

- ✅ Update the declared canonical status in the same change that alters reality.
- ✅ Dated/one-off reports go to `docs/archive/` with an `ARCHIVED — YYYY-MM-DD` banner.
- ❌ Never commit secrets or real `.env` files (only `.env.example`).
- ❌ Never edit files under `supabase/migrations/` that were already applied; create new migrations.
- ❌ Never mark work done without evidence (tests/CI/merged PR).
- ❌ No new status/plan files outside the canonical set — ask the owner first.

## 7) Money / security notes (if applicable)

{E.g. "All money math uses decimal — never binary floats", "RLS is the authorization boundary", or write N/A.}

## 8) Definition of done

A task is done only when:
1. Code + tests pass (`{test command}` output is green),
2. The declared canonical status reflects the change,
3. The owner received an Arabic summary with any decisions they must make.

## 9) Shared skills and session start

Start at the center's AGENTS.md, PROJECTS.md and current README session registry.
Then read this repository's rules and applicable local SKILL.md files. State the
actual paths read; do not assume automatic discovery. Keep complete applicable
shared skills locally in `.agents/skills/` or the documented native path.
Record the source commit in each sync PR and preserve project-specific additions.
All UI tasks use frontend-rtl-design. Prepare changes on a task branch via PR;
never delete documents. Report checks, missing evidence, PR state and handoff.

