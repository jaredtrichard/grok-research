# BTG house model

| Field | Value |
| --- | --- |
| Clock | **3y run-rate** (2026 guide year held). Y2/Y3 ounces beyond the 2026 guide = **UNSOURCED** (Regional 2028 >150 koz @ 65/35, Goose ~300 colour) and **dropped from the mid**. |
| Gold | GOLD-METAL **3,900 / 4,500 / 4,900 / 5,900**. Spot print **~4,600**. GOLD-METAL file **not edited**. |
| As-of | 22 Aug 2026. Statements from **Q2 2026 NR / Ex 99.2 (6 Aug 2026)**. |
| Units | US$m in csv (rounded 0.001 from USD). Ounces 100% unless `oz_attrib`. |
| Official k | **UNSOURCED** — no official $/sh mid |
| Store | segments.csv, is.csv, bs.csv, cf.csv, valuation.csv, working_table.csv, summary.json |
| Stage | **watch**. View is **draft — pending fresh review**, not current. |

## Ties (must be ~0)

- `bear` IS→CF→BS cash/RE/NCI: **tie_gap = 0.000000** (USD)
- `check12` IS→CF→BS cash/RE/NCI: **tie_gap = 0.000000** (USD)
- `spot` IS→CF→BS cash/RE/NCI: **tie_gap = 0.000000** (USD)
- `base` IS→CF→BS cash/RE/NCI: **tie_gap = 0.000000** (USD)
- `bull` IS→CF→BS cash/RE/NCI: **tie_gap = 0.000000** (USD)

Cash BS = CF ending cash. NI → SE / NCI. Capex sustaining + growth = total (H1×2).

## Official mid construction

- Volume = 2026 guide **mid 870 koz** (820–920). Attrib **780 koz** (Fekola 80%, Otjikoto 90%, Goose/Masbate 100%).
- Costs = guide cash-op mids. Royalties = Q2 mine royalty **% of site realized**, scaled to scenario gold.
- Capex / G&A / SBC / community / interest / dividends / NCI dist = **H1 × 2** (computed; no FY guide printed).
- Tax = **Q2 current tax / Q2 gold revenue** × EBT. Deferred tax **UNSOURCED** (0 in mid).
- WC = **0** (labelled). Q2 WC $(118)m is not the mid.
- OCF = NI + DA + SBC + **all IS interest** (BTG prints interest paid in financing).
- Company FCF = OCF − all mining-interest capex.
- Shares = diluted WASO **1,489.867m**. Convert ITM = dilution not second debt.
- Net debt in PT = **working open** $169.510m (30 Jun cash $286.576 − debt $456.086; +$95m/+$95m RCF).
- Stream $257.3m **not** in net debt.
- **Lead: 7.0x EV / IS-built EBITDA.** FCF yield 9% / 8% / 11% is a **check only** (FLAG if |gap| > 20%).

## Official 7.0x PTs (rounded $0.05)

| case | gold | ebitda $m | pt_7x | fcf $m | fcf check | gap | flag |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| base | 4900 | 2670.12 | **12.40** | 1508.075 | 11.10 | 11.7% | ok |
| bull | 5900 | 3452.446 | **16.10** | 2112.145 | 17.60 | -8.5% | ok |
| bear | 3900 | 1887.795 | **8.75** | 904.005 | 5.40 | 62.3% | FLAG |
| check12 | 4500 | 2357.19 | **10.95** | 1266.447 | 9.30 | 17.5% | ok |
| spot | 4600 | 2435.423 | **11.30** | 1326.854 | 9.75 | 15.9% | ok |

## UNSOURCED (dropped from mid)

- Company adj. EBITDA KPI (7× uses IS-built)
- FY 2026 capex / G&A / ETR guides (H1×2 is computed)
- Deferred tax run-rate (**0** in mid)
- Collar leftover notional (3y mid is pre-collar; 12m check pre-collar labelled)
- Regional 2028 ounces / 65/35 2026 oz (not in 2026 guide)
- Goose 300 koz colour
- Gramalote FID
- TSX:BTO close
- Period-end diluted shares (WASO used)
