# Grok Research

Instructions for setting up a buy-side equity research factory on top of Grok Bot.
The user just needs to tell any bot in their Grok Bot: follow this file.

This file is an installer. Do not summarize.

## What you are installing

- A Firstmate the captain talks to from then on
- Global skills from this pack: lavish-session, adversarial-review, project-management, ahoy
- Empty factory dirs for reports, views, and per-bot memory
- A book path at `/home/box/agent-data/grok-research/book.db` (Firstmate inits the book on first intake)
- A researcher template and thin charters for later sign-on

Do not invent a paper book. Do not create a paper-book file or directory.

## The computers

- The captain's Mac: their own machine. Bots never execute here.
- The shared Grok Bot computer: a persistent cloud VM that runs every bot. Pack, book, reports, views, memory, skills, browser grind, and lavish-axi all run here.

There is no Cursor cloud in this factory. Do not sign on a crewmate. Do not use grok-ship paths.

## Files in this pack

Same directory as this file:

- `GROK_BOT_FIRSTMATE.md` — Firstmate charter (Ass PM; public name Firstmate)
- `GROK_BOT_RESEARCHER.md` — generic researcher template
- `charters/GROK_BOT_IDEA.md`
- `charters/GROK_BOT_SECTOR.md`
- `charters/GROK_BOT_NAME.md`
- `charters/GROK_BOT_JURISDICTION.md`
- `skills/lavish-session/SKILL.md`
- `skills/adversarial-review/SKILL.md`
- `skills/project-management/SKILL.md`
- `skills/ahoy/SKILL.md`

## Steps

1. Copy this whole pack to `/home/box/agent-data/grok-research/pack/` on the shared computer (clone or download it first if you only have this file's text). Every later reference to a pack file means that path. If a copy is already there, refresh it. Never copy to a grok-ship path.

2. Create these empty directories if they do not exist. Do not seed files into them.

   - `/home/box/agent-data/grok-research/reports/`
   - `/home/box/agent-data/grok-research/views/`
   - `/home/box/agent-data/grok-research/memory/`

   Do not create a paper book. Do not invent other factory roots.

3. Point the book at `/home/box/agent-data/grok-research/book.db`. Schema is owned by the project-management skill. That skill is still landing, so do not invent a schema and do not run a grok-ship `factory.db` init. Firstmate inits the book on first intake.

4. Look at the existing roster (agent profile folders). If a Firstmate already exists, reuse it. Do not create a second.

5. Read `/home/box/agent-data/grok-research/pack/GROK_BOT_FIRSTMATE.md`. CreateAgent name `Firstmate` with that description. If you are already Firstmate, keep your name and update your description instead of cloning yourself.

6. Do not pre-create researchers at install. Firstmate signs them on later from `/home/box/agent-data/grok-research/pack/GROK_BOT_RESEARCHER.md` plus the matching thin charter under `pack/charters/`. One persistent researcher per sector; never one shared sector agent. Do not pre-create inbox, docs, or models. Do not sign on a platform researcher. Do not invent a sector or name just to have a bot.

7. After the pack is copied, write four global workflows from `pack/skills/`. Names:

   - Lavish session
   - Adversarial review
   - Project management
   - Ahoy

   Use each skill's description line as the workflow description. Do not install extra plugins without a yes from the user.

8. Check for lavish-axi on the shared computer. Minimum version 0.1.53. If missing, run `npx -y lavish-axi@latest` or ask the captain to install it. Session URLs are served from the shared computer and the captain views them from their own computer, so confirm they can reach it (tailnet or exposed address). Do not pretend the live loop works without it.

9. Message Firstmate with ready-id `GR-READY`. Tell it the pack path, the four skills, the empty dirs, and that the book is `/home/box/agent-data/grok-research/book.db` (Firstmate inits it on first intake). Tell it to reply ready against that id. Empty or blocked still gets a reply. Tell Firstmate to leave a greeting message to the captain.

10. Tell the captain: talk only to Firstmate from here. This starter bot is leftover. They can delete it from the sidebar (right-click the row, Delete). You cannot delete it yourself.
