# Preparation updates and classroom computers

Use [SESSION_PREP.md](SESSION_PREP.md) as the single shared preparation record. Use the [weekly print-and-bring checklists](01_Instructor/Class_Preparation/README.md) to pack for class. Everyone can read these files on GitHub without installing Git or cloning the repository.

## Update preparation directly on GitHub

An authorized collaborator can make a small update entirely in the browser:

1. Open [SESSION_PREP.md on GitHub](https://github.com/FRC999/YMCA-SPIKE-education/blob/main/SESSION_PREP.md) and sign in with an account that has write access.
2. Select the pencil button to edit the file. Change `- [ ]` to `- [x]` for a completed task, or reverse it to reopen a task.
3. Add the date, kit identifier and actual result where relevant. Record failures and shortages too. Preserve other people's notes. A checked box alone does not document a hardware test.
4. Preview the change, review the diff and commit with a short description. Refresh the rendered file to confirm the update is present.

Public read access does not grant editing permission. The normal Markdown reading view is sufficient for checking status; use the editor to change checkbox markers. Completed child attendance, assessment and family records belong in the approved private system, not this public repository.

## Set up the classroom computers

Bookmark the [main materials index](README.md). No teaching computer needs Git, a local HTML page or a full repository clone.

- **Two robot-control laptops:** prepare and test the required SPIKE software and hub connection. Download the week's complete `.py` source from [04_Python](04_Python), paste it into a SPIKE Python project, and save/test the project before class. The source file is not a native SPIKE project bundle.
- **Presentation computer:** download the week's PDF slides, or the PPTX when using PowerPoint and Presenter View. Read the corresponding Markdown speaker notes during preparation. Save the DOCX notes too if an offline copy is needed.
- **Two build-reference laptops:** open the weekly build card and reference images/PDFs from the index. Save the relevant PDFs locally before class so a connection outage does not interrupt the activity. Printed build cards can serve the same purpose.
- **Printing:** follow the week's checklist for exact quantities. Download the PDFs for reliable printing.

These are device roles; the presentation display can use one of the available laptops if the room setup permits. Keep each team's saved SPIKE project separate and retain a known-good starter. Before each session, check GitHub for changes and replace outdated downloaded copies. Individual downloads do not update automatically.

## Optional local maintenance with Codex

A clone is useful on the computer where you edit curriculum documents, regenerate reading copies or work with Codex. Follow [CONTINUE_HERE.md](CONTINUE_HERE.md) for that workflow. It is not required on every classroom PC.

When editing a local checkout, review existing work and pull the latest changes before editing. Review your diff, commit and push to share the result. Changes made in a text editor or downloaded copy do not reach GitHub until committed and pushed. Avoid editing an old local copy while someone updates the same file in the browser; reconcile their changes rather than overwriting them.

The former HTML checklist was a local checkbox editor for this same Markdown file. It did not contain a separate preparation record or synchronize automatically. It has been retired, along with duplicate HTML reference pages; useful lesson content remains in Markdown, PDF, DOCX and PPTX.
