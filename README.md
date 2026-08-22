<h1 align="center">Grok Research</h1>
<p align="center">
  <a
    href="https://img.shields.io/badge/platform-Grok%20Bot-blue?style=flat-square"
    ><img
      alt="Platform"
      src="https://img.shields.io/badge/platform-Grok%20Bot-blue?style=flat-square"
  /></a>
</p>

<h3 align="center">Buy-side equity research factory on Grok Bot.</h3>

## What it is

Grok Research is an agent distro for Grok Bot.
It turns a Grok Bot into a buy-side equity research factory: persistent researchers, official views, and Firstmate as the only agent the captain talks to.

Bots never execute on the captain's machine.
They run on the shared Grok Bot computer.

Talk only to **Firstmate**. Ass PM is the role, not the public name. Firstmate never takes a live trade.

## Vocabulary

| Word | Who authorizes | What it is | What it is not |
| --- | --- | --- | --- |
| **scout** | Firstmate files; no captain "make the change" | Investigation. Deliverable = report under `/home/box/agent-data/grok-research/reports/<task id>.md`. | Not an update. Not a ship. |
| **update** | Captain | A view change. New or revised official view under `/home/box/agent-data/grok-research/views/`. Adversarial review of the view before it is current. | Not a ship. Not a scout. |
| **ship** | Captain | Pursue a name idea. | Not a repo change. Not code. Not an update. |
| **watch** | Captain | Keep covering a name. | Not a drop. |

Do not call a view change "ship." Use **update**. Do not call a repo change "ship."

Two ladders, never collapsed:

- **Task:** scout → update.
- **Coverage:** idea → investment. A paper book is deferred; do not treat a ship or an update as a fill.

Promoting a scout to an update changes the official view. It is not a ship.

## Comms graph

Each **sector has its own persistent researcher**. Every researcher talks to Firstmate; they are on equal footing. Researchers also talk among themselves as needed — a mesh, not only name↔sector and name↔jurisdiction. Jurisdiction still joins when a listing, filing, or legal boundary is in play. Idea gen, inbox, docs, and models sign on as needed and may talk to others as needed; idea gen is not a routing hub and does not own coverage. Only Firstmate talks to the captain. The research factory is Firstmate plus idea, sector, name, and jurisdiction researchers.

```
            captain
                  │  talk only to Firstmate
                  ▼
 ┌─────────────────────────────────────────┐
 │ Firstmate (Ass PM)                      │
 │ book.db · scout / update / ship         │
 └──┬───────────┬───────────┬───────────┬──┘
    ▼           ▼           ▼           ▼
 idea gen    sector      name        jurisdiction
    └──────────┴───────────┴───────────┘
         talk among themselves as needed
```

Firstmate always delegates grind. No subagents on Firstmate. Firstmate never calls Cursor cloud. Secrets are per-bot; never pasted in chat. Task ids on every handoff; empty outcomes still reported.

## Scorecard

A paper book versus **S&P 500 total return** is deferred — too complex to add now. Do not fake a substitute scorecard. No live exchange or brokerage in v1.

## Shared computer

Suggested paths on the Grok Bot computer (not a local Mac app):

- Pack: `/home/box/agent-data/grok-research/pack/`
- Book db: `/home/box/agent-data/grok-research/book.db`
- Scout reports: `/home/box/agent-data/grok-research/reports/`
- Official views: `/home/box/agent-data/grok-research/views/`
- Coverage memory: `/home/box/agent-data/grok-research/memory/<agent-id>.md` — one file per signed-on bot

Sqlite owns which sectors and names exist, coverage stage, and the current official view pointer. Charters are rules, not the coverage list. Each signed-on agent also keeps its own coverage memory at that path: read at the start of work, write before context dies. That file is not the book, not an official view, and not a scout report. Firstmate's file is factory-level (routing, roster, open handoffs), not a substitute for a researcher's coverage memory.

## Non-goals

- Not a software factory.
- Not a local Mac app.
- No live exchange, brokerage, or order routing in v1.
- No paper book in the current product.
- No researcher takes a live trade.
- No Firstmate grind, subagents, or Cursor cloud.
- Ass PM is not a public bot name.
- One shared sector agent is forbidden.
- Skills and installer are later work, not this pack's public face.

## Charters

Installer: [GROK_RESEARCH.md](GROK_RESEARCH.md).

- [GROK_BOT_FIRSTMATE.md](GROK_BOT_FIRSTMATE.md) — Ass PM; public name Firstmate
- [GROK_BOT_RESEARCHER.md](GROK_BOT_RESEARCHER.md) — generic researcher template
- [charters/GROK_BOT_SECTOR.md](charters/GROK_BOT_SECTOR.md) — instantiate one bot per sector
- [charters/GROK_BOT_NAME.md](charters/GROK_BOT_NAME.md)
- [charters/GROK_BOT_IDEA.md](charters/GROK_BOT_IDEA.md)
- [charters/GROK_BOT_JURISDICTION.md](charters/GROK_BOT_JURISDICTION.md)

## License

MIT — see [LICENSE](LICENSE).
