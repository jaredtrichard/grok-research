# SpaceX consolidated income statement

as_of: 2026-08-30
units: USD millions
generator: `compute.py`

The forecast is built from the combined segment statements in `segments.md`; consolidated revenue and EBIT are not separate plugs. FY2023–FY2025 remain retrospectively recast for xAI/X. FY2026E equals H1 actual plus H2 forecast. Cursor P&L is a non-zero `[VIEW; as_of 2026-08-30; not a filing line]` from H2 2026 onward and is not back-cast into Q2. Starship commercial and pending EchoStar spectrum/mobile overlays are also explicit forecast views.

## Segment revenue bridge

| period | Space | Connectivity | AI | consolidated |
| --- | ---: | ---: | ---: | ---: |
| FY2023 | $3,557.0 [FACT] | $3,869.0 [FACT] | $2,961.0 [FACT] | $10,387.0 [DEDUCTED F119] |
| FY2024 | $3,796.0 [FACT] | $7,599.0 [FACT] | $2,620.0 [FACT] | $14,015.0 [DEDUCTED F127] |
| FY2025 | $4,086.0 [FACT] | $11,387.0 [FACT] | $3,201.0 [FACT] | $18,674.0 [DEDUCTED F135] |
| H1 2026A | $1,581.0 [FACT] | $7,548.0 [FACT] | $3,379.0 [FACT] | $12,508.0 [DEDUCTED F143] |
| FY2026E | $3,861.0 [DEDUCTED F050] | $15,940.0 [DEDUCTED F054] | $10,139.0 [DEDUCTED F058] | $29,940.0 [DEDUCTED F151] |
| FY2027E | $6,274.4 [DEDUCTED F074] | $20,791.5 [DEDUCTED F078] | $15,737.1 [DEDUCTED F082] | $42,802.9 [DEDUCTED F159] |
| FY2028E | $12,084.5 [DEDUCTED F099] | $26,936.4 [DEDUCTED F103] | $21,202.4 [DEDUCTED F107] | $60,223.3 [DEDUCTED F167] |

## Consolidated statement

| line | FY2023 | FY2024 | FY2025 | H1 2026A | FY2026E | FY2027E | FY2028E |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Revenue | $10,387.0 [FACT] | $14,015.0 [FACT] | $18,674.0 [FACT] | $12,508.0 [FACT] | $29,940.0 [DEDUCTED F151] | $42,802.9 [DEDUCTED F159] | $60,223.3 [DEDUCTED F167] |
| Cost of revenue | $6,110.0 [FACT] | $7,996.0 [FACT] | $9,451.0 [FACT] | $5,883.0 [FACT] | $13,118.5 [DEDUCTED F152] | $16,546.5 [DEDUCTED F160] | $21,771.7 [DEDUCTED F168] |
| Gross profit | $4,277.0 [DEDUCTED F126] | $6,019.0 [DEDUCTED F134] | $9,223.0 [DEDUCTED F142] | $6,625.0 [DEDUCTED F150] | $16,821.5 [DEDUCTED F158] | $26,256.4 [DEDUCTED F166] | $38,451.6 [DEDUCTED F174] |
| Research and development | $2,105.0 [FACT] | $3,464.0 [FACT] | $8,643.0 [FACT] | $7,062.0 [FACT] | $14,812.0 [DEDUCTED F153] | $14,700.0 [DEDUCTED F161] | $15,300.0 [DEDUCTED F169] |
| Selling, general and administrative | $1,665.0 [FACT] | $1,813.0 [FACT] | $2,644.0 [FACT] | $1,658.0 [FACT] | $3,558.0 [DEDUCTED F154] | $4,570.0 [DEDUCTED F162] | $5,430.0 [DEDUCTED F170] |
| Restructuring | $237.0 [FACT] | $213.0 [FACT] | $487.0 [FACT] | $(9.0) [FACT] | $(9.0) [DEDUCTED F155] | $0.0 [DEDUCTED F163] | $0.0 [DEDUCTED F171] |
| Impairment | $3,775.0 [FACT] | $63.0 [FACT] | $38.0 [FACT] | $0.0 [FACT] | $0.0 [DEDUCTED F156] | $0.0 [DEDUCTED F164] | $0.0 [DEDUCTED F172] |
| Operating income / EBIT | $(3,505.0) [FACT] | $466.0 [FACT] | $(2,589.0) [FACT] | $(2,086.0) [FACT] | $(1,539.5) [DEDUCTED F157] | $6,986.4 [DEDUCTED F165] | $17,721.6 [DEDUCTED F173] |
| Interest expense | $1,693.0 [FACT] | $1,580.0 [FACT] | $1,945.0 [FACT] | $1,293.0 [FACT] | $2,793.0 [DEDUCTED F210] | $2,500.0 [VIEW; as_of 2026-08-30; not a filing line] | $2,400.0 [VIEW; as_of 2026-08-30; not a filing line] |
| Interest income | $249.0 [FACT] | $371.0 [FACT] | $492.0 [FACT] | $553.0 [FACT] | $2,353.0 [DEDUCTED F211] | $3,000.0 [VIEW; as_of 2026-08-30; not a filing line] | $2,500.0 [VIEW; as_of 2026-08-30; not a filing line] |
| Other income / (expense) | $(42.0) [FACT] | $985.0 [FACT] | $(177.0) [FACT] | $(1,962.0) [FACT] | $(1,962.0) [DEDUCTED F212] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] |
| Pretax income | $(4,991.0) [DEDUCTED F204] | $242.0 [DEDUCTED F205] | $(4,219.0) [DEDUCTED F206] | $(4,788.0) [DEDUCTED F207] | $(3,941.5) [DEDUCTED F215] | $7,486.4 [DEDUCTED F216] | $17,821.6 [DEDUCTED F219] |
| Tax provision / (benefit) | $(363.0) [FACT] | $(549.0) [FACT] | $718.0 [FACT] | $29.0 [FACT] | $29.0 [DEDUCTED F213] | $1,272.7 [DEDUCTED F217] | $3,564.3 [DEDUCTED F220] |
| Net income | $(4,628.0) [FACT] | $791.0 [FACT] | $(4,937.0) [FACT] | $(4,817.0) [FACT] | $(3,970.5) [DEDUCTED F214] | $6,213.7 [DEDUCTED F218] | $14,257.3 [DEDUCTED F221] |

## Below-EBIT forecast drivers

| period | driver | assumption | research instruction |
| --- | --- | --- | --- |
| H2 2026E | Interest expense / income / other income / tax | $1,500.0 / $1,800.0 / $0.0 / $0.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Corporate / financing; tax attributes not obtained |
| FY2027E | Interest expense / income / other income / tax rate | $2,500.0 / $3,000.0 / $0.0 / 17.0% [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Corporate / financing |
| FY2028E | Interest expense / income / other income / tax rate | $2,400.0 / $2,500.0 / $0.0 / 20.0% [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Corporate / financing |

FY2027E and FY2028E tax provisions apply the explicit `[VIEW; as_of 2026-08-30; not a filing line]` rates in `compute.py` to positive pretax income. FY2026E includes the H1 actual tax provision plus a zero H2 cash/book provision `[VIEW; as_of 2026-08-30; not a filing line]` because utilization of tax attributes is not obtained. Fully diluted EPS is not presented because fully diluted shares are **not obtained**.

## Formula register

Every `[DEDUCTED]` cell above points to one of these formulas.

| id | output | expression | named inputs | result |
| --- | --- | --- | --- | --- |
| F119 | `income.FY2023.revenue` | space + connectivity + ai | space=3557; connectivity=3869; ai=2961 | 10,387.0 |
| F120 | `income.FY2023.cor` | space + connectivity + ai | space=1669; connectivity=2786; ai=1655 | 6,110.0 |
| F121 | `income.FY2023.rd` | space + connectivity + ai | space=1538; connectivity=381; ai=186 | 2,105.0 |
| F122 | `income.FY2023.sga` | space + connectivity + ai | space=351; connectivity=233; ai=1081 | 1,665.0 |
| F123 | `income.FY2023.restruct` | space + connectivity + ai | space=0; connectivity=0; ai=237 | 237.0 |
| F124 | `income.FY2023.impairment` | space + connectivity + ai | space=0; connectivity=0; ai=3775 | 3,775.0 |
| F125 | `income.FY2023.ebit` | space + connectivity + ai | space=(-1); connectivity=469; ai=(-3973) | (3,505.0) |
| F126 | `income.FY2023.gross_profit` | revenue - cost_of_revenue | revenue=10387; cost_of_revenue=6110 | 4,277.0 |
| F127 | `income.FY2024.revenue` | space + connectivity + ai | space=3796; connectivity=7599; ai=2620 | 14,015.0 |
| F128 | `income.FY2024.cor` | space + connectivity + ai | space=1541; connectivity=4768; ai=1687 | 7,996.0 |
| F129 | `income.FY2024.rd` | space + connectivity + ai | space=1835; connectivity=453; ai=1176 | 3,464.0 |
| F130 | `income.FY2024.sga` | space + connectivity + ai | space=375; connectivity=333; ai=1105 | 1,813.0 |
| F131 | `income.FY2024.restruct` | space + connectivity + ai | space=0; connectivity=0; ai=213 | 213.0 |
| F132 | `income.FY2024.impairment` | space + connectivity + ai | space=24; connectivity=39; ai=0 | 63.0 |
| F133 | `income.FY2024.ebit` | space + connectivity + ai | space=21; connectivity=2006; ai=(-1561) | 466.0 |
| F134 | `income.FY2024.gross_profit` | revenue - cost_of_revenue | revenue=14015; cost_of_revenue=7996 | 6,019.0 |
| F135 | `income.FY2025.revenue` | space + connectivity + ai | space=4086; connectivity=11387; ai=3201 | 18,674.0 |
| F136 | `income.FY2025.cor` | space + connectivity + ai | space=1352; connectivity=5921; ai=2178 | 9,451.0 |
| F137 | `income.FY2025.rd` | space + connectivity + ai | space=3004; connectivity=575; ai=5064 | 8,643.0 |
| F138 | `income.FY2025.sga` | space + connectivity + ai | space=349; connectivity=468; ai=1827 | 2,644.0 |
| F139 | `income.FY2025.restruct` | space + connectivity + ai | space=0; connectivity=0; ai=487 | 487.0 |
| F140 | `income.FY2025.impairment` | space + connectivity + ai | space=38; connectivity=0; ai=0 | 38.0 |
| F141 | `income.FY2025.ebit` | space + connectivity + ai | space=(-657); connectivity=4423; ai=(-6355) | (2,589.0) |
| F142 | `income.FY2025.gross_profit` | revenue - cost_of_revenue | revenue=18674; cost_of_revenue=9451 | 9,223.0 |
| F143 | `income.H1 2026A.revenue` | space + connectivity + ai | space=1581; connectivity=7548; ai=3379 | 12,508.0 |
| F144 | `income.H1 2026A.cor` | space + connectivity + ai | space=610; connectivity=3711; ai=1562 | 5,883.0 |
| F145 | `income.H1 2026A.rd` | space + connectivity + ai | space=2006; connectivity=499; ai=4557 | 7,062.0 |
| F146 | `income.H1 2026A.sga` | space + connectivity + ai | space=169; connectivity=494; ai=995 | 1,658.0 |
| F147 | `income.H1 2026A.restruct` | space + connectivity + ai | space=0; connectivity=0; ai=(-9) | (9.0) |
| F148 | `income.H1 2026A.impairment` | space + connectivity + ai | space=0; connectivity=0; ai=0 | 0.0 |
| F149 | `income.H1 2026A.ebit` | space + connectivity + ai | space=(-1204); connectivity=2844; ai=(-3726) | (2,086.0) |
| F150 | `income.H1 2026A.gross_profit` | revenue - cost_of_revenue | revenue=12508; cost_of_revenue=5883 | 6,625.0 |
| F151 | `income.FY2026E.revenue` | space + connectivity + ai | space=3861; connectivity=15940; ai=10139 | 29,940.0 |
| F152 | `income.FY2026E.cor` | space + connectivity + ai | space=1515.5; connectivity=7313; ai=4290 | 13,118.5 |
| F153 | `income.FY2026E.rd` | space + connectivity + ai | space=4206; connectivity=849; ai=9757 | 14,812.0 |
| F154 | `income.FY2026E.sga` | space + connectivity + ai | space=369; connectivity=844; ai=2345 | 3,558.0 |
| F155 | `income.FY2026E.restruct` | space + connectivity + ai | space=0; connectivity=0; ai=(-9) | (9.0) |
| F156 | `income.FY2026E.impairment` | space + connectivity + ai | space=0; connectivity=0; ai=0 | 0.0 |
| F157 | `income.FY2026E.ebit` | space + connectivity + ai | space=(-2229.5); connectivity=6934; ai=(-6244) | (1,539.5) |
| F158 | `income.FY2026E.gross_profit` | revenue - cost_of_revenue | revenue=29940; cost_of_revenue=13118.5 | 16,821.5 |
| F159 | `income.FY2027E.revenue` | space + connectivity + ai | space=6274.36; connectivity=20791.5; ai=15737.05 | 42,802.9 |
| F160 | `income.FY2027E.cor` | space + connectivity + ai | space=2567.2184; connectivity=8328.49; ai=5650.78 | 16,546.5 |
| F161 | `income.FY2027E.rd` | space + connectivity + ai | space=4200; connectivity=1000; ai=9500 | 14,700.0 |
| F162 | `income.FY2027E.sga` | space + connectivity + ai | space=220; connectivity=1100; ai=3250 | 4,570.0 |
| F163 | `income.FY2027E.restruct` | space + connectivity + ai | space=0; connectivity=0; ai=0 | 0.0 |
| F164 | `income.FY2027E.impairment` | space + connectivity + ai | space=0; connectivity=0; ai=0 | 0.0 |
| F165 | `income.FY2027E.ebit` | space + connectivity + ai | space=(-712.8584); connectivity=10363.01; ai=(-2663.73) | 6,986.4 |
| F166 | `income.FY2027E.gross_profit` | revenue - cost_of_revenue | revenue=42802.91; cost_of_revenue=16546.4884 | 26,256.4 |
| F167 | `income.FY2028E.revenue` | space + connectivity + ai | space=12084.4832; connectivity=26936.375; ai=21202.425 | 60,223.3 |
| F168 | `income.FY2028E.cor` | space + connectivity + ai | space=4590.482944; connectivity=10255.46875; ai=6925.7006 | 21,771.7 |
| F169 | `income.FY2028E.rd` | space + connectivity + ai | space=3600; connectivity=1200; ai=10500 | 15,300.0 |
| F170 | `income.FY2028E.sga` | space + connectivity + ai | space=230; connectivity=1300; ai=3900 | 5,430.0 |
| F171 | `income.FY2028E.restruct` | space + connectivity + ai | space=0; connectivity=0; ai=0 | 0.0 |
| F172 | `income.FY2028E.impairment` | space + connectivity + ai | space=0; connectivity=0; ai=0 | 0.0 |
| F173 | `income.FY2028E.ebit` | space + connectivity + ai | space=3664.000256; connectivity=14180.90625; ai=(-123.2756) | 17,721.6 |
| F174 | `income.FY2028E.gross_profit` | revenue - cost_of_revenue | revenue=60223.2832; cost_of_revenue=21771.652294 | 38,451.6 |
| F196 | `income.H2 2026E.revenue` | space + connectivity + ai | space=2280; connectivity=8392; ai=6760 | 17,432.0 |
| F197 | `income.H2 2026E.cor` | space + connectivity + ai | space=905.5; connectivity=3602; ai=2728 | 7,235.5 |
| F198 | `income.H2 2026E.rd` | space + connectivity + ai | space=2200; connectivity=350; ai=5200 | 7,750.0 |
| F199 | `income.H2 2026E.sga` | space + connectivity + ai | space=200; connectivity=350; ai=1350 | 1,900.0 |
| F200 | `income.H2 2026E.restruct` | space + connectivity + ai | space=0; connectivity=0; ai=0 | 0.0 |
| F201 | `income.H2 2026E.impairment` | space + connectivity + ai | space=0; connectivity=0; ai=0 | 0.0 |
| F202 | `income.H2 2026E.ebit` | space + connectivity + ai | space=(-1025.5); connectivity=4090; ai=(-2518) | 546.5 |
| F203 | `income.H2 2026E.gross_profit` | revenue - cost_of_revenue | revenue=17432; cost_of_revenue=7235.5 | 10,196.5 |
| F204 | `income.FY2023.pretax` | EBIT - interest_expense + interest_income + other_income | EBIT=(-3505); interest_expense=1693; interest_income=249; other_income=(-42) | (4,991.0) |
| F205 | `income.FY2024.pretax` | EBIT - interest_expense + interest_income + other_income | EBIT=466; interest_expense=1580; interest_income=371; other_income=985 | 242.0 |
| F206 | `income.FY2025.pretax` | EBIT - interest_expense + interest_income + other_income | EBIT=(-2589); interest_expense=1945; interest_income=492; other_income=(-177) | (4,219.0) |
| F207 | `income.H1 2026A.pretax` | EBIT - interest_expense + interest_income + other_income | EBIT=(-2086); interest_expense=1293; interest_income=553; other_income=(-1962) | (4,788.0) |
| F208 | `income.H2 2026E.pretax` | EBIT - interest_expense + interest_income + other_income | EBIT=546.5; interest_expense=1500; interest_income=1800; other_income=0 | 846.5 |
| F209 | `income.H2 2026E.net_income` | pretax_income - tax_provision | pretax_income=846.5; tax_provision=0 | 846.5 |
| F210 | `income.FY2026E.interest_expense` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=1293; H2_2026_forecast=1500 | 2,793.0 |
| F211 | `income.FY2026E.interest_income` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=553; H2_2026_forecast=1800 | 2,353.0 |
| F212 | `income.FY2026E.other_income` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=(-1962); H2_2026_forecast=0 | (1,962.0) |
| F213 | `income.FY2026E.tax` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=29; H2_2026_forecast=0 | 29.0 |
| F214 | `income.FY2026E.net_income` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=(-4817); H2_2026_forecast=846.5 | (3,970.5) |
| F215 | `income.FY2026E.pretax` | EBIT - interest_expense + interest_income + other_income | EBIT=(-1539.5); interest_expense=2793; interest_income=2353; other_income=(-1962) | (3,941.5) |
| F216 | `income.FY2027E.pretax` | EBIT - interest_expense + interest_income + other_income | EBIT=6986.4216; interest_expense=2500; interest_income=3000; other_income=0 | 7,486.4 |
| F217 | `income.FY2027E.tax` | positive_pretax_income × tax_rate | positive_pretax_income=7486.4216; tax_rate=0.17 | 1,272.7 |
| F218 | `income.FY2027E.net_income` | pretax_income - tax_provision | pretax_income=7486.4216; tax_provision=1272.691672 | 6,213.7 |
| F219 | `income.FY2028E.pretax` | EBIT - interest_expense + interest_income + other_income | EBIT=17721.630906; interest_expense=2400; interest_income=2500; other_income=0 | 17,821.6 |
| F220 | `income.FY2028E.tax` | positive_pretax_income × tax_rate | positive_pretax_income=17821.630906; tax_rate=0.2 | 3,564.3 |
| F221 | `income.FY2028E.net_income` | pretax_income - tax_provision | pretax_income=17821.630906; tax_provision=3564.3261812 | 14,257.3 |
