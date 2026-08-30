# SpaceX research file

as_of: 2026-08-30
task: GF-SPCX-1, Gate 1
name_id: spcx
ticker: SPCX

Facts live in `register.md`. This file is the research: how the business makes money, which units drive each segment, and what a three-statement model must number. Do not copy the register. Point at it.

## What this is

Space Exploration Technologies Corp. is a Nasdaq-listed (SPCX) Texas company that reports three CODM segments: Space, Connectivity, and AI. [FACT] `register.md` Reported segments. FY2023–FY2025 statements are retrospectively recast for the xAI / X common-control combinations; they are not stand-alone legacy launch history. [FACT] `register.md` Available annual history. Cursor closed 2026-08-14, after the Q2 print, and is not in Q2 results. [FACT] `register.md` Dilution.

Q2 2026 revenue was $7,814 million. Connectivity was $4,291, AI $2,561, Space $962. [FACT] `register.md` Q2 segment scorecard. LTM revenue $23,044, LTM Adjusted EBITDA $8,305, LTM FCF $(32,348). Last sale $141.50 (Nasdaq lastTradeTimestamp 2026-08-27). Market cap $1,920,554 million. Mixed-date EV $1,859,909 million. [FACT]/[DEDUCTED] `register.md` What is already priced. Sell-side consensus and a consolidated company guide: **not obtained**.

Post-Cursor basic shares 13,572,821,625. Point-in-time fully diluted shares and public float: **not obtained**. Musk 48.4% as-converted economic interest (event 2026-06-30) and 82.3% voting power immediately after the IPO. Latest post-IPO voting percentage: **not obtained**. [FACT]/[DEDUCTED] `register.md` Corporate.

## Node map

Who pays whom, where value sits, what would break it. Sourced flows: `register.md` Node map.

**Value sits in Connectivity.** Q2 operating margin 38.59%, Adjusted EBITDA $2,597 million, capex $1,367 million. Consumer Starlink (12.0 million service lines, $66 monthly ARPU) plus Enterprise & Government (aviation, maritime, mobility, Starlink Mobile, Starshield). Internal Starlink launches do not book Space revenue; launch cost is capitalized into Connectivity satellites. That is the flywheel: Space cadence feeds Connectivity PP&E, Connectivity pays the cash.

**Space is the scarce capacity and the R&D hole.** Company reports more than 80% of global mass to orbit each year since 2023. Q2 Space revenue $962 million against Space R&D $1,076 million and Space capex $1,174 million; operating loss $(542) million. Customer Falcon launches are the revenue unit (10 in Q2, $648 million Launch Services). Internal Falcon launches (27 in Q2) plus Starship (1, all internal to date) are constellation and development spend. NASA Commercial Crew ($4,927.3 million contract value through 2030, status 2022-08-31) and NSSL Phase 3 Lane 2 (SpaceX anticipated $5,923.6 million) sit in Launch & Development and government launch, not as a standalone segment.

**AI is the capex bid, not yet the cash engine.** Q2 AI revenue $2,561 million (+247.5% YoY), operating loss $(1,257) million, capex $15,828 million. Customer B was 19.5% of consolidated Q2 revenue. Nameplate compute 1.4 GW. Advertising is a small line ($367 million Q2). Solutions & Infrastructure ($2,194 million Q2) is the growth and concentration risk.

**What would break the map**

- Connectivity net adds stall, or ARPU keeps falling ($99 in FY2023 → $66 in Q2 2026) without Enterprise mix covering it.
- AI capex ($15,828 million in one quarter) does not convert into contracted infrastructure revenue, or Customer B rolls off.
- Starship remains a cost center past the company’s stated H2 2026 payload-to-orbit expectation, with Space R&D still larger than Space revenue.
- Dilution (Cursor 391 million shares issued; EchoStar ~261.8 million Class A contemplated; 564 million potentially dilutive awards plus 1,331 million unmet-condition awards) outruns per-share value.
- National-security launch share is reassigned if ULA or Blue Origin recover cadence (FY2026 NSSL assignments: SpaceX 5 / $714 million; ULA 2 / $428 million; Blue Origin 0).

Barriers the company names: capital, technical expertise, licenses, spectrum/orbital resources, customer relationships. Cumulative Starship investment exceeded $15,000 million through the prospectus date. Competitor facts (ULA 2026 list, Blue Origin New Glenn anomaly, Amazon Leo 396 satellites / 14 missions including three Falcon 9, OneWeb 600+ satellites) are in `register.md` Barriers. Sourced market shares for most named competitors: **not obtained**.

## Segment drivers

The model must build the income statement from these lines, not from a consolidated plug. Reported CODM segments are three; model splits follow disclosure, not wish.

### 1. Space — Launch Services

Unit: customer Falcon launch, with payload mass as a check.

| driver | obtained | gap |
| --- | --- | --- |
| Customer Falcon launches | 10 Q2 / 17 H1 2026; 33 / 45 / 43 in FY2023 / FY2024 / FY2025 | manifest / cadence guide: not obtained |
| Launch Services revenue | $648 Q2 / $978 H1 | Falcon 9 vs Heavy mix: not obtained |
| Recognized revenue per customer launch | $64.80 Q2 / $57.53 H1 [DEDUCTED] | list price: not obtained |
| Customer mass to orbit | 87 metric tons Q2 / 132 H1 | payload count and $/kg: not obtained |

Internal launches (27 Falcon Q2) are not this line. Do not treat total cadence as revenue cadence.

### 2. Space — Launch & Development

Unit: recognized development / mission revenue (NASA, DoD, other funded work).

| driver | obtained | gap |
| --- | --- | --- |
| Launch & Development revenue | $314 Q2 / $603 H1 | revenue by named contract: not obtained |
| NASA Commercial Crew | $4,927.3 million total contract value through 2030; 14 missions (2022-08-31 status) | remaining unearned and recognition schedule: not obtained |
| NSSL Phase 3 Lane 2 | SpaceX anticipated $5,923.6 million (2025-04-04); FY2026 assignments 5 missions / $714 million | remaining value and year-by-year recognition: not obtained |

Space segment R&D ($1,076 million Q2, “mainly Starship”) and Space capex ($1,174 million Q2) sit on this franchise even when they do not produce Launch & Development revenue.

### 3. Connectivity — Consumer

Unit: average service lines × ARPU. Kit revenue is real and **not obtained** as a separate line, so it currently lives inside consumer revenue.

| driver | obtained | gap |
| --- | --- | --- |
| Ending Starlink service lines | 12.0 million at 2026-06-30; 6.0 million at 2025-06-30; 2.3 / 4.4 / 8.9 million YE2023 / YE2024 / YE2025 | churn, gross adds, geo mix: not obtained |
| ARPU | $66/month Q2 and H1 2026; $85/month year-ago; $99 / $91 / $81 FY2023 / FY2024 / FY2025 | mix vs price cut: not obtained |
| Consumer revenue | $2,485 Q2 / $4,633 H1 | kit ASP, kit cost, subsidies: not obtained |
| LTM Connectivity capex per net add | $822 [DEDUCTED] (includes satellites, launches, kits, ground) | growth vs maintenance split: not obtained |

ARPU is falling while lines are doubling. The model has to take a stand on whether volume still outruns price, and it cannot hide that in a blended Connectivity growth rate.

### 4. Connectivity — Enterprise & Government

Unit: recognized managed-service and government connectivity revenue. Starshield is buried here. [FACT] `register.md` Connectivity.

| driver | obtained | gap |
| --- | --- | --- |
| Enterprise & Government revenue | $1,806 Q2 / $2,915 H1; +$939 Q2 YoY | Starshield / aviation / maritime / mobile split: not obtained |
| Accounting | certain multi-year Starshield revenue over time, cost-to-cost | standalone Starshield revenue, margin, backlog, satellites, customers: not obtained |

Until Starshield is disclosed, do not invent a Starshield segment. Keep a memo line and leave it **not obtained**.

### 5. AI — Advertising

Unit: X advertising revenue. $367 Q2 / $710 H1. [FACT] `register.md` AI. Tesla purchases on X were $0.5 / $4 / $0.1 in 2024 / 2025 / through 2026-04-30. Not a load-bearing driver. Model it as a slow line, not the AI story.

### 6. AI — Solutions & Infrastructure

Unit: recognized infrastructure / subscription / API revenue, with compute capacity as a check.

| driver | obtained | gap |
| --- | --- | --- |
| Solutions & Infrastructure revenue | $2,194 Q2 / $2,669 H1 | GPU-hours, utilization, $/GPU-hour: not obtained |
| Nameplate compute | 1.4 GW at 2026-06-30 | contracted vs idle: not obtained |
| Concentration | Customer B 19.5% of consolidated Q2 revenue, 12.2% of H1 | customer identity and term: not obtained |
| AI capex | $15,828 Q2; AI capex / AI revenue 618% [DEDUCTED] | build vs buy, useful life, utilization ramp: not obtained |

This is where Q2 cash went. The model cannot treat AI as optionality sitting off the statements. Cursor is incremental to this segment after 2026-08-14; Q2 does not include it. Cursor contribution, margin, and overlapping AI product: **not obtained**.

### 7. Starship overlay (not a reportable segment)

Do not forecast Starship revenue until a commercial line is disclosed. Overlay is Space R&D, Space capex, and cadence.

| driver | obtained | gap |
| --- | --- | --- |
| Cumulative investment | >$15,000 million through 2026-06-12 | Starship-only capex: not obtained |
| Starship R&D | $3,004 million FY2025; Space R&D $1,076 Q2 / $2,006 H1 “mainly Starship” | exact H1 Starship R&D: not obtained |
| Tests / launches | 12 cumulative through May 2026; 1 H1 2026 launch, internal | cost per test: not obtained |
| Company expectation | payload delivery to orbit in H2 2026 (prospectus statement, not an outcome) | achieved payload and commercial price: not obtained |
| Design | 100 metric tons to orbit, Starship V3 fully reusable; up to 60 V3 satellites per launch | achieved: not obtained |

### 8. Corporate / financing / eliminations

Carry: interest on $38,433 million debt principal ($25,000 million June notes at 5.855% weighted-average coupon; $13,329 million Valor-related failed sale-leasebacks); taxes; SBC ($1,470 million H1); D&A ($5,290 million H1); IPO cash ($85,675 million net) and notes proceeds. No variable-rate debt at 2026-06-30. Intersegment: internal Starlink launches have no Space revenue. Related-party Tesla Megapacks $329 million H1 are cost/capex, not a revenue node.

## What the three-statement model must number

Build FY2023–H1 2026 history from `register.md`, then a three-year forecast from the segments above. The income statement is the sum of the segments. If it cannot be rebuilt from Launch Services + Launch & Development + Consumer + Enterprise & Government + Advertising + Solutions & Infrastructure + corporate, granularity is too coarse.

Required forecast drivers (use register history; mark **not obtained** rather than invent):

1. Customer Falcon launches and Launch Services revenue per customer launch.
2. Launch & Development revenue path from remaining NASA / NSSL / other funded work — remaining schedule **not obtained**, so state the assumption.
3. Starlink ending lines and ARPU; consumer revenue as lines × ARPU plus kit (kit **not obtained**).
4. Enterprise & Government connectivity growth without a fake Starshield split.
5. Advertising vs Solutions & Infrastructure separately; Customer B concentration as a named risk, not a hidden growth rate.
6. Starship as R&D/capex/cadence, not revenue, until disclosed.
7. Segment capex: Connectivity per net add, Space per launch, AI as the residual cash bid. H1 2026 FCF was $(25,010) million because capex was $28,476 million against $3,466 million operating cash flow. Cash + marketable securities $100,009 million at 2026-06-30 funds the bid for now.
8. Shares: start from 13,572,821,625 post-Cursor basic; layer EchoStar ~261.8 million if/when closed; do not pretend fully diluted is known.
9. Backlog $47,461 million and deferred revenue $14,286 million as working-capital constraints, not as a revenue plug. Segment backlog: **not obtained**.
10. Recast history includes xAI/X; Cursor is a H2 2026 step-up with **not obtained** contribution. Do not back-cast Cursor into Q2.

Annual history to seed the workbook (all $ millions; FCF = OCF − capex):

| year | revenue | operating income | net income | OCF | capex | FCF |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2023 | 10,387 | (3,505) | (4,628) | 4,520 | 4,415 | 105 |
| 2024 | 14,015 | 466 | 791 | 5,776 | 11,163 | (5,387) |
| 2025 | 18,674 | (2,589) | (4,937) | 6,785 | 20,737 | (13,952) |

Point at `register.md` Available annual history for gross profit, opex, cash, and debt. H1 2026 and Q2 segment lines are in the register scorecard, not repeated here.

## Capital cycle the forecast has to live inside

Capex $4,415 → $11,163 → $20,737 → $28,476 (FY2023 / FY2024 / FY2025 / H1 2026). Q2 capex mix: AI $15,828 / Connectivity $1,367 / Space $1,174. FCF has not inflected; cash burn is capex, not an operating-cash collapse (LTM OCF $9,900 million). EchoStar spectrum consideration ~$19,600 million (~$11,100 million equity at $42.40 plus up to $8,500 million tied to EchoStar debt payoff) is a pending cash-and-dilution event; closing: **not obtained**. Non-cancelable commitments $27,955 million at 2026-06-30, primarily AI infrastructure, third-party cloud, other services, and spectrum.

## Gaps that block precision, not the model

Leave these **not obtained** and do not fill them with folklore:

- 10-K and proxy (none filed through 2026-08-30)
- Fully diluted shares, float, current voting power
- Quoted launch price, Falcon 9 vs Heavy mix, payload $/kg
- Starship-only capex and commercial price
- Starlink churn, kits, Gbps, managed-customer count
- Standalone Starshield
- Segment backlog
- GPU-hours, utilization, Cursor P&L
- Sell-side consensus and quantitative consolidated guide

Primary documents opened are catalogued at the bottom of `register.md`.

## Model instruction

Next artifact is `models/spcx/`: `segments.md`, `income.md`, `balance.md`, `cashflow.md`. Valuation is not this file. Thesis is not this file. If a later sentence is not in those statements, it is not the thesis.
