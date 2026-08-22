<h1 align="center">Grok Research</h1>
<p align="center">
  <a
    href="https://img.shields.io/badge/platform-Grok%20Bot-blue?style=flat-square"
    ><img
      alt="Platform"
      src="https://img.shields.io/badge/platform-Grok%20Bot-blue?style=flat-square"
  /></a>
</p>

<h3 align="center">Turn your Grok Bot into an equity research factory.</h3>

## What it is

Grok Research is an agent distro for Grok Bot.
It turns a Grok Bot into a buy-side equity research factory: persistent researchers, scout reports, official views, and a local sqlite book.
Its mandate is to find high-value ideas with exceptional upside, not to beat an index.

Bots never execute on the captain's computer.
They run on the shared Grok Bot computer. There is no Cursor cloud in this factory.

After install, talk only to Firstmate — the one agent the captain chats with in the factory. No bot takes a live trade.

## Features

- **Scout, update, ship** — a scout investigates and produces a report; an update changes an official view after adversarial review; a ship pursues a name idea.
- **High-upside research** — sector researchers produce a map and a 3–5 name shortlist with outsized upside; name researchers number the durable edge in service of that upside case.
- **Captain-gated name coverage** — a sector shortlist is not a wake. Firstmate signs on or wakes a name researcher only when you authorize that name. `update` and `ship` stay captain-gated.
- **Persistent researchers** — one researcher per sector. Name researchers are signed on only after you authorize the name.
- **Durable research** — reports, official views, and per-bot coverage memory live under `/home/box/agent-data/grok-research/`.
- **Coverage diary** — Firstmate keeps the factory-level coverage diary and handoff record. Each researcher keeps a queryable register, not a prose diary. There is no reporter bot.
- **Local sqlite book** — chat is not the source of truth. Sqlite owns sectors, names, coverage stage, and each name's current view pointer.
- **No live trades** — there is no exchange, brokerage, or order routing.

## Quick Start

Tell any Grok Bot:

```
follow https://github.com/jaredtrichard/grok-research/blob/main/GROK_RESEARCH.md
```

That sets up the factory on the shared computer and hands you over to Firstmate.
Talk only to Firstmate from then on.

```
> scout the latest evidence on XYZ

# A researcher investigates and saves a scout report.

  Scout complete: /home/box/agent-data/grok-research/reports/GR-42.md
```

## How It Works

```
            captain
                  │  work requests and decisions
                  ▼
 ┌─────────────────────────────────────┐
 │ Grok Research                       │
 │ book.db · scout / update / ship     │
 └──┬──────────────┬───────────────┬───┘
    ▼              ▼               ▼
 sector          sector           name
 researcher      researcher       researcher
    └──────────────┴───────────────┘
          talk among themselves
```

Every researcher talks to Firstmate and may talk to other researchers as needed. Only Firstmate talks to the captain.
Each sector has one persistent researcher. Firstmate signs researchers on from one template and writes their role, agent id, book path, and learning notes into the bot. It does not start name coverage until the captain authorizes that name.

The data layer stays on the shared computer:

- `/home/box/agent-data/grok-research/book.db`
- `/home/box/agent-data/grok-research/reports/`
- `/home/box/agent-data/grok-research/views/`
- `/home/box/agent-data/grok-research/memory/<agent-id>.md`

A researcher's coverage memory is a queryable register, not the book, an official view, or a scout report. Firstmate's memory is the factory coverage diary and handoff record.

## License

MIT — see [LICENSE](LICENSE).
