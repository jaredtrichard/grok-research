# FNV historical EV/EBITDA — source memo

**FNV-HOUSE k call (Firstmate 22 Aug 2026, captain skipped card):** official k = StockIntent 5y TTM **19.23 / 24.09 mid-range / 28.94**. Median 24.42 is a check. TTM-k on Adj-E accepted (FLAG). GuruFocus 10y out. Draft PTs $304 / $416 / $209 — not current until review.

The vendor dump below is the archive. It does not pick k.

---

# Franco-Nevada (NYSE: FNV, TSX: FNV) — sourced historical EV/EBITDA

**Research date:** 2026-08-22 (America/New_York).  
**Purpose:** Collect sourced current and historical EV/EBITDA so a researcher can later set PT `k` as low/mid/high of *history*. This memo is **facts only**. It is **not** an official view and does **not** pick a k.

**Rule applied:** Do not invent multiples. Every figure below is printed on a cited page (or, if labeled “derived,” is simple arithmetic on that page’s printed series). Sources that disagree are **not averaged**.

---

## Status for PT k

History **is sourced** from multiple independent vendors. They **do not agree** on current k, window min/max, or whether 2023–2024 (Cobre Panamá / negative GAAP EBITDA) is a valid observation.

**Do not** treat 7.0x or 25.6x as sourced from this work. No official base/bull/bear k is stated here.

If using history for k, the researcher must **choose one vendor + one window + one E definition** (and whether to drop E≤0 observations). Mixing vendors or averaging them is not supported by the pages.

---

## 1. Current EV/EBITDA (tape / latest printed)

| Source | Printed current EV/EBITDA | As-of on page | E definition (as printed) | EV construction (as printed) | URL |
|---|---|---|---|---|---|
| GuruFocus | **20.85** | **2026-05-22** (page title/body: “As of May. 22, 2026”) | TTM EBITDA ended **Mar. 2026** = **$2,058 Mil** (table uses 2057.9) | Enterprise Value (Today) = **$42,897 Mil** (table: 42897.005). `42897.005 / 2057.9 = 20.85` | https://www.gurufocus.com/term/enterprise-value-to-ebitda/FNV |
| StockIntent | **20.42** | Quarter date **2026-06-30** (latest row; page also shows close **$258.14**) | TTM EBITDA **$2.22B** | EV **$45.42B**; page: `EV = MarketCap + Debt − CashnEq`; `45.42B / 2.22B = 20.42` | https://www.stockintent.com/app/data-browser/FNV/evebitda |
| ValueSense | **19.1x** LTM | FAQ: “based on the financial report for **Jun 29, 2026 (Q2’2026)**”; header also prints Last Price **$251.17**, Market Cap **$48.6B** | **EV/EBITDA LTM** (EBITDA = earnings before interest, taxes, depreciation, and amortization). Not labeled Adj. | EV not printed next to 19.1x. Key-stats block prints EV/other LTM multiples separately (20.5x / 27.1x / 52.4x / 32.7x / 5.9x) without naming which is EV/EBITDA | https://valuesense.io/ticker/fnv/ev-to-ebitda |
| Alpha Spread (TSX:FNV) | **26.3** | Page live fetch 2026-08-22; price **364.04 CAD**; “vs 3-y average of **24.4**” | EBITDA printed **$1.9B** next to “Mar 2026” in the forward table (“Current”) | EV printed **CA$61.3B**. Printed identity `26.3 = CA$61.3B / $1.9B` does **not** arithmetically reconcile (26.3 × 1.9B ≈ 50.0B ≠ 61.3B). Currency of E vs EV is not stated cleanly | https://www.alphaspread.com/security/tsx/fnv/relative-valuation/ratio/enterprise-value-to-ebitda |
| GoodMoat | **22.59x** | **As of Aug 22, 2026**; price **$265.74**; Market Cap **$51.25B** | Not specified beyond “EV / EBITDA” | Not specified | https://goodmoat.com/dataexplorer/fnv/ev-ebitda |
| VCP Scanner | **30.70** TTM (FAQ: “current EV/EBITDA is **30.7x**”) | Page “Period: **2026Q2**”; TTM Market Cap **$49.8B**, TTM EV **$49.4B** | “equity + debt − cash” over EBITDA; not labeled Adj. vs GAAP | EV printed TTM **$49.4B**. 49.4 / 30.70 implies E ≈ $1.61B (not printed as a standalone TTM EBITDA) | https://vcpscanner.com/stock/fnv/financial-ratios |
| valueinvesting.io (FNV.TO) | **36.11** | **2026-08-22** | “TTM EBITDA according to its financial statements” **1,878.10 mil CAD** | EV **67,809.16 mil CAD**. `67809.16 / 1878.10 ≈ 36.11`. Daily table on the same page for 2026-08-20 prints **36.25** | https://valueinvesting.io/FNV.TO/valuation/ev_ebitda-multiples |
| Yahoo Finance key statistics (NYSE:FNV) — **search-index snapshot, not a successful live table fetch** | Valuation table **Enterprise Value/EBITDA Current = 21.97**; same table: 3/31/2026 **27.29**, 12/31/2025 **27.46**, 9/30/2025 **34.21**, 6/30/2025 **27.67**, 3/31/2025 **29.33** | Snapshot as retrieved by web index on 2026-08-22; live `curl` of the URL returned HTTP 502; live WebFetch omitted the valuation grid | Income statement block (live WebFetch): **EBITDA 2.09B**, Revenue (ttm) **2.3B**, MRQ **6/30/2026**. Footnote **7**: “EBITDA is calculated by **S&P Global Market Intelligence** using methodology that may differ from that used by a company in its reporting.” | Same snapshot: Current Market Cap **49.82B**, Enterprise Value **48.80B**. 48.80 / 2.09 ≈ 23.3, which is **not** the printed 21.97 — do not reconcile | https://finance.yahoo.com/quote/FNV/key-statistics/ |
| Yahoo Finance (FNV.TO) — search-index snapshot | Current **Enterprise Value/EBITDA 22.18**; EV **63.69B** (CAD listing) | Same research day | Same S&P Global footnote family as Yahoo | Current Market Cap **64.69B**, EV **63.69B** | https://finance.yahoo.com/quote/FNV.TO/key-statistics/ |
| Morningstar quote (tape, no EV/EBITDA) | **Not printed** on quote page (P/E Normalized 32.59, P/B 5.52, P/S 19.67, P/CF 25.39) | Fetch 2026-08-22 | n/a | n/a | https://www.morningstar.com/stocks/xnys/fnv/quote |

**Macrotrends EV/EBITDA:** **not found.** URLs  
`https://www.macrotrends.net/stocks/charts/FNV/franco-nevada/ev-ebitda`,  
`.../enterprise-value-to-ebitda`,  
`.../ev-to-ebitda`  
redirected to the EBIT page or 404. Financial-ratios page is paywalled/empty of printed EV/EBITDA. Macrotrends **does** print **EBITDA dollars**, not the multiple (see §5).

**CompaniesMarketCap:** market cap only as of August 2026 (**$51.24B**; Aug 21, 2026 EOD **$51.27B / $51.24B**). **No EV/EBITDA series.**  
https://companiesmarketcap.com/franco-nevada/marketcap/

---

## 2. Historical series / ranges (do not average across sources)

### A. GuruFocus — 10-year range + annual/quarterly table (partial)

**URL:** https://www.gurufocus.com/term/enterprise-value-to-ebitda/FNV  
**As-of for current:** 2026-05-22.  
**E:** TTM GAAP-style EBITDA (vendor).  
**Frequency printed:** annual year-end + quarterly.  
**Window printed:** “Over the Past 10 Years”; also “During the past 13 years…”

**Printed 10-year range (quote):**  
`FNV' s EV-to-EBITDA Range Over the Past 10 Years Min: -250.47 Med: 26.1 Max: 66.55 Current: 20.85`

**Printed 13-year statement (quote):**  
“During the past 13 years, the highest EV-to-EBITDA of Franco-Nevada was 66.55. The lowest was -250.47. And the median was 26.10.”

**Printed annual EV-to-EBITDA (visible columns only; earlier years behind trial wall):**  
Dec16–Dec21 not shown in the public snippet. Visible: **Dec22 22.12**, **Dec23 22.21**, **Dec24 -215.40**, **Dec25 21.61**, and a following **22.69** in the truncated annual row (year label not fully shown in the snippet).

**Printed quarterly (last visible cells):** **27.31, 24.58, 29.28, 22.69, 23.12** (full date headers behind trial wall; last quarters on the page run through **Mar26**).

**Note:** Min **-250.47** / FY **-215.40** are **not usable as a bear k** if E is intended to be positive operating earnings. They coincide with the period when vendor TTM EBITDA went negative.

Live `curl` of GuruFocus was Cloudflare-blocked (“Just a moment…”). Figures above are from the public search-index / earlier fetch of the same URL.

### B. StockIntent — TTM quarterly points + printed 5-year stats

**URL:** https://www.stockintent.com/app/data-browser/FNV/evebitda  
**E:** TTM EBITDA (vendor: EBIT + DepAmor).  
**EV:** MarketCap + Debt − Cash.  
**Frequency:** quarterly TTM (table). Chart zoom buttons: 1Y / 3Y / 5Y / 10Y (10Y min/max/avg/med **not printed** as numbers; only “Ranked better than **91%** of FNV's values over the past **10 years**”).

**Printed last 10 quarter-ends:**

| Date | TTM EBITDA | EV | EV/EBITDA |
|---|---|---|---|
| 2026-06-30 | $2.22B | $45.42B | **20.42** |
| 2026-03-31 | $2.06B | $44.99B | **21.83** |
| 2025-12-31 | $1.73B | $49.95B | **28.94** |
| 2025-09-30 | $1.45B | $35.37B | **24.36** |
| 2025-06-30 | $1.25B | $33.69B | **26.91** |
| 2025-03-31 | $1.1B | $31.47B | **28.62** |
| 2024-12-31 | $991.8M | $26.2B | **26.42** |
| 2024-09-30 | $-181.2M | $23.02B | **0** |
| 2024-06-30 | $-162.2M | $21.07B | **0** |
| 2024-03-31 | $-103.2M | $22.08B | **0** |

**Printed “Last 5 years” / “Key Performance Insights” (quotes):**
- average **24.13**
- median **24.42**
- highest **28.94** (Maximum date printed **Dec 31, 2025**)
- lowest **19.23** (Minimum date printed **Sep 30, 2022**)
- latest TTM **20.42**

The printed 5-year min **19.23** ignores the **0** rows (E < 0). Those zeros are **not** a low-k observation.

### C. ValueSense — annual LTM year-end 2008–2025

**URL:** https://valuesense.io/ticker/fnv/ev-to-ebitda  
**E:** **EV/EBITDA LTM** (not labeled Adj.).  
**Frequency:** annual year-end (table). Page also offers Quarterly / Daily UI (“Crunching data…” — those grids were **not** printed in the fetch).  
**Window:** Dec'08–Dec'25.

**Printed year-end LTM series (quote of table):**

| Dec'08 | Dec'09 | Dec'10 | Dec'11 | Dec'12 | Dec'13 | Dec'14 | Dec'15 | Dec'16 | Dec'17 | Dec'18 | Dec'19 | Dec'20 | Dec'21 | Dec'22 | Dec'23 | Dec'24 | Dec'25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 14.1x | 16.9x | 15.7x | 15.2x | 35.0x | 19.5x | 33.0x | 21.8x | 25.9x | 30.9x | 24.6x | 37.9x | 45.7x | 24.2x | 20.5x | 18.4x | **(105.9x)** | 27.4x |

**Printed vendor summaries (do not mix with the table):**
- Header: EV/EBITDA LTM **19.1x**, **5Y avg (6.8x)**
- FAQ: 3-year average annual EV/EBITDA LTM **(19.0x)**; 5-year **(7.1x)**  
  (parentheses and the gap vs 6.8x are as printed; 2024’s **(105.9x)** pulls a 5-year mean down.)

**Derived from the 18 printed year-end points only (not printed by ValueSense):**
- including Dec'24: min **(105.9x)**, max **45.7x** (Dec'20)
- excluding Dec'24: min **14.1x** (Dec'08), max **45.7x** (Dec'20); n=17 mean **≈25.1x**; median **24.2x** (9th of 17 sorted positives)

### D. Alpha Spread — 3y / 5y averages (no min/max series)

**URL:** https://www.alphaspread.com/security/tsx/fnv/relative-valuation/ratio/enterprise-value-to-ebitda  

Printed scenario table:

| Scenario | EV/EBITDA Value |
|---|---|
| Current Multiple | **26.3** |
| 3-Year Average | **24.4** |
| 5-Year Average | **24.4** |
| Industry Average | **9.7** |
| Country Average | **10.2** |

Forward (today’s EV / future EBITDA, as printed): Dec 2026 **24.7**, Dec 2027 **22.8**, Dec 2028 **22.6**, Dec 2029 **23**, Dec 2030 **23.9**. These are **NTM/FY forward**, not history.

### E. VCP Scanner — FY year-end 2016–2025 + TTM + one historical average

**URL:** https://vcpscanner.com/stock/fnv/financial-ratios  

Printed **EV / EBITDA** row:

| TTM | FY2025 | FY2024 | FY2023 | FY2022 | FY2021 | FY2020 | FY2019 | FY2018 | FY2017 | FY2016 |
|---|---|---|---|---|---|---|---|---|---|---|
| **30.70** | **24.62** | **22.31** | **19.62** | **22.59** | **23.78** | **40.46** | **28.77** | **30.13** | **27.68** | **23.85** |

FAQ quote: “The historical average is **24.7x**.” Window for that average is **not** specified beyond the FY2016–FY2025 table.

**Derived from the 10 printed FY points only (not printed as min/max):** min **19.62** (FY2023), max **40.46** (FY2020). TTM **30.70** is above every FY in the table.

This series stays **positive in FY2023–FY2024**, unlike GuruFocus / ValueSense / StockIntent. That is a **definition split** (likely closer to adjusted/operating E), not a reason to average.

### F. marketcap.ru — annual FY 2011–2025

**URL:** https://marketcap.ru/de/stocks/FNV/financial-ratios  
**Currency note on page:** “Alle Zahlen in USD-Währung.”  
**E:** not labeled Adj. vs GAAP. FY2023 EV/EBITDA is **negative** (**-48.6**), so this vendor’s 2023 E is negative (EBITDA per share printed **-2.23**).

Printed **EV/EBITDA**:

| 2025 | 2024 | 2023 | 2022 | 2021 | 2020 | 2019 | 2018 | 2017 | 2016 | 2015 | 2014 | 2013 | 2012 | 2011 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 33.2 | 36.9 | **-48.6** | 30.4 | 32.4 | 26.3 | 31.5 | 32.9 | 26.7 | 25.1 | 27.1 | 25.5 | 35.7 | 27.1 | 29.3 |

Also printed: current-group EV/EBITDA **33.24x** vs five-year median **32.42x** (interval **2020–2025**).

**Derived from 15 printed FY points:** min **-48.6** (2023), max **36.9** (2024). Ex-2023: min **25.1** (2016), max **36.9** (2024).

This vendor’s FY levels are **systematically different** from ValueSense year-end LTM and from VCP Scanner FY (e.g. 2020: 26.3 vs ValueSense 45.7 vs VCP 40.46). **Do not average.**

### G. Morningstar valuation table — incomplete capture

**URL:** https://www.morningstar.com/stocks/xnys/fnv/valuation  
Web search index printed a row `Enterprise Value/EBITDA | 26.20 | 31.12 | 25.12 | 37.88 | 45.59 | 24.01 | 21.06 | 19.52 | — | 28.22 | 20.03 | 24.11 | —`  
Live WebFetch of the same URL **did not include the table** (JS). Column headers (Current vs FY years vs 5-yr avg) were **not confirmed**. **Do not assign years. Do not use this row for k.**

TSX mirror https://www.morningstar.com/stocks/xtse/fnv/valuation returned HTTP 500 on fetch. Search snippet there: `26.66 | 29.76 | 26.67 | 37.27 | 43.15 | 24.20 | 22.33 | 19.10 | — | 27.59 | 20.74 | 24.50 | —` — same caveat.

---

## 3. Independent-source disagreement (do not blend)

| Question | Source A | Source B | Source C |
|---|---|---|---|
| Current ~Aug-2026 | GuruFocus 20.85 (as-of **May 22**) | StockIntent 20.42 (2026-06-30) / ValueSense 19.1x (Q2’2026) / GoodMoat 22.59x (Aug 22) | Alpha Spread 26.3 / VCP 30.7 / valueinvesting.io 36.11 |
| 5y central | StockIntent mean **24.13** / median **24.42** | Alpha Spread 5y avg **24.4** | ValueSense 5y avg **(6.8x)** or FAQ **(7.1x)** (includes 2024 hole) |
| 10y / long high | GuruFocus max **66.55** | ValueSense year-end max **45.7x** (2020) | VCP FY max **40.46** (2020); marketcap.ru FY max **36.9** (2024) |
| Long low (raw) | GuruFocus min **-250.47** | ValueSense Dec'24 **(105.9x)**; marketcap.ru 2023 **-48.6** | StockIntent prints **0** when E<0; 5y min among positives **19.23** |
| 2020 year-end | ValueSense **45.7x** | VCP FY **40.46** | marketcap.ru **26.3** |
| 2024 | ValueSense **(105.9x)**; GuruFocus **-215.40** | StockIntent **26.42** (E +$991.8M) | VCP **22.31**; marketcap.ru **36.9** |

These are **different E and/or different EV dates**, not rounding error.

---

## 4. Adj. EBITDA vs GAAP / street TTM

**Company (FNV) reports Adjusted EBITDA as a non-GAAP measure.** It does **not** print an EV/EBITDA multiple in the filings checked.

Quoted company figures (USD millions):

- FY2025 Adjusted EBITDA **$1,656.1**; FY2024 **$951.6**; FY2023 **$1,014.7**  
  https://www.sec.gov/Archives/edgar/data/1456346/000110465926032133/fnv-20251231xex99d2.htm  
  and Asset Handbook / exhibits: https://www.sec.gov/Archives/edgar/data/1456346/000110465926032144/fnv-20251231xex99d1.pdf
- Q1 2026 Adjusted EBITDA **$591.9**; recon from net income + tax + finance + D&A ± other  
  https://s201.q4cdn.com/345177888/files/doc_financials/2026/q1/NR-Franco-Nevada-Reports-Record-Q1-2026-Results-vFinal-2026-05-12.pdf

**Macrotrends EBITDA $ (not a multiple)** tracks the **Adjusted** run-rate, not the negative GAAP TTM used by some multiple vendors:

- TTM ending **Jun 30, 2026: $2.154B**; Q2’26 **$0.530B**; FY2025 **$1,656**; FY2024 **$952**; FY2023 **$1,018**  
  https://www.macrotrends.net/stocks/charts/FNV/franco-nevada/ebitda

**Street / vendor multiples in §1–§2 generally use vendor TTM EBITDA (Yahoo footnote: S&P Global), not FNV Adjusted EBITDA.** Evidence:
- StockIntent TTM E **negative** in 2024 Q1–Q3 (−$103.2M to −$181.2M) while company Adjusted EBITDA those years was **positive** (~$0.95–1.02B annually on Macrotrends/filings).
- GuruFocus FY2024 **-215.40** and 10y min **-250.47** require a **negative E**.
- ValueSense Dec'24 **(105.9x)** is the same family of problem (E near zero or signed the other way).
- VCP Scanner staying positive in FY2023–24 is the exception and is still **not labeled “Adjusted EBITDA.”**

**Implication for applying k to modeled Adj. EBITDA:** a k taken from **GAAP/vendor TTM** history is **not the same object** as k × **modeled Adj. EBITDA**. The 2023–2024 Cobre Panamá impairment is why several histories go to 0 / negative / triple-digit. Those points are **not** a bear-case royalty multiple.

---

## 5. What was searched and not usable

| Source | Result |
|---|---|
| Macrotrends EV/EBITDA | **No page / no printed multiple.** EBITDA $ only. |
| CompaniesMarketCap | **Market cap history only.** |
| S&P / FactSet terminal | **No public series found** beyond Yahoo’s “S&P Global Market Intelligence” EBITDA footnote. |
| Company filings | Adj. EBITDA **disclosed**; EV/EBITDA **not** disclosed. |
| GuruFocus live HTML | Cloudflare challenge; figures from indexed public page of the same URL. |
| Yahoo live valuation grid | `curl` HTTP 502; WebFetch dropped the grid. Search-index snapshot kept and labeled. |
| Morningstar valuation grid | Not recoverable with year headers. |

---

## 6. Researcher notes (still not a view)

1. **Two independent, usable positive-E histories** if the goal is “range of history” without inventing k:  
   - **StockIntent 5y TTM (positives):** low **19.23** (2022-09-30), mid **24.42 median / 24.13 mean**, high **28.94** (2025-12-31).  
   - **ValueSense annual LTM 2008–2025 excluding Dec'24:** low **14.1x**, mid **~24.2x median / ~25.1x mean** (derived), high **45.7x**.  
   GuruFocus 10y **median 26.1** / **max 66.55** is a third independent **range**, but its **min -250.47 is not a k**.

2. **Do not** use Alpha Spread 26.3, VCP 30.7, or valueinvesting.io 36.11 as “the” current multiple without reading their E/EV units; they disagree with GuruFocus/StockIntent/ValueSense/GoodMoat (~19–23).

3. **Do not** apply a GAAP-history k to Adj. EBITDA (or the reverse) without an explicit bridge. Macrotrends TTM E **$2.154B** (Jun-2026) vs StockIntent TTM E **$2.22B** vs Yahoo **$2.09B** vs GuruFocus **$2.058B** (Mar-2026) vs valueinvesting.io **1,878.10 mil CAD**.

4. No official PT k is set in this file.
