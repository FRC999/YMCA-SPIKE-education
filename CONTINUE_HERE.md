# Continue this project on another computer

The repository contains the curriculum and a maintained AI handoff. A fresh chat does not automatically inherit the original conversation; the prompt below tells it exactly which project files to load. Keep the handoff current when decisions or actual results change.

For teaching or reading, use the [main index](README.md) and download only the needed class files. No Git installation or clone is required. The steps below are for maintaining the curriculum with Codex on another computer. Small Markdown changes can also be made directly on GitHub.

## On the curriculum maintenance computer

1. Read or clone the public `FRC999/YMCA-SPIKE-education` repository without signing in. To push changes, sign in with an authorized collaborator account. Credentials and installed LEGO software are not copied with the project.
2. Clone it into any convenient folder, using GitHub Desktop or:

   ```sh
   gh repo clone FRC999/YMCA-SPIKE-education
   cd YMCA-SPIKE-education
   ```

   For an existing checkout, review `git status` first, preserve local work, then update with `git pull --ff-only` when appropriate. Do not discard edits to make the pull succeed.

3. Open that cloned folder as the Codex project/workspace. Do not open the separate competition robot-code repository for this work.
4. Start a chat and paste the prompt below. If you already have a specific task or new kit results, append them.

## Copy and paste this prompt

```text
Continue the MechaRAMS / Cheshire YMCA robotics education project in this repository, FRC999/YMCA-SPIKE-education.

Before answering or changing files, read AGENTS.md, PROJECT_CONTEXT.md, SESSION_PREP.md, and MAINTENANCE.md. Use the repository skill at .agents/skills/ymca-spike-maintenance/SKILL.md; if it is not automatically available, read that file directly. Check the current Git status and remote so you work in the correct checkout and preserve local edits.

Treat those files as the project handoff from our earlier work. Do not ask me to repeat the program design, chosen demo, or document conventions already recorded. Do not assume that the trainer workshop, robot assembly, hardware tests, or R3PTAR rehearsal happened just because their plans exist. Ask only for missing results or decisions needed for the next step.

For your first reply, briefly state the current confirmed status and the most useful next action. If I appended a concrete task or new results, incorporate them and proceed with the authorized work instead of stopping at a plan.

Keep the DOCX and generated Markdown versions in sync using the repository script. Update the prep tracker and project handoff when facts or decisions change. Commit and push all completed project updates to the existing repository, run the relevant checks, and verify the remote received the changes. Report any actual blocker rather than claiming a sync or hardware test passed.
```

## What the new chat should learn

- The curriculum is accepted; the current phase is equipment/trainer preparation.
- The two teaching SPIKE bases should be assembled before the first class. They use the existing complete SPIKE App 3 Python starters.
- The selected separate EV3 demonstration is autonomous R3PTAR, with movement and a sensor-triggered strike/retreat sequence.
- The two-hour trainer session starts with assembly and testing and includes individual teaching practice.
- Only reported or observed results count as completed work.
- Four core DOCX files have generated Markdown copies; standalone plans/trackers are authored Markdown.
- The user expects all project updates to be synced to GitHub.

The detailed decisions, unknowns, and next actions are in [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md) and [SESSION_PREP.md](SESSION_PREP.md), not duplicated in this prompt. This avoids making the prompt stale as the program moves forward.

## Tool portability

Reading and editing Markdown needs no special plugin. The sync checker uses Python 3.10+ and the standard library. DOCX/PPTX layout changes need appropriate document/presentation tools on the new computer. SPIKE and EV3 apps, USB/Bluetooth connections, GitHub authentication, and any Codex plugins must be available there independently. Resolve their paths locally rather than copying old machine paths.

The custom skill is checked in under `.agents/skills/ymca-spike-maintenance/`. Codex supports repository-local skills in that location; root `AGENTS.md` provides repository instructions. If discovery does not work in a particular client, the explicit file-reading prompt above still provides the handoff. See [OpenAI’s skill documentation](https://learn.chatgpt.com/docs/build-skills) and [AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

Before switching computers again, commit and push new material decisions and results. The other computer can only recover what was saved and synced; these files are a maintained project summary rather than a guarantee of access to every prior chat message.
