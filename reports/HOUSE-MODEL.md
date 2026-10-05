# HOUSE-MODEL — gold name operating + valuation kit

| Field | Value |
| --- | --- |
| Id | HOUSE-MODEL |
| Kind | scout / kit |
| Status | **draft-for-names** |
| As-of | Saturday 22 Aug 2026 (America/New_York) |
| Official gold line | `/home/box/agent-data/grok-research/views/GOLD-METAL.md` — **current**. **DO NOT RETUNE.** Copy the numbers below. File wins if chat differs. |
| Horizon | **3 years — to 22 Aug 2029** |
| 12-month path | check-in only (to 22 Aug 2027); **not** the official gold or equity line |
| Who runs it | Every gold **name** researcher. Colour and one-off 7× remakes are not a substitute. |
| Style | **T. Rowe-style miner kit** — operating build as guided, hedge the miss. Default **md+csv**, not an xlsx clone. |
| T. Rowe workbook | `/workspace/trowe/FCX Model.xlsx` — name template. **Load-bearing:** Model (per-segment) → Financials. Debt **simplified**. Summary tabs (**Share Price / Financial Summary / Valuation / Other**) **dropped**. |
| Guide convention | **Official mid = company guide.** Sensitivities / invalidation hold the miss. No path-weighted unprinted cut. (Captain 22 Aug 2026.) |
| Fully modeled | **Each reporting segment** has its own volume / cost / revenue path into consol. **IS / BS / CF**. A single rolled-up EBITDA × 7× is **not** enough. Missing segment = **UNSOURCED**, not a plug. |
| Official PT | **EV/EBITDA**. `k` = that name’s **sourced historical EV/EBITDA range** (as-of, window, what E). Base = **mid**, bull = **high**, bear = **low**. 7.0× T. Rowe is a **check**. If history **UNSOURCED**, no official mid. |
| What this kit does **not** do | Does **not** change `names.stage` (stay **watch**). Does **not** ship. Does **not** flip a view current. Does **not** edit GOLD-METAL. Does **not** invent TIPS/DXY paths. Does **not** rebuild 3y gold S/D. GOLD-RATES does **not** move **4,900 / 5,900 / 3,900**. |

This is the shared **operating + valuation method**. Official output is a quantified **$/sh** (base / bull / bear **or** band + midpoint) on the **same three GOLD-METAL scenarios**. The name researcher owns the official view. Models may tell them the numbers this kit produces. Adversarial review of any view still happens **before** current.

Captain 22 Aug 2026: house models should **mirror his T. Rowe Price metals model as best they can**. That model **is** `FCX Model.xlsx`. **Keep the per-segment mapping into the financials.** **Include the three statements (IS, BS, CF).** Formatting does not matter; good numbers do; he does not need to see the sheets. **Simplify the debt schedule. Drop the summary tabs.** Operating build as guided; hedge the miss (§3.0).

---

## 0. T. Rowe layout — Model → Financials (summary tabs dropped)

**Template:** `/workspace/trowe/FCX Model.xlsx`. There is **no** gold-name T. Rowe workbook. This **is** the name template. Captain 22 Aug: **simplify the debt schedule. Drop the summary tabs. Keep the per-segment mapping into the financials.** That is the load-bearing part (Model → Financials), **not** Share Price / Financial Summary extras.

### Required (load-bearing)

**HARD RULE — fully modeled means segments AND statements.** Captain 22 Aug: he wants **both**. Confirm: numbers later bots can re-read; every material line **sourced or labelled computed**; IS/BS/CF **tie**; default **md+csv** under `models/<ticker>/`; **xlsx optional**.

**A single company EBITDA × 7× is not a house model.** That is a colour remake. It does **not** satisfy this kit.

**Each reporting segment** (as the company reports it: mine, region, or royalty asset) must have its **own** volume / cost / revenue path that **feeds** consol. IS / BS / CF. If a segment is missing: write **UNSOURCED** and **do not plug** it (do not spread residual ounces, do not scale last year’s mix, do not dump the gap into “other”).

**Model — per segment, then roll up.** Copy the FCX spine, swap sites for the name’s mines / regions / royalty assets:

1. Commodity header: gold from **GOLD-METAL** (4,900 / 5,900 / 3,900). Other metals from **MASTER** if the name has a by-product; **do not retune gold** from MASTER (2024-01-01 Base $2,000 is stale).
2. **Each segment** (mine or region, attributable): throughput / grade only if the company prints them; otherwise start at **guided oz or GEO** and **guided unit cost**. Actual-vs-guide is a **check**, not a haircut (§3.0).
3. Segment revenue = guided oz × scenario gold (hedge book if sourced) − segment cost → segment EBITDA → segment tax / royalty as reported → segment capex (sustaining vs committed growth) → segment FCF.
4. **Sum segments into the three statements.** Captain 22 Aug: **include IS, BS, and CF.** He does **not** care about formatting. Optimize for **good numbers**, not a pretty workbook. He does **not** need to see the sheets. Print the numbers in the name view (or a working table). Do not spend kit time on tab colors or a replica xlsx.
5. FCF identity from the file (row 842): `CFO + capex + NCI dividend / contribution lines`. Prefer the **company FCF definition** when it exists; label if you use the FCX row-842 version instead.

**Three statements (required numbers).** Captain: include IS, BS, CF. Formatting does not matter. He will **not** look at them — researchers must be able to re-read them **without hallucinating**. Feel free **not** to use an Excel model if that is best. **Do not force FCX-as-xlsx cloning.**

| Statement | Minimum lines |
| --- | --- |
| **IS** | Revenue, cash costs / AISC-mapped opex, EBITDA (if sourced or built), D&A if needed for EBIT, interest (simplified debt), tax, NI, attrib. to owners vs NCI |
| **BS** | Cash, remaining assets one line if not built, total debt, NCI, book equity if sourced. Net debt must tie: cash − debt |
| **CF** | CFO, capex (sustaining vs committed growth), FCF, debt proceeds/paydowns if material, buybacks/dividends if already in the share/cash date, cash bridge to the BS |

**Re-read rules (no silent plugs):**

1. Every **material** line is **sourced** (file / print / date) **or** labelled **computed** from **named** cells (e.g. `IS.revenue = seg.oz × GOLD-METAL.base`). No silent plugs.
2. **IS, BS, CF must tie.** NI flows to retained earnings. Cash on the BS **=** CF ending cash. **No invented balancing figure.**
3. **Units and as-of on every table** (US$m, koz, US$/sh; date or year).
4. If a line is missing: write **UNSOURCED** and **drop it from the mid**. Do **not** fill it.
5. **Default store:** markdown + csv under `/home/box/agent-data/grok-research/models/<ticker>/` for IS, BS, CF, **and** the segment map. A later bot must be able to re-read the exact numbers. `xlsx` only if it **helps and still ties**.

A missing statement is a **gap**, not a formatting choice. A pretty FCX clone with weak or unsourced ounces is a fail.

**Debt — simplified.** Do **not** rebuild the FCX note-by-note schedule (2023–2043 seniors, PT-FI / Cerro Verde loans, LIBOR, proceeds/payments by year). Gold names print:

| Line | Source |
| --- | --- |
| Cash + ST investments | Latest quarter |
| Total debt | Latest quarter (one line) |
| Net debt / net cash | Cash − debt; leases / NCI only if company net-debt or material + sourced |
| Interest | Latest run-rate or a **single** blended rate if you need a P&L plug |

Instrument detail, maturity ladder, and “new debt” rows are **out** unless a refinancing is already announced.

### Dropped (summary extras — do not require)

**Share Price, Financial Summary, Valuation, Other =>** are in the FCX file and are **not** required house tabs. Do not print Mid-Cycle / Recession / Priced-in / consensus / ROIC-@-37.5% / tape P/E just to look like the workbook. Official house output stays **base / bull / bear $/sh** from the Model financials (§4).

The 7× EV/EBITDA identity (FCX Share Price H = 7 on up-rows) is still how you **turn Model EBITDA into a price** if that is the engine you lead with. It is **not** a license to keep the Share Price tab.

### Inputs that sit beside the model

- **Commodity deck:** MASTER + official GOLD-METAL. MASTER Gold tab = **history**. Scenario *names* in MASTER are unused once summary tabs are dropped. **Do not retune 4,900.**
- **Cost curve:** `/workspace/trowe/Gold Cost Curve Data, Aggregated.xlsx`. Context only. Not an AISC rank.

**Operating rule (unchanged):** model as guided, then hedge knowing it might be different. Official mid = printed guide. Miss (oz / cost / timing) in sensitivities + invalidation. No path-weighted unprinted cut.

---

## 1. Locked GOLD-METAL deck (copy; do not retune)

Spot tape **21 Aug 2026** (not the forward line): Kitco bid **$4,602.40/oz** / Trading Economics CFD **$4,607.35**. Official 21 Aug LBMA AM/PM and COMEX settlement: **not captured**. Company realized and WGC Q2 LBMA PM avg **$4,506** are marks, not the 3y line. **Models do NOT take Kitco as the forward gold line.**

| Scenario | Band (US$/oz) | Midpoint models use | Horizon | Role |
| --- | --- | --- | --- | --- |
| **3y Base** (official) | **4,400–5,400** | **4,900** | 3y to 22 Aug 2029 | **NAV / CF gold line** |
| **3y Bull** | **5,400–6,400** | **5,900** | 3y | same |
| **3y Bear** | **3,400–4,400** | **3,900** | 3y | same |
| *12m check-in* (not official) | *4,400–5,000* | *4,500* | *12m to 22 Aug 2027* | *realized-price check-in only* |

**Rules that travel with the metal (do not rewrite inside a name):**

- 3y CF / NAV / remake uses **$4,900 / $5,900 / $3,900**. 12m P&L uses **$4,500 only**.
- A print in **$5,000–$5,400 without** official hold **>$5,400** + 10y real **sustained below 2.40** + Western ETF tonnes **in** **stays 3y base**.
- Official **breaks $4,400** toward **$4,000** with TIPS still **≥2.40** and at least one GOLD-METAL companion (June-style Western liquidation; CB year like revised Q1; DXY through **101**; Hormuz resolution while hike pricing stays) → migrate **3y bear**.
- **GOLD-RATES** (scout): sourced 3y policy is hold-to-slightly-higher then a slow glide. **Does not move 4,900 / 5,900 / 3,900.** TIPS gate stays Bar B. **No invented 2028–29 TIPS or DXY path.**
- **3y S/D rebuild stays tabled.** Do not invent CB / ETF / mine-supply tonne paths to retune gold inside a name.
- If GOLD-METAL later changes, **names re-run this kit**. They do **not** retune gold inside the name view.

---

## 2. What existing name files already do (do not contradict)

Extracted 22 Aug 2026 from `/workspace/hm/*.md` and GOLD-COMPARE / GOLD-ROIC. Not a rank.

| Name | Cash line used | Multiple / yield used | Shares | Net cash / debt | Official $/sh? |
| --- | --- | --- | --- | --- | --- |
| **NEM** (current) | Company FCF = CFO − **all** cash PP&E. 12m node **$10.0bn** at $4,500 (desk). Gold lever: co. pretax **$505m / $100** × **0.67** = **$338m AT / $100**. | **FCF yield desk:** 8.0% base / 6.5% bull / 10.0% bear / 7.5% 12m. Identity: `FCF/yield + residual net cash` / **1.0537bn**. | 10-Q **1,053,692,271** (16 Jul 2026) | 30 Jun net cash **$3,411m incl. leases** ($3,926m ex-leases). $1.95bn **out of yield denom**; residual cash haircut labelled. | **Yes.** 3y **$136 / $217 / $77**. No EV/EBITDA card. |
| **B** (current) | 1H attrib. adj. EBITDA **$5,306m** → labelled annualized **$10,612m**. Slope **$2.7m EBITDA / $1/oz** (Q2 endnote 6). Attrib. FCF after **all** attrib. capex (Q2 **$141m**) is **not** the PT engine. After-sustaining FCF is **inference, not a Barrick KPI**. | **7.0x EV / attrib. adj. EBITDA** in **all** gold cases. 6.0x / 8.0x at **$4,900 only** = sensitivity (**$42 / $49 / $56**). Tape implied **~6.79x** on the $4,900 remake. **Not a print. Not street.** | Official denom **1.65B**; Q2 diluted WASO **1,666m** FLAG | 30 Jun net cash **$1,245m** (debt net of cash). $1.95bn **out**. IPO % **unused**. | **Yes.** 3y **$49 / $61 / $38**. 12m check **$44**. |
| **AEM** (draft) | Company FCF after **total** capex. Identity: `oz × (gold − TCC) − cash tax − total capex − $400m recon`. After-sustaining **rejected** (Hope Bay cash is real). | **FCF yield desk:** **5.0%** mid; **4.5%** only on metal flip; bear **5–6%** (explicitly **not** mid-tier 8–10%). Identity: `(FCF/yield)/shares + $6.45 net cash/sh`. | Tape/aggregator **506.36M** (YE filing 500.7684M). CVRs **out**. | 30 Jun net cash **$3,267m**. Held flat. | **Yes (draft).** 3y **$265 / $345 / $180**. |
| **KGC** (draft) | Company attrib. FCF after **all** attrib. capex. **Do not 2× 1H FCF.** Headline **attrib. GEO**, not gold produced (produced **UNSOURCED**). | **No $/sh.** Explicitly **does not copy Barrick 7.0x**. No NAV / P/E. This kit **now requires** a $/sh on the next KGC run. | MD&A **1,186.2m** (28 Jul); aggregator **1.19B** | Net cash **$1,917.6m** (cash − LT debt) | **No.** Stance only. **Gap the kit closes for the next run.** |
| **BTG** (current) | Company FCF = OCF − **all** mining-interest capex. (Gold − AISC) × oz **overstates** cash (Mali royalties already in AISC; priority dividends / cash tax still hit OCF). | **Not a 7× EBITDA card.** Watch-stage **distribution** on 2028–29 ounce mix. Convert **in the money** → diluted. | Diluted WASO **1.4899bn** (basic 1.3317bn) | Desk net debt **~$169m** (**not** a company print). Stream **$257m** and convert **$460m** sit **outside** that arithmetic (stream in ops; convert in shares). | **Yes.** 3y **$8.00 / $13.00 / $3.50** — **colour distribution**, not a solved identity. Next run should **also** print the kit identities and flag if they disagree with $8. |
| **FNV** (draft) | **OCF is the cash line.** H1 OCF **$1,002.9m** → labelled annualized **$10.40/sh**. **No labelled FCF. Do not invent EBITDA.** Gold cash-op elasticity **67.7%**. Volume convention **A**: H1 OCF flat. | **Computed tape P/OCF 25.6x** held **constant** across gold. OCF yield **≈ 3.91%** (= 1/25.6). **Not street. Not 30×.** | **192,873,810** (MD&A 11 Aug) | Cash **$1,014.2m**; interest-bearing debt **none on printed BS** | **Yes (draft).** 3y **$280 / $320 / $240**. |
| **AGI / EQX** | GOLD-COMPARE rows only for this kit (official AGI/EQX views not re-opened here). AGI company FCF = CFO − mineral PP&E **+ hedge-settlement add-back**. EQX: **no** corporate FCF-after-sustaining line; Q2 **pre-Orla**; 31 Jul pro forma net cash **drops converts**, 30 Jun IFRS net debt **includes** them. | No house multiple in GOLD-COMPARE. | EQX Orla **378.1m** shares issued 31 Jul — **count post-deal diluted**. | Use the **labelled** BS date; do not mix pre/post-Orla. | Run this kit on the next AGI/EQX pass. |

**GOLD-ROIC (process, not a multiple):** what paid in the **stock** is gold beta that is not hedged away, a capital account that survives a down tape, priced host/title residual, and a **per-share** claim (dilution). ROIC and AISC ranks are **demoted**. Peak-cycle ounce M&A, unpriced host-control, hard forwards/prepays, and single-asset geotech the market still treats as “safe” are **must-avoids**. Do **not** invent a GDX/gold beta. Do **not** mix FNV GEOs with miner koz.

**GOLD-COMPARE (definition locks):** GEO ≠ koz; AISC definitions are **not one function**; FNV cash cost/GEO is **not** miner AISC; attrib. ≠ 100%; company FCF defs differ (growth in or out); reserve gold-price assumptions **$1,350–$2,500** — **do not NAV any book at Kitco $4,602**.

---

## 3. 3y operating build (every name)

State **which clock** you are building: **year-by-year Y1 / Y2 / Y3** (to Aug 2027 / Aug 2028 / Aug 2029) **or** a **3y run-rate plus a path** if volume is ramping. Barrick’s current view is a **gold remake of a 2026 run-rate**, not a 2029 volume model — allowed **if** you label it and list the project path as **uncertainty**, not invented ounces.

### 3.0 Official mid = company guide (captain 22 Aug 2026)

**Model as guided, then hedge knowing it might be different in reality.**

1. **The official midpoint uses the company guide.** Volume, AISC/TCC (or the unit that maps to FCF), sustaining/growth capex, tax — take the **printed guide**. If they print a range, the mid is the **arithmetic midpoint of that range** (KGC **2,000 ±5%** → **2,000**; NEM/B/AEM/BTG range mids the same way). If they print a single point, that point is the mid. **No invented haircut** on ounces, cost, or timing.
2. **Do not path-weight an unprinted cut into the midpoint.** “Already take the lower end,” H2 catch-up risk, Goose-fire colour, Barnat *up to* −150 koz, “on track for the low end,” a Q2 print outside the FY band — **not a second mid**. A quarter outside the band is **not** a cut until FY prints outside the band **or** the company **restates** the guide.
3. **Sensitivities and invalidation hold the miss.** Ounce miss, cost miss, timing slip live in:
   - a labelled **guide-miss** node (low-end ounces / high-end AISC / slip a year), **and**
   - **invalidation** (“3y-base $X invalid if they formally cut through Y Moz / AISC stuck ≥ Z / first gold slips out of the 3y clock”).
4. **After a formal cut** (PR / MD&A / 8-K restates the guide), the **new** guide **is** the mid. Do not keep the old guide and “know better.”
5. Outlook / PEA / FID colour / “management tone” **without a restated guide** stays in §6.3 and the miss node. It does **not** move the official $/sh mid.
6. This **overrides** any name draft that already haircut the mid for an unprinted miss (AEM “already take lower-end ounces” is a **sensitivity**, not the official mid, until Agnico reprints). Existing current views are **not** flipped by this scout; the next name run uses this rule.

### 3.1 Volume

- Miners: **attributable oz** (or **attrib. GEO** if that is the company headline — KGC). Label **attributable vs 100% operated**.
- Royalty / streamers: **GEOs**, not miner koz. Label the conversion ruler (FNV 2026 GEOs use **fixed $4,500**).
- Source: latest company **guidance / MD&A / 40-F / 10-K / AIF**. **Do not invent ounces.**
- JV / NCI math as **filed**: NGM **61.5 / 38.5** until Exhibit 10.1 restates; BTG Fekola Mine **80/20**, Regional **65/35** (not AIF 90%); KGC Manh Choh **70%**.
- Uncommitted projects, PEA/Inferred, Hope Bay 2030 ounces, Great Bear late-2029 colour, Gramalote / Antelope, Cobre **restart**, Fourmile/Fiberline/Mike ounces **not in the 8-K**: **out of the number** (list in §6).
- Hedges / prepays / collars: if they exist and are **sourced**, revenue uses **realized + remaining hedge book**, not 100% spot. AGI residual **50 koz @ $1,821** into 1H 2027; BTG collars through **Jan 2027**; BTG prepay **done 30 Jun 2026**.

### 3.2 Unit cost

- Use **AISC or cash cost as the company reports it**. Keep **G&A / sustaining vs growth capex** split **explicit**.
- If AISC is the wrong FCF lever, **say why** and use the reported unit that maps to FCF (AEM binds on **TCC + cash tax + total capex**, not AISC; BTG AISC already includes royalties/tax so (gold − AISC) × oz **overstates** OCF).
- Do **not** rank AISC across the eight (GOLD-COMPARE / GOLD-ROIC).
- Royalty/stream: **cash cost / GEO** (FNV Q2 **$347**). Not AISC.

### 3.3 Tax / royalty

- Statutory + **mine-level** royalty / streaming deductions **as reported**.
- Effective tax rate from **latest year + guided rate if given**. Do **not** invent a country blend.
- Gold-scaled tax: use the **company factor** if printed (NEM pretax $505m/$100 then **33%** guide; KGC **+$16m cash tax / +$100**; AEM royalty colour **$3/oz TCC per $100** and a **labelled** ETR plug). If no factor, scale only the slice the company says moves and **label the plug**.
- Stream / offtake haircuts live here or in volume — **not again as debt** (§5.2).

### 3.4 Revenue and cash

- Revenue = **oz/GEO × GOLD-METAL scenario midpoint** (or realized + sourced hedge book).
- 12m P&L / cost-deck check-in uses **$4,500 only**. Company cost decks (**$4,500** NEM/B/AEM/KGC; **$5,000** BTG; FNV GEO ruler **$4,500**) are **not** the 3y gold line.
- **Miners — FCF:** `CFO − sustaining − growth you treat as committed`. **Label what is in/out.** Prefer the **company FCF definition** as the binding KPI when it exists (NEM/AEM/AGI/BTG/KGC). A desk after-sustaining line is allowed only as a **labelled alternative**, never as a silent overwrite (B/KGC/AEM already flag this).
- **Royalty / streamers — OCF is still the cash line on the statements.** Official PT is **EV/EBITDA** if **Adj. EBITDA is sourced**. Do **not** invent EBITDA. Do **not** use 25.6× P/OCF as the official mid.

---

## 4. Valuation / price target (official output)

**Official PT is EV/EBITDA for every name** (miners and FNV). Format is standardized. Captain 22 Aug: `k` is that name’s **historical EBITDA multiple range**, **not** a flat 7.0× on every scenario.

Official output is quantified US$/sh **base / bull / bear** on GOLD-METAL. 12m row at **$4,500** is a check-in, not official.

### 4.0 Official identity

`PT = (EBITDA × k_scenario − net debt) / diluted shares`

| Piece | Rule |
| --- | --- |
| **EBITDA** | Consol. adj. EBITDA from the **segment roll-up** (or company Adj. EBITDA if that is the printed KPI **and** it ties to the segments). **If EBITDA is UNSOURCED, no official mid.** Do not invent E. |
| **k** | **Sourced historical EV/EBITDA range** for **that name**. Label **as-of, window, and what E** (NTM / LTM / adj.). **Base = mid of the range. Bull = high. Bear = low.** |
| **7.0× T. Rowe** | **Check only** (FCX Share Price H = 7). Use as official k **only if** it is that name’s sourced history. |
| **net debt** | Latest-quarter simplified stack (§5). Sign: net cash is **negative** net debt (adds to equity). |
| **shares** | Diluted WASO (§5.1). |
| **Tape-implied k** | `(tape equity + net debt) / E` at $4,900 and at ~$4,600. **Check only.** |
| **FCF yield** | **Sanity FLAG**, not the official mid. If FCF-yield implied $/sh disagrees with the EV/EBITDA mid by >20%, FLAG. Do not average. |
| **P/OCF 25.6×** | **Retired as official PT** (including FNV). |

**Royalty / FNV:** same identity **if Adj. EBITDA is sourced**. If FNV Adj. EBITDA is UNSOURCED, **no official mid** — do not invent E and do not fall back to 25.6×.

**If the historical range is UNSOURCED, no official mid.** Do not invent k. Do not silently use 7.0× as the mid.

### 4.0b Standard pack (everyone, same columns)

Directory: `/home/box/agent-data/grok-research/models/<ticker>/`

| File | What |
| --- | --- |
| `segment.csv` | Every reporting segment: oz, cost, revenue (and ebitda if built) |
| `is.csv` | Income statement lines |
| `bs.csv` | Balance sheet lines |
| `cf.csv` | Cash flow lines |
| `valuation.csv` | Official PT stack |
| `tie.json` | NI→RE, BS cash = CF ending cash, list of UNSOURCED drops |

Every table: **same columns**, **same units**, **as-of**, **status** = `sourced` / `computed` / `UNSOURCED`, plus `source`. Markdown twins allowed (`segment.md` …) if they match the csv **exactly**. `xlsx` only if it helps and still ties. Do not clone FCX as xlsx.

**segment.csv columns:** `ticker,segment,year,as_of,oz,oz_unit,cost,cost_unit,revenue_usdm,ebitda_usdm,status,source`

**is.csv / bs.csv / cf.csv columns:** `ticker,statement,line,year,value,unit,as_of,status,source`

**valuation.csv columns:** `ticker,scenario,gold_usdoz,ebitda_usdm,k,k_basis,net_debt_usdm,shares_m,pt_us,tape_implied_k,fcf_yield_pct,as_of,status,source`

`k_basis` names the history (e.g. `LTM adj. EV/EBITDA 2019–2025 mid`). `scenario` is `base` / `bull` / `bear` / `check_12m`.

**tie.json minimum keys:** `ni_to_re` (bool), `bs_cash_eq_cf_end` (bool), `unsourced` (list of lines dropped from the mid), `as_of`, `gold_line` (`GOLD-METAL 4900/5900/3900`).

### 4.1 7.0× T. Rowe and 6–8× — checks, not official k

**Official k is the name’s historical range (§4.0).** 7.0× is the T. Rowe FCX check. The 6.0–8.0 band is a **sensitivity only** (Barrick already printed $42 / $49 / $56 at $4,900). Do **not** put 7.0× in `valuation.csv` as `k` unless that name’s sourced history **is** 7.0×.

Why 7.0× exists as a check:

1. Barrick is the **only** name that printed a complete EV/EBITDA remake. It used **7.0× in all gold cases**, labelled **desk assumption, not a print**, with **no peer-set multiple in the scout**.
2. At 3y-base gold **$4,900**, B’s own sensitivity is **6.0× = $42 / 7.0× = $49 / 8.0× = $56**. The band **is** that table.
3. 21 Aug B tape **$47.60** implied **~6.79×** on the same $4,900 remake — **cycle-mid of observed tape vs labelled 7.0×**, not a gold miss. Quality-neutral senior (Africa + project-capex wall, not AEM Canada-heavy) cleared **just under 7×**.
4. KGC correctly refused to **copy** 7× without a sourced KGC multiple. The kit now **supplies** the missing house rule so the next KGC run can print $/sh without inventing a street card.

**How to pick a point inside 6.0–8.0×** (one notch each; start at **7.0×**):

| Knob | Toward **8.0×** | Toward **6.0×** |
| --- | --- | --- |
| Quality / cost conversion | High FCF conversion; AEM-like after-tax cash | Company FCF << EBITDA (growth wall, WC, host take) |
| Reserve / mine life | Long booked life; ounces inside the 3y are **guided** | Life hangs on PEA / 2029+ colour |
| Jurisdiction / title | Canada / Australia book; residual host take already in AISC/tax | Unpriced Mali / Mauritania / Panama / Ghana step-up |
| Balance sheet | Net cash, no ITM convert surprise | Net debt + stream + convert stack (count once each — §5) |
| Hedge book | Unhedged (GOLD-ROIC beta) | Hard forwards / prepays into a rising tape |

Do **not** walk 6.0–8.0 as official k. Gold + the name’s **history** do the work. **EBITDA must be sourced.** Do not invent a (gold − AISC) × oz “EBITDA.”

### 4.2 House FCF yield / exit (desk)

**Default band: 5.0–8.0% FCF yield on 3y run-rate FCF at $4,900.**

FCF in the denominator is the **company FCF** you built in §3.4 (after committed growth if that is the KPI). Do not switch to after-sustaining in the yield without labelling it.

| Quality bucket | 3y base yield | 3y bull | 3y bear | Source in files |
| --- | --- | --- | --- | --- |
| **AEM-quality** (Canada-heavy, net cash, clean FCF) | **5.0%** | **5.0%**; **4.5% only if** GOLD-METAL 3y-bull **flip** prints | **5.0–6.0%** (mild; **not** 8–10%) | AEM draft |
| **Quality-neutral senior** | **6.5–7.0%** | 6.0–6.5% only on flip | 8.0–9.0% | Interpolation between AEM 5% and NEM 8%; not a regression |
| **Residual-risk senior** (Ghana / NGM cheque / host residual) | **8.0%** | **6.5%** only on flip | **10.0%** | NEM current |
| **EQX / BTG mid-tier** (integration, host, growth wall) | **8.0–10.0%** | 7.0–8.0% only on flip **and** guided ounces | **10–12%** | AEM text: mid-tier is **8–10%**; NEM bear 10% is the derate shape |

**FCF yield is a sanity FLAG, not the official mid.** Print it. If it disagrees with the EV/EBITDA official mid by **>20%**, FLAG. Do not average. Do not replace `k` with a yield.

### 4.3 Royalty / FNV — same official identity

Official PT is **EV/EBITDA** if **Adj. EBITDA is sourced**. **25.6× P/OCF is retired as the official mid.** Keep P/OCF / OCF yield as a **FLAG**. If Adj. EBITDA is UNSOURCED, **no official mid** — do not invent E or k. Gold elasticity still uses the sourced gold-cash weight on the **statements**, not as a second PT.

---

## 5. Dilution and net cash / net debt (house rules — were missing)

### 5.1 Dilution

1. **Shares = diluted shares outstanding from the latest filing** (options / RSUs / converts **if in-the-money** or if the company reports diluted WASO as the KPI). BTG convert @ ~$3.17 vs $5.52 tape → **1.49bn diluted**, not 1.33bn basic.
2. **Known committed equity** (closed bought deals, closed all-stock M&A, announced-and-priced ATM that has printed) is **in the number**. EQX Orla **378.1m** shares (31 Jul 2026) are in.
3. **Uncommitted ATM / optional convert / unissued authorization: out of the number.** List under “what is not in the number.”
4. **Development-funded-by-equity that is not announced: out.** Do **not** haircut shares for a guess (Hope Bay, Great Bear, Gramalote, Reko).
5. Buyback **paths** are not in the midpoint unless the shares are **already retired** by the filing date you use (NEM 16 Jul count already after most of the July $606m; do not also subtract the cash without aligning dates).
6. CVRs / cash-contingent paper (AEM **207.7m** CVRs) are **not** common. Out of the count.
7. If filing WASO and the 21 Aug aggregator differ, **print both**; pick one, label it (B: **1.65B official**, 1.666B FLAG; AEM: **506.36M tape** vs 500.77M filing).

### 5.2 Net cash / net debt → EV → $/sh

1. **EV = equity + net debt + NCI + leases** if the company reports them in net debt **or** they are material and sourced (NEM net cash **$3,411m incl. leases** vs **$3,926m** ex-leases — pick and label).
2. **Cash, ST investments, debt from the latest quarter.** Post-quarter cheques that are **sourced** (NEM July buybacks; BTG $95m RCF for Goose fuel) adjust cash **and** the share/debt date in the same sentence.
3. **Gold inventory / bullion:** in EV **only if** the company marks it and you can source the mark. Otherwise out.
4. **Stream liabilities / offtakes:** keep in the **operating build** (lower oz or GEO, or a delivery cost). **Do not double-count as debt** unless the company **classifies them as debt**. BTG stream **$257m** sits outside desk net-debt arithmetic.
5. **Converts:** if **ITM**, they are **dilution** (shares), not a second debt add **if** you already used diluted shares. If **OTM**, keep as debt. Do not treat the conversion price as a put (BTG rival 4).
6. **Equity investments / marketable securities:** add **if marked and liquid**; otherwise out.
7. **Contingent deal cash** (NEM→Barrick Member **$1.95bn** after Fourmile): **out of the number** until received. Footnote $/sh only (B **$1.18/sh**; NEM **$1.85/sh**). Not in the yield denominator. Not in run-rate FCF.
8. **IPO stubs / SOTP / unsourced % float:** out (B / NEM lock).
9. **Official identity (every name):** `$/sh = (EBITDA × k_scenario − net_debt) / diluted_shares` with `k` from **that name’s historical range** (base = mid, bull = high, bear = low). FCF-yield and P/OCF are FLAGS. 7.0× is a check.

---

## 6. Sanity (required every run)

### 6.1 Tape vs implied

Print current share price vs implied $/sh at **$4,900** and at spot **~$4,600**. State the **% gap**.

Worked pattern (B, already done): tape **$47.60** vs 3y-base **$49** = **+3% / ~$1.40**; implied **~6.8× vs labelled 7.0×**; implied gold at 7× **~$4,772**. That is a **desk-multiple gap**, not proof the tape has discounted $4,900.

### 6.2 Gold sensitivity

Print **$Δ P / $100 gold** from the **same identity** (and the four gold nodes: **$4,500** check-in, **$3,900**, **$4,900**, **$5,900**).

Use the **company lever** if sourced; otherwise the kit identity’s slope. Do **not** invent a GDX beta.

| Node | Gold | What it is |
| --- | --- | --- |
| 12m check-in | **$4,500** | Realized-price check-in |
| Spot tape | **~$4,600** | Kitco/TE 21 Aug — **not** the forward line |
| 3y base | **$4,900** | Official CF line |
| 3y bear / bull | **$3,900 / $5,900** | Official scenarios |

### 6.3 What is NOT in the number

Required list (drop rows that do not apply; do not silently include them):

- Exploration option / resource conversion
- Uncommitted projects (PEA, FS without FID, Hope Bay 2030 oz, Great Bear late-2029 colour, Gramalote, Antelope, Lobo-Marte NPV, US FID NPV)
- M&A not announced; Barrick NA IPO % / multiple; NEM 38.5% moving into a listco
- $1.95bn until cash is received
- Hedges **if you excluded them** (or residual notional **UNSOURCED**)
- Uncommitted ATM / optional convert / refillable buyback authorization
- **Invented guide haircut** (unprinted ounce/cost/timing cut path-weighted into the mid)
- A fake T. Rowe tab/layout (workbook **not in hand**)
- GDX / gold-equity beta (none on the desk)
- Invented TIPS path / invented DXY path
- 3y gold S/D rebuild
- Unsourced street multiples / street PTs / P/NAV
- Invented EBITDA (FNV) or invented ounces
- Reserve-price NAV at $1,500–$2,000 or at Kitco $4,602

---

## 7. Process / governance

1. This kit does **not** change `names.stage` (stay **watch**). Does **not** ship. Does **not** flip a view current.
2. The **name researcher owns** the official view. Models may compute the kit identities and hand back the numbers.
3. **Adversarial review** of any view **before** current (existing workflow). A view that is only internally consistent is not done — test rivals on **sourced** numbers (GOLD-METAL already did this for metal; names do it for equity).
4. If GOLD-METAL later changes, names **re-run the kit**. They do **not** retune gold inside the name view.
5. No invented TIPS/DXY. No 3y S/D rebuild. GOLD-RATES does not move **4,900 / 5,900 / 3,900**.
6. Do **not** use an unsourced street multiple as the multiple. Compute/label **desk**.
7. Colour commentary is **not** a substitute for this build. BTG $8 as a distribution is allowed as **colour on top of** the identities, not instead of them, on the next run.
8. Do not rank the eight on AISC or ROIC. Do not mix GEO and koz. Do not NAV at Kitco.
9. **Guide is the official mid** (§3.0). Hedge the miss in sensitivities / invalidation. Do not path-weight an unprinted cut.
10. **Official PT = EV/EBITDA** with **historical k range** (base mid / bull high / bear low). 7.0× is a check. Standard pack: `models/<ticker>/{segment,is,bs,cf,valuation}.csv` + `tie.json`. Fully modeled segments required. Missing E or k history = **no official mid**.

---

## 8. Blank working table (names fill every cell)

Clock used: **Y1/Y2/Y3** **or** **3y run-rate + path** (circle one). Gold mids locked.

| Cell | Unit | Y1 to Aug 2027 | Y2 to Aug 2028 | Y3 to Aug 2029 | 3y run-rate (if used) | Source (filing / date) |
| --- | --- | --- | --- | --- | --- | --- |
| Volume **(guide mid — no haircut)** | attrib. oz **or** GEO (label) |  |  |  |  |  |
| Guide-miss node (oz / cost / timing) | labelled sensitivity, **not** the mid |  |  |  |  |  |
| Realized / hedge residual | US$/oz; koz hedged |  |  |  |  |  |
| Revenue at $4,900 / $5,900 / $3,900 | US$m |  |  |  |  | gold × oz; hedge if sourced |
| Unit cost (AISC or TCC — label) | US$/oz or /GEO |  |  |  |  |  |
| Sustaining capex | US$m |  |  |  |  |  |
| Growth capex (committed / not) | US$m |  |  |  |  |  |
| Cash tax + mine royalty | US$m; ETR % |  |  |  |  |  |
| IS / BS / CF + segment map | md+csv in models/<ticker>/ |  |  |  |  | sourced or computed; must tie |
| Company FCF **or** OCF | US$m |  |  |  |  | definition one line |
| After-sustaining FCF (labelled alt.) | US$m |  |  |  |  |  |
| Adj. EBITDA if **sourced** | US$m |  |  |  |  |  |
| Net (cash) / debt | US$m; date | — | — | — |  |  |
| Diluted shares | m | — | — | — |  |  |
| Desk multiple **or** FCF/OCF yield | × or % | — | — | — |  | §4 bucket |
| PT base / bull / bear | US$/sh | — | — | — |  | both identities if miner |
| 12m check-in @ $4,500 | US$/sh |  | — | — |  | not official |
| Tape vs $4,900 PT / vs ~$4,600 PT | % gap | — | — | — |  | §6.1 |
| $ΔP / $100 Au | US$/sh | — | — | — |  | §6.2 |
| Not in the number | list | — | — | — |  | §6.3 |

---

## 9. Worked identities (algebra; fill the blanks)

Symbols: \(G\) = GOLD-METAL mid; \(Q\) = attrib. oz or GEO; \(c\) = unit cost that maps to cash; \(T\) = cash tax + royalties not already in \(c\); \(S\) = sustaining capex; \(X\) = committed growth capex; \(F\) = company FCF; \(E\) = sourced adj. EBITDA; \(k\) = desk EV/EBITDA; \(y\) = desk FCF yield; \(D\) = net debt (negative if net cash); \(N\) = diluted shares; \(Z\) = extras in (§5.2).

### (1) Miner FCF-yield PT — primary for seniors with clean FCF

\[
F_{3y}(G) = \text{company FCF remade to } G
\]

\[
\text{Equity} = \frac{F_{3y}(G)}{y} + (-D) + Z, \quad \$/\mathrm{sh} = \frac{\text{Equity}}{N}
\]

**NEM worked (already in NEM.md, not re-tuned):** \(F(4900)=11.35\), \(y=0.080\), residual cash \(+0.86\), \(N=1.0537\) → **$136**. Bull \(F=14.74\), \(y=0.065\) → **$217**. Bear \(F=7.97\), \(y=0.100\) → **$77**.

**AEM worked (draft):** \(F(4900)=6.53\), \(y=0.050\), net cash/sh \(+6.45\), \(N=506.36\mathrm{m}\) → **$265**.

### (2) Miner EV/EBITDA PT — printed every miner; lead only if FCF is distorted and \(E\) is sourced

\[
E(G) = E_{\mathrm{run-rate}} + \lambda \cdot (G - G_{\mathrm{realized}})
\]

\[
\mathrm{EV} = k \cdot E(G), \quad \text{Equity} = \mathrm{EV} - D + Z, \quad \$/\mathrm{sh} = \frac{\text{Equity}}{N}
\]

**B worked (already in B.md, not re-tuned):** \(E_{1H\times2}=10{,}612\) at realized \(4{,}613\); \(\lambda=2.7\) $m per $1/oz; \(k=7.0\); \(D=-1{,}245\); \(N=1.65\mathrm{B}\). \(G=4900\) → \(E=11{,}386.9\) → EV \(79{,}708\) → equity \(80{,}953\) → **$49**. \(G=5900\) → **$61**. \(G=3900\) → **$38**. \(G=4500\) check-in → **$44**.

Default \(k=7.0\) inside **6.0–8.0** per §4.1.

### (3) Royalty OCF PT

\[
\mathrm{OCF}(G) = \mathrm{OCF}_{0} \cdot \bigl(1 + w \cdot (G/G_{0} - 1)\bigr)
\]

\[
\$/\mathrm{sh} = P_{0} \cdot \frac{\mathrm{OCF}(G)}{\mathrm{OCF}_{0}} \quad \text{(constant P/OCF)} \quad \text{or} \quad \frac{\mathrm{OCF}(G)/y_{\mathrm{OCF}} + (-D) + Z}{N}
\]

**FNV worked (draft):** \(P_0=265.74\), \(G_0=4500\), \(w=0.677\), volume **A** (H1 OCF flat). \(G=4900\) → factor **1.060** → **$280**. \(G=5900\) → **1.211** → **$320**. \(G=3900\) → **0.910** → **$240**. Implied P/OCF **25.6×** / OCF yield **≈ 3.9%**. **Not 30× street.**

---

## 10. Gaps this kit could not close without inventing

These stay **open**. Do not fill them with a guess inside a name run.

1. **No panel of sourced peer EV/EBITDA or P/OCF** for NEM / AEM / KGC / AGI / EQX / BTG / WPM / RGLD on 21–22 Aug 2026. 7.0× and 25.6× are **desk / tape-computed**, not a regression.
2. **No house gold-equity beta / GDX residual.** Tufano ~2% equity per 1% gold is **published history**, not a 2026 desk beta. Sensitivity stays **$ΔP / $100 gold** from the identity.
3. **No YE 2028 / YE 2029 gold point** (GOLD-METAL). 4,900 is a **band midpoint**, not a 2029 print. Do not invent one to discount a terminal year.
4. **No sourced 2028–29 TIPS or DXY path** (GOLD-RATES / GOLD-METAL). Do not invent.
5. **3y S/D rebuild tabled** — no 2028–29 CB / ETF / mine-supply tonne table to retune gold.
6. **KGC attrib. gold ounces produced** — UNSOURCED; use **GEO** until a filing prints gold produced.
7. **FNV 2027–29 GEOs** — UNSOURCED; volume stays a labelled convention (A: H1 OCF flat), not a CAGR.
8. **Company FY FCF guides** — none of the eight print a FY FCF guide usable as a house number; FCF nodes are **desk remakes** and must stay labelled.
9. **Official 21 Aug LBMA/COMEX** — still missing. Spot mark remains Kitco/TE.
10. **EQX post-Orla corporate FCF / combined R&R** and **BTG company-printed net debt** — not in GOLD-COMPARE. Do not invent; use labelled desk arithmetic and the first consolidated print when it exists.
11. **NEM 10-Q adj. EBITDA for the 7× cross-check** — not extracted in NEM.md. Next NEM run sources it or **flags** the EV/EBITDA cell as empty (do not invent EBITDA).
12. **AGI / EQX full kit run** — not executed in this scout (official views not opened / not edited).
13. **MASTER gold scenarios are 2024-01-01** (Base $2,000). History and other metals only. **Do not retune GOLD-METAL.** Mid-Cycle / Recession gold stay mapped to 4,900 / 3,900 until GOLD-METAL prints them.

---

## 11. One-page run order (name researcher)

1. Copy GOLD-METAL mids. Do not retune. Note Kitco/TE as tape only.
2. Pull latest attrib. oz or GEO, unit cost, tax/royalty, capex split, hedges, diluted shares, cash/debt/leases/NCI — **from filings**. **Official mid = printed guide** (§3.0). No invented haircut.
3. Build Y1–Y3 **or** labelled 3y run-rate + path on that guide. Put the miss (oz / cost / timing) in the **guide-miss** node and in invalidation. Output FCF (miner) or OCF (royalty).
4. Remake cash to **$4,900 / $5,900 / $3,900**. 12m row at **$4,500**.
5. Apply §4–5 identities. Print **both** miner engines. Flag >20% gap.
6. Sanity: tape vs $4,900 and ~$4,600; $ΔP/$100; not-in-the-number list.
7. Hand the numbers to the name owner. Stage stays **watch**. View stays draft until adversarial review is empty / info-only.

*End HOUSE-MODEL. Scout/kit only. No official view edited. No name restaged.*
