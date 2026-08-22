---
name: Project management
description: Use at Grok Research intake and whenever work is handed to a researcher.
---

# Project management

A local sqlite database is the research book. Chat is not the source of truth.

## Database path

On the shared Grok Bot computer:

`/home/box/agent-data/grok-research/book.db`

Create the parent directory if needed. Same path every time. Do not create this file on the captain's computer.
Scout reports live in `/home/box/agent-data/grok-research/reports/`, official views in `/home/box/agent-data/grok-research/views/`, and each bot's separate coverage memory in `/home/box/agent-data/grok-research/memory/<agent-id>.md`. Firstmate's file is the factory coverage diary and handoff record. A researcher's file is a queryable register, not a prose diary.

## Schema

```sql
CREATE TABLE IF NOT EXISTS sectors (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  researcher_id TEXT NOT NULL,
  created_at INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS names (
  id TEXT PRIMARY KEY,
  ticker TEXT,
  name TEXT NOT NULL,
  sector_id TEXT NOT NULL,
  researcher_id TEXT,
  stage TEXT NOT NULL,
  listing_venue TEXT,
  view_ref TEXT,
  created_at INTEGER NOT NULL,
  updated_at INTEGER
);

CREATE TABLE IF NOT EXISTS tasks (
  id TEXT PRIMARY KEY,
  kind TEXT NOT NULL,
  title TEXT NOT NULL,
  prompt TEXT NOT NULL,
  name_id TEXT,
  sector_id TEXT,
  status TEXT NOT NULL,
  gate_kind TEXT,
  gate_ref TEXT,
  result TEXT,
  created_at INTEGER NOT NULL,
  updated_at INTEGER
);
```

`names.stage` is `idea`, `investment`, or `watch`. `names.listing_venue` is optional data, not a researcher role or routing hook. `names.view_ref` is the current official view path, or null.

`tasks.kind` is `scout`, `update`, `ship`, or `decision`. `tasks.status` is `queued`, `underway`, `blocked`, `done`, or `cancelled`. `tasks.result` is the outcome pointer. `gate_kind` is optional: `after-task`, `at-time`, or `captain`.

The schema is deliberately minimal. Do not add execution or portfolio tracking, a portfolio stage, or a trade task kind.

## Setup

On Firstmate's first intake, if `book.db` is missing, create it and run the schema above. This `listing_venue` and no-`projects` schema applies only to fresh books. If `book.db` exists, leave its schema and data untouched; this pack does not migrate existing books.

## Intake

Firstmate writes a task row before handing work off. Reuse the task id in the researcher message. The prompt carries the goal, acceptance criteria, and constraints.

If a sector has no row, Firstmate fills `GROK_BOT_RESEARCHER.md` for that sector, signs on one persistent researcher, and inserts the row. Reuse that researcher thereafter; never create one shared researcher for multiple sectors.

When a sector shortlist names a ticker, insert a `names` row if missing, with stage `idea` and `researcher_id` null. A shortlist is not a wake. Sign on or wake a name researcher from the same template only after the captain authorizes that name; then set `researcher_id`. If the captain states a stage, use it; otherwise leave `idea`. Researchers may talk to Firstmate and one another directly.

## Promotion and updates

When the captain authorizes a view change after a scout, flip the same task row from `scout` to `update` and provide the report as context. A `ship` pursues a name idea; it is not an update and does not change coverage stage or the current view. Direction commit and coverage-stage promotion are captain word; the name researcher drafts LONG / SHORT / PASS and does not write `names.stage`.

Researchers update `status`, `result`, and `updated_at` as they work. After an approved update, set `names.view_ref` to the official view path. Change `names.stage` only on captain word.

## Do not

- Do not keep the book only in chat
- Do not treat sqlite as coverage memory
- Do not take a live trade
- Do not open a pull request from this factory
