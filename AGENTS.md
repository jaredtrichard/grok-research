# Project agent memory

Grok Research is a buy-side equity research factory on Grok Bot, not a software factory. Captain talks only to Firstmate (Ass PM is the role). Paper book vs **S&P 500 total return**. No live exchange.

Vocabulary is locked in [README.md](README.md): **scout** (report only), **update** (official view change), **ship** (this repo PR only), **trade** (captain-only paper fill/exit/size), **watch** (keep covering after a no-buy). Do not call view changes "ship" or "view-ship."

Comms: one persistent researcher per sector as hub. Name researchers talk to their sector researcher, not to Firstmate. Charters live in [GROK_BOT_FIRSTMATE.md](GROK_BOT_FIRSTMATE.md), [GROK_BOT_RESEARCHER.md](GROK_BOT_RESEARCHER.md), and [charters/](charters/).

Leave `skills/` in the tree but do not present them as the product. No installer file in this pass (`GROK_RESEARCH.md` is later). Shared-computer paths are `/home/box/agent-data/grok-research/{pack,book.db,reports,views}/` — do not create those on a local Mac.

## Maintaining this file

Keep this file for knowledge useful to almost every future agent session in this project.
Do not repeat what the codebase already shows; point to the authoritative file or command instead.
Prefer rewriting or pruning existing entries over appending new ones.
When updating this file, preserve this bar for all agents and keep entries concise.
