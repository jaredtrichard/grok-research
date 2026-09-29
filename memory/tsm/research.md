# TSMC initiation research file

GF-TSM-1 · as of 2026-09-29 · name id `tsm`

Numeric facts live in [`register.md`](register.md); this file owns the business, driver and risk structure. No price target, recommendation or investment thesis is stated here.

## 1. Business and reporting segments

1. **[FACT] Reporting architecture.** TSMC reports one operating segment—the foundry segment—which includes wafer manufacturing, masks, design support, packaging and testing. Process nodes, platforms and advanced packaging are management/revenue lenses, not reportable financial segments. See R1.
2. **[FACT] Foundry model.** Customers supply proprietary circuit designs; TSMC supplies process technology, manufacturing scale, yield/quality, design enablement and, where selected, integrated advanced packaging/testing. TSMC does not market its own semiconductor products. See R1.1.
3. **[FACT] Process-node lens.** TSMC reports wafer-revenue shares by node and calls 7nm-and-below “advanced technologies.” Use the Q2 node mix in R3, but do not mistake revenue mix for wafer volume, capacity or margin mix.
4. **[FACT] Platform lens.** TSMC reports total-revenue mix across HPC, Smartphone, IoT, Automotive, DCE and Other. These are application platforms, not segments with separate P&Ls. See R3.
5. **[FACT] Backend/packaging.** CoWoS, SoIC, InFO, SoW and COUPE are material to system integration and AI/HPC enablement, but their standalone financials are not disclosed. See R4.6–R4.8 and R10.3.
6. **[DEDUCTED] Model treatment.** Keep packaging inside the foundry segment unless primary disclosure later supports a separate model.

## 2. Segment driver tree

### 2.1 Wafer fabrication

1. **[DEDUCTED] Revenue bridge:** 12-inch-equivalent wafer shipments × blended realized revenue per wafer equivalent, adjusted for node mix, wafer size conversion, customer/product mix, pricing/FX and non-wafer services. The R3.3 quotient is a cross-check, not ASP.
2. **[DEDUCTED] Volume drivers:** installed capacity × utilization × cycle-time/productivity × yield, constrained by tool/material/utility/labor availability and customer allocation. Exact starts, utilization and yield are not obtained (R10.2).
3. **[DEDUCTED] Price/mix drivers:** leading-edge node share, platform/customer mix, die size and mask layers, product complexity, specialty options, contractual pricing and USD/NTD. Exact node ASP is not obtained (R3.4/R10.1).
4. **[DEDUCTED] Gross-profit bridge:** wafer revenue less materials, direct labor, utilities, depreciation, maintenance, masks, yield loss, ramp inefficiency and fixed-cost under-absorption. Use company gross margin until node/site cost disclosure exists.
5. **[FACT] Current mix anchors.** Q2 node and platform mix, shipment equivalents and direction by platform are in R2–R3.

### 2.2 Advanced packaging and backend

1. **[DEDUCTED] Revenue bridge:** packaged units × package price, with mix across CoWoS/SoIC/InFO/SoW/COUPE plus testing/masks. Units, pricing and revenue are not obtained (R10.3).
2. **[DEDUCTED] Capacity drivers:** qualified lines/tools × utilization × package size/complexity × yield and test time, constrained by substrates, HBM integration, OSAT/tester availability and customer allocation.
3. **[FACT] Demand/capacity signal.** Management said advanced-packaging capacity was tight enough to limit customer growth; the exact gap was not disclosed. See R4.7.
4. **[DEDUCTED] Economics.** Integrated frontend-plus-backend capability can increase value captured per customer product, but no primary disclosure supports a standalone packaging margin or return assumption. Model no separate margin until R10.3 is resolved.

### 2.3 Specialty and mature technologies

1. **[DEDUCTED] Revenue bridge:** specialty/mature wafer shipments × realized revenue per wafer, with mix across power management, CMOS image sensors, automotive/industrial, RF, embedded memory and other applications.
2. **[FACT] Current demand frame.** Management described AI-linked power-management IC and sensor areas as constrained but did not describe broad commodity mature-node strength. See R4.10.
3. **[DEDUCTED] Watchpoint.** Mature capacity can improve diversification and extend depreciated assets, but commodity pricing/utilization can be more cyclical; standalone economics are not obtained.

### 2.4 Corporate operating items

1. **[DEDUCTED] R&D drivers:** node-development cadence, materials/transistor/interconnect research, design enablement, packaging/3D integration, mask/lithography work and engineering headcount.
2. **[DEDUCTED] G&A/marketing drivers:** global footprint, customer support, professional costs, systems/compliance and employee compensation.
3. **[FACT]** Annual R&D/G&A/marketing and Q2 2026 R&D/SG&A are disclosed. See R6.4.

## 3. Historical financial skeleton

**[FACT]** Take history once from R2:

| model block | periods | register pointer | status |
|---|---|---|---|
| Revenue, gross profit, operating income, parent net income, EPS | FY2023–FY2025 | R2 annual table | obtained on IASB-IFRS basis |
| Operating cash flow and PP&E purchases | FY2023–FY2025 | R2 annual table; R7.1 | obtained |
| Revenue, margins, operating income, parent net income, EPS and shipments | Q2 2025–Q2 2026 | R2 latest-quarter table | obtained on TIFRS basis |
| Accounting-basis bridge | FY2025 | R2.3–R2.3A | difference identified; detailed bridge **not obtained** |
| Node/platform/packaging P&Ls | all periods | R1.2/R10.3–R10.4 | **not obtained** |

## 4. Capacity and technology roadmap

1. **[FACT] Installed base.** FY2025 shipment/capacity anchors are in R4.1; exact utilization is not obtained (R4.2).
2. **[DEDUCTED] Utilization treatment.** Do not infer utilization by dividing annual shipments by year-end capacity. See R4.2A.
3. **[FACT] N3/N5.** TSMC was adding N3 fabs, converting N5 tools for N3 support and optimizing flexible capacity across N7/N5/N3. See R4.9.
4. **[FACT] N2.** High-volume manufacturing began in late 2025 and the 2026 ramp was visible in Q2 wafer mix. See R3 and R4.3.
5. **[FACT] N2P/A16.** Both were scheduled for 2H 2026 production; A16 adds backside power delivery. See R4.4.
6. **[FACT] A14.** Risk/volume timing and management’s PPA targets are in R4.5. They are roadmap claims, not model-ready realized economics.
7. **[FACT] Advanced packaging.** CoWoS generation/status, SoIC and COUPE milestones are in R4.6–R4.8. Capacity and financial contribution remain not obtained.
8. **[FACT] Footprint.** Taiwan, Arizona, Japan and Germany plans are summarized in R4.9–R4.10; site capacity, economics and firm schedules remain not obtained (R10.6).

## 5. Geography and customer concentration

1. **[FACT] Customer-headquarters revenue.** FY2025 and Q2 2026 mixes are in R5. This is not fab-location revenue or production.
2. **[FACT] Customer concentration.** Top-ten and top-two concentration are in R5.1; customer identities remain anonymous.
3. **[FACT] Asset geography.** Noncurrent operating assets by geography are in R5.2; this does not reveal site output or profit.
4. **[DEDUCTED] Model treatment.** Keep customer concentration and platform concentration as separate sensitivities: one large customer may span multiple platforms, and a platform can span many customers.

## 6. Margin and cost-structure drivers

1. **[FACT] Utilization/absorption.** Higher utilization and cost improvement supported recent margin; lower utilization would reverse fixed-cost absorption. See R6.1/R6.3.
2. **[FACT] Node ramps.** N2’s early ramp was expected to dilute 2H margin before scale/yield maturation. See R6.1.
3. **[FACT] Overseas fabs.** Management’s corporate gross-margin dilution ranges are in R6.2; site margin was not disclosed.
4. **[DEDUCTED] Mix/price.** More leading-edge and advanced packaging can raise revenue per wafer/product, while customer/platform mix, strategic pricing and FX can amplify or offset that benefit.
5. **[DEDUCTED] Cost bridge.** Materials + labor + utility + depreciation + maintenance + yield/ramp loss + logistics, with fixed-cost absorption over good output. Exact node/site unit costs are not obtained (R6.5).
6. **[FACT] Exogenous risks.** Earthquakes, electricity/water interruptions, equipment/material constraints, inflation and export controls can affect output and cost. See R9.
7. **[FACT] Earnings quality.** Q2 net income included a material non-operating VIS disposal/mark-to-market gain. See R2.4A.
8. **[DEDUCTED] Model treatment.** Separate the VIS gain from recurring earnings.

## 7. Capex and cash conversion

1. **[FACT] Historical conversion.** FY2023–FY2025 OCF/capex and deduced FCF are in R2; latest-quarter cash conversion is in R7.2.
2. **[FACT] 2026 budget.** Aggregate guidance and allocation ranges are in R7.3. Do not fabricate advanced-packaging or site capex from the broad buckets.
3. **[DEDUCTED] Cash conversion bridge:** operating profit after cash tax + D&A/noncash − working-capital investment − capex, then financing/dividends. Track N2 inventory and overseas construction separately where disclosure permits.
4. **[FACT] Balance-sheet anchors.** Liquidity, debt, working capital, PP&E and total assets are in R7.4–R7.5.
5. **[DEDUCTED] Watchpoint.** Elevated capex precedes output; near-term FCF can compress even if demand is strong. Returns depend on future utilization, pricing, yield and overseas-fab cost convergence—not capex alone.

## 8. Node map

| node / flow | who pays whom | where value sits | what breaks it |
|---|---|---|---|
| Fabless/system/IDM customer → TSMC **[DEDUCTED]** | wafer, mask, design-enable, packaging and test fees | process IP, yield, scale, time-to-volume, customer trust; R1 | design loss, customer concentration, weak end demand, price pressure, export controls |
| Customer/CSP end demand → chip designer → TSMC **[DEDUCTED]** | end-user/cloud capex funds chip demand and foundry orders | scarce leading-edge and packaging capacity, product differentiation | AI deployment/power delays, inventory, customer overforecast, architecture shift |
| TSMC frontend → TSMC/partner backend **[DEDUCTED]** | wafers move into CoWoS/SoIC/InFO/SoW, test and assembly | heterogeneous integration, HBM bandwidth, package yield and system power | substrate/HBM/test bottlenecks, package yield, alternative backend technologies; R4/R9 |
| TSMC → equipment vendors **[DEDUCTED]** | lithography, deposition, etch, metrology and other tools | unique tool capability and install/service capacity; TSMC process integration | export controls, lead times, inflation, tool performance; R7/R9 |
| TSMC → material/substrate suppliers **[DEDUCTED]** | wafers, gases, chemicals, photoresist, metals and packaging inputs | qualification, purity, reliability and local supply | sole-source failure, trade barriers, shortages, quality excursions; R9.2 |
| TSMC → utilities/labor/governments **[DEDUCTED]** | electricity, water, wages, tax; governments may provide incentives | stable power/water, engineering density, fab ecosystem and subsidies | outage/drought, labor scarcity, subsidy conditions/clawbacks, fragmented ecosystem; R9 |
| Governments/regulators → TSMC/customers **[DEDUCTED]** | grants/loans and permits; controls may restrict tools/chips/customers | geographic resilience and market access | export-license loss, tariffs, permit delay, geopolitical escalation; R9.3–R9.6 |

**[VIEW] Value concentration.** Near-term measurable value sits in leading-edge wafer economics (N3/N5/N2 mix, utilization/absorption, and USD-linked pricing) and in cash conversion after the elevated advanced-process and packaging capex cycle. Advanced packaging (CoWoS and related) is a throughput and attach constraint that supports frontend wafer demand, but it is not yet a separately measurable P&L; do not assign a standalone packaging multiple until R10.3 resolves. Overseas fabs are a multi-year corporate-margin dilution and execution risk, not a second profit center in the current disclosure. Customer concentration (top ten ~78% of FY2025 revenue) means end-demand and export-eligibility shocks transmit quickly; Taiwan production continuity remains the binding continuity risk under R9.5.

## 9. Competitive and regulatory frame

1. **[FACT] Foundry competition.** TSMC’s filing frames competitors as pure-play foundries and IDMs; technology, yield, capacity, quality, resilience, service and price are the axes. See R9.1.
2. **[FACT] Samsung/Intel.** These firms were named by an analyst, not by TSMC’s filing, in the Q2 call. Comparative operating facts are not obtained from the primary TSMC set, so this draft does not assert node parity, yield, share or economics.
3. **[FACT] Backend alternatives.** Management viewed alternative packaging capacity as potentially relieving a bottleneck for TSMC frontend wafers, while frontend and backend remain different competitive arenas. See R9.1A.
4. **[FACT] Export controls.** Advanced-chip/customer restrictions and the annual Nanjing equipment license can constrain shipments and tools. See R9.3–R9.4.
5. **[FACT] Taiwan/geopolitics.** Production concentration, cross-strait relations, military conflict, natural disasters and utility continuity are material disclosed risks. See R9.5.
6. **[FACT] Globalization.** Arizona/Japan/Germany add geographic flexibility but bring cost, labor, ecosystem and execution penalties; incentives are conditional. See R6.2/R9.6.
7. **[DEDUCTED] Regulatory sensitivity.** Scenario analysis should separately shock (a) customer/export eligibility, (b) tool access, (c) Taiwan production continuity, and (d) overseas cost dilution. Combining all four into one haircut hides different timing and recovery paths.

## 10. Numbers the model must take

Values live only in the register. “Take” means link the assumption to the cited register item and preserve its accounting basis, source date and classification.

| named input | take from | source / as-of | status |
|---|---|---|---|
| Annual revenue, gross profit, operating income, parent net income, EPS | R2 annual table | S1; FY2023–FY2025 | obtained; IASB-IFRS |
| Quarterly revenue, margins, operating income, parent net income, EPS | R2 latest-quarter table | S3–S5; Q2 2025–Q2 2026 | obtained; TIFRS |
| R&D and SG&A | R6.4 | S1/S4; FY2025/Q2 2026 | obtained |
| Non-operating income, VIS gain and income-tax expense | R2.4A | S4/S6; Q2 2026 | obtained; separate recurring/nonrecurring treatment needed |
| D&A | R7.1–R7.2 | S1/S4; FY2025/Q2 2026 | obtained |
| FY2025 IASB-IFRS/TIFRS bridge | R2.3–R2.3A | S1/S2; FY2025 | difference identified; detailed bridge **not obtained** |
| Wafer shipments and revenue quotient cross-check | R2 latest-quarter table; R3.3 | S4/S5; Q2 2026 | obtained / deduced; quotient is not ASP |
| Exact wafer ASP by node/customer | R3.4/R10.1 | through 2026-09-29 | **not obtained** |
| Node revenue mix | R3 table | S3–S6; Q2 2026 | obtained |
| Platform revenue mix and sequential direction | R3 table/R3.1 | S4/S6; Q2 2026 | obtained |
| Monthly revenue run rate | R2.7 | S7; August/YTD 2026 | obtained through August |
| Packaging revenue/margin/capacity/backlog | R10.3 | through 2026-09-29 | **not obtained** |
| Capacity and exact utilization | R4.1–R4.2A | S1/S2/S4/S6; through Q2 2026 | capacity obtained; utilization **not obtained** |
| N2/N2P/A16/A14 timing | R4.3–R4.5 | S2/S3/S6; through 2026-07-16 | obtained as company roadmap |
| CoWoS/SoIC/InFO/SoW/COUPE timing | R4.6–R4.8 | S2/S6; through 2026-07-16 | obtained as company roadmap; economics **not obtained** |
| Geography and customer concentration | R5/R5.1 | S1/S2/S4; FY2025/Q2 2026 | obtained |
| Node/site cost, yield and margin | R6.5/R10.2/R10.4 | through 2026-09-29 | **not obtained** |
| OCF, capex, FCF and 2026 capital budget | R2/R7.1–R7.3 | S1/S4–S6; FY2023–Q2 2026 | obtained / deduced where labeled |
| Cash, securities, debt, working capital, PP&E | R7.4–R7.5 | S4–S6; 2026-06-30 | obtained |
| Shares, dividends and buybacks | R8 | S1/S5/S8/S9; through 2026-09-29 | obtained; current open buyback **not obtained** |
| Export/geopolitical/utility risk anchors | R9 | S1; filed 2026-04-16 | qualitative facts obtained; event probabilities **not obtained** |
| Street consensus and price targets | R10.9; `consensus.md` | through 2026-09-29 | **not obtained** |
