# SpaceX balance sheet

as_of: 2026-08-30
units: USD millions except shares
generator: `compute.py`

Cash ties to `cashflow.md`. Forecast PP&E uses opening PP&E + capex − D&A `[VIEW]`; this simplifying bridge treats all D&A as PP&E depreciation because an intangible-amortization forecast is **not obtained**. Other assets are the explicit balancing residual and include Cursor purchase accounting, goodwill/intangibles and other items not separately forecast.

## Balance sheet

| line | FY2025 | H1 2026A | FY2026E | FY2027E | FY2028E |
| --- | ---: | ---: | ---: | ---: | ---: |
| Cash | $24,747.0 [FACT] | $93,522.0 [FACT] | $79,733.7 [DEDUCTED F230] | $66,804.3 [DEDUCTED F247] | $66,835.4 [DEDUCTED F264] |
| Marketable securities | $0.0 [FACT] | $6,487.0 [FACT] | $6,487.0 [VIEW] | $6,487.0 [VIEW] | $6,487.0 [VIEW] |
| Accounts receivable | $1,579.0 [FACT] | $3,596.0 [FACT] | $4,303.5 [DEDUCTED F221] | $5,180.4 [DEDUCTED F238] | $5,944.0 [DEDUCTED F255] |
| Inventory | $2,416.0 [FACT] | $2,718.0 [FACT] | $2,869.0 [DEDUCTED F222] | $3,330.3 [DEDUCTED F239] | $3,657.9 [DEDUCTED F256] |
| PP&E, net | $42,602.0 [FACT] | $65,736.0 [FACT] | $81,220.3 [DEDUCTED F232] | $104,280.3 [DEDUCTED F249] | $119,655.3 [DEDUCTED F266] |
| Other assets / purchase-accounting residual | $20,735.0 [DEDUCTED F212] | $20,711.0 [DEDUCTED F214] | $83,711.0 [DEDUCTED F236] | $85,711.0 [DEDUCTED F253] | $87,711.0 [DEDUCTED F270] |
| Total assets | $92,079.0 [FACT] | $192,770.0 [FACT] | $258,324.5 [DEDUCTED F237] | $271,793.2 [DEDUCTED F254] | $290,290.5 [DEDUCTED F271] |
| Debt and finance leases | $22,896.0 [FACT] | $39,364.0 [FACT] | $39,364.0 [VIEW] | $39,364.0 [VIEW] | $39,364.0 [VIEW] |
| Deferred revenue | $12,116.0 [FACT] | $14,286.0 [FACT] | $16,000.0 [VIEW] | $18,500.0 [VIEW] | $21,000.0 [VIEW] |
| Other liabilities | $15,742.0 [DEDUCTED F213] | $11,896.0 [DEDUCTED F215] | $13,000.0 [VIEW] | $15,000.0 [VIEW] | $17,000.0 [VIEW] |
| Total liabilities | $50,754.0 [FACT] | $65,546.0 [FACT] | $68,364.0 [DEDUCTED F234] | $72,864.0 [DEDUCTED F251] | $77,364.0 [DEDUCTED F268] |
| Redeemable preferred stock | $38,752.0 [FACT] | $0.0 [FACT] | $0.0 [VIEW] | $0.0 [VIEW] | $0.0 [VIEW] |
| Shareholders' equity | $2,573.0 [FACT] | $127,224.0 [FACT] | $189,960.5 [DEDUCTED F233] | $198,929.2 [DEDUCTED F250] | $212,926.5 [DEDUCTED F267] |

## Forecast balance drivers

| period | driver | assumption | research instruction |
| --- | --- | --- | --- |
| H2 2026E | Accounts receivable / inventory | 15.0% / 10.0% of annual revenue [VIEW] | `research.md` Working capital |
| H2 2026E | Deferred revenue / other liabilities | $16,000.0 / $13,000.0 [VIEW] | `research.md` Backlog and deferred revenue as constraints |
| H2 2026E | Debt / marketable securities | $39,364 / $6,487 held flat [VIEW] | `research.md` Corporate / financing; new financing not obtained |
| FY2027E | Accounts receivable / inventory | 14.0% / 9.0% of annual revenue [VIEW] | `research.md` Working capital |
| FY2027E | Deferred revenue / other liabilities | $18,500.0 / $15,000.0 [VIEW] | `research.md` Backlog and deferred revenue as constraints |
| FY2027E | Debt / marketable securities | $39,364 / $6,487 held flat [VIEW] | `research.md` Corporate / financing; new financing not obtained |
| FY2028E | Accounts receivable / inventory | 13.0% / 8.0% of annual revenue [VIEW] | `research.md` Working capital |
| FY2028E | Deferred revenue / other liabilities | $21,000.0 / $17,000.0 [VIEW] | `research.md` Backlog and deferred revenue as constraints |
| FY2028E | Debt / marketable securities | $39,364 / $6,487 held flat [VIEW] | `research.md` Corporate / financing; new financing not obtained |
| H2 2026E | Cursor stock consideration | $60,000.0 [VIEW] | Share step-up is required by `research.md`; final purchase accounting is not obtained |

The H2 2026 Cursor bridge assumes $60,000 of stock consideration `[VIEW]` in equity and the other-assets residual; final purchase accounting and Cursor standalone net assets are **not obtained**. Cursor P&L contribution is zero `[VIEW]`. Debt is held flat after 2026-06-30 `[VIEW]`; refinancing, repayment and new borrowing are not obtained.

## Balance check

| period | total assets | liabilities + preferred + equity | difference |
| --- | ---: | ---: | ---: |
| FY2025 | $92,079.0 [FACT] | $92,079.0 [DEDUCTED F289] | 0.0 |
| H1 2026A | $192,770.0 [FACT] | $192,770.0 [DEDUCTED F290] | 0.0 |
| FY2026E | $258,324.5 [DEDUCTED F237] | $258,324.5 [DEDUCTED F235] | 0.0 |
| FY2027E | $271,793.2 [DEDUCTED F254] | $271,793.2 [DEDUCTED F252] | 0.0 |
| FY2028E | $290,290.5 [DEDUCTED F271] | $290,290.5 [DEDUCTED F269] | 0.0 |

## Basic shares

| period | ending basic shares (millions) | treatment |
| --- | --- | --- |
| H1 2026A | 13,176.0 [FACT] | June 30 issued Class A plus Class B; July 28 count is higher |
| FY2026E | 13,572.8 [DEDUCTED F288] | Post-Cursor basic shares from `research.md`; Cursor closed 2026-08-14 |
| FY2027E | 13,572.8 [VIEW] | Held flat because exercises, repurchases and fully diluted shares are not obtained |
| FY2028E | 13,572.8 [VIEW] | Held flat because exercises, repurchases and fully diluted shares are not obtained |

Point-in-time fully diluted shares and float remain **not obtained**. Share-based compensation is included in expense/cash-flow reconciliation, but no exercise issuance is modeled.

## EchoStar scenario memo — excluded from base case

The base case does not close EchoStar. Scenario inputs are approximately 261.8 million Class A shares and approximately $19,600 consideration (approximately $11,100 equity at $42.40 plus up to $8,500 tied to EchoStar debt payoff) `[FACT]` from `register.md`. Closing date, final cash use and purchase accounting remain **not obtained**.

## Formula register

Every `[DEDUCTED]` cell above points to one of these formulas.

| id | output | expression | named inputs | result |
| --- | --- | --- | --- | --- |
| F212 | `balance.FY2025.other_assets` | total_assets - cash - securities - accounts_receivable - inventory - PP&E | total_assets=92079; cash=24747; securities=0; accounts_receivable=1579; inventory=2416; PP&E=42602 | 20,735.0 |
| F213 | `balance.FY2025.other_liabilities` | total_liabilities - debt_and_finance_leases - deferred_revenue | total_liabilities=50754; debt_and_finance_leases=22896; deferred_revenue=12116 | 15,742.0 |
| F214 | `balance.H1 2026A.other_assets` | total_assets - cash - securities - accounts_receivable - inventory - PP&E | total_assets=192770; cash=93522; securities=6487; accounts_receivable=3596; inventory=2718; PP&E=65736 | 20,711.0 |
| F215 | `balance.H1 2026A.other_liabilities` | total_liabilities - debt_and_finance_leases - deferred_revenue | total_liabilities=65546; debt_and_finance_leases=39364; deferred_revenue=14286 | 11,896.0 |
| F221 | `balance.H2 2026E.accounts_receivable` | annual_revenue × accounts_receivable_pct_revenue | annual_revenue=28690; accounts_receivable_pct_revenue=0.15 | 4,303.5 |
| F222 | `balance.H2 2026E.inventory` | annual_revenue × inventory_pct_revenue | annual_revenue=28690; inventory_pct_revenue=0.1 | 2,869.0 |
| F232 | `balance.H2 2026E.PP&E` | opening_PP&E + capital_expenditures - depreciation_and_amortization | opening_PP&E=65736; capital_expenditures=21984.28; depreciation_and_amortization=6500 | 81,220.3 |
| F233 | `balance.H2 2026E.equity` | opening_equity + net_income + share_based_compensation + stock_issued_for_Cursor | opening_equity=127224; net_income=936.5; share_based_compensation=1800; stock_issued_for_Cursor=60000 | 189,960.5 |
| F234 | `balance.H2 2026E.total_liabilities` | debt_and_finance_leases + deferred_revenue + other_liabilities | debt_and_finance_leases=39364; deferred_revenue=16000; other_liabilities=13000 | 68,364.0 |
| F235 | `balance.H2 2026E.total_liabilities_and_equity` | total_liabilities + redeemable_preferred + shareholders_equity | total_liabilities=68364; redeemable_preferred=0; shareholders_equity=189960.5 | 258,324.5 |
| F236 | `balance.H2 2026E.other_assets` | total_liabilities_and_equity - cash - securities - accounts_receivable - inventory - PP&E | total_liabilities_and_equity=258324.5; cash=79733.72; securities=6487; accounts_receivable=4303.5; inventory=2869; PP&E=81220.28 | 83,711.0 |
| F237 | `balance.H2 2026E.total_assets` | cash + securities + accounts_receivable + inventory + PP&E + other_assets | cash=79733.72; securities=6487; accounts_receivable=4303.5; inventory=2869; PP&E=81220.28; other_assets=83711 | 258,324.5 |
| F238 | `balance.FY2027E.accounts_receivable` | annual_revenue × accounts_receivable_pct_revenue | annual_revenue=37002.91; accounts_receivable_pct_revenue=0.14 | 5,180.4 |
| F239 | `balance.FY2027E.inventory` | annual_revenue × inventory_pct_revenue | annual_revenue=37002.91; inventory_pct_revenue=0.09 | 3,330.3 |
| F249 | `balance.FY2027E.PP&E` | opening_PP&E + capital_expenditures - depreciation_and_amortization | opening_PP&E=81220.28; capital_expenditures=38060; depreciation_and_amortization=15000 | 104,280.3 |
| F250 | `balance.FY2027E.equity` | opening_equity + net_income + share_based_compensation + stock_issued_for_Cursor | opening_equity=189960.5; net_income=4968.729928; share_based_compensation=4000; stock_issued_for_Cursor=0 | 198,929.2 |
| F251 | `balance.FY2027E.total_liabilities` | debt_and_finance_leases + deferred_revenue + other_liabilities | debt_and_finance_leases=39364; deferred_revenue=18500; other_liabilities=15000 | 72,864.0 |
| F252 | `balance.FY2027E.total_liabilities_and_equity` | total_liabilities + redeemable_preferred + shareholders_equity | total_liabilities=72864; redeemable_preferred=0; shareholders_equity=198929.229928 | 271,793.2 |
| F253 | `balance.FY2027E.other_assets` | total_liabilities_and_equity - cash - securities - accounts_receivable - inventory - PP&E | total_liabilities_and_equity=271793.229928; cash=66804.280628; securities=6487; accounts_receivable=5180.4074; inventory=3330.2619; PP&E=104280.28 | 85,711.0 |
| F254 | `balance.FY2027E.total_assets` | cash + securities + accounts_receivable + inventory + PP&E + other_assets | cash=66804.280628; securities=6487; accounts_receivable=5180.4074; inventory=3330.2619; PP&E=104280.28; other_assets=85711 | 271,793.2 |
| F255 | `balance.FY2028E.accounts_receivable` | annual_revenue × accounts_receivable_pct_revenue | annual_revenue=45723.2832; accounts_receivable_pct_revenue=0.13 | 5,944.0 |
| F256 | `balance.FY2028E.inventory` | annual_revenue × inventory_pct_revenue | annual_revenue=45723.2832; inventory_pct_revenue=0.08 | 3,657.9 |
| F266 | `balance.FY2028E.PP&E` | opening_PP&E + capital_expenditures - depreciation_and_amortization | opening_PP&E=104280.28; capital_expenditures=33375; depreciation_and_amortization=18000 | 119,655.3 |
| F267 | `balance.FY2028E.equity` | opening_equity + net_income + share_based_compensation + stock_issued_for_Cursor | opening_equity=198929.229928; net_income=8997.3047248; share_based_compensation=5000; stock_issued_for_Cursor=0 | 212,926.5 |
| F268 | `balance.FY2028E.total_liabilities` | debt_and_finance_leases + deferred_revenue + other_liabilities | debt_and_finance_leases=39364; deferred_revenue=21000; other_liabilities=17000 | 77,364.0 |
| F269 | `balance.FY2028E.total_liabilities_and_equity` | total_liabilities + redeemable_preferred + shareholders_equity | total_liabilities=77364; redeemable_preferred=0; shareholders_equity=212926.5346528 | 290,290.5 |
| F270 | `balance.FY2028E.other_assets` | total_liabilities_and_equity - cash - securities - accounts_receivable - inventory - PP&E | total_liabilities_and_equity=290290.5346528; cash=66835.3651808; securities=6487; accounts_receivable=5944.026816; inventory=3657.862656; PP&E=119655.28 | 87,711.0 |
| F271 | `balance.FY2028E.total_assets` | cash + securities + accounts_receivable + inventory + PP&E + other_assets | cash=66835.3651808; securities=6487; accounts_receivable=5944.026816; inventory=3657.862656; PP&E=119655.28; other_assets=87711 | 290,290.5 |
| F288 | `balance.FY2026E.basic_shares` | July_28_basic_shares_m + Cursor_merger_shares_m + Cursor_vested_RSU_shares_m | July_28_basic_shares_m=13181.779945; Cursor_merger_shares_m=389.289254; Cursor_vested_RSU_shares_m=1.752426 | 13,572.8 |
| F289 | `balance.FY2025.total_liabilities_and_equity` | total_liabilities + redeemable_preferred + shareholders_equity | total_liabilities=50754; redeemable_preferred=38752; shareholders_equity=2573 | 92,079.0 |
| F290 | `balance.H1 2026A.total_liabilities_and_equity` | total_liabilities + redeemable_preferred + shareholders_equity | total_liabilities=65546; redeemable_preferred=0; shareholders_equity=127224 | 192,770.0 |
