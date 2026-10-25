# Using the session preparation checklist

The shared record is [SESSION_PREP.md](SESSION_PREP.md). The [interactive checklist page](SESSION_PREP_CHECKLIST.html) edits its checkboxes locally. Save and push the Markdown file to share those updates through this private GitHub repository. There is no second checklist database, login token in the page, or automatic background sync.

## On a new laptop

Install Git and sign in with an account that can access the private repository. Clone it once, or use **Clone repository** in GitHub Desktop:

```sh
git clone https://github.com/FRC999/YMCA-SPIKE-education.git
cd YMCA-SPIKE-education
```

Open `SESSION_PREP_CHECKLIST.html` from the clone in current Chrome or Edge. Double-click the file or use the browser's Open File command. Keep the `scripts` folder beside the page as it is in the repository. No web server or installation of project packages is required.

## Each time you update preparation

1. Close an old checklist tab. In the repository, run `git status`, resolve any unfinished local work, and run `git pull --ff-only`. In GitHub Desktop, use Fetch origin and Pull origin.
2. Open `SESSION_PREP_CHECKLIST.html`, select **Open prep file**, and choose this clone's `SESSION_PREP.md`. The page does not silently load an older cached checklist.
3. Read the relevant notes using **Full prep notes and records**. Check only work that was actually completed. Clearing a box reopens that task. The counter covers all operational checkboxes, including repeated reminders; it is not a kit-readiness score.
4. Select **Save prep file**. Allow the browser's file-write prompt if shown. A successful save explicitly says it wrote to the file. Until then, clicks exist only in the open tab; closing or refreshing can lose them.
5. Close the checklist before editing the prep file elsewhere. Add dates, test evidence, kit records, shortages, owners and notes in a text editor. Checking a box alone does not fill in those records. Do not mark a task complete merely because it was planned.
6. Review and share the change:

```sh
git diff -- SESSION_PREP.md
git add SESSION_PREP.md
git commit -m "Update session preparation results"
git push
```

GitHub Desktop provides the equivalent: review Changes, enter a summary, Commit to main, then Push origin. Refresh the prep file on GitHub to confirm the result. The page never runs Git commands or pushes on your behalf.

## If direct saving is unavailable

Browsers without the file-writing API use a file upload and download workflow. Select the prep file, change the boxes, and select **Download updated file**. Move that downloaded file into the repository as `SESSION_PREP.md`, replacing the prior file after checking you have the correct clone. A browser may name the download `SESSION_PREP (1).md`; restore the exact original name. Reopen it in the checklist to verify, then review, commit and push as above.

If a browser advertises the picker but blocks it for a local file, select **Open in download mode**. As a fallback, edit `[ ]` to `[x]` directly in the Markdown file. A download alone does not update the local clone or GitHub.

## Editing entirely on GitHub

Open [SESSION_PREP.md on GitHub](https://github.com/FRC999/YMCA-SPIKE-education/blob/main/SESSION_PREP.md), select **Edit this file**, change `- [ ]` to `- [x]` (or back), and commit. The rendered file is a reading view, so the local page supplies the clickable controls. Pull the change before using a local copy again. Do not alternate GitHub edits and an unsaved local checklist tab.

## When someone else changes the file

The page checks the file before saving and refuses to overwrite an outside change. Download pending edits if you need a record, reopen the latest file, and reapply the intended checkboxes. The check is a protection against accidental stale writes, not a multiuser lock: avoid simultaneous edits.

If Git rejects a push because the remote changed, keep your local commit, fetch the remote changes, and reconcile them in GitHub Desktop or your Git workflow. Review both people's results before resolving a conflict. Do not force-push to bypass it.
