# SpaceX balance sheet

as_of: 2026-08-30
units: USD millions except shares
generator: `compute.py`

Cash ties to `cashflow.md`. Forecast PP&E uses opening PP&E + capex − D&A `[VIEW; as_of 2026-08-30; not a filing line]`; this simplifying bridge treats all D&A as PP&E depreciation because an intangible-amortization forecast is **not obtained**. Other assets are the explicit balancing residual and include Cursor purchase accounting, goodwill/intangibles and other items not separately forecast.

## Balance sheet

| line | FY2025 | H1 2026A | FY2026E | FY2027E | FY2028E |
| --- | ---: | ---: | ---: | ---: | ---: |
| Cash | $24,747.0 [FACT] | $93,522.0 [FACT] | $70,831.2 [DEDUCTED F255] | $57,720.3 [DEDUCTED F272] | $60,050.4 [DEDUCTED F289] |
| Marketable securities | $0.0 [FACT] | $6,487.0 [FACT] | $6,487.0 [VIEW; as_of 2026-08-30; not a filing line] | $6,487.0 [VIEW; as_of 2026-08-30; not a filing line] | $6,487.0 [VIEW; as_of 2026-08-30; not a filing line] |
| Accounts receivable | $1,579.0 [FACT] | $3,596.0 [FACT] | $4,491.0 [DEDUCTED F246] | $5,992.4 [DEDUCTED F263] | $7,829.0 [DEDUCTED F280] |
| Inventory | $2,416.0 [FACT] | $2,718.0 [FACT] | $2,994.0 [DEDUCTED F247] | $3,852.3 [DEDUCTED F264] | $4,817.9 [DEDUCTED F281] |
| PP&E, net | $42,602.0 [FACT] | $65,736.0 [FACT] | $81,220.3 [DEDUCTED F257] | $104,685.3 [DEDUCTED F274] | $121,310.3 [DEDUCTED F291] |
| Pending EchoStar spectrum assets | $0.0 [FACT] | $0.0 [FACT] | $19,600.0 [VIEW; as_of 2026-08-30; not a filing line] | $19,600.0 [VIEW; as_of 2026-08-30; not a filing line] | $19,600.0 [VIEW; as_of 2026-08-30; not a filing line] |
| Other assets / purchase-accounting residual | $20,735.0 [DEDUCTED F237] | $20,711.0 [DEDUCTED F239] | $83,711.3 [DEDUCTED F261] | $85,711.3 [DEDUCTED F278] | $87,711.3 [DEDUCTED F295] |
| Total assets | $92,079.0 [FACT] | $192,770.0 [FACT] | $269,334.8 [DEDUCTED F262] | $284,048.5 [DEDUCTED F279] | $307,805.9 [DEDUCTED F296] |
| Debt and finance leases | $22,896.0 [FACT] | $39,364.0 [FACT] | $39,364.0 [VIEW; as_of 2026-08-30; not a filing line] | $39,364.0 [VIEW; as_of 2026-08-30; not a filing line] | $39,364.0 [VIEW; as_of 2026-08-30; not a filing line] |
| Deferred revenue | $12,116.0 [FACT] | $14,286.0 [FACT] | $16,000.0 [VIEW; as_of 2026-08-30; not a filing line] | $18,500.0 [VIEW; as_of 2026-08-30; not a filing line] | $21,000.0 [VIEW; as_of 2026-08-30; not a filing line] |
| Other liabilities | $15,742.0 [DEDUCTED F238] | $11,896.0 [DEDUCTED F240] | $13,000.0 [VIEW; as_of 2026-08-30; not a filing line] | $15,000.0 [VIEW; as_of 2026-08-30; not a filing line] | $17,000.0 [VIEW; as_of 2026-08-30; not a filing line] |
| Total liabilities | $50,754.0 [FACT] | $65,546.0 [FACT] | $68,364.0 [DEDUCTED F259] | $72,864.0 [DEDUCTED F276] | $77,364.0 [DEDUCTED F293] |
| Redeemable preferred stock | $38,752.0 [FACT] | $0.0 [FACT] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] |
| Shareholders' equity | $2,573.0 [FACT] | $127,224.0 [FACT] | $200,970.8 [DEDUCTED F258] | $211,184.5 [DEDUCTED F275] | $230,441.9 [DEDUCTED F292] |

## Forecast balance drivers

| period | driver | assumption | research instruction |
| --- | --- | --- | --- |
| H2 2026E | Accounts receivable / inventory | 15.0% / 10.0% of annual revenue [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Working capital |
| H2 2026E | Deferred revenue / other liabilities | $16,000.0 / $13,000.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Backlog and deferred revenue as constraints |
| H2 2026E | Debt / marketable securities | $39,364 / $6,487 held flat [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Corporate / financing; new financing not obtained |
| FY2027E | Accounts receivable / inventory | 14.0% / 9.0% of annual revenue [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Working capital |
| FY2027E | Deferred revenue / other liabilities | $18,500.0 / $15,000.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Backlog and deferred revenue as constraints |
| FY2027E | Debt / marketable securities | $39,364 / $6,487 held flat [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Corporate / financing; new financing not obtained |
| FY2028E | Accounts receivable / inventory | 13.0% / 8.0% of annual revenue [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Working capital |
| FY2028E | Deferred revenue / other liabilities | $21,000.0 / $17,000.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Backlog and deferred revenue as constraints |
| FY2028E | Debt / marketable securities | $39,364 / $6,487 held flat [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Corporate / financing; new financing not obtained |
| H2 2026E | Cursor stock consideration | $60,000.0 [VIEW; as_of 2026-08-30; not a filing line] | Share step-up is required by `research.md`; final purchase accounting is not obtained |
| H2 2026E | Pending EchoStar consideration | $19,600.0 spectrum asset / $11,100.3 equity / $8,500.0 cash [VIEW; as_of 2026-08-30; not a filing line] | Pending deal included in base; not a closed filing balance |

The H2 2026 Cursor bridge assumes $60,000 of stock consideration `[VIEW; as_of 2026-08-30; not a filing line]` in equity and the other-assets residual; final purchase accounting and Cursor standalone net assets are **not obtained**. Cursor P&L is modeled separately in AI. The pending EchoStar base view adds spectrum assets, equity shares and cash consideration while holding debt flat. Refinancing, repayment and new borrowing are not obtained.

## Balance check

| period | total assets | liabilities + preferred + equity | difference |
| --- | ---: | ---: | ---: |
| FY2025 | $92,079.0 [FACT] | $92,079.0 [DEDUCTED F317] | 0.0 |
| H1 2026A | $192,770.0 [FACT] | $192,770.0 [DEDUCTED F318] | 0.0 |
| FY2026E | $269,334.8 [DEDUCTED F262] | $269,334.8 [DEDUCTED F260] | 0.0 |
| FY2027E | $284,048.5 [DEDUCTED F279] | $284,048.5 [DEDUCTED F277] | 0.0 |
| FY2028E | $307,805.9 [DEDUCTED F296] | $307,805.9 [DEDUCTED F294] | 0.0 |

## Basic shares

| period | ending basic shares (millions) | treatment |
| --- | --- | --- |
| H1 2026A | 13,176.0 [FACT] | June 30 issued Class A plus Class B; July 28 count is higher |
| FY2026E | 13,834.6 [DEDUCTED F313] | Post-Cursor plus 261.8 million pending EchoStar shares `[VIEW; as_of 2026-08-30; not a filing line]` |
| FY2027E | 13,834.6 [VIEW; as_of 2026-08-30; not a filing line] | Held flat after pending EchoStar inclusion; exercises and fully diluted shares are not obtained |
| FY2028E | 13,834.6 [VIEW; as_of 2026-08-30; not a filing line] | Held flat after pending EchoStar inclusion; exercises and fully diluted shares are not obtained |

Point-in-time fully diluted shares and float remain **not obtained**. Share-based compensation is included in expense/cash-flow reconciliation, but no exercise issuance is modeled.

## EchoStar pending base treatment

The base includes approximately 261.8 million Class A shares and approximately $19,600 consideration: $11,100.32 equity at $42.40 and $8,500 cash `[VIEW; as_of 2026-08-30; not a filing line]`. The transaction terms are `[FACT]` in `register.md`; including the pending close in forecast shares, cash and spectrum assets is a view. Closing date, final cash use and purchase accounting remain **not obtained**.

## Formula register

Every `[DEDUCTED]` cell above points to one of these formulas.

| id | output | expression | named inputs | result |
| --- | --- | --- | --- | --- |
| F237 | `balance.FY2025.other_assets` | total_assets - cash - securities - accounts_receivable - inventory - PP&E - spectrum_assets | total_assets=92079; cash=24747; securities=0; accounts_receivable=1579; inventory=2416; PP&E=42602; spectrum_assets=0 | 20,735.0 |
| F238 | `balance.FY2025.other_liabilities` | total_liabilities - debt_and_finance_leases - deferred_revenue | total_liabilities=50754; debt_and_finance_leases=22896; deferred_revenue=12116 | 15,742.0 |
| F239 | `balance.H1 2026A.other_assets` | total_assets - cash - securities - accounts_receivable - inventory - PP&E - spectrum_assets | total_assets=192770; cash=93522; securities=6487; accounts_receivable=3596; inventory=2718; PP&E=65736; spectrum_assets=0 | 20,711.0 |
| F240 | `balance.H1 2026A.other_liabilities` | total_liabilities - debt_and_finance_leases - deferred_revenue | total_liabilities=65546; debt_and_finance_leases=39364; deferred_revenue=14286 | 11,896.0 |
| F246 | `balance.H2 2026E.accounts_receivable` | annual_revenue × accounts_receivable_pct_revenue | annual_revenue=29940; accounts_receivable_pct_revenue=0.15 | 4,491.0 |
| F247 | `balance.H2 2026E.inventory` | annual_revenue × inventory_pct_revenue | annual_revenue=29940; inventory_pct_revenue=0.1 | 2,994.0 |
| F257 | `balance.H2 2026E.PP&E` | opening_PP&E + capital_expenditures - depreciation_and_amortization | opening_PP&E=65736; capital_expenditures=21984.28; depreciation_and_amortization=6500 | 81,220.3 |
| F258 | `balance.H2 2026E.equity` | opening_equity + net_income + share_based_compensation + stock_issued_for_Cursor + pending_stock_issued_for_EchoStar | opening_equity=127224; net_income=846.5; share_based_compensation=1800; stock_issued_for_Cursor=60000; pending_stock_issued_for_EchoStar=11100.32 | 200,970.8 |
| F259 | `balance.H2 2026E.total_liabilities` | debt_and_finance_leases + deferred_revenue + other_liabilities | debt_and_finance_leases=39364; deferred_revenue=16000; other_liabilities=13000 | 68,364.0 |
| F260 | `balance.H2 2026E.total_liabilities_and_equity` | total_liabilities + redeemable_preferred + shareholders_equity | total_liabilities=68364; redeemable_preferred=0; shareholders_equity=200970.82 | 269,334.8 |
| F261 | `balance.H2 2026E.other_assets` | total_liabilities_and_equity - cash - securities - accounts_receivable - inventory - PP&E - spectrum_assets | total_liabilities_and_equity=269334.82; cash=70831.22; securities=6487; accounts_receivable=4491; inventory=2994; PP&E=81220.28; spectrum_assets=19600 | 83,711.3 |
| F262 | `balance.H2 2026E.total_assets` | cash + securities + accounts_receivable + inventory + PP&E + spectrum_assets + other_assets | cash=70831.22; securities=6487; accounts_receivable=4491; inventory=2994; PP&E=81220.28; spectrum_assets=19600; other_assets=83711.32 | 269,334.8 |
| F263 | `balance.FY2027E.accounts_receivable` | annual_revenue × accounts_receivable_pct_revenue | annual_revenue=42802.91; accounts_receivable_pct_revenue=0.14 | 5,992.4 |
| F264 | `balance.FY2027E.inventory` | annual_revenue × inventory_pct_revenue | annual_revenue=42802.91; inventory_pct_revenue=0.09 | 3,852.3 |
| F274 | `balance.FY2027E.PP&E` | opening_PP&E + capital_expenditures - depreciation_and_amortization | opening_PP&E=81220.28; capital_expenditures=38465; depreciation_and_amortization=15000 | 104,685.3 |
| F275 | `balance.FY2027E.equity` | opening_equity + net_income + share_based_compensation + stock_issued_for_Cursor + pending_stock_issued_for_EchoStar | opening_equity=200970.82; net_income=6213.729928; share_based_compensation=4000; stock_issued_for_Cursor=0; pending_stock_issued_for_EchoStar=0 | 211,184.5 |
| F276 | `balance.FY2027E.total_liabilities` | debt_and_finance_leases + deferred_revenue + other_liabilities | debt_and_finance_leases=39364; deferred_revenue=18500; other_liabilities=15000 | 72,864.0 |
| F277 | `balance.FY2027E.total_liabilities_and_equity` | total_liabilities + redeemable_preferred + shareholders_equity | total_liabilities=72864; redeemable_preferred=0; shareholders_equity=211184.549928 | 284,048.5 |
| F278 | `balance.FY2027E.other_assets` | total_liabilities_and_equity - cash - securities - accounts_receivable - inventory - PP&E - spectrum_assets | total_liabilities_and_equity=284048.549928; cash=57720.280628; securities=6487; accounts_receivable=5992.4074; inventory=3852.2619; PP&E=104685.28; spectrum_assets=19600 | 85,711.3 |
| F279 | `balance.FY2027E.total_assets` | cash + securities + accounts_receivable + inventory + PP&E + spectrum_assets + other_assets | cash=57720.280628; securities=6487; accounts_receivable=5992.4074; inventory=3852.2619; PP&E=104685.28; spectrum_assets=19600; other_assets=85711.32 | 284,048.5 |
| F280 | `balance.FY2028E.accounts_receivable` | annual_revenue × accounts_receivable_pct_revenue | annual_revenue=60223.2832; accounts_receivable_pct_revenue=0.13 | 7,829.0 |
| F281 | `balance.FY2028E.inventory` | annual_revenue × inventory_pct_revenue | annual_revenue=60223.2832; inventory_pct_revenue=0.08 | 4,817.9 |
| F291 | `balance.FY2028E.PP&E` | opening_PP&E + capital_expenditures - depreciation_and_amortization | opening_PP&E=104685.28; capital_expenditures=34625; depreciation_and_amortization=18000 | 121,310.3 |
| F292 | `balance.FY2028E.equity` | opening_equity + net_income + share_based_compensation + stock_issued_for_Cursor + pending_stock_issued_for_EchoStar | opening_equity=211184.549928; net_income=14257.3047248; share_based_compensation=5000; stock_issued_for_Cursor=0; pending_stock_issued_for_EchoStar=0 | 230,441.9 |
| F293 | `balance.FY2028E.total_liabilities` | debt_and_finance_leases + deferred_revenue + other_liabilities | debt_and_finance_leases=39364; deferred_revenue=21000; other_liabilities=17000 | 77,364.0 |
| F294 | `balance.FY2028E.total_liabilities_and_equity` | total_liabilities + redeemable_preferred + shareholders_equity | total_liabilities=77364; redeemable_preferred=0; shareholders_equity=230441.8546528 | 307,805.9 |
| F295 | `balance.FY2028E.other_assets` | total_liabilities_and_equity - cash - securities - accounts_receivable - inventory - PP&E - spectrum_assets | total_liabilities_and_equity=307805.8546528; cash=60050.3651808; securities=6487; accounts_receivable=7829.026816; inventory=4817.862656; PP&E=121310.28; spectrum_assets=19600 | 87,711.3 |
| F296 | `balance.FY2028E.total_assets` | cash + securities + accounts_receivable + inventory + PP&E + spectrum_assets + other_assets | cash=60050.3651808; securities=6487; accounts_receivable=7829.026816; inventory=4817.862656; PP&E=121310.28; spectrum_assets=19600; other_assets=87711.32 | 307,805.9 |
| F313 | `balance.FY2026E.basic_shares` | July_28_basic_shares_m + Cursor_merger_shares_m + Cursor_vested_RSU_shares_m + pending_EchoStar_shares_m | July_28_basic_shares_m=13181.779945; Cursor_merger_shares_m=389.289254; Cursor_vested_RSU_shares_m=1.752426; pending_EchoStar_shares_m=261.8 | 13,834.6 |
| F317 | `balance.FY2025.total_liabilities_and_equity` | total_liabilities + redeemable_preferred + shareholders_equity | total_liabilities=50754; redeemable_preferred=38752; shareholders_equity=2573 | 92,079.0 |
| F318 | `balance.H1 2026A.total_liabilities_and_equity` | total_liabilities + redeemable_preferred + shareholders_equity | total_liabilities=65546; redeemable_preferred=0; shareholders_equity=127224 | 192,770.0 |
