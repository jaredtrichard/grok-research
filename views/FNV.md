# FNV — official view

| Field | Value |
| --- | --- |
| Id | FNV |
| Kind | official view (name) |
| Status | **current** — FNV-HOUSE 22 Aug 2026. Stage `watch`. |
| As-of | Saturday 22 Aug 2026 (America/New_York) |
| Kit | HOUSE-MODEL royalty. Tables `/home/box/agent-data/grok-research/models/FNV/` |
| Horizon | **3y to 22 Aug 2029**. Clock: **Y1=Y2=Y3 run-rate** at guide mid **540k GEOs**. |
| Stage | `watch` |
| Gold | GOLD-METAL **$4,900 / $5,900 / $3,900**. 12m check-in **$4,500**. Do not retune. |
| Volume | Official mid = **540k** (510–570). Pick **A**: Cobre miss does not cut the book. |
| Revolver | Distress / unproductive only. |
| PT engine | StockIntent 5y TTM EV/EBITDA (fetched 22 Aug 2026): bear **19.23** / base **24.09** = (19.23+28.94)/2 / bull **28.94**. Applied to modeled **Adj. EBITDA**. |
| Constraints | No ship. No live trade. No invented FCF. GuruFocus 10y **out**. Median 24.42, 25.6× P/OCF, and 7× are **checks only**. |

## Thesis

Duration royalty. 3y statements are a four-type segment roll-up into IS/BS/CF that **tie**. Official 3y mids use **k × Adj. E(G) + net cash**, with k from the sourced 5y TTM range and E from the tied IS.

**Official 3y $/sh: $304 / $416 / $209** at gold **$4,900 / $5,900 / $3,900**. 12m check-in at $4,500 and k=24.09 is **$287** (not a 3y mid).

**FLAG:** k is vendor **TTM EBITDA** (StockIntent). E is FNV **Adj. EBITDA** (H1 sourced $1,121.6 m → G0 modeled $2,254.8 m). Firstmate accepted the mix. Do not silently swap in GAAP TTM E.

Tape 21 Aug **$265.74** sits **13% under** the $304 base (and 6% under the 25.6× OCF check $282). Split the $38: same-k $4,600 node is **~$291**, so tape is **~9% under $291**; **~$13** of the gap is $4,600→$4,900 gold and the rest is multiple. Tape-implied k is **~21.0×** on $4,900 Adj. E ($2,392.8 m, EV ≈ $50.24 bn) and **~22.0×** on the $4,600 E. Official k=24.09 matches this tape only at **~$4,010** gold. Same-k $ΔP/$100 from $287 to $304 is **~$4.25**. StockIntent **20.42** is the **30 Jun 2026** vendor print at close $258, not the 21 Aug tape multiple.

## Segment map → IS

Q2 type mix (MDA, sourced) applied to guide **540,000 GEOs**:

| Segment | Q2 GEOs | Q2 rev | Weight | Y1–Y3 GEOs |
| --- | ---: | ---: | ---: | ---: |
| Revenue royalties | 47,079 | $211.5 m | 35.6% | 192.0k |
| Streams | 66,166 | $287.1 m | 50.0% | 269.8k |
| Profit-based | 16,537 | $70.5 m | 12.5% | 67.4k |
| Interest / other | 2,623 | $11.8 m | 2.0% | 10.7k |
| **Total** | **132,405** | **$580.9 m** | 100% | **540k** |

G0 revenue **$2,474.6 m** = H1 MDA **$1,231.6 m** ×2 × (540/537.516). **FLAG:** that is the H1 print annualized and volume-scaled, then parked on the $4,500 node — not a restatement of H1 ounces at $4,500 (Q1 LBMA was ~$4,873; Q2 implied ~$4,418). Closed PTs **$304 / $416 / $209 / $287** stay. Named mines stay in `assets_memo.csv` — no second ounce book. **Cobre out of the mid.** Gold scale: Q2 gold rev **$403.0 / $580.9 = 69.4%**. Residual unscaled. Stream cash cost **$40.6 / $45.9** of Q2 cash costs scales with **G/4,500** (`is_3y.csv`).

## 3y IS (US$m, Y1=Y2=Y3) — from `is_3y.csv`

D&A **$325** (guide mid 310–340). G&A H1×2×vol_scale. FIN **Q2×2×vol_scale** (H1 finance income **UNSOURCED**). ETR **21.94%** (H1 tax $231.2 / PBT $1,053.8).

| | $4,500 | $4,900 | $5,900 | $3,900 |
| --- | ---: | ---: | ---: | ---: |
| Revenue | 2,474.6 | 2,627.2 | 3,008.7 | 2,245.7 |
| Cash costs | 185.7 | 200.3 | 236.7 | 163.8 |
| G&A | 34.2 | 34.2 | 34.2 | 34.2 |
| Adj. EBITDA | 2,254.8 | 2,392.8 | 2,737.8 | 2,047.8 |
| D&A | 325.0 | 325.0 | 325.0 | 325.0 |
| GP | 1,963.9 | 2,101.9 | 2,446.9 | 1,756.9 |
| Finance inc. | 13.7 | 13.7 | 13.7 | 13.7 |
| PBT | 1,943.4 | 2,081.4 | 2,426.4 | 1,736.4 |
| Tax | 426.4 | 456.7 | 532.4 | 381.0 |
| NI | 1,517.1 | 1,624.8 | 1,894.1 | 1,355.5 |
| **OCF** | **2,015.1** | **2,122.8** | **2,392.1** | **1,853.5** |

OCF = NI + D&A + **extra $173.0** (residual so OCF@$4,500 = H1 OCF ×2 × vol_scale). Extra held in $ across gold; BS other/WC absorbs it. Sourced G0 E check: H1 Adj. EBITDA ×2 ×vol_scale **$2,253.6** vs modeled **$2,254.8**.

## 3y CF / BS (tie)

Cash += OCF − div; R/S/WI −= D&A; other/WC −= extra; equity += NI − div; debt **0**; liab held. **imbalance = 0** on all 12 scenario-years. Div **$323.7 m** = H1 cash div $161.1 ×2 ×vol_scale. Buys **$0** in the mid. LOMI C$25 m: FNV is the **lender** ($17.8 m advanced 17 Jun), not drawn debt.

| Y3 @ | Cash | R/S/WI | Equity | OCF |
| --- | ---: | ---: | ---: | ---: |
| Open 30 Jun 26 | 1,014.2 | 6,262.3 | 8,240.7 | — |
| $4,500 | 6,088 | 5,287 | 11,821 | 2,015 |
| $4,900 | 6,412 | 5,287 | 12,144 | 2,123 |
| $5,900 | 7,220 | 5,287 | 12,952 | 2,392 |
| $3,900 | 5,604 | 5,287 | 11,336 | 1,854 |

Open BS sourced. 8,922.2 = 1,014.2+6,262.3+1,215.1+430.6.

## Valuation

`EV = k × Adj. EBITDA(G)`; `Equity = EV + net cash $1,014.2 m`; `/ 192,873,810`.

k from StockIntent 5y TTM (page fetched 22 Aug 2026): https://www.stockintent.com/app/data-browser/FNV/evebitda — min **19.23** (30 Sep 2022), max **28.94** (31 Dec 2025). Base k is **mid of that range 24.09**, not the printed median 24.42. E is `is_3y` Adj. EBITDA. **FLAG TTM-k on Adj-E.**

| Scenario | Gold | E $m | k | EV | Equity | **$/sh** | 25.6× OCF | 24.42× E | 7× E |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 12m check-in | 4,500 | 2,254.8 | 24.09 | 54,317 | 55,332 | 287 | 267 | 291 | 87 |
| **3y base** | 4,900 | 2,392.8 | 24.09 | 57,642 | 58,656 | **304** | 282 | 308 | 92 |
| **3y bull** | 5,900 | 2,737.8 | 28.94 | 79,231 | 80,246 | **416** | 318 | 352 | 105 |
| **3y bear** | 3,900 | 2,047.8 | 19.23 | 39,379 | 40,393 | **209** | 246 | 265 | 80 |

Official mids are the bold 3y column. Median 24.42, 25.6× OCF, and 7× are **checks**. Do not average them into $304. GuruFocus 10y **out**.

Tape $265.74 vs $304 = **0.87×** the base. Implied k @ $4,900 E ≈ **21.0×**; implied gold @ k=24.09 ≈ **$4,010**. Same-k $ΔP/$100 ≈ **$4.25**. Bull is not that slope: k also steps 24.09→28.94.

## Invalidation

GOLD-METAL gates. Cobre miss does **not** break the book (A). Distress draw only. Formal GEO guide cut through **510k** breaks the 540k mid. A sourced Adj EV/EBITDA tape that is not the StockIntent 5y TTM range would reopen k — it does not exist in filings.

## Not in the number

Cobre restart; 27–29 GEO CAGR; undeployed $4.3 bn as ounces; Cascabel first production; Fourmile; invented FCF; 7× as official k; 25.6× as official k; median 24.42 as official k; GuruFocus 10y min/max; Kitco as forward gold; Ag beta 1; guide haircut in the mid; H1 finance income (used Q2×2).

## Rivals (on numbers)

### 1) Pay 25.6× OCF / $282 as the 3y base
Kit royalty identity. Run-rate 540k is already in OCF. Gap vs $304 is **8%** ($22). Tape $266 is closer to this check than to $304. **Does not beat** the Firstmate k call. Watch the gap; do not average.

### 2) Leftover torque in high-AISC miners
$4,900→$5,900 gold is **+20%**, not +31% (+31% is $4,500→$5,900). Same-k (24.09) bull is **~$347**. Official **$416** is that $347 plus the 24.09→28.94 k step. Leftover miner torque vs a same-k royalty is the $347 node, not $416. Do **not** pair $347/GEO cash cost with miner AISC.

### 3) Cobre restart already in $266
Stockpile **27.5k / 540k ≈ 5%** of one year. Q2 gold GEOs nil. No restart decision. $266→$304 is **k + $4,500→$4,900**, not Cobre.

### 4) Energy second book
Q2 Energy **$70.4 m / $580.9 m ≈ 12%**. No 3y WTI. Residual unscaled.

### 5) 7× miner template → $92
Closed. Firstmate retired 7× as official. 91% Adj. EBITDA margin / no-mine book is why 7× loses to the 5y tape (~20–29).

### 6) Median 24.42 instead of mid-range 24.09 → $308
Same bucket as a check. **$4** vs $304. Not official.

### 7) Ag/PGM beta 1
No 3y Ag line. Residual **unscaled**, not uncorrelated.

**Bottom line.** Official identity is StockIntent 5y range k on Adj. E. Checks (25.6×, 24.42, 7×) stay checks. Tape $266 is the remaining steelman that 24.09 is rich vs the **21 Aug implied ~21.0×** on $4,900 Adj. E (StockIntent **20.42** is the **30 Jun** print, not today).

## Uncertainties

- Official 21 Aug LBMA/COMEX missing.
- 2027–29 GEOs missing — run-rate, not a path.
- TTM-k vs Adj-E FLAG (accepted).
- Incremental 20–23% tax on the gold step.
- Stream costs treated gold-linked; Ag/PGM slice would understate w.
- H1×2 vs Q1/Q2 mix: Musselwhite Q2 **3,951 GEOs** 2025 catch-up (~1.5% H1); H2 weighting. Neither moves $5 on $304.
- H1 revenue **$1,231.6 m** is an **MDA print**.
- FM net debt **$5,407 m** (30 Jun) — stockpile timing can slip; does not break A.
- Transfer-pricing law 26 Mar 2026 under evaluation. Barbados QDMTT $32.8 m.
- Extra $173 OCF residual is disclosed; it is not the H1 OCF−NI−DA leftover.

## Sources

- HOUSE-MODEL: `/home/box/agent-data/grok-research/reports/HOUSE-MODEL.md`
- GOLD-METAL current: `/home/box/agent-data/grok-research/views/GOLD-METAL.md`
- FNV-SCOUT: `/home/box/agent-data/grok-research/reports/FNV-SCOUT.md`
- k tape: `models/FNV/ev_ebitda_history.md` (StockIntent 5y only for official k)
- Statements: `models/FNV/is_3y.csv`, `bs_3y.csv`, `cf_3y.csv`, `valuation_3y.csv`
