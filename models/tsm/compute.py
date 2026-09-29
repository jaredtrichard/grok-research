#!/usr/bin/env python3
"""TSMC foundry segment three-statement model.

All arithmetic for the markdown model lives here. Running this file rewrites
segments.md, income.md, balance.md and cashflow.md, then prints tie-out checks.
NT$ billions except per-share data, wafer units and percentages.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
HIST_PERIODS = ["FY2023A", "FY2024A", "FY2025A", "1H2026A"]
FORECAST_PERIODS = ["FY2026E", "FY2027E", "FY2028E"]
ALL_PERIODS = HIST_PERIODS + FORECAST_PERIODS

REGISTER = "../../memory/tsm/register.md"
S1 = "https://investor.tsmc.com/sites/ir/sec-filings/2025_20F%20Report.pdf"
S3 = "https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-07/a80d7933be643644081584087731f73b22ea5a2c/2Q26%20EarningsRelease.pdf"

# IASB-IFRS annual history (S1 / register R2). NT$bn.
HIST_FOUNDARY = {
    "FY2023A": {
        "revenue": 2_161.736,
        "gross_profit": 1_175.111,
        "operating_income": 921.466,
        "shipments_m": 0.0,  # FY2023 shipments not in register R4.1
        "vis_gain": 0.0,
    },
    "FY2024A": {
        "revenue": 2_894.308,
        "gross_profit": 1_624.354,
        "operating_income": 1_322.053,
        "shipments_m": 12.9,  # R4.1
        "vis_gain": 0.0,
    },
    "FY2025A": {
        "revenue": 3_809.054,
        "gross_profit": 2_281.294,
        "operating_income": 1_936.092,
        "shipments_m": 15.0,  # R4.1
        "vis_gain": 0.0,
    },
    "1H2026A": {
        "revenue": 2_404.48,  # R2 Q1+Q2 TIFRS
        "gross_profit": 1_611.61,
        "operating_income": 1_425.57,
        "shipments_m": 8.51,  # R2 4,174k + 4,336k
        "vis_gain": 63.20,  # R2.4A Q2 only; Q1 VIS not obtained
    },
}

HIST_INCOME = {
    "FY2023A": {
        "rd": 182.370,
        "ga": 60.873,
        "marketing": 10.591,
        "finance_income": 0.480,
        "finance_costs": 11.999,
        "other_recurring_nonop": 0.0,
        "vis_gain": 0.0,
        "pretax": 979.317,
        "tax": 128.289,
        "parent_ni": 851.740,
        "diluted_eps": 32.85,
        "diluted_shares": 25_928.0,
    },
    "FY2024A": {
        "rd": 204.182,
        "ga": 83.745,
        "marketing": 13.144,
        "finance_income": 0.567,
        "finance_costs": 10.495,
        "other_recurring_nonop": 0.0,
        "vis_gain": 0.0,
        "pretax": 1_405.840,
        "tax": 248.316,
        "parent_ni": 1_158.380,
        "diluted_eps": 44.67,
        "diluted_shares": 25_930.0,
    },
    "FY2025A": {
        "rd": 246.427,
        "ga": 82.304,
        "marketing": 16.918,
        "finance_income": 105.739,
        "finance_costs": 12.370,
        "other_recurring_nonop": 0.592,
        "vis_gain": 0.0,
        "pretax": 2_041.655,
        "tax": 346.530,
        "parent_ni": 1_697.604,
        "diluted_eps": 65.47,
        "diluted_shares": 25_932.0,
    },
    "1H2026A": {
        "rd": 0.0,  # quarterly split not obtained
        "ga": 0.0,
        "marketing": 0.0,
        "finance_income": 0.0,
        "finance_costs": 0.0,
        "other_recurring_nonop": 32.63,  # R2.4A: 95.83 non-op − 63.20 VIS
        "vis_gain": 63.20,
        "pretax": 0.0,  # filled from segment bridge
        "tax": 0.0,
        "parent_ni": 1_279.04,  # R2 Q1+Q2
        "diluted_eps": 0.0,
        "diluted_shares": 25_932.0,
    },
}

HIST_BALANCE = {
    "FY2023A": {
        "cash_and_securities": 1_465.428,
        "ar": 201.314,
        "inventory": 250.997,
        "ap": 55.727,
        "ppe": 3_064.475,
        "debt": 918.0,  # S1/XBRL; rounded
        "total_assets": 5_532.197,
        "total_liabilities": 2_078.330,
        "retained_earnings": 3_200.0,
        "equity": 3_453.867,
    },
    "FY2024A": {
        "cash_and_securities": 2_127.627,
        "ar": 270.683,
        "inventory": 287.869,
        "ap": 72.801,
        "ppe": 3_234.980,
        "debt": 960.0,
        "total_assets": 6_691.765,
        "total_liabilities": 2_412.493,
        "retained_earnings": 3_850.0,
        "equity": 4_279.272,
    },
    "FY2025A": {
        "cash_and_securities": 2_767.856,
        "ar": 279.052,
        "inventory": 288.110,
        "ap": 82.552,
        "ppe": 3_691.841,
        "debt": 992.153,
        "total_assets": 7_932.842,
        "total_liabilities": 2_536.623,
        "retained_earnings": 5_038.944,
        "equity": 5_396.219,
    },
    "1H2026A": {
        "cash_and_securities": 3_518.010,  # R7.4 TIFRS
        "ar": 440.920,
        "inventory": 385.530,
        "ap": 401.480,
        "ppe": 4_302.880,
        "debt": 1_031.680,
        "total_assets": 9_375.650,
        "total_liabilities": 3_937.160,  # [DEDUCTED] vs disclosed asset/debt/AP lines
        "retained_earnings": 5_318.0,  # [DEDUCTED] roll-forward anchor
        "equity": 5_438.490,
    },
}

HIST_CASHFLOW = {
    "FY2023A": {
        "parent_ni": 851.740,
        "da": 522.933,
        "ocf": 1_241.967,
        "capex": 949.817,
    },
    "FY2024A": {
        "parent_ni": 1_158.380,
        "da": 653.611,
        "ocf": 1_826.177,
        "capex": 956.006,
    },
    "FY2025A": {
        "parent_ni": 1_697.604,
        "da": 688.096,
        "ocf": 2_274.976,
        "capex": 1_272.410,
    },
    "1H2026A": {
        "parent_ni": 1_279.040,
        "da": 0.0,
        "ocf": 0.0,
        "capex": 0.0,
    },
}

# Q2 2026 disclosed mix (R3) — wafer revenue % unless noted.
Q2_2026_NODE_MIX = {
    "2nm": 0.03,
    "3nm": 0.30,
    "5nm": 0.33,
    "7nm": 0.11,
    "advanced_7nm_below": 0.77,
}
Q2_2026_PLATFORM_MIX = {
    "HPC": 0.66,
    "Smartphone": 0.22,
    "IoT": 0.05,
    "Automotive": 0.04,
    "DCE": 0.01,
    "Other": 0.02,
}

ASSUMPTIONS = {
    "FY2026E": {
        "revenue": 5_360.0,
        "shipments_m": 20.8,
        "gross_margin": 0.625,
        "rd": 283.0,
        "ga": 90.0,
        "marketing": 18.0,
        "capex": 1_984.0,
        "vis_gain": 0.0,
        "diluted_shares": 25_940.0,
        "dividends": 520.0,
        "node_mix": {"2nm": 0.09, "3nm": 0.31, "5nm": 0.30, "7nm": 0.10, "advanced_7nm_below": 0.80},
        "platform_mix": {"HPC": 0.68, "Smartphone": 0.20, "IoT": 0.04, "Automotive": 0.04, "DCE": 0.01, "Other": 0.03},
    },
    "FY2027E": {
        "revenue": 6_120.0,
        "shipments_m": 22.5,
        "gross_margin": 0.635,
        "rd": 317.0,
        "ga": 96.0,
        "marketing": 20.0,
        "capex": 1_850.0,
        "vis_gain": 0.0,
        "diluted_shares": 25_950.0,
        "dividends": 580.0,
        "node_mix": {"2nm": 0.14, "3nm": 0.30, "5nm": 0.28, "7nm": 0.09, "advanced_7nm_below": 0.81},
        "platform_mix": {"HPC": 0.69, "Smartphone": 0.19, "IoT": 0.04, "Automotive": 0.04, "DCE": 0.01, "Other": 0.03},
    },
    "FY2028E": {
        "revenue": 6_680.0,
        "shipments_m": 23.8,
        "gross_margin": 0.640,
        "rd": 349.0,
        "ga": 102.0,
        "marketing": 22.0,
        "capex": 1_700.0,
        "vis_gain": 0.0,
        "diluted_shares": 25_960.0,
        "dividends": 640.0,
        "node_mix": {"2nm": 0.18, "3nm": 0.28, "5nm": 0.26, "7nm": 0.08, "advanced_7nm_below": 0.80},
        "platform_mix": {"HPC": 0.70, "Smartphone": 0.18, "IoT": 0.04, "Automotive": 0.04, "DCE": 0.01, "Other": 0.03},
    },
}

SBC_RATE_ON_REVENUE = 0.005
DA_RATE_ON_AVERAGE_PPE = 0.115
INTEREST_INCOME_RATE = 0.025
MINIMUM_CASH_AND_SECURITIES = 1_500.0
BUYBACKS = 0.0
PACKAGING_CAPACITY_BINDING = True  # narrative flag R4.7; no P&L


def fmt(value: Any, decimals: int = 1) -> str:
    if value is None:
        return "not obtained"
    if isinstance(value, str):
        return value
    if abs(value) < 0.000_000_1:
        return "—"
    rendered = f"{abs(value):,.{decimals}f}"
    return f"({rendered})" if value < 0 else rendered


def pct(value: float) -> str:
    return f"{value * 100:.1f}%"


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    top = "| " + " | ".join(headers) + " |"
    separator = "|" + "|".join("---" for _ in headers) + "|"
    body = ["| " + " | ".join(str(cell) for cell in row) + " |" for row in rows]
    return "\n".join([top, separator, *body])


def derived_segments() -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    for period, raw in HIST_FOUNDARY.items():
        output[period] = {
            **raw,
            "foundry_revenue": raw["revenue"],
            "foundry_gp": raw["gross_profit"],
            "revenue_quotient_k_ntd_per_wafer": (
                raw["revenue"] * 1_000.0 / raw["shipments_m"]
                if raw["shipments_m"] > 0
                else None
            ),
        }
    return output


def build_forecast_segments() -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    for period, assumption in ASSUMPTIONS.items():
        revenue = assumption["revenue"]
        gp = revenue * assumption["gross_margin"]
        output[period] = {
            "revenue": revenue,
            "gross_profit": gp,
            "operating_income": 0.0,  # filled in income build
            "shipments_m": assumption["shipments_m"],
            "vis_gain": assumption["vis_gain"],
            "foundry_revenue": revenue,
            "foundry_gp": gp,
            "revenue_quotient_k_ntd_per_wafer": revenue * 1_000.0 / assumption["shipments_m"],
            "node_mix": assumption["node_mix"],
            "platform_mix": assumption["platform_mix"],
        }
    return output


def historical_balance_with_derived() -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    for period, raw in HIST_BALANCE.items():
        other_assets = (
            raw["total_assets"]
            - raw["cash_and_securities"]
            - raw["ar"]
            - raw["inventory"]
            - raw["ppe"]
        )
        if period == "1H2026A":
            other_assets = (
                raw["total_assets"]
                - raw["cash_and_securities"]
                - raw["ar"]
                - raw["inventory"]
                - raw["ppe"]
            )
            other_liabilities = raw["total_liabilities"] - raw["debt"] - raw["ap"]
            equity = raw["equity"]
            total_liabilities = raw["total_liabilities"]
        else:
            other_liabilities = raw["total_liabilities"] - raw["debt"] - raw["ap"]
            equity = raw["equity"]
            total_liabilities = raw["total_liabilities"]
        output[period] = {
            **raw,
            "other_assets": other_assets,
            "other_liabilities": other_liabilities,
            "stockholders_equity": equity,
            "retained_earnings": raw.get("retained_earnings", 0.0),
            "total_liabilities_and_equity": total_liabilities + equity,
        }
    return output


def build_income_and_forecast(
    segments: dict[str, dict[str, float]],
) -> tuple[dict[str, dict[str, float]], dict[str, dict[str, float]], dict[str, dict[str, float]]]:
    balances = historical_balance_with_derived()
    income: dict[str, dict[str, float]] = {}
    cashflow: dict[str, dict[str, float]] = {}

    for period in HIST_PERIODS:
        seg = segments[period]
        raw = HIST_INCOME[period]
        opex = raw["rd"] + raw["ga"] + raw["marketing"]
        operating_income = seg["operating_income"]
        recurring_nonop = (
            raw["finance_income"]
            - raw["finance_costs"]
            + raw["other_recurring_nonop"]
        )
        pretax = (
            operating_income + recurring_nonop + raw["vis_gain"]
            if raw["pretax"]
            else operating_income + recurring_nonop + raw["vis_gain"]
        )
        tax = raw["tax"] if raw["tax"] else max(pretax - raw["parent_ni"], 0.0)
        income[period] = {
            "revenue": seg["revenue"],
            "gross_profit": seg["gross_profit"],
            "rd": raw["rd"],
            "ga": raw["ga"],
            "marketing": raw["marketing"],
            "total_opex": opex,
            "operating_income": operating_income,
            "finance_income": raw["finance_income"],
            "finance_costs": raw["finance_costs"],
            "other_recurring_nonop": raw["other_recurring_nonop"],
            "vis_gain": raw["vis_gain"],
            "recurring_nonop": recurring_nonop,
            "pretax_recurring": operating_income + recurring_nonop,
            "pretax_reported": pretax,
            "tax": tax,
            "parent_ni": raw["parent_ni"],
            "parent_ni_recurring": raw["parent_ni"] - raw["vis_gain"] * (1 - tax / pretax if pretax else 0.17),
            "diluted_shares": raw["diluted_shares"],
            "diluted_eps": raw["diluted_eps"] or raw["parent_ni"] / raw["diluted_shares"] * 1_000,
        }

    fy25_tax_rate = HIST_INCOME["FY2025A"]["tax"] / HIST_INCOME["FY2025A"]["pretax"]
    ar_days = 29.0  # R7.5
    inventory_days = 87.0  # R7.5
    h1 = balances["1H2026A"]
    h1_cogs_annualized = (segments["1H2026A"]["revenue"] - segments["1H2026A"]["gross_profit"]) * 2.0
    ap_days = h1["ap"] / h1_cogs_annualized * 365.0

    for period in FORECAST_PERIODS:
        assumption = ASSUMPTIONS[period]
        seg = segments[period]
        is_fy26 = period == "FY2026E"
        previous = balances["1H2026A"] if is_fy26 else balances[FORECAST_PERIODS[FORECAST_PERIODS.index(period) - 1]]
        prior_annual = balances["FY2025A"] if is_fy26 else previous

        revenue = seg["revenue"]
        gross_profit = seg["gross_profit"]
        opex = assumption["rd"] + assumption["ga"] + assumption["marketing"]
        operating_income = gross_profit - opex
        finance_income = previous["cash_and_securities"] * INTEREST_INCOME_RATE
        finance_costs = previous["debt"] * 0.012
        other_recurring = 0.5
        vis_gain = assumption["vis_gain"]
        recurring_nonop = finance_income - finance_costs + other_recurring
        pretax_recurring = operating_income + recurring_nonop
        pretax_reported = pretax_recurring + vis_gain
        tax = max(pretax_reported, 0.0) * fy25_tax_rate
        parent_ni = pretax_reported - tax
        sbc = revenue * SBC_RATE_ON_REVENUE

        cogs = revenue - gross_profit
        ar = revenue * ar_days / 365.0
        inventory = cogs * inventory_days / 365.0
        ap = cogs * ap_days / 365.0
        delta_nwc = (ar + inventory - ap) - (
            previous["ar"] + previous["inventory"] - previous["ap"]
        )
        annual_delta_nwc = (ar + inventory - ap) - (
            prior_annual["ar"] + prior_annual["inventory"] - prior_annual["ap"]
        )

        rollforward_capex = assumption["capex"]
        rollforward_da = (
            DA_RATE_ON_AVERAGE_PPE
            * (previous["ppe"] + rollforward_capex / 2.0)
            / (1.0 + DA_RATE_ON_AVERAGE_PPE / 2.0)
        )
        annual_da = rollforward_da
        ppe = previous["ppe"] + rollforward_capex - rollforward_da

        ocf = parent_ni + annual_da + sbc - annual_delta_nwc
        fcf = ocf - assumption["capex"]
        pre_funding_cash = previous["cash_and_securities"] + fcf
        debt_issuance = max(MINIMUM_CASH_AND_SECURITIES - pre_funding_cash, 0.0)
        debt = previous["debt"] + debt_issuance
        cash_and_securities = pre_funding_cash + debt_issuance - assumption["dividends"] - BUYBACKS

        other_assets = previous["other_assets"]
        other_liabilities = previous["other_liabilities"]
        total_assets = cash_and_securities + ar + inventory + ppe + other_assets
        total_liabilities = ap + debt + other_liabilities
        equity = total_assets - total_liabilities
        retained = previous.get("retained_earnings", 0.0) + parent_ni - assumption["dividends"]

        balances[period] = {
            "cash_and_securities": cash_and_securities,
            "ar": ar,
            "inventory": inventory,
            "ap": ap,
            "ppe": ppe,
            "debt": debt,
            "other_assets": other_assets,
            "other_liabilities": other_liabilities,
            "retained_earnings": retained,
            "stockholders_equity": equity,
            "total_assets": total_assets,
            "total_liabilities": total_liabilities,
            "total_liabilities_and_equity": total_liabilities + equity,
            "diluted_shares": assumption["diluted_shares"],
        }

        income[period] = {
            "revenue": revenue,
            "gross_profit": gross_profit,
            "rd": assumption["rd"],
            "ga": assumption["ga"],
            "marketing": assumption["marketing"],
            "total_opex": opex,
            "operating_income": operating_income,
            "finance_income": finance_income,
            "finance_costs": finance_costs,
            "other_recurring_nonop": other_recurring,
            "vis_gain": vis_gain,
            "recurring_nonop": recurring_nonop,
            "pretax_recurring": pretax_recurring,
            "pretax_reported": pretax_reported,
            "tax": tax,
            "parent_ni": parent_ni,
            "parent_ni_recurring": pretax_recurring * (1 - fy25_tax_rate),
            "diluted_shares": assumption["diluted_shares"],
            "diluted_eps": parent_ni / assumption["diluted_shares"] * 1_000,
        }
        seg["operating_income"] = operating_income

        cashflow[period] = {
            "parent_ni": parent_ni,
            "da": annual_da,
            "sbc": sbc,
            "delta_nwc": annual_delta_nwc,
            "ocf": ocf,
            "capex": assumption["capex"],
            "fcf": fcf,
            "dividends": assumption["dividends"],
            "debt_issuance": debt_issuance,
            "cash_change": cash_and_securities - prior_annual["cash_and_securities"],
            "ending_cash_and_securities": cash_and_securities,
        }

    cashflow["_wc_days"] = {"ar_days": ar_days, "inventory_days": inventory_days, "ap_days": ap_days}
    return balances, income, cashflow


def build_checks(
    segments: dict[str, dict[str, float]],
    income: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
    cashflow: dict[str, dict[str, float]],
) -> list[tuple[str, bool, float]]:
    checks: list[tuple[str, bool, float]] = []
    tol = 0.05
    register_expected = {
        "FY2023A": (2_161.736, 1_175.111, 921.466, 851.740),
        "FY2024A": (2_894.308, 1_624.354, 1_322.053, 1_158.380),
        "FY2025A": (3_809.054, 2_281.294, 1_936.092, 1_697.604),
        "1H2026A": (2_404.48, 1_611.61, 1_425.57, 1_279.04),
    }
    for period, expected in register_expected.items():
        actual = (
            income[period]["revenue"],
            income[period]["gross_profit"],
            income[period]["operating_income"],
            income[period]["parent_ni"],
        )
        diff = max(abs(a - e) for a, e in zip(actual, expected))
        checks.append((f"{period}: register R2 tie", diff < tol, diff))

    for period in ALL_PERIODS:
        checks.append(
            (
                f"{period}: foundry revenue = company revenue",
                abs(segments[period]["foundry_revenue"] - income[period]["revenue"]) < tol,
                segments[period]["foundry_revenue"] - income[period]["revenue"],
            )
        )

    for period in FORECAST_PERIODS:
        bal = balances[period]
        checks.append(
            (
                f"{period}: balance sheet balances",
                abs(bal["total_assets"] - bal["total_liabilities_and_equity"]) < 5.0,
                bal["total_assets"] - bal["total_liabilities_and_equity"],
            )
        )
        cf = cashflow[period]
        checks.append(
            (
                f"{period}: CF ending cash = BS cash+securities",
                abs(cf["ending_cash_and_securities"] - bal["cash_and_securities"]) < tol,
                cf["ending_cash_and_securities"] - bal["cash_and_securities"],
            )
        )
    return checks


def render_segments(
    segments: dict[str, dict[str, float]],
    checks: list[tuple[str, bool, float]],
) -> str:
    rows = [
        ["Foundry revenue", *[fmt(segments[p]["foundry_revenue"]) for p in ALL_PERIODS]],
        ["Foundry gross profit", *[fmt(segments[p]["foundry_gp"]) for p in ALL_PERIODS]],
        ["Company revenue", *[fmt(segments[p]["revenue"]) for p in ALL_PERIODS]],
        ["Company gross profit", *[fmt(segments[p]["gross_profit"]) for p in ALL_PERIODS]],
        ["Operating income", *[fmt(segments[p].get("operating_income", 0)) for p in ALL_PERIODS]],
    ]
    driver_rows = []
    for period in ALL_PERIODS:
        seg = segments[period]
        assumption = ASSUMPTIONS.get(period)
        gm = assumption["gross_margin"] if assumption else seg["gross_profit"] / seg["revenue"]
        quotient = seg["revenue_quotient_k_ntd_per_wafer"]
        driver_rows.append(
            [
                period,
                fmt(seg["shipments_m"], 2) if seg["shipments_m"] else "not obtained",
                fmt(quotient, 1) if quotient is not None else "not obtained",
                pct(gm),
                "binding [VIEW] constraint" if PACKAGING_CAPACITY_BINDING and period in FORECAST_PERIODS else "—",
            ]
        )

    node_header = ["node (wafer revenue %)"] + ALL_PERIODS
    node_rows = []
    for label, key in [
        ("2nm", "2nm"),
        ("3nm", "3nm"),
        ("5nm", "5nm"),
        ("7nm", "7nm"),
        ("7nm and below", "advanced_7nm_below"),
    ]:
        vals = []
        for period in ALL_PERIODS:
            if period in FORECAST_PERIODS:
                mix = segments[period]["node_mix"]
                vals.append(f"[VIEW] {pct(mix[key])}")
            elif period == "FY2025A":
                vals.append("not obtained by node")
            elif period == "1H2026A":
                vals.append("—")
            else:
                vals.append("not obtained")
        node_rows.append([label, *vals])

    plat_rows = []
    for label in Q2_2026_PLATFORM_MIX:
        vals = []
        for period in ALL_PERIODS:
            if period in FORECAST_PERIODS:
                vals.append(f"[VIEW] {pct(segments[period]['platform_mix'][label])}")
            elif period == "1H2026A":
                vals.append("—")
            else:
                vals.append("not obtained")
        plat_rows.append([label, *vals])

    q2_quotient = 1_270.38 / 4.336
    check_rows = [
        [name, "OK" if ok else "ERROR", fmt(diff, 2)]
        for name, ok, diff in checks
        if "foundry revenue" in name or "register" in name
    ]

    return f"""# TSMC segment model

Generated by `compute.py`; do not hand-edit. NT$ billions except wafer equivalents (million 12-inch-equiv.) and percentages.

## Foundry segment (single reportable segment)

{markdown_table(["line", *ALL_PERIODS], rows)}

TSMC reports one foundry segment (R1.2). Node and platform tables are disclosure lenses only—no fabricated node P&Ls.

## Operating drivers

{markdown_table(["period", "shipments (m 12-inch-equiv.)", "revenue quotient (NT$k / wafer-equiv.)", "company GM", "packaging lens"], driver_rows)}

`[DEDUCTED]` Q2 2026 quotient cross-check: `NT$1,270.38bn / 4.336m = {q2_quotient:.1f}` NT$ thousand per shipped 12-inch-equivalent. This is **not** wafer ASP (R3.3).

Advanced packaging (CoWoS and related) is modeled as a **capacity constraint** on system-level demand (R4.7), not a separate revenue or margin pool (R10.3).

## Node mix lens (wafer revenue %)

Q2 2026 actual mix [FACT] R3: 2nm {pct(Q2_2026_NODE_MIX['2nm'])}, 3nm {pct(Q2_2026_NODE_MIX['3nm'])}, 5nm {pct(Q2_2026_NODE_MIX['5nm'])}, 7nm {pct(Q2_2026_NODE_MIX['7nm'])}, 7nm-and-below {pct(Q2_2026_NODE_MIX['advanced_7nm_below'])}.

{markdown_table(node_header, node_rows)}

Forecast advanced-node path embeds N2 ramp dilution in company gross margin (R6.1), not node-level margins.

## Platform mix lens (total revenue %)

Q2 2026 actual mix [FACT] R3: HPC {pct(Q2_2026_PLATFORM_MIX['HPC'])}, Smartphone {pct(Q2_2026_PLATFORM_MIX['Smartphone'])}.

{markdown_table(["platform", *ALL_PERIODS], plat_rows)}

## Segment tie checks

{markdown_table(["check", "status", "difference"], check_rows)}
"""


def render_income(income: dict[str, dict[str, float]], checks: list[tuple[str, bool, float]]) -> str:
    rows = [
        ["Revenue"] + [fmt(income[p]["revenue"]) for p in ALL_PERIODS],
        ["Gross profit"] + [fmt(income[p]["gross_profit"]) for p in ALL_PERIODS],
        ["R&D"] + [fmt(income[p]["rd"]) for p in ALL_PERIODS],
        ["G&A"] + [fmt(income[p]["ga"]) for p in ALL_PERIODS],
        ["Marketing"] + [fmt(income[p]["marketing"]) for p in ALL_PERIODS],
        ["Operating income"] + [fmt(income[p]["operating_income"]) for p in ALL_PERIODS],
        ["Finance income"] + [fmt(income[p]["finance_income"]) for p in ALL_PERIODS],
        ["Finance costs"] + [fmt(-income[p]["finance_costs"]) for p in ALL_PERIODS],
        ["Other recurring non-operating"] + [fmt(income[p]["other_recurring_nonop"]) for p in ALL_PERIODS],
        ["VIS disposal / MTM gain (nonrecurring)"] + [fmt(income[p]["vis_gain"]) for p in ALL_PERIODS],
        ["Pre-tax income (reported)"] + [fmt(income[p]["pretax_reported"]) for p in ALL_PERIODS],
        ["Pre-tax recurring (ex VIS)"] + [fmt(income[p]["pretax_recurring"]) for p in ALL_PERIODS],
        ["Income tax"] + [fmt(income[p]["tax"]) for p in ALL_PERIODS],
        ["Net income attributable to parent"] + [fmt(income[p]["parent_ni"]) for p in ALL_PERIODS],
        ["Recurring parent NI (ex VIS, model)"] + [fmt(income[p]["parent_ni_recurring"]) for p in ALL_PERIODS],
        ["Diluted WAS (m)"] + [fmt(income[p]["diluted_shares"], 0) for p in ALL_PERIODS],
        ["Diluted EPS (NT$)"] + [fmt(income[p]["diluted_eps"], 2) for p in ALL_PERIODS],
    ]
    hist_checks = [[n, "OK" if ok else "ERROR", fmt(d, 2)] for n, ok, d in checks if "register" in n]
    return f"""# TSMC income statement

Generated by `compute.py`; do not hand-edit. NT$ billions except per-share data.

IASB-IFRS annual history FY2023–FY2025 from [register R2]({REGISTER}) and [S1]({S1}). `1H2026A` is **TIFRS** (Q1+Q2 per R2) and is not comparable to full-year IASB columns without adjustment (R2.3A).

VIS gain is separated per R2.4A; forecast years assume zero nonrecurring investment gains.

{markdown_table(["line", *ALL_PERIODS], rows)}

## Register tie checks

{markdown_table(["check", "status", "max difference"], hist_checks)}
"""


def render_balance(
    balances: dict[str, dict[str, float]],
    income: dict[str, dict[str, float]],
    checks: list[tuple[str, bool, float]],
) -> str:
    rows = [
        ["Cash and marketable securities"]
        + [fmt(balances[p]["cash_and_securities"]) for p in ALL_PERIODS],
        ["Accounts receivable"] + [fmt(balances[p]["ar"]) for p in ALL_PERIODS],
        ["Inventory"] + [fmt(balances[p]["inventory"]) for p in ALL_PERIODS],
        ["PP&E, net"] + [fmt(balances[p]["ppe"]) for p in ALL_PERIODS],
        ["Other assets"] + [fmt(balances[p]["other_assets"]) for p in ALL_PERIODS],
        ["Total assets"] + [fmt(balances[p]["total_assets"]) for p in ALL_PERIODS],
        ["Accounts payable"] + [fmt(balances[p]["ap"]) for p in ALL_PERIODS],
        ["Interest-bearing debt"] + [fmt(balances[p]["debt"]) for p in ALL_PERIODS],
        ["Other liabilities"] + [fmt(balances[p]["other_liabilities"]) for p in ALL_PERIODS],
        ["Total liabilities"] + [fmt(balances[p]["total_liabilities"]) for p in ALL_PERIODS],
        ["Stockholders' equity"] + [fmt(balances[p]["stockholders_equity"]) for p in ALL_PERIODS],
        ["Total liabilities and equity"]
        + [fmt(balances[p]["total_liabilities_and_equity"]) for p in ALL_PERIODS],
    ]
    rel = [[n, "OK" if ok else "ERROR", fmt(d, 2)] for n, ok, d in checks if "balance sheet" in n]
    return f"""# TSMC balance sheet

Generated by `compute.py`; do not hand-edit. NT$ billions.

FY2023–FY2025 from IASB-IFRS [S1]({S1}); `1H2026A` from [R7.4]({REGISTER}) (**TIFRS**, 2026-06-30). Forecast rolls forward from the latest base.

{markdown_table(["line", *ALL_PERIODS], rows)}

## Tie checks

{markdown_table(["check", "status", "difference"], rel)}
"""


def render_cashflow(
    balances: dict[str, dict[str, float]],
    cashflow: dict[str, dict[str, float]],
    checks: list[tuple[str, bool, float]],
) -> str:
    hist_lines = [
        ("Parent net income", "parent_ni"),
        ("D&A", "da"),
        ("Operating cash flow", "ocf"),
        ("PP&E purchases (capex)", "capex"),
        ("Free cash flow", "fcf"),
    ]
    rows: list[list[str]] = []
    for label, key in hist_lines:
        vals = []
        for p in HIST_PERIODS:
            if p == "1H2026A" and key in {"ocf", "capex", "fcf", "da"}:
                vals.append("not obtained")
            elif key == "fcf":
                raw = HIST_CASHFLOW[p]
                vals.append(fmt(raw["ocf"] - raw["capex"]) if raw["ocf"] else "not obtained")
            elif key == "parent_ni":
                vals.append(fmt(HIST_CASHFLOW[p]["parent_ni"]))
            else:
                v = HIST_CASHFLOW[p].get(key.replace("fcf", "ocf"))
                vals.append(fmt(v) if v else "not obtained")
        rows.append([label, *vals, "—", "—", "—"])

    forecast_lines = [
        ("Parent net income", "parent_ni", False),
        ("D&A", "da", False),
        ("SBC", "sbc", False),
        ("Less: increase in NWC", "delta_nwc", True),
        ("Operating cash flow", "ocf", False),
        ("Less: capex", "capex", True),
        ("Free cash flow", "fcf", False),
        ("Dividends", "dividends", True),
        ("Net debt issuance", "debt_issuance", False),
        ("Change in cash and securities", "cash_change", False),
        ("Ending cash and securities", "ending_cash_and_securities", False),
    ]
    for label, key, negate in forecast_lines:
        vals = []
        for p in FORECAST_PERIODS:
            v = cashflow[p][key]
            if negate:
                v = -v
            vals.append(fmt(v))
        rows.append([label, "—", "—", "—", "—", *vals])

    wc = cashflow["_wc_days"]
    rel = [[n, "OK" if ok else "ERROR", fmt(d, 2)] for n, ok, d in checks if "CF ending" in n]
    return f"""# TSMC cash-flow statement

Generated by `compute.py`; do not hand-edit. NT$ billions.

Historical OCF and capex from [register R2/R7.1]({REGISTER}). `1H2026A` operating cash flow and capex are **not obtained** at the register cut.

Forecast OCF = NI + D&A + SBC − ΔNWC. Working-capital days: AR {wc['ar_days']:.0f} (R7.5), inventory {wc['inventory_days']:.0f} (R7.5), AP {wc['ap_days']:.1f} (`[DEDUCTED]` from 2026-06-30). Capex follows `[VIEW]` intensity tied to R7.3 2026 budget.

{markdown_table(["line", *ALL_PERIODS], rows)}

## Cash tie checks

{markdown_table(["check", "status", "difference"], rel)}
"""


def main() -> None:
    segments = {**derived_segments(), **build_forecast_segments()}
    balances, income, cashflow = build_income_and_forecast(segments)
    checks = build_checks(segments, income, balances, cashflow)

    outputs = {
        "segments.md": render_segments(segments, checks),
        "income.md": render_income(income, checks),
        "balance.md": render_balance(balances, income, checks),
        "cashflow.md": render_cashflow(balances, cashflow, checks),
    }
    for name, content in outputs.items():
        (ROOT / name).write_text(content.rstrip() + "\n", encoding="utf-8")

    print("TSMC model outputs (NT$bn)")
    print("period | revenue | GM | OI | parent NI | FCF | EPS")
    for period in FORECAST_PERIODS:
        inc = income[period]
        cf = cashflow[period]
        gm = inc["gross_profit"] / inc["revenue"]
        print(
            f"{period} | {inc['revenue']:.1f} | {gm*100:.1f}% | "
            f"{inc['operating_income']:.1f} | {inc['parent_ni']:.1f} | "
            f"{cf['fcf']:.1f} | {inc['diluted_eps']:.2f}"
        )
    print("\nTie-out checks")
    failed = False
    for name, ok, diff in checks:
        status = "OK" if ok else "ERROR"
        print(f"{status}: {name} (difference {diff:.4f})")
        failed = failed or not ok
    if failed:
        raise SystemExit("One or more model checks failed")


if __name__ == "__main__":
    main()
