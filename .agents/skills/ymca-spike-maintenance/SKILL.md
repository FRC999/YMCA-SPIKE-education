---
name: ymca-spike-maintenance
description: Continue or update the MechaRAMS Cheshire YMCA SPIKE robotics curriculum, trainer preparation, robot readiness records, and synchronized DOCX/Markdown materials in this repository. Use for this program, not unrelated FRC robot code or general LEGO projects.
---

# Maintain the YMCA SPIKE program

Treat the repository as the durable project handoff. Read [AGENTS.md](../../../AGENTS.md), [PROJECT_CONTEXT.md](../../../PROJECT_CONTEXT.md), and the relevant current tasks in [SESSION_PREP.md](../../../SESSION_PREP.md). New information from the user overrides an older snapshot. Do not repeat settled planning questions or mark planned physical work complete without a result.

Choose the existing artifact that serves the request. For trainer preparation, use the [facilitator plan](../../../01_Instructor/Trainer_Session_Plan.md) and [work orders](../../../01_Instructor/Trainer_Work_Orders.md). For the first class, use the current Week 1 deck with speaker notes and its companion identified in the project context. Preserve the two assembled teaching bases, A/B drive wiring, beginner recipe focus, and separate autonomous R3PTAR demonstration.

## Keep paired documents together

For a core document with both DOCX and Markdown, edit the DOCX source with suitable document tools, review its layout, then run these commands from the repository root:

```sh
python scripts/sync_documents.py --write
python scripts/sync_documents.py --check
```

Do not treat a Markdown-only edit as a completed change to a paired document. If the user drafts a Markdown correction, apply it to the Word source before regeneration. Standalone Markdown plans and trackers remain directly editable. See [MAINTENANCE.md](../../../MAINTENANCE.md) for converter limitations and update checks.

## Close the handoff

Update operational results in the prep tracker and material decisions/next work in the project context. Distinguish source/logic checks from actual hardware tests. Follow the user’s standing request to commit and push scoped updates to the existing private repository, preserving unrelated work and verifying the remote commit. If access or a required tool is unavailable, preserve completed local work and identify the actual remaining step. Do not expand this authorization to messages, public publishing, or unrelated repositories.

Use current artifact skills when available for Word/PowerPoint edits. Discover runtime paths on the current computer; do not depend on the original machine’s `.build` directory or installed software. The sync script itself uses standard Python only.
