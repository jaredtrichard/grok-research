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
It turns a Grok Bot into a buy-side equity research factory: persistent researchers, a paper book scored against **S&P 500 total return**, and Firstmate as the only agent the captain talks to.

Bots never execute on the captain's machine.
They run on the shared Grok Bot computer.

Talk only to **Firstmate**. Ass PM is the role, not the public name. Firstmate never takes a trade.

## Vocabulary

| Word | Who authorizes | What it is | What it is not |
| --- | --- | --- | --- |
| **scout** | Firstmate files; no captain "make the change" | Investigation. Deliverable = report under `/home/box/agent-data/grok-research/reports/<task id>.md`. | Not a trade. Not a PR. |
| **update** | Captain | Authorized official view change. Deeper pursuit of an idea or investment. New or revised official view under `/home/box/agent-data/grok-research/views/`. Adversarial review of the view before it is current. | Not a trade. Not a PR. |
| **ship** | Captain | Repo PR for `jaredtrichard/grok-research` (platform/code). Branch, review, PR; captain merges. | Not research. Not a trade. Keep this word for this repo only. |
| **trade** | Captain only | Paper-portfolio fill, exit, or size change. | Not an update. Not a ship. Researchers never execute it. |
| **watch** | Captain, at the investment gate | Keep covering after a no-buy. | Not a drop. Not a fill. |

Do not call official view changes "ship" or "view-ship." Use **update**.

Two ladders, never collapsed:

- **Task:** scout → update (research) or scout → ship (platform).
- **Coverage:** idea → investment → paper portfolio **or** watch.

Promoting a scout to an update does not put a name in the book. Firstmate never flips an update into a fill.

## Comms graph

Each **sector has its own persistent researcher**. That bot is the hub for that sector: it talks to that sector's name researchers and to Firstmate. Name researchers talk to their sector researcher, not to Firstmate. Jurisdiction joins when a listing, filing, or legal boundary is in play. Idea gen, inbox, docs, and models sign on as needed. One platform researcher owns this repo only.

```
            captain
                  │  talk only to Firstmate
                  ▼
 ┌─────────────────────────────────────────┐
 │ Firstmate (Ass PM)                      │
 │ book.db · scout / update / ship / trade │
 └──┬───────────┬────────────┬─────────────┘
    │           │            │
    ▼           ▼            ▼
 idea gen   sector hub    platform
                │         (this repo)
                ▼
         name researchers
                │
        jurisdiction joins
```

Firstmate always delegates grind. No subagents on Firstmate. Firstmate never calls Cursor cloud. Secrets are per-bot; never pasted in chat. Task ids on every handoff; empty outcomes still reported.

## Scorecard

Paper book versus **S&P 500 total return**. No live exchange or brokerage in v1. Captain alone takes trades. Code PRs exist only for platform/repo work.

Price return is the wrong scorecard (drops dividends). Russell 3000 is wrong unless the charter is all-cap. A hedge-fund or market-neutral index is wrong without shorts.

## Shared computer

Suggested paths on the Grok Bot computer (not a local Mac app):

- Pack: `/home/box/agent-data/grok-research/pack/`
- Book db: `/home/box/agent-data/grok-research/book.db`
- Scout reports: `/home/box/agent-data/grok-research/reports/`
- Official views: `/home/box/agent-data/grok-research/views/`

Sqlite owns which sectors and names exist, coverage stage, and the current official view pointer. Charters are rules, not the coverage list.

## Non-goals

- Not a software factory.
- Not a local Mac app.
- No live exchange, brokerage, or order routing in v1.
- No researcher takes a trade.
- No Firstmate grind, subagents, or Cursor cloud.
- Ass PM is not a public bot name.
- One shared sector agent is forbidden.
- Skills and installer are later work, not this pack's public face.

## Charters

- [GROK_BOT_FIRSTMATE.md](GROK_BOT_FIRSTMATE.md) — Ass PM; public name Firstmate
- [GROK_BOT_RESEARCHER.md](GROK_BOT_RESEARCHER.md) — generic researcher template
- [charters/GROK_BOT_SECTOR.md](charters/GROK_BOT_SECTOR.md) — instantiate one bot per sector
- [charters/GROK_BOT_NAME.md](charters/GROK_BOT_NAME.md)
- [charters/GROK_BOT_IDEA.md](charters/GROK_BOT_IDEA.md)
- [charters/GROK_BOT_JURISDICTION.md](charters/GROK_BOT_JURISDICTION.md)
- [charters/GROK_BOT_PLATFORM.md](charters/GROK_BOT_PLATFORM.md) — `jaredtrichard/grok-research` only

## License

MIT — see [LICENSE](LICENSE).
