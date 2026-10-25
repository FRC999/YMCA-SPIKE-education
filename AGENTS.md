# Repository instructions for AI assistants

This repository holds the MechaRAMS / Cheshire YMCA SPIKE curriculum and session preparation. Work from this checkout, not the separate FRC competition-code repository.

## Recover context before changing materials

Read [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md), [SESSION_PREP.md](SESSION_PREP.md), and the relevant section of [MAINTENANCE.md](MAINTENANCE.md). Use the repository skill at [.agents/skills/ymca-spike-maintenance/SKILL.md](.agents/skills/ymca-spike-maintenance/SKILL.md) for curriculum or preparation updates. New user instructions take precedence over an older project snapshot.

Do not ask the user to repeat decisions already recorded. Do not infer that a scheduled workshop happened, a checklist passed, or a robot was built. Record actual results only when reported or observed.

## Document and Git workflow

- For the four paired curriculum documents, DOCX is the editorial source and Markdown is the generated GitHub-reading copy. Update the DOCX, then run `python scripts/sync_documents.py --write` and `python scripts/sync_documents.py --check`. Never leave a requested edit only in the generated Markdown.
- Standalone plans, project context, rules, and backlog files are authored Markdown; they do not need artificial DOCX counterparts.
- When changing the converter, run `python -m unittest discover -s tests -v`. Unsupported DOCX content must be handled explicitly, not silently dropped.
- Use available document/presentation skills when editing those artifacts. Render and review changed DOCX/PPTX outputs before delivery. The sync checker verifies content pairing, not visual layout or robot behavior.
- Update links and any affected lesson notes, task cards, and programs together. Preserve the original design and student-facing simplicity unless the user requests changes.
- Update `SESSION_PREP.md` for operational results and `PROJECT_CONTEXT.md` for material decisions or the next-session handoff. Keep maintenance work in `MAINTENANCE.md`.
- The user explicitly requested that all project updates be synced to GitHub. After appropriate checks, commit and push the requested work to the existing `FRC999/YMCA-SPIKE-education` remote. Check status first, preserve unrelated edits, and verify the remote received the commit. Never force-push or change repository visibility as a routine sync step. Report an actual push/access blocker clearly.
- Keep `.build/`, local caches, credentials, and duplicate distribution ZIPs out of Git. Use repository-relative paths in maintained instructions. Do not copy private student/family records into this repository.

## Instructional invariants

Preserve the accepted eight-session, one-hour course and beginner-friendly scaffolded Python approach. Enrollment is not confirmed; eight students/two kits is the baseline. Both SPIKE bases are preassembled for Week 1, with left drive motor A and right drive motor B; the auxiliary motor stays unplugged. Sensors C/D are later additions. EV3 R3PTAR is a separate autonomous demonstration, not remote driving and not a substitute for either teaching base. See the context and prep tracker for the current demo and trainer-session plans.
