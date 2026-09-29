# Microsoft fact register

GF-MSFT-1 · as of 2026-09-29 · name id `msft` · USD millions except per-share data and where noted.

Each material item is tagged `[FACT]`, `[DEDUCTED]`, or `[VIEW]`. `not obtained` means no usable figure was found in the reviewed primary-source set.

## Source set

- **S1** — [Microsoft FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm), fiscal year ended 2026-06-30, filed 2026-07-29.
- **S2** — SEC inline-XBRL tables from S1: [income statement](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R2.htm), [balance sheet](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R4.htm), [cash flow](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R6.htm), and [segment/product revenue](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R45.htm).
- **S3** — [Microsoft FY2026 Q4 earnings release](https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q4/press-release-webcast), dated 2026-07-29.
- **S4** — [Microsoft FY2026 Q4 investor metrics](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/metrics), current as of 2026-07-29.
- **S5** — [Microsoft FY2026 Q4 official earnings-call transcript](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4), dated 2026-07-29.
- **S6** — [Microsoft IR stock lookup](https://www.microsoft.com/en-us/investor/stock-lookup), queried for 2026-09-28.

## R1 — Reporting perimeter and products

- **R1.1 [FACT]** Microsoft reports three segments: Productivity and Business Processes (“PBP”), Intelligent Cloud (“IC”), and More Personal Computing (“MPC”). [S1](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm)
- **R1.2 [FACT]** PBP includes Microsoft 365 Commercial and Consumer products/cloud services, LinkedIn, and Dynamics. Microsoft 365 Commercial cloud includes Microsoft 365, Enterprise Mobility + Security, the cloud portion of Windows Commercial, per-user Power BI, Exchange, SharePoint, Teams, Security and Compliance, and Microsoft 365 Copilot. LinkedIn includes Talent, Marketing, Premium, and Sales Solutions. Dynamics includes Dynamics 365 ERP/CRM, Power Apps, and Power Automate. [S1](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm)
- **R1.3 [FACT]** IC includes Azure and other cloud services, GitHub cloud services, Health and Life Sciences cloud services, virtual desktop offerings, SQL Server, Windows Server, Visual Studio, System Center, CALs, and other on-premises server offerings. [S1](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm)
- **R1.4 [FACT]** MPC includes Windows OEM and Devices, XBOX hardware/content/services, and Search advertising through Bing, Copilot, Microsoft News, Edge, and third-party affiliates. [S1](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm)
- **R1.5 [FACT]** Azure revenue, Microsoft 365 Copilot revenue, GitHub revenue, and AI revenue are not separately reported dollar lines. Product-level gross profit, operating income, assets, capex, and cash flow are also not separately reported. See R9.

## R2 — Segment economics

| segment / line **[FACT]** | FY2024 | FY2025 | FY2026 |
|---|---:|---:|---:|
| PBP revenue | 106,820 | 120,810 | 139,996 |
| PBP cost of revenue | 19,611 | 22,422 | 25,017 |
| PBP operating expense | 27,548 | 28,615 | 31,100 |
| PBP operating income | 59,661 | 69,773 | 83,879 |
| IC revenue | 87,464 | 106,265 | 137,791 |
| IC cost of revenue | 29,611 | 40,171 | 57,876 |
| IC operating expense | 20,040 | 21,505 | 22,943 |
| IC operating income | 37,813 | 44,589 | 56,972 |
| MPC revenue | 50,838 | 54,649 | 54,052 |
| MPC cost of revenue | 24,892 | 25,238 | 23,481 |
| MPC operating expense | 13,987 | 15,245 | 16,185 |
| MPC operating income | 11,959 | 14,166 | 14,386 |
| Total revenue | 245,122 | 281,724 | 331,839 |
| Total cost of revenue | 74,114 | 87,831 | 106,374 |
| Total operating expense | 61,575 | 65,365 | 70,228 |
| Total operating income | 109,433 | 128,528 | 155,237 |

Source: [S2 segment table](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R45.htm). Segment gross profit is `[DEDUCTED]` as revenue less disclosed segment cost of revenue; the workbook computes it.

- **R2.1 [FACT]** FY2026 PBP revenue increased 16%, IC revenue increased 30%, and MPC revenue decreased 1% from the disclosed FY2025 values above. No growth percentage is used in the workbook unless `compute.py` derives it from the table. [S2](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R45.htm)
- **R2.2 [FACT]** Q4 FY2026 PBP revenue was $37.8 billion and operating margin was 58%; IC revenue was $39.3 billion and operating margin was 41%; MPC revenue was $12.9 billion and operating margin was 21%. [S5](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)
- **R2.3 [FACT]** Q4 IC gross-margin percentage declined year over year because of mix toward Azure and continued AI-infrastructure scaling ahead of demand, partly offset by Azure efficiency gains. PBP gross-margin percentage decreased slightly with increased Microsoft 365 Copilot usage. MPC gross-margin percentage increased because Activision acquisition amortization declined. [S5](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)

## R3 — Product and service revenue

| offering revenue **[FACT]** | FY2024 | FY2025 | FY2026 |
|---|---:|---:|---:|
| Server products and cloud services | 79,828 | 98,435 | 129,425 |
| Microsoft 365 Commercial products and cloud services | 76,969 | 87,767 | 101,997 |
| XBOX | 21,503 | 23,455 | 21,790 |
| LinkedIn | 16,372 | 17,812 | 19,817 |
| Windows and Devices | 17,026 | 17,314 | 17,084 |
| Search advertising | 12,306 | 13,878 | 15,176 |
| Microsoft 365 Consumer products and cloud services | 6,648 | 7,404 | 9,175 |
| Dynamics products and cloud services | 6,831 | 7,827 | 9,006 |
| Enterprise and partner services | 7,594 | 7,760 | 8,260 |
| Other | 45 | 72 | 109 |
| Total | 245,122 | 281,724 | 331,839 |

Source: [S2 product table](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R45.htm).

- **R3.1 [FACT]** Microsoft Cloud revenue, which includes Microsoft 365 Commercial cloud, Azure and other cloud services, the commercial portion of LinkedIn, and Dynamics 365, was $137.7 billion, $168.9 billion, and $214.4 billion in FY2024, FY2025, and FY2026. It overlaps product lines in the table and must not be added to reported revenue. [S2](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R45.htm)
- **R3.2 [FACT]** Geographic revenue was $170,794 in the United States and $161,045 in other countries in FY2026; OEM and certain multinational billings are included in the U.S. because geographic sourcing is impracticable. [S2](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R45.htm)

## R4 — Latest operating KPIs and drivers

- **R4.1 [FACT]** Q4 FY2026 Microsoft Cloud revenue was $59.3 billion, up 27%; full-year Microsoft Cloud revenue was $214.4 billion, up 27% (25% constant currency), and full-year Microsoft Cloud gross margin was 66% versus 69% in FY2025. [S3](https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q4/press-release-webcast); [S4](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/metrics)
- **R4.2 [FACT]** Commercial remaining performance obligation (“RPO”) was $678 billion at Q4 FY2026, up 84%. Management said RPO increased 25% excluding OpenAI and that all sequential commercial RPO growth came from customers outside frontier-model companies. RPO is a backlog indicator, not revenue and not all due within one year. [S3](https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q4/press-release-webcast); [S5](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)
- **R4.3 [FACT]** Azure and other cloud services revenue grew 43% in Q4 and 41% in FY2026. Azure exceeded $100 billion of revenue in FY2026, but an exact dollar amount was not obtained. Management said demand continued to exceed available capacity. [S3](https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q4/press-release-webcast); [S4](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/metrics); [S5](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)
- **R4.4 [FACT]** Q4 Microsoft 365 Commercial cloud revenue grew 14%, paid seat count grew 6%, and Microsoft 365 Copilot exceeded 30 million paid seats after net seat additions more than doubled sequentially. Premium offerings, including Copilot, E5, and early E7 traction, drove ARPU growth. Standalone Copilot revenue, ARPU, usage revenue, and gross profit were not obtained. [S4](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/metrics); [S5](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)
- **R4.5 [FACT]** Q4/FY2026 growth was 12%/11% for LinkedIn, 13%/18% for Dynamics 365, 24%/28% for Microsoft 365 Consumer cloud, and 10%/12% for Search advertising ex-TAC. Q4 Windows OEM and Devices fell 7%; Q4 XBOX content and services fell 10%, and FY2026 XBOX content and services fell 5%. [S3](https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q4/press-release-webcast); [S4](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/metrics)
- **R4.6 [FACT]** GitHub Copilot had 50 million users at Q4 FY2026. A paid-user count, ARPU, standalone revenue, and profit were not obtained. [S5](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)

## R5 — Consolidated income statement

| income statement **[FACT]** | FY2024 | FY2025 | FY2026 |
|---|---:|---:|---:|
| Revenue | 245,122 | 281,724 | 331,839 |
| Cost of revenue | 74,114 | 87,831 | 106,374 |
| Gross margin | 171,008 | 193,893 | 225,465 |
| Research and development | 29,510 | 32,488 | 35,562 |
| Sales and marketing | 24,456 | 25,654 | 26,710 |
| General and administrative | 7,609 | 7,223 | 7,956 |
| Operating income | 109,433 | 128,528 | 155,237 |
| Other income / (expense), net | (1,646) | (4,901) | 10,697 |
| Income before tax | 107,787 | 123,627 | 165,934 |
| Tax provision | 19,651 | 21,795 | 32,185 |
| Net income | 88,136 | 101,832 | 133,749 |
| Diluted weighted-average shares | 7,469 | 7,465 | 7,453 |
| Diluted EPS | $11.80 | $13.64 | $17.95 |

Source: [S2 income statement](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R2.htm).

- **R5.1 [FACT]** The FY2026 release reconciled GAAP net income of $133,749 to non-GAAP net income of $128,786 by removing a $4,963 after-tax benefit from OpenAI investments. FY2025 GAAP net income of $101,832 reconciled to $105,452 by removing a $3,620 after-tax expense from OpenAI investments. [S3](https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q4/press-release-webcast)

## R6 — Balance sheet, cash flow, and capital intensity

- **R6.1 [FACT]** At 2026-06-30: cash $20,935; short-term investments $55,908; accounts receivable $80,876; inventory $1,397; PP&E $313,076; accounts payable $42,416; current debt $9,227; long-term debt $31,067; short- and long-term unearned revenue $72,965 and $2,747; stockholders’ equity $442,387; shares outstanding 7,427 million. [S2 balance sheet](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R4.htm)
- **R6.2 [FACT]** FY2026 operating cash flow was $182,935; additions to property and equipment were $115,948; D&A and other were $38,534; SBC was $12,405; common-stock repurchases were $22,271; cash dividends were $26,445; and debt repayments were $3,000. [S2 cash flow](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R6.htm)
- **R6.3 [DEDUCTED]** FY2026 filing free cash flow is $66,987, defined only as operating cash flow less additions to property and equipment. The workbook computes it; this is not a reported GAAP measure. [S2 cash flow](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R6.htm)
- **R6.4 [FACT]** Gross PP&E at cost was $431,767 at 2026-06-30, including $215,874 of servers, network equipment, and software; net PP&E was $313,076. [S1 PP&E table](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R61.htm)
- **R6.5 [FACT]** Q4 capital expenditures were $41 billion, roughly two-thirds for short-lived assets, primarily CPUs and GPUs. At the start of FY2027 Microsoft extended estimated useful lives for datacenters and office buildings from 15 to 25 years; management expected minimal FY2027 operating-income benefit but a lease-classification effect on reported capital expenditures. [S5](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)

## R7 — Management’s FY2027 operating bar

- **R7.1 [FACT]** For FY2027, management expected double-digit revenue and operating-income growth, mid- to high-single-digit operating-expense growth, capital expenditures to grow year over year, operating margin to decline by less than one percentage point, an effective tax rate of approximately 20%, and positive free cash flow. [S5](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)
- **R7.2 [FACT]** Q1 FY2027 guidance: PBP revenue $36.7–$37.0 billion; IC $40.95–$41.25 billion; MPC $12.2–$12.7 billion; company revenue $89.85–$90.95 billion; cost of revenue $29.6–$29.8 billion; operating expense $16.8–$16.9 billion; approximately 20% tax rate; and capex above $50 billion. [S5](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)
- **R7.3 [FACT]** Q1 Azure constant-currency revenue growth was guided to approximately 45%; management expected first-half growth to accelerate and said demand still exceeded supply. Q1 Microsoft Cloud gross margin was expected to remain relatively stable sequentially. [S5](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)
- **R7.4 [FACT]** FY2027 headwinds cited by management included mid-single-digit declines in M365 Commercial products and Server products, a high-teens decline in Windows OEM and Devices, and PC-market pressure from component prices and channel inventory. [S5](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)

## R8 — Risks and dependency points

- **R8.1 [FACT]** Microsoft states that accelerated AI datacenter, component, and energy investment is made in advance of fully developed revenue streams; returns depend on AI adoption, Azure workload use, pricing, monetization, competition, and access to capital. [S1](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm)
- **R8.2 [FACT]** Microsoft has a long-term strategic partnership with OpenAI and states that strategic alliances can produce unsatisfactory returns, limited influence over third parties, delayed/smaller benefits, or impairment charges. [S1](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm)
- **R8.3 [FACT]** Microsoft identifies competition across cloud infrastructure/platforms, productivity/business applications, operating systems/devices, gaming, search/advertising, professional networks, and AI. Product bundling, regulation, cybersecurity, supply, energy, and datacenter execution can alter economics. [S1](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm)
- **R8.4 [FACT]** Management said short-lived CPUs/GPUs are the largest capex component and can be slowed if demand changes; land and datacenter build timing is more flexible. This is a mitigation, not evidence that overcapacity cannot occur. [S5](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)

## R9 — Explicit gaps

- **R9.1 [FACT]** Azure exact revenue, AI revenue, AI gross profit, AI capex, GPU/CPU utilization, token volume, token price, power capacity, and product-level AI return on invested capital: **not obtained**.
- **R9.2 [FACT]** Microsoft 365 Copilot standalone revenue, ARPU, usage revenue, gross profit, churn, and seat mix by SKU: **not obtained**.
- **R9.3 [FACT]** GitHub Copilot paid users, standalone revenue, ARPU, and gross profit: **not obtained**.
- **R9.4 [FACT]** Segment assets, liabilities, capex, D&A, SBC, working capital, and cash flow: **not obtained**.
- **R9.5 [FACT]** Azure capacity utilization and the dollar amount/timing of demand deferred specifically because of supply constraints: **not obtained**.
- **R9.6 [FACT]** Company-published sell-side consensus revenue, EPS, free cash flow, recommendation split, and analyst price-target distribution as of 2026-09-29: **not obtained**.
- **R9.7 [FACT]** Exact duration profile of the $678 billion commercial RPO and the amount attributable to OpenAI beyond management’s 25% ex-OpenAI growth comparison: **not obtained**.
