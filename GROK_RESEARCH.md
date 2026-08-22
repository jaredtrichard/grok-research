# Grok Research

Instructions for setting up a buy-side equity research factory on top of Grok Bot.
The user just needs to tell any bot in their Grok Bot: follow this file.

This file is an installer. Do not summarize.

## What you are installing

- A Firstmate the captain talks to from then on
- Global skills: lavish-session, adversarial-review, project-management, ahoy
- Empty directories for scout reports, official views, and per-bot coverage memory
- A book at `/home/box/agent-data/grok-research/book.db`, initialized by Firstmate on first intake
- One researcher template for later sector and name researchers

Do not invent a paper book. Do not pre-create researchers.

## The computers

- The captain's computer: their own machine. Bots never execute here.
- The shared Grok Bot computer: the persistent cloud VM where every bot, the book, research files, browser work, and lavish-axi run.

There is no Cursor cloud in this factory. Do not use grok-ship paths.

## Files in this pack

Same directory as this file:

- `GROK_BOT_FIRSTMATE.md` — Firstmate charter
- `GROK_BOT_RESEARCHER.md` — researcher template
- `skills/lavish-session/SKILL.md`
- `skills/adversarial-review/SKILL.md`
- `skills/project-management/SKILL.md`
- `skills/ahoy/SKILL.md`

## Steps

1. Copy this whole pack to `/home/box/agent-data/grok-research/pack/` on the shared computer (clone or download it first if you only have this file's text). Every later reference to a pack file means that path. If a copy is already there, refresh it.

2. Create these empty directories if they do not exist. Do not seed files into them:
   - `/home/box/agent-data/grok-research/reports/`
   - `/home/box/agent-data/grok-research/views/`
   - `/home/box/agent-data/grok-research/memory/`

3. Look at the existing roster. If a Firstmate already exists, reuse it. Do not create a second.

4. Read `GROK_BOT_FIRSTMATE.md`. CreateAgent name `Firstmate` with that description. If you are already Firstmate, keep your name and update your description instead of cloning yourself.

5. Write four global workflows from the skill files. Names: Lavish session, Adversarial review, Project management, Ahoy. Use each skill's description line as the workflow description. Do not install extra plugins without a yes from the captain.

6. Check for lavish-axi on the shared computer. Minimum version 0.1.53. If missing, run `npx -y lavish-axi@latest` or ask the captain to install it. Confirm that the captain can reach its session URLs. Do not pretend the live loop works without it.

7. Message Firstmate with ready-id `GR-READY`. Tell it the skills are installed, the three empty directories exist, and it must initialize `/home/box/agent-data/grok-research/book.db` with the project-management skill on first intake. Tell it to reply ready against that id and leave a greeting for the captain.

8. Tell the captain to talk only to Firstmate from here. This starter bot is leftover; the captain can delete it from the sidebar. You cannot delete it yourself.

Firstmate signs researchers on later from `GROK_BOT_RESEARCHER.md` only. It fills the role (sector or name), agent id, book path, and learning notes into each bot. One persistent researcher serves each sector; name researchers are added only when needed.
