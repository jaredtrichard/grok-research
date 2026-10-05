# NEM house model — file map

As-of: Saturday 22 Aug 2026 (America/New_York). Clock: **3y run-rate remake of FY26 company guide**, not a Y1/Y2/Y3 ounce path. GOLD-METAL locked: 3900 / 4500 / 4900 / 5900. Official mid = printed guide (no haircut).

Directory: `/home/box/agent-data/grok-research/models/NEM/`

| File | Role |
| --- | --- |
| `segment.csv` | Per-mine / JV Model tab. Attrib oz + unit cost + sustain/growth. Rolls to 5,260 koz / $1,950m / $1,400m. |
| `is.csv` | Consol. P&L run-rate at four gold nodes. Guide opex. Gold lever $505m pretax / $100. |
| `bs.csv` | Simplified debt (one cash, one debt, leases). 30 Jun print + July $606m haircut. |
| `cf.csv` | Company FCF and the $4,500 node computed from 1H + H2 capex seasonality. |
| `valuation.csv` | Official EV/EBITDA PTs (historical k). `k_history.csv` + `tie.json`. |

Draft view (not current): `/workspace/NEM-VIEW-draft.md` **and** `/home/box/agent-data/grok-research/views/NEM.md` (same draft). Status **draft — not current**. Stage stays **watch**.

## How the files tie

### Segment → consol (Model → Financials)

1. `segment.oz_koz` sums to **5,260** (official mid). Managed 3,915 + NGM 935 + PV 255 + FdN 155. Sourced Feb 19 site table (SEC Exhibit 99.1 / ASX copy). Reaffirmed 23 Jul as totals; site table was not reprinted in Q2 — site cells stay Feb 19.
2. NGM **38.5%**. **935 koz is sourced** from Feb 19 guidance PR/exhibit (URL on the row). Not a desk 100% figure.
3. PV 40% and FdN 32% ounces are **inside 5,260**. Cash = distributions only when sourced (Q2 PV $100m, FdN $93m). **Not annualized.** CAS/AISC/capex empty (guide is production-only; capital guidance excludes PV).
4. Sustain site sum **1,935** vs guide **1,950**. Residual **$15m** on Corporate / rounding row, labelled **computed residual to guide total**. Growth sites sum **1,400** exact.
5. Consol unit costs on IS are the **company totals** ($1,055 CAS / $1,680 AISC), not a re-weighted site blend.

### IS NI → CF (what holds, what does not)

**Identity that holds on CF:**

`FCF := CFO − additions to PP&E` (company definition; growth and capitalized interest **in**).

In `cf.csv` this is forced: `cfo_implied_by_fcf_identity = fcf_remade + cash_ppe_guide` with `cash_ppe_guide = 1,950 + 1,400 + 175 = 3,525`.

**Identity that does NOT close (and is not plugged):**

`CFO := NI + D&A + non-cash + WC − cash tax timing − reclamation cash vs accretion + equity distributions`

Empty on purpose: `working_capital`, `equity_income_affiliates` (FY), `nci` (FY), `ni_attributable_to_nem`, `cfo_before_wc`. Those cells are **UNSOURCED**, not invented. 1H prints exist and are cited; they are not FY plugs.

IS `ni_before_equity_and_nci` is a **guide-cost book** number (gold sales − by-product CAS − guided G&A / exploration / D&A / accretion / interest, then company $505m/$100 from the $4,500 node, then 33% tax). CF `fcf_remade` is a **1H-cash run-rate** remade to gold. They are different bases. Do not force NI = FCF.

### Cash roll

`bs.net_cash_incl_leases = cash − debt − leases` (9,009 − 5,083 − 515 = **3,411**) — sourced 30 Jun.

Official valuation residual (16 Jul share date):

`net_cash_after_july_buybacks = 3,411 − 606 = 2,805`

$1.95bn NGM cheque is **out of the official mid** (footnote $1.85/sh). A full YE cash roll (dividends, further buybacks, WC, FX) is **UNSOURCED** and not built.

### FCF definition and $4,500 node

Company: FCF = CFO − all cash PP&E.

**$4,500 node (computed, labelled):**

- 1H FCF **$5,349m** sourced.
- H2 extra capex vs H1 = (1,950 × 0.58 − 819) + (1,400 × 0.63 − 524) = **$670m** (23 Jul seasonality 58/63).
- If 1H FCF repeats before that extra spend: H2 **$4,679m**. FY **$10,028m**.
- Remake: `FCF(G) = 10,028 + 3.38 × (G − 4,500)` using **$338m AT / $100** = $505m × (1 − 0.33). The ~$6/oz royalty/tax/workers rider is **not** in the midpoint.

This remake embeds H1 unit-cost outperformance (1H by-product AISC $1,321 vs guide $1,680). That is a **cash node**, not a silent guide haircut. Guide-miss lives in the draft-view sensitivity.

### EBITDA (official E)

- **Official E** = `is.csv` **`EBITDA_IS_computed`** (guide-cost EBIT+D&A): **12,513 / 15,423 / 17,363 / 22,213** at 3,900 / 4,500 / 4,900 / 5,900.
- TTM Adj. **$16,765** and `EBITDA_TTM_remade_505` (14,999 / 18,029 / 20,049 / 25,099) are **rival 5 only** (TTM-fat × hist k → $80 / $157 / $175 / $304).
- **Do not** use (gold − AISC) × oz as EBITDA.

## Official k (22 Aug 2026 remake — valuation only)

Operating `is.csv` / `bs.csv` / `cf.csv` / `segment.csv` **not rewritten**. Official PT is **EV/EBITDA** (HOUSE-MODEL §4.0).

- **E official** = `EBITDA_IS_computed` **12,513 / 15,423 / 17,363 / 22,213**.
- **k official** from WSN YE EV/EBITDA 2016–2025 (https://wallstreetnumbers.com/stocks/nem/ev-ebitda). **Bear 5.45 / base 9.04 (mid-of-range, not median 8.36) / bull 12.63**. Official PTs **$67 / $151 / $269**. 7.0× check on guide E **$86 / $118 / $150**.
- **ND = −2,805** (net cash $2,805m; $1.95bn cheque **out**). Shares **1,053.692271m**.
- Files: `valuation.csv` (kit columns), `k_history.csv`, `tie.json`.
- Status **draft**. Stage **watch**. Do not flip current. Do not ship.

### Sources (canonical)

- Feb 19 2026 Exhibit 99.1: https://www.sec.gov/Archives/edgar/data/1164727/000116472726000009/newmontq42025earningsand20.htm
- ASX copy of same: https://announcements.asx.com.au/asxpdf/20260220/pdf/06wjfkvtcljwn0.pdf
- Q2 23 Jul Exhibit 99.1: https://www.sec.gov/Archives/edgar/data/1164727/000116472726000034/newmontq22026earningsrelea.htm
- 10-Q 30 Jun / 16 Jul shares: https://www.sec.gov/Archives/edgar/data/1164727/000116472726000036/nem-20260630.htm
- NGM 8-K 10 Aug: https://www.sec.gov/Archives/edgar/data/1164727/000110465926095968/tm2623048d1_8k.htm

Kit: `/workspace/HOUSE-MODEL.md`. Scout: `/workspace/NEM-SCOUT.md`. Gold: `/workspace/GOLD-METAL-VIEW.md`.
