# Tesla initiation research file

GF-TSLA-1 · as of 2026-08-29 · name id `tsla`

Read numeric facts in [`register.md`](register.md); this file owns driver structure and interpretation. No fact is intentionally duplicated here.

## 1. Business and reported segments

1. **[FACT] Reporting architecture.** Tesla reports two segments: Automotive and Energy generation and storage. “Services and other” is a disclosed revenue/cost line inside Automotive, not a third reportable segment. See R1.1–R1.2.
2. **[FACT] Automotive.** Vehicles, leasing and regulatory credits are the core lines. Services and other adds used vehicles, non-warranty repair/collision, paid Supercharging, insurance, parts and merchandise. See R1.1 and R1.3.
3. **[FACT] Energy.** Powerwall, Megapack, leasing/financing, installation/service and energy incentives comprise the segment; software includes Autobidder and Powerhub. See R1.4.
4. **[FACT] FSD / Robotaxi / other.** FSD (Supervised), Robotaxi, insurance and Supercharging are discussed operationally but are not separately reported financial lines. Robotaxi used Model Y and Tesla disclosed that Cybercab production had started. See R1.2 and R3.5.

## 2. Segment driver tree

### 2.1 Automotive vehicle and leasing

1. **[DEDUCTED] Vehicle sales revenue bridge:** cash deliveries × realized revenue per cash delivery, then add separately recognized software/ancillary revenue. Do not call the quotient “ASP” without adjusting for FSD and ancillary revenue; the clean figure is not obtained (R8.1).
2. **[FACT] Volume drivers:** production capacity, pack/cell supply, factory uptime, demand, inventory, logistics, allocation between customer sale and owned Robotaxi fleet, and product/factory mix. Capacity and current production are not equivalent (R3.2–R3.6).
3. **[DEDUCTED] Mix/price drivers:** Model 3/Y versus other models; geography and FX; trims/options; incentives/financing; lease share; software take-rate; and the timing of revenue recognition. Filing evidence for the current direction is in R2.1–R2.2.
4. **[DEDUCTED] Cost per unit:** materials/cells, labor, freight/duties, warranty, depreciation, fixed-cost absorption and ramp inefficiency divided by units. A sourced dollar/unit is not obtained (R8.1).
5. **[FACT] Regulatory credits:** model separately from vehicle economics because supply, rules and third-party automaker demand drive the line (R7.3).
6. **[FACT] Leasing/residuals:** model leasing revenue, operating-lease depreciation, lease fleet, used-vehicle disposal and residual guarantee exposure. Source points are R3.1 and R5.7.
7. **[DEDUCTED] Automotive gross-profit bridge:** volume + realized price/mix + software/ancillary + credits − unit cost − warranty − lease depreciation − ramp/under-absorption. Take reported and ex-credit margins from R2.1–R2.3, not an unsourced estimate.

### 2.2 FSD and Robotaxi

1. **[FACT] FSD inputs disclosed:** active subscriptions, deferred revenue, North American attach commentary and supervised-status caveat. See R3.1, R5.5 and R8.4.
2. **[DEDUCTED] FSD revenue bridge:** eligible fleet × paid attach × monthly/upfront mix × net price × recognition period. Churn, regional price and standalone revenue are not obtained (R8.3).
3. **[DEDUCTED] Robotaxi revenue bridge:** active commercial fleet × paid miles/vehicle × revenue/mile. Costs should include cleaning/service, energy, insurance, remote assistance/safety operations, depreciation and payment/platform expense.
4. **[FACT] Robotaxi paid miles were backfilled in register R3.5; active paid fleet, fares, revenue, cost and margin remain not obtained.** Do not convert the cumulative chart or authorization roster into modeled commercial scale without a labeled `[VIEW]`.
5. **[VIEW]** Researcher-specified autonomy scenarios rebuilt to be in dialogue with the last price live only in [`models/tsla/inputs.md`](../../models/tsla/inputs.md) and are not filing facts.

### 2.3 Energy generation and storage

1. **[DEDUCTED] Revenue bridge:** Megapack deployed GWh × realized revenue/GWh + Powerwall units × ASP + solar + services/incentives + lease revenue. Tesla publishes aggregate deployed GWh, not the full product bridge; deployment timing follows R3.7 (R3 and R8.2).
2. **[FACT] Key operating drivers:** deployments, Megapack/Powerwall mix, realized ASP, manufacturing mix, warranty, logistics/installation, tariffs, incentive treatment and production ramp. The latest filing’s direction is summarized in R2.5 and R7.5.
3. **[DEDUCTED] Backlog conversion:** opening remaining performance obligations + bookings/price changes − recognized revenue − cancellations/adjustments. Use R5.6; one-year-or-less arrangements are subject to a disclosure expedient.
4. **[DEDUCTED] Gross profit bridge:** deployments × `(realized revenue/MWh − cost/MWh)` plus services/incentives and lease margin, less warranty/ramp effects. Product ASP and cost/MWh are not obtained (R8.2).

### 2.4 Services and other

1. **[FACT] Revenue pools:** used vehicles, non-warranty maintenance/collision, paid Supercharging, insurance, parts and merchandise (R1.1).
2. **[DEDUCTED] Driver bridge:** installed fleet × attach/use × revenue per event/policy/session, plus used-volume × spread. Supercharging also depends on station/connectors, utilization, electricity price and third-party vehicle access.
3. **[FACT] Costs include used-vehicle acquisition/refurbishment, service labor/materials, charging operations, insurance claims, parts and merchandise. Standalone line economics are available only in aggregate (R2.4 and R8.3).
4. **[DEDUCTED] Watchpoint:** positive aggregate gross profit does not establish that each constituent business is profitable.

### 2.5 Corporate operating items

1. **[DEDUCTED] R&D:** headcount/compensation and SBC; AI training/inference compute; FSD/Robotaxi; Optimus; cells/materials; and product programs.
2. **[DEDUCTED] SG&A:** employee/professional costs, SBC, facilities, litigation, sales/service overhead and insurance administration.
3. **[FACT] Company-level opex and SBC are disclosed; segment opex and segment operating income are not (R2.6, R5.2, R8.5).
4. **[DEDUCTED] Warranty:** provision follows current sales and expected lifetime claims; costs incurred consume the reserve; prior-period estimate changes can move margin. Use R5.4.

## 3. Historical financial skeleton

**[FACT]** The required history is housed once in R2:

| model block | periods | register pointer | disclosure status |
|---|---|---|---|
| Automotive revenue / gross profit | FY2023–FY2025; Q2 and 1H 2026 | R2 tables, R2.1–R2.3 | obtained |
| Energy revenue / gross profit | FY2023–FY2025; Q2 and 1H 2026 | R2 tables, R2.5 | obtained |
| Services revenue / gross profit | FY2023–FY2025; Q2 and 1H 2026 | R2 tables, R2.4 | gross profit deduced from named lines |
| Segment operating income / opex | same periods | R8.5 | not obtained |

## 4. Production, deliveries, deployments and service footprint

1. **[FACT]** FY2025 and Q1/Q2 2026 production, deliveries and storage deployment are in the R3 table.
2. **[FACT]** Latest official delivery detail and operating-lease share come from the July production release (S7).
3. **[FACT]** Latest Supercharger stations/connectors, FSD subscriptions, lease fleet and inventory days are in R3.1.
4. **[FACT]** Q2 service-center/location count and mobile-service fleet were not obtained (R8.4).
5. **[DEDUCTED]** The production-to-delivery gap is a working-capital/logistics signal, not a demand measure by itself.

## 5. Geography and factory capacity

1. **[FACT] Geographic revenue.** Use R4 for U.S., China and other international revenue by sales location. No finer recurring country split was obtained.
2. **[FACT] Fremont/California.** Model 3/Y production capacity was disclosed; Model S/X lines had been decommissioned and Optimus lines were being installed. See R3.2 and S6 p. 6.
3. **[FACT] Austin/Texas.** Model Y, Cybertruck and Cybercab were in production; Megapack was commissioning. See R3.2–R3.3.
4. **[FACT] Shanghai.** Model 3/Y and Megapack capacity were in production. See R3.2–R3.3.
5. **[FACT] Berlin.** Model Y capacity was in production. See R3.2.
6. **[FACT] Nevada.** Semi was commissioning and Powerwall capacity was in production. See R3.2–R3.3.
7. **[FACT] Newer disclosed plants.** Megafactory Texas was the new energy plant identified in the Q2 materials. No additional new vehicle assembly plant was disclosed in the reviewed primary set.
8. **[FACT] Utilization.** Site utilization was not disclosed; installed capacity is explicitly not current output (R3.6).

## 6. Automotive ASP, COGS and margin

1. **[FACT]** Named automotive sales, credits, leasing, COGS and reported total automotive margin are in R2.1.
2. **[DEDUCTED]** Ex-credit margins use only named filing lines and are in R2.2–R2.3.
3. **[FACT]** Dollar ASP is not obtained; Tesla’s qualitative ASP commentary cannot support a model input by itself (R8.1).
4. **[FACT]** Automotive COGS is obtained at the reported line level, but vehicle-only COGS excluding lease costs and ancillary/software effects is not obtained.

## 7. Energy economics

1. **[FACT]** Historical/latest revenue and gross profit live in R2; deployments live in R3.
2. **[FACT]** Capacity and backlog/RPO live in R3.3 and R5.6.
3. **[FACT]** Latest margin drivers—Megapack deployment/ASP, Powerwall mix, cost/MWh mix and warranty—live in R2.5.
4. **[FACT]** Product-level ASP, units, cost/MWh and gross profit are not obtained (R8.2).

## 8. Services and other economics

1. **[FACT]** Historical/latest revenue and deduced gross profit live in R2; Q2 management margin commentary lives in R2.4.
2. **[FACT]** Latest growth was attributed to used vehicles, non-warranty maintenance/collision and paid Supercharging; constituents are not separately quantified (R8.3).
3. **[DEDUCTED]** Model aggregate Services until primary disclosure supports a product split.

## 9. Balance sheet and cash-flow inputs

1. **[FACT] Liquidity/working capital/debt.** Cash, investments, receivables, inventory, payables and debt/leases are in R5.1.
2. **[FACT] Cash-flow add-backs/investment.** Operating cash flow, capex, D&A and SBC are in R5.2.
3. **[FACT] Shares.** Latest outstanding and diluted weighted-average shares are in R5.3.
4. **[FACT] Warranty.** Reserve, provision and claims are in R5.4.
5. **[FACT] Contract liabilities/RPO.** Automotive/software, regulatory-credit and Energy obligations are in R5.5–R5.6.
6. **[FACT] Segment balance sheets/capex are not obtained (R8.5).**
7. **[FACT] Quarterly cash conversion and 2026 aggregate capex outlook are in R5.8; the Q2 AI hardware acquisition is in R5.9.**

## 10. Musk-entity related parties

1. **[FACT]** Include only the filing facts in R6: SpaceX Megapack purchases, Tesla’s SpaceX investment and prior xAI Megapack purchases.
2. **[DEDUCTED]** Separate recurring related-party customer economics from mark-to-market investment gains; neither should be treated as third-party Automotive demand.
3. **[FACT]** No SpaceX operating-company analysis belongs in this file.

## 11. Node map

| node / flow | who pays whom | where value sits | what breaks it |
|---|---|---|---|
| Vehicle buyer / lessee → Tesla **[DEDUCTED]** | cash purchase, financing proceeds or lease payments | manufacturing scale, brand/distribution, software attach, resale ecosystem | weak demand, price cuts, financing rates, residual losses, quality/warranty |
| Automaker → Tesla **[FACT]** | regulatory-credit purchases | surplus compliance credits | rule changes or lower buyer need (R7.3) |
| Vehicle owner → Tesla **[DEDUCTED]** | FSD, charging, insurance, repair, parts | installed fleet, software, charging/service density, proprietary data | low attach/use, regulation, liability, poor service economics |
| Rider → Tesla/vehicle owner **[DEDUCTED]** | Robotaxi fare; economics split depends on fleet ownership | autonomy stack, utilization, dispatch/network density | safety/regulatory limits, low utilization, high support/insurance/depreciation |
| Utility/C&I/homeowner → Tesla **[FACT]** | storage purchase/lease/service | integrated hardware, controls software, deployment capacity and backlog | tariffs, interconnection, cell constraints, ASP pressure, warranty |
| Other Musk entity → Tesla **[FACT]** | disclosed Megapack purchases | incremental Energy volume/margin | concentration/governance/collection risk; see R6 |
| Tesla → cell/electronics/assembly suppliers **[FACT]** | components and contracted materials | supplier scale/technology; Tesla integration and procurement | single-source failure, commodity inflation, export controls, tariffs |
| Tesla → chip/compute ecosystem **[DEDUCTED]** | semiconductors, memory, training/inference hardware and power | scarce compute/chip capability and Tesla software/data | supply, power, capex overrun, model progress below spend |
| Tesla → labor / logistics / governments **[DEDUCTED]** | wages, freight, duties/tax; governments/customers may provide incentives | efficient factories/localization | labor disruption, logistics congestion, tariff/incentive reversal |

**[VIEW] Value concentration.** Near-term reported value is measurable in vehicle, Energy and Services gross profit. FSD/Robotaxi/Optimus optionality is economically material only when paid adoption, unit revenue, cost and capital intensity become observable.

## 12. Competitive and regulatory frame

1. **[FACT] Automotive competition:** EV and ICE manufacturers; product-level positioning is summarized in R7.2.
2. **[FACT] Autonomy competition:** ride-hailing/taxi and AI participants; FSD remains supervised for customer vehicles (R1.3, R7.2).
3. **[FACT] Energy competition:** storage manufacturers/integrators and conventional generation alternatives (R7.2).
4. **[FACT] U.S./NHTSA:** regulatory patchwork and information requests are in R7.4 and R7.6.
5. **[FACT] EU/ECE and China:** differing driver-assistance/autonomy rules can delay or restrict deployment (R7.4).
6. **[FACT] Credits/tariffs:** credit-program restrictions and trade-policy exposure are in R7.3 and R7.5.
7. **[DEDUCTED]** Model regulatory credits as a declining/volatile standalone line unless new primary evidence supports durability; do not bury them in vehicle ASP.

## 13. Numbers the model must take

Values live only in the register. “Take” means link the model assumption to the cited register item, preserving its source date and classification.

| named input | take from | source / as-of | status |
|---|---|---|---|
| Automotive revenue, COGS, gross profit | R2 tables; R2.1 | S1 FY2025; S3 2026-06-30 | obtained |
| Automotive gross margin with / without credits | R2.1–R2.3 | S1 FY2025; S3/S6 Q2 2026 | obtained / deduced |
| Dollar vehicle ASP; clean vehicle cost/unit | R8.1 | through 2026-08-29 | **not obtained** |
| Regulatory-credit revenue | R2.1 | S3 2026-06-30 | obtained |
| Production / deliveries / lease share | R3 table; S7 | FY2025, Q1 and Q2 2026 | obtained |
| Energy deployments, revenue, COGS, gross profit | R2 tables; R3 table | S1/S3/S4/S5/S7 | obtained |
| Energy product ASP, units, cost/MWh | R8.2 | through 2026-08-29 | **not obtained** |
| Services revenue, COGS, gross profit | R2 tables; R2.4 | S1/S3/S6 | obtained / deduced |
| FSD / Robotaxi / insurance / charging standalone economics | R8.3 | through 2026-08-29 | **not obtained** |
| R&D, SG&A, total opex | R2.6 | S3 2026-06-30 | obtained |
| Cash, investments, receivables, inventory, payables, debt | R5.1 | S3 2026-06-30 | obtained |
| Capex, SBC, D&A, operating cash flow | R5.2, R5.8 | S3/S6 Q2 and 1H 2026 | obtained |
| FY2026 aggregate capex outlook | R5.8 | S3 2026-06-30 | obtained; no segment split |
| Diluted / outstanding shares | R5.3 | S3 Q2 / 2026-07-16 | obtained |
| Warranty reserve/provision/claims | R5.4 | S3 2026-06-30 | obtained |
| Automotive and Energy performance obligations | R5.5–R5.6 | S3 2026-06-30 | obtained |
| Geographic revenue | R4 | S1 FY2025; S3 Q2/1H 2026 | obtained |
| Factory capacity / utilization | R3.2–R3.3, R3.6 | S6 Q2 2026 | capacity obtained; utilization **not obtained** |
| Segment opex, operating income, assets, debt and capex | R8.5 | through 2026-08-29 | **not obtained** |
