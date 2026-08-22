# Project agent memory

This file is the project's committed home for project-intrinsic agent knowledge: build, test, release, architecture, and sharp-edge notes that should travel with the code.

- Every signed-on bot keeps its own durable coverage memory at `/home/box/agent-data/grok-research/memory/<agent-id>.md` (read at start of work, write before context dies). Firstmate's file is factory-level, not a researcher's store. That is not the book, views, reports, or charter learning notes. See `GROK_BOT_RESEARCHER.md` and `GROK_BOT_FIRSTMATE.md`.

## Maintaining this file

Keep this file for knowledge useful to almost every future agent session in this project.
Do not repeat what the codebase already shows; point to the authoritative file or command instead.
Prefer rewriting or pruning existing entries over appending new ones.
When updating this file, preserve this bar for all agents and keep entries concise.
