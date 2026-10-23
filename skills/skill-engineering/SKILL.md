---
name: skill-engineering
description: Design, modify, merge, delete, or evaluate Agent Skills. Use when changing SKILL.md files, trigger descriptions, multi-step agent workflows, delegation, safety gates, progressive disclosure, or the portfolio skills library itself.
---

# Skill Engineering

Use before adding or changing any Agent Skill in the portfolio library.

## First principle

Do not add a skill because a useful upstream one exists. Start from a
demonstrated portfolio gap.

Classify the request:
- KEEP: current skill already covers it.
- MODIFY: improve one skill.
- MERGE: combine overlapping capabilities.
- DELETE: remove redundant or stale skill.
- MISSING: add only when no coherent existing skill can own the workflow.

## Design workflow

1. **Trigger class.** The description says what the skill does AND when to use
   it, with concrete task vocabulary; broad enough to help, narrow enough to
   trigger predictably. Slightly "pushy" descriptions beat under-triggering.
2. **One coherent job per skill.** Avoid chaining many tiny skills; avoid
   mega-skills that activate randomly.
3. **Progressive disclosure.** SKILL.md focused; detailed checklists,
   templates, and examples live in `references/` one level below, loaded only
   when their trigger condition is met.
4. **Workflow control.** Explicit phases for fragile multi-step work; safety
   gates before irreversible/security-sensitive/destructive/external actions;
   separate review from implementation; delegate only via clear I/O contracts.
5. **Evaluate before expanding.** Test positive triggers AND near-miss
   non-triggers; compare output with/without the skill; delete instructions
   the agent already handles reliably.
6. **Hygiene.** Canonical portfolio skills live ONLY in `command-center-/skills/`.
   Per-repo copies are downstream: refresh them by copying from the masters;
   merge or remove superseded skills in the same change.

## Spec constraints (Agent Skills open format)

- Folder name = `name` in frontmatter; lowercase letters, numbers, hyphens.
- `description` non-empty, explains capability + trigger.
- SKILL.md under 500 lines; no README.md inside a skill folder.

## Definition of done for skill changes

Run a structural check (valid frontmatter, name matches folder, trigger
vocabulary present) and record positive/negative trigger examples; then apply
`verification-before-completion`.

> 🏛️ Portfolio binding: this file IS the library's own constitution.
