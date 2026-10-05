---
name: Project management
description: Use at Grok Research intake and whenever work is handed to a researcher.
---

# Project management

A local sqlite database is the research book. Chat is not the source of truth.

Authoritative product: `README.md`, `GROK_BOT_FIRSTMATE.md`, `GROK_BOT_RESEARCHER.md`, `charters/`.

## Database path

On the shared Grok Bot computer:

`/home/box/agent-data/grok-research/book.db`

Create the parent directory if needed. Same path every time. Do not invent a second database. Do not create this file on the captain's Mac.

Scout reports live beside it in `/home/box/agent-data/grok-research/reports/`, one file per task id.
Official views live in `/home/box/agent-data/grok-research/views/`.
Coverage memory is **not** this database. Each bot keeps `/home/box/agent-data/grok-research/memory/<agent-id>.md`.

## Schema

```sql
CREATE TABLE IF NOT EXISTS projects (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  created_at INTEGER NOT NULL
);

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
  jurisdiction TEXT,
  view_ref TEXT,
  created_at INTEGER NOT NULL,
  updated_at INTEGER
);

CREATE TABLE IF NOT EXISTS tasks (
  id TEXT PRIMARY KEY,
  kind TEXT NOT NULL,
  title TEXT NOT NULL,
  prompt TEXT NOT NULL,
  project_id TEXT,
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

`names.stage` is `idea`, `investment`, or `watch`.
`names.view_ref` is the current official view path, or null until the first update.

`tasks.kind` is `scout`, `update`, `ship`, or `decision`.
`tasks.status` is `queued`, `underway`, `blocked`, `done`, or `cancelled`.
`tasks.result` is the outcome pointer: scout or ship report path, or update view path.
`gate_kind` is optional: `after-task`, `at-time`, or `captain`.

The schema is deliberately minimal. Do not add a fills or positions table. Do not add a portfolio stage. Do not add a trade or platform-ship task kind.

## Setup

If `book.db` does not exist on the shared Grok Bot computer, create it and run the schema. If it exists, do not migrate inventively. Report the path to Firstmate.

## Intake

Firstmate writes a task row before handing work off. Reuse the task id in the researcher message. A good `prompt` states the goal, acceptance criteria, and constraints — enough to act on without coming back for basics.

Research work files under the reserved `book` project row. Create that row on first use (`id` = `book`). Nothing else is required. Do not invent a `default` or `platform` project.

If the work belongs to a sector that has no sector row, sign on a researcher from `charters/GROK_BOT_SECTOR.md` and insert the sector row (`researcher_id` required). If a sector row already maps that sector to a researcher, reuse that researcher.

If the work belongs to a name that has no name row, insert the name (`stage` = `idea` unless the captain already said `investment` or `watch`) and sign on a name researcher from `charters/GROK_BOT_NAME.md` when that name needs its own bot. If a name row already maps that name to a researcher, reuse that researcher.

Firstmate talks to any researcher. Researchers talk among themselves as needed. Do not route only through a sector hub.

## Two ladders

Never collapse these.

**Task ladder:** scout → update. When the captain authorizes a view change after a scout, do not open a duplicate task: flip the same row's kind to `update` and hand it back to the researcher with the scout report as context.

**Coverage ladder:** idea → investment. `watch` exists (keep covering). Coverage stage lives on `names.stage`. Update it only on captain word. An update does not promote coverage. A ship does not promote coverage and does not change the official view.

When the captain authorizes pursuing a name idea, file a `ship` task. That is not an update and not a scout promotion.

## Updates

The researcher updates `status`, `result`, and `updated_at` as it goes. Done means `result` holds the pointer: report path for scout or ship, view path for update. After a successful update, set `names.view_ref` to that view path.

## Do not

- Do not keep the book only in chat
- Do not treat sqlite as a bot's coverage memory
- Do not write a fill or invent a paper book
- Do not create one Firstmate per sector or name
- Do not open a pull request from this factory
