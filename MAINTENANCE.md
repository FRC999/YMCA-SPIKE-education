# Maintenance rules and backlog

Updated October 25, 2026. This file tracks repository maintenance and reusable update rules. Equipment results, session delivery, kit shortages, and personal-part loans belong in [SESSION_PREP.md](SESSION_PREP.md); do not maintain competing copies of those checklists here.

## Document ownership and synchronization

The four core curriculum DOCX files and eight class speaker-note DOCX files are the editorial sources. See the [speaker-note index](01_Instructor/Speaker_Notes/README.md) for the additional eight DOCX/Markdown pairs. Their same-name `.md` companions are generated reading copies for GitHub. The body text, headings, tables, source links, and code are preserved; Word retains print layout, pagination, headers/footers, and physical writing-space height.

| Editorial source | GitHub reading copy |
|---|---|
| [Program proposal DOCX](00_Start_Here/Program_Proposal_and_Resources.docx) | [Program proposal Markdown](00_Start_Here/Program_Proposal_and_Resources.md) |
| [Instructor guide DOCX](01_Instructor/Instructor_and_Mentor_Guide.docx) | [Instructor guide Markdown](01_Instructor/Instructor_and_Mentor_Guide.md) |
| [Student workbook DOCX](02_Student/Student_Workbook.docx) | [Student workbook Markdown](02_Student/Student_Workbook.md) |
| [Evaluation forms DOCX](05_Evaluation/Evaluation_and_Partner_Forms.docx) | [Evaluation forms Markdown](05_Evaluation/Evaluation_and_Partner_Forms.md) |

Do not manually edit only a generated Markdown copy. Apply the content change to its DOCX source, preserve/review the Word layout, and regenerate. A user may draft a correction in Markdown; the assistant must carry that correction into the DOCX before regenerating. This is a controlled one-way generation workflow, not a bidirectional converter.

Standalone Markdown such as trainer plans, context, backlog, and this file is independently authored. Do not create unnecessary Word copies of it.

From the repository root, with Python 3.10 or later:

```sh
python scripts/sync_documents.py --write
python scripts/sync_documents.py --check
python -m unittest discover -s tests -v
```

The converter uses only the Python standard library and needs no Word installation. It discovers DOCX files outside hidden/build directories, preserves the source content in reading order, and records a source hash in each mirror. It refuses to overwrite independently authored Markdown and reports orphan mirrors when a DOCX disappears. It stops on unsupported content such as images, tracked changes, footnotes, fields, or merged/nested tables; extend and review the converter before introducing those features. Do not remove a content guard just to make a check pass.

The [Document sync workflow](.github/workflows/document-sync.yml) runs tests and `--check` on pushes and pull requests. It reports drift; it does not silently rewrite or push files. The normal update task is responsible for regeneration and committing both formats. No background local-folder synchronization is configured.

## Interactive prep checklist maintenance

[SESSION_PREP_CHECKLIST.html](SESSION_PREP_CHECKLIST.html) opens the real [SESSION_PREP.md](SESSION_PREP.md); it does not embed a status snapshot. It only changes checkbox marks. Narrative records remain editable Markdown. Follow [CHECKLIST_INSTRUCTIONS.md](CHECKLIST_INSTRUCTIONS.md), and run `node --test tests/test_prep_checklist.cjs` after changing the parser or save behavior. The page needs no installed JavaScript packages. Its direct-save/browser permission flow still needs a manual Chrome or Edge check; automated browser preview was unavailable because the browser tool blocked local file URLs. Parsing, character preservation and JavaScript syntax checks passed.

## Completion checklist for each update

- [ ] Read the latest project context and operational tracker; distinguish reported results from planned checks.
- [ ] Make the requested change in the correct source; preserve other people’s edits.
- [ ] Update directly affected notes, programs, task cards, and links.
- [ ] If DOCX changed, render/review it with the available document tools, regenerate Markdown, and check the pair.
- [ ] If presentation content or notes changed, keep the slide-by-slide companion aligned and inspect the final deck.
- [ ] Run the relevant checks. Converter changes require the unit tests; physical robot changes require an actual reported bench test before being called verified.
- [ ] Update `SESSION_PREP.md`, this backlog, or `PROJECT_CONTEXT.md` where the new facts belong.
- [ ] Review `git status` and the diff, commit the scoped changes, push to the existing remote, and verify the received commit.
- [ ] If synchronization fails, report the actual blocker and what is still only local. Do not claim the GitHub copy is current.

## Skills and tools for future assistants

- Repository skill: [.agents/skills/ymca-spike-maintenance/SKILL.md](.agents/skills/ymca-spike-maintenance/SKILL.md). Use for curriculum, first-session preparation, trainer plans, and document-pair maintenance.
- Persistent repository instructions: [AGENTS.md](AGENTS.md).
- Portable handoff and new-chat prompt: [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md) and [CONTINUE_HERE.md](CONTINUE_HERE.md).
- Use the current environment’s document skill for DOCX layout edits, presentation skill for PPTX, and PDF skill when inspecting or changing build references. Resolve tools/runtime paths on the current machine. The repository does not copy the user’s installed plugins or their credentials.
- No special plugin is needed to read the Markdown or run the sync checker. Editing Word/PowerPoint layouts requires appropriate tools; do not claim visual review if none is available.

## Established rules worth preserving

- Keep the accepted eight-week, one-hour beginner program. Eight students/two kits remains the baseline until enrollment is confirmed.
- Preassemble both SPIKE driving bases before Week 1. Use left motor A/right B, auxiliary motor unplugged, and add distance C/color D later.
- Keep Week 1 simple: one letter, wait, short move, predict, test, explain. Teach wheel degrees accurately and keep students inside the recipe area.
- R3PTAR is a separate autonomous demo. Remote driving alone does not meet Alex’s requirement. Its behavior and current readiness are in the context/tracker.
- Student trainers need both operating and teaching practice. A completed build is not proof that a kit or trainer is ready.
- Never invent attendance, successful tests, learning gains, photos, quotes, or outreach outcomes. Use approved records and report what actually happened.
- The user wants everything produced for this project synced to the repository. Keep it private unless explicitly asked otherwise; omit credentials, identifiable family records, private build caches, and redundant ZIPs.

## Maintenance backlog

### Implemented

- [x] Add separate detailed DOCX/Markdown speaker notes for each of eight classes.
- [x] Add an interactive local prep checklist that edits checkbox marks in the shared Markdown file, plus save/pull/push instructions.

- [x] Add Markdown mirrors of all four core DOCX files.
- [x] Add a deterministic generator and a non-writing drift check.
- [x] Add tests for content preservation, stale edits, missing sources, and unsupported content.
- [x] Add the GitHub Document sync workflow.
- [x] Add persistent AI instructions, project context, a repository skill, and a continuation prompt.
- [x] Link GitHub reading copies from the repository entry points and trainer documents.

### Pending when new facts or work require them

- [ ] Reconcile the historical proposal calendar with confirmed session dates. Do not invent dates.
- [ ] Once enrollment/staffing is confirmed, update affected schedules in DOCX, Markdown, slides, and trainer notes together.
- [ ] Incorporate actual workshop results and first-session findings into operational documents; preserve blank master forms.
- [ ] If the revised Week 1 notes change again, update the embedded PowerPoint notes and HTML companion together.
- [ ] Consider Markdown companions for HTML-only station cards and code guides if direct GitHub reading of those is needed. All eight class speaker-note documents now have DOCX/Markdown pairs.
- [ ] Promote additional build/rehearsal scripts into portable, tracked tooling only when regeneration or further code testing requires them. The old local `.build` directory is not a dependency for this sync workflow.
- [ ] After any source rename/deletion, review and remove or rename its generated mirror and repair incoming links; the checker intentionally does not delete content automatically.

## Change record

| Date | Change |
|---|---|
| 2026-10-25 | Added DOCX/Markdown synchronization, maintenance rules, backlog, and the portable AI continuation package. DOCX source content and layout were not changed by this conversion. |
