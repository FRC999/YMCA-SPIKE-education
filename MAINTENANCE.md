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
python scripts/check_reading_copies.py --check
python -m unittest discover -s tests -v
```

The converter uses only the Python standard library and needs no Word installation. It discovers DOCX files outside hidden/build directories, preserves the source content in reading order, and records a source hash in each mirror. It refuses to overwrite independently authored Markdown and reports orphan mirrors when a DOCX disappears. It stops on unsupported content such as images, tracked changes, footnotes, fields, or merged/nested tables; extend and review the converter before introducing those features. Do not remove a content guard just to make a check pass.

The [Document sync workflow](.github/workflows/document-sync.yml) runs tests and `--check` on pushes and pull requests. It reports drift; it does not silently rewrite or push files. The normal update task is responsible for regeneration and committing both formats. No background local-folder synchronization is configured.

## PDF and other reading copies

The root README is the GitHub reading index. PDFs preserve page/slide layout; Markdown provides searchable text. Editable DOCX/PPTX files remain available. The 43 new PDFs include four core documents, ten decks, eight team sheets, eight build cards, eight packing checklists, baseline/final checks, attendance, role cards and the hub guide. The official LEGO build PDF is an external reference and is not regenerated.

Source ownership and regeneration:

- Core PDFs: export the matching DOCX to PDF with Word or the available document renderer; inspect every page.
- Deck PDFs: export the matching PPTX as slides, with one slide per page. The current PDFs contain the reviewed slide images at 1280 × 720, preserving layout. Use the Markdown speaker notes for text and the PPTX for Presenter View. When notes change, update the corresponding embedded PPTX notes from the six slide sections in the speaker-note DOCX. Keep both Week 1 PPTX filenames identical.
- Team sheets, baseline and final checks: extract the matching pages from the newly exported workbook PDF. Attendance comes from the evaluation-forms PDF. Locate pages by heading, rather than assuming old page numbers still apply. Current workbook pages are baseline 2, Weeks 1–8 on 3–10, final check 11; attendance is evaluation page 2.
- Build cards and packing checklists: edit their same-name Markdown sources, then typeset/re-export the affected PDFs. Check quantities against the reusable kit. Packing PDFs are compact one-page summaries; the Markdown includes the complete preparation and closeout steps.
- Role cards: use `01_Instructor/Grouping_and_Roles.md`; preserve two pages, three cards per page. Hub guide: use its Markdown source and the supplied reference image.
- Code guide, research sources, station-card index and hub guide: their Markdown files are the maintained sources. Week 1 notes use the same DOCX/Markdown workflow as the other weeks. Duplicate HTML versions were retired after their content was preserved in Markdown/PDF.

[`scripts/reading_copies.json`](scripts/reading_copies.json) records the reviewed source/output hashes. The standard-library checker detects changed or missing files, including embedded-note dependencies; it cannot prove semantic agreement or visual quality. Text hashes normalize Windows line endings. Regeneration is a normal authoring task using available tools; private `.build` scripts are not required on another computer.

After regenerating and reviewing an output, record that specific repository-relative path, for example:

```sh
python scripts/check_reading_copies.py --record 03_Presentations/W01_signal.pdf
python scripts/check_reading_copies.py --check
```

Pass multiple output paths when several reviewed copies changed. Do not record hashes merely to hide stale exports. Add source/output mappings to the manifest for new companions. CI checks both the DOCX/Markdown pairs and this manifest without modifying files.

## Preparation record maintenance

[SESSION_PREP.md](SESSION_PREP.md) is the sole preparation record. Follow [CHECKLIST_INSTRUCTIONS.md](CHECKLIST_INSTRUCTIONS.md) to edit checkboxes and evidence directly on GitHub or in an optional local checkout. Preserve actual results and leave unreported work unchecked. The former local HTML editor, JavaScript helper and its tests have been retired. Teaching PCs need the class files and appropriate LEGO software, not Git or a clone.

## Completion checklist for each update

- [ ] Read the latest project context and operational tracker; distinguish reported results from planned checks.
- [ ] Make the requested change in the correct source; preserve other people’s edits.
- [ ] Update directly affected notes, programs, task cards, and links.
- [ ] If DOCX changed, render/review it with the available document tools, regenerate Markdown, and check the pair.
- [ ] If presentation content or notes changed, keep the slide-by-slide companion aligned and inspect the final deck.
- [ ] Refresh affected PDF/Markdown copies, review them, and record only the reviewed exports in the reading-copy manifest.
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

- Keep the accepted eight-week, one-hour beginner program. Confirmed enrollment is 12 children in grades 5–6: four teams of three, two kits, four laptops and 4–6 student instructors plus an adult lead.
- Preassemble both SPIKE driving bases before Week 1. Use left motor A/right B, auxiliary motor unplugged, and add distance C/color D later.
- Keep Week 1 simple: one letter, wait, short move, predict, test, explain. Teach wheel degrees accurately and keep students inside the recipe area.
- R3PTAR is a separate autonomous demo. Remote driving alone does not meet Alex’s requirement. Its behavior and current readiness are in the context/tracker.
- Student trainers need both operating and teaching practice. A completed build is not proof that a kit or trainer is ready.
- Never invent attendance, successful tests, learning gains, photos, quotes, or outreach outcomes. Use approved records and report what actually happened.
- The user wants everything produced for this project synced to the repository and explicitly authorized public read access on October 25. Public visibility is verified. Omit credentials, identifiable family records, private build caches, and redundant ZIPs.

## Maintenance backlog

### Implemented

- [x] Reconcile all eight classes with 12 learners, three rotating jobs, weekly hands-on builds, four laptops and 4–6 student instructors.
- [x] Merge the old code/prediction slides, add hub-light guidance and final reflection prompts, and align embedded/companion notes.
- [x] Add per-session print-and-bring checklists with quantities, reusable supplies and individual one-page printouts.
- [x] Add GitHub-readable PDFs, Markdown companions for previous HTML-only references, and source/export drift checks.
- [x] Make the repository public for reading at Alex’s request.
- [x] Add separate detailed DOCX/Markdown speaker notes for each of eight classes.
- [x] Replace the former local HTML checklist workflow with direct Markdown editing on GitHub; preserve all preparation records.

- [x] Add Markdown mirrors of all four core DOCX files.
- [x] Add a deterministic generator and a non-writing drift check.
- [x] Add tests for content preservation, stale edits, missing sources, and unsupported content.
- [x] Add the GitHub Document sync workflow.
- [x] Add persistent AI instructions, project context, a repository skill, and a continuation prompt.
- [x] Link GitHub reading copies from the repository entry points and trainer documents.

### Pending when new facts or work require them

- [ ] Reconcile the historical proposal calendar with confirmed session dates. Do not invent dates.
- [ ] Incorporate actual workshop results and first-session findings into operational documents; preserve blank master forms.
- [ ] If the revised Week 1 notes change again, update the embedded PowerPoint notes and DOCX/Markdown companion together.
- [ ] Promote additional build/rehearsal scripts into portable, tracked tooling only when regeneration or further code testing requires them. The old local `.build` directory is not a dependency for this sync workflow.
- [ ] After any source rename/deletion, review and remove or rename its generated mirror and repair incoming links; the checker intentionally does not delete content automatically.

## Change record

| Date | Change |
|---|---|
| 2026-10-25 | Retired seven redundant/local HTML pages and the checkbox-editor helper; preserved useful content in Markdown/PDF, made code/research Markdown authoritative, and clarified that classroom PCs need no repository clone. |
| 2026-10-25 | Applied instructor practice feedback across all eight sessions; updated enrollment, roles/builds, hub guidance, reflection prompts, notes and blank forms; added browser/print copies, quantified packing lists and export checks; made the repository public as requested. |
| 2026-10-25 | Added DOCX/Markdown synchronization, maintenance rules, backlog, and the portable AI continuation package. DOCX source content and layout were not changed by this conversion. |
