#!/usr/bin/env python3
"""TSMC foundry segment three-statement model.

All arithmetic for the markdown model lives here. Running this file rewrites
segments.md, income.md, balance.md, cashflow.md and valuation.md, then prints tie-out checks.
NT$ billions except per-share data, wafer units and percentages.
"""

from __future__ import annotations

from datetime import date
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

# Valuation as-of and market (ADR, USD). Primary last close from Yahoo chart API 2026-09-29.
VALUATION_AS_OF = date(2026, 9, 29)
LAST_PRICE_DATE = date(2026, 9, 29)
LAST_PRICE = 456.94
LAST_PRICE_SOURCE = "https://finance.yahoo.com/quote/TSM/history/"
YAHOO_TSM_CHART = "https://query1.finance.yahoo.com/v8/finance/chart/TSM?range=5d&interval=1d"
ADR_SHARES_PER_ADR = 5  # register R8.1
USD_NTD_VIEW = 32.0  # [VIEW]; aligns with Q3 2026 guidance FX in R2.5

# Official 12-month PT: EV / recurring EBIT + net cash (single foundry segment).
OFFICIAL_EBIT_PERIOD = "FY2027E"
OFFICIAL_NET_CASH_PERIOD = "FY2027E"
OFFICIAL_EBIT_MULTIPLE = 21.0  # [VIEW]; premium pure-play foundry vs diversified semi
OFFICIAL_SHARES_PERIOD = "FY2027E"

# Equity DCF cross-check on modeled recurring FCF (ex VIS).
DCF_WACC = 0.095  # [VIEW]; net-cash foundry, Taiwan listing + ADR
DCF_TERMINAL_GROWTH = 0.030  # [VIEW]; advanced-node TAM, capped below GDP+inflation
DCF_MID_YEAR_OFFSETS = (0.5, 1.5, 2.5)  # FY2026E–FY2028E mid-year from as-of

# Sensitivity / alternate horizon checks (not additional official targets).
BEAR_EBIT_MULTIPLE = 18.0  # [VIEW]
BULL_EBIT_MULTIPLE = 24.0  # [VIEW]
THREE_YEAR_EBIT_PERIOD = "FY2028E"
THREE_YEAR_NET_CASH_PERIOD = "FY2028E"
THREE_YEAR_EBIT_MULTIPLE = 19.0  # [VIEW]
WACC_SENS_DOWN = 0.085  # [VIEW]
WACC_SENS_UP = 0.105  # [VIEW]


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


def _net_cash_ntd(balances: dict[str, dict[str, float]], period: str) -> float:
    bal = balances[period]
    return bal["cash_and_securities"] - bal["debt"]


def _equity_from_ebit_multiple(
    income: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
    ebit_period: str,
    net_cash_period: str,
    multiple: float,
) -> tuple[float, float, float]:
    """Return (operating_ev, net_cash, equity_value) in NT$bn."""
    operating_ev = income[ebit_period]["operating_income"] * multiple
    net_cash = _net_cash_ntd(balances, net_cash_period)
    return operating_ev, net_cash, operating_ev + net_cash


def _pt_from_equity_ntd(
    equity_ntd_bn: float,
    shares_m: float,
) -> tuple[float, float, float]:
    """Return (common PT NT$, ADR PT USD, equity USD bn)."""
    common_pt_ntd = equity_ntd_bn * 1_000.0 / shares_m
    adr_pt_usd = common_pt_ntd * ADR_SHARES_PER_ADR / USD_NTD_VIEW
    equity_usd_bn = equity_ntd_bn / USD_NTD_VIEW
    return common_pt_ntd, adr_pt_usd, equity_usd_bn


def _dcf_equity_ntd(
    cashflow: dict[str, dict[str, float]],
    wacc: float,
    terminal_growth: float,
) -> tuple[float, float, float, float]:
    """Equity DCF on forecast FCF; returns (pv_fcfs, pv_terminal, terminal_fcf, equity). NT$bn."""
    fcfs = [cashflow[p]["fcf"] for p in FORECAST_PERIODS]
    pv_fcfs = sum(
        fcf / ((1.0 + wacc) ** year_offset)
        for fcf, year_offset in zip(fcfs, DCF_MID_YEAR_OFFSETS)
    )
    terminal_fcf = fcfs[-1] * (1.0 + terminal_growth)
    terminal_value = terminal_fcf / (wacc - terminal_growth)
    pv_terminal = terminal_value / ((1.0 + wacc) ** DCF_MID_YEAR_OFFSETS[-1])
    return pv_fcfs, pv_terminal, terminal_fcf, pv_fcfs + pv_terminal


def build_valuation(
    income: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
    cashflow: dict[str, dict[str, float]],
) -> tuple[str, dict[str, float]]:
    shares_m = income[OFFICIAL_SHARES_PERIOD]["diluted_shares"]
    adr_shares_m = shares_m / ADR_SHARES_PER_ADR

    op_ev, net_cash_official, official_equity = _equity_from_ebit_multiple(
        income,
        balances,
        OFFICIAL_EBIT_PERIOD,
        OFFICIAL_NET_CASH_PERIOD,
        OFFICIAL_EBIT_MULTIPLE,
    )
    common_pt, adr_pt, _ = _pt_from_equity_ntd(official_equity, shares_m)

    bear_equity = _equity_from_ebit_multiple(
        income,
        balances,
        OFFICIAL_EBIT_PERIOD,
        OFFICIAL_NET_CASH_PERIOD,
        BEAR_EBIT_MULTIPLE,
    )[2]
    bull_equity = _equity_from_ebit_multiple(
        income,
        balances,
        OFFICIAL_EBIT_PERIOD,
        OFFICIAL_NET_CASH_PERIOD,
        BULL_EBIT_MULTIPLE,
    )[2]
    bear_adr_pt = _pt_from_equity_ntd(bear_equity, shares_m)[1]
    bull_adr_pt = _pt_from_equity_ntd(bull_equity, shares_m)[1]

    three_year_equity = _equity_from_ebit_multiple(
        income,
        balances,
        THREE_YEAR_EBIT_PERIOD,
        THREE_YEAR_NET_CASH_PERIOD,
        THREE_YEAR_EBIT_MULTIPLE,
    )[2]
    three_year_adr_pt = _pt_from_equity_ntd(three_year_equity, shares_m)[1]

    h1_net_cash = _net_cash_ntd(balances, "1H2026A")

    pv_fcfs, pv_terminal, terminal_fcf, dcf_equity = _dcf_equity_ntd(
        cashflow, DCF_WACC, DCF_TERMINAL_GROWTH
    )
    dcf_equity += h1_net_cash
    dcf_adr_pt = _pt_from_equity_ntd(dcf_equity, shares_m)[1]
    dcf_bear = _dcf_equity_ntd(cashflow, WACC_SENS_UP, DCF_TERMINAL_GROWTH)[3] + h1_net_cash
    dcf_bull = _dcf_equity_ntd(cashflow, WACC_SENS_DOWN, DCF_TERMINAL_GROWTH)[3] + h1_net_cash
    dcf_bear_pt = _pt_from_equity_ntd(dcf_bear, shares_m)[1]
    dcf_bull_pt = _pt_from_equity_ntd(dcf_bull, shares_m)[1]

    market_cap_usd_m = LAST_PRICE * adr_shares_m
    market_cap_usd_bn = market_cap_usd_m / 1_000.0
    market_cap_ntd_bn = market_cap_usd_bn * USD_NTD_VIEW
    current_operating_ev = market_cap_ntd_bn - h1_net_cash

    ebit_official = income[OFFICIAL_EBIT_PERIOD]["operating_income"]
    recurring_ni_official = income[OFFICIAL_EBIT_PERIOD]["parent_ni_recurring"]
    revenue_official = income[OFFICIAL_EBIT_PERIOD]["revenue"]
    ebit_fy28 = income["FY2028E"]["operating_income"]
    recurring_ni_fy28 = income["FY2028E"]["parent_ni_recurring"]
    revenue_fy28 = income["FY2028E"]["revenue"]

    implied_ev_ebit_fy27 = current_operating_ev / ebit_official
    implied_ev_ebit_fy28 = current_operating_ev / ebit_fy28
    implied_pe_fy27 = market_cap_ntd_bn / recurring_ni_official
    implied_pe_fy28 = market_cap_ntd_bn / recurring_ni_fy28
    implied_ev_sales_fy27 = current_operating_ev / revenue_official

    residual_adr = LAST_PRICE - adr_pt
    tape_premium_pct = (LAST_PRICE / adr_pt - 1.0) * 100.0 if adr_pt else 0.0

    summary = {
        "adr_pt": adr_pt,
        "common_pt_ntd": common_pt,
        "official_equity_ntd": official_equity,
        "bear_adr_pt": bear_adr_pt,
        "bull_adr_pt": bull_adr_pt,
        "three_year_adr_pt": three_year_adr_pt,
        "dcf_adr_pt": dcf_adr_pt,
        "residual_adr": residual_adr,
    }

    bridge_rows = [
        [
            f"{OFFICIAL_EBIT_PERIOD} recurring operating income (foundry)",
            "income.md; ex VIS",
            fmt(ebit_official),
        ],
        [
            f"[VIEW] Selected EV / EBIT",
            f"{OFFICIAL_EBIT_MULTIPLE:.1f}×; premium foundry vs diversified semi",
            f"{OFFICIAL_EBIT_MULTIPLE:.1f}×",
        ],
        [
            "[VIEW] Operating enterprise value",
            "EBIT × multiple",
            fmt(op_ev),
        ],
        [
            f"{OFFICIAL_NET_CASH_PERIOD} net cash",
            "Cash + securities − interest-bearing debt; model balance.md",
            fmt(net_cash_official),
        ],
        [
            "Official equity value (NT$bn)",
            "Operating EV + net cash",
            fmt(official_equity),
        ],
        [
            "Diluted WAS (m)",
            f"R8.5 / {OFFICIAL_SHARES_PERIOD} [VIEW] path",
            fmt(shares_m, 0),
        ],
        [
            "Official 12-month PT / common share",
            "Equity ÷ diluted WAS",
            fmt(common_pt, 2),
        ],
        [
            "Implied PT / ADR (USD)",
            f"Common PT × {ADR_SHARES_PER_ADR} ÷ {USD_NTD_VIEW:.0f} USD/NTD [VIEW]",
            f"${adr_pt:.2f}",
        ],
    ]

    dcf_rows = [
        [p, fmt(cashflow[p]["fcf"]), f"{DCF_MID_YEAR_OFFSETS[i]:.1f}", fmt(DCF_WACC * 100, 1) + "% [VIEW]"]
        for i, p in enumerate(FORECAST_PERIODS)
    ]

    check_rows = [
        ["Bear EV/EBIT", f"{BEAR_EBIT_MULTIPLE:.0f}× {OFFICIAL_EBIT_PERIOD} OI + net cash", f"${bear_adr_pt:.2f}"],
        ["Base (official)", f"{OFFICIAL_EBIT_MULTIPLE:.0f}× {OFFICIAL_EBIT_PERIOD} OI + net cash", f"${adr_pt:.2f}"],
        ["Bull EV/EBIT", f"{BULL_EBIT_MULTIPLE:.0f}× {OFFICIAL_EBIT_PERIOD} OI + net cash", f"${bull_adr_pt:.2f}"],
        [
            "3-year exit check",
            f"{THREE_YEAR_EBIT_MULTIPLE:.0f}× {THREE_YEAR_EBIT_PERIOD} OI + net cash",
            f"${three_year_adr_pt:.2f}",
        ],
        [
            "DCF base",
            f"WACC {DCF_WACC*100:.1f}%, terminal g {DCF_TERMINAL_GROWTH*100:.0f}% on FY2028E FCF",
            f"${dcf_adr_pt:.2f}",
        ],
        [
            "DCF WACC +1.0pp",
            f"WACC {WACC_SENS_UP*100:.1f}%",
            f"${dcf_bear_pt:.2f}",
        ],
        [
            "DCF WACC −1.0pp",
            f"WACC {WACC_SENS_DOWN*100:.1f}%",
            f"${dcf_bull_pt:.2f}",
        ],
    ]

    tape_rows = [
        ["Last-price market cap (USD bn)", "Last close × ADR count", fmt(market_cap_usd_bn, 1)],
        ["Last-price market cap (NT$bn)", f"× {USD_NTD_VIEW:.0f} USD/NTD [VIEW]", fmt(market_cap_ntd_bn, 1)],
        ["2026-06-30 net cash (NT$bn)", "R7.4; model 1H2026A", fmt(h1_net_cash, 1)],
        ["Current operating EV (NT$bn)", "Market cap − net cash", fmt(current_operating_ev, 1)],
        [f"EV / {OFFICIAL_EBIT_PERIOD} recurring EBIT", "Operating EV ÷ OI", fmt(implied_ev_ebit_fy27, 1) + "×"],
        ["EV / FY2028E recurring EBIT", "Operating EV ÷ OI", fmt(implied_ev_ebit_fy28, 1) + "×"],
        [f"P/E on {OFFICIAL_EBIT_PERIOD} recurring NI", "Market cap ÷ recurring parent NI", fmt(implied_pe_fy27, 1) + "×"],
        ["P/E on FY2028E recurring NI", "Market cap ÷ recurring parent NI", fmt(implied_pe_fy28, 1) + "×"],
        [f"EV / {OFFICIAL_EBIT_PERIOD} revenue", "Operating EV ÷ revenue", fmt(implied_ev_sales_fy27, 1) + "×"],
        [
            "[DEDUCTED] Tape vs official PT / ADR",
            f"${LAST_PRICE:.2f} − ${adr_pt:.2f}",
            f"${residual_adr:.2f} ({tape_premium_pct:+.1f}% vs PT)",
        ],
    ]

    comps_rows = [
        ["Samsung Electronics (foundry + devices)", "EV/EBIT, EV/Sales", "not obtained", "R10.8; no comparable foundry-only financials in TSMC primary set"],
        ["Intel (Intel Foundry + products)", "EV/EBIT", "not obtained", "R10.8"],
        ["GlobalFoundries (GFS)", "EV/EBIT", "not obtained", "R10.9; no refreshed peer pull in this gate"],
        ["UMC / SMIC (pure-play foundry peers)", "EV/EBIT", "not obtained", "R10.8; multiples not sourced here"],
    ]

    content = f"""# TSMC valuation

At the ${LAST_PRICE:.2f} ADR last close, the official **12-month price target** is **${adr_pt:.2f} per ADR** (**NT${common_pt:,.2f} per common share**), from a single-segment foundry **EV / recurring EBIT** bridge on the modeled `{OFFICIAL_EBIT_PERIOD}` path plus net cash. TSMC reports one foundry segment (R1.2); this is not a platform SOTP.

## Official method and as-of

| item | value |
|---|---|
| Valuation as-of | {VALUATION_AS_OF.isoformat()} |
| Last close (ADR, USD) | ${LAST_PRICE:.2f} on {LAST_PRICE_DATE.isoformat()} |
| Last-price source | [Yahoo Finance TSM history]({LAST_PRICE_SOURCE}) (cross-check: [Yahoo chart API]({YAHOO_TSM_CHART})) |
| ADR ratio | 1 ADR = {ADR_SHARES_PER_ADR} common shares (R8.1) |
| FX for ADR bridge | {USD_NTD_VIEW:.0f} NT$ / USD `[VIEW]` (Q3 2026 guidance anchor R2.5) |
| PT denominator | {fmt(shares_m, 0)}m diluted WAS, `{OFFICIAL_SHARES_PERIOD}` model path |
| Primary method | {OFFICIAL_EBIT_MULTIPLE:.1f}× `{OFFICIAL_EBIT_PERIOD}` **recurring operating income** + `{OFFICIAL_NET_CASH_PERIOD}` net cash |
| Recurring earnings | Operating income and parent NI exclude Q2 2026 VIS gain (R2.4A); forecast VIS = 0 `[VIEW]` |

## What the tape must be paying for

The table below compares the **last price** to **model recurring foundry earnings** from [`income.md`](income.md). If the market is rational on this `[VIEW]` forecast path, the implied multiples should bracket the selected {OFFICIAL_EBIT_MULTIPLE:.0f}× EBIT anchor or embed extra growth, packaging scarcity, or geopolitical discount not in the base case.

{markdown_table(["item", "formula", "value"], tape_rows)}

At tape, **EV / {OFFICIAL_EBIT_PERIOD} recurring EBIT** is **{implied_ev_ebit_fy27:.1f}×** versus the official **{OFFICIAL_EBIT_MULTIPLE:.0f}×** selection. A higher tape multiple implies the market is paying for faster AI/HPC foundry growth, longer advanced-node pricing power, or net-cash optionality beyond the base `{OFFICIAL_EBIT_PERIOD}` `{OFFICIAL_EBIT_MULTIPLE:.0f}×` frame; a lower multiple would imply overseas-fab dilution (R6.2), export-control risk (R9.3), or cyclical utilization stress not captured in the `[VIEW]` margin path.

## Official equity bridge (NT$ billions → per share)

{markdown_table(["item", "basis", "NT$bn or multiple"], bridge_rows)}

**[VIEW] Multiple rationale ({OFFICIAL_EBIT_MULTIPLE:.0f}×):** TSMC is modeled as a single pure-play leading-edge foundry with net cash and elevated capex converting to revenue on the R7.3 budget path. {OFFICIAL_EBIT_MULTIPLE:.0f}× `{OFFICIAL_EBIT_PERIOD}` recurring operating income sits near the **tape-implied {implied_ev_ebit_fy27:.1f}×** on the same model EBIT, slightly below a bull foundry premium to reflect overseas margin dilution (R6.2) and concentration risk (R5.1, R9.5). It is **not** sourced from peer multiples (R10.8).

## Recurring foundry operating path (valuation inputs)

| line | FY2026E | FY2027E | FY2028E | source |
|---|---:|---:|---:|---|
| Revenue | {fmt(income['FY2026E']['revenue'])} | {fmt(income['FY2027E']['revenue'])} | {fmt(income['FY2028E']['revenue'])} | income.md |
| Gross margin | {pct(income['FY2026E']['gross_profit']/income['FY2026E']['revenue'])} | {pct(income['FY2027E']['gross_profit']/income['FY2027E']['revenue'])} | {pct(income['FY2028E']['gross_profit']/income['FY2028E']['revenue'])} | `[VIEW]` inputs.md |
| Operating income (recurring) | {fmt(income['FY2026E']['operating_income'])} | {fmt(income['FY2027E']['operating_income'])} | {fmt(income['FY2028E']['operating_income'])} | income.md |
| Recurring parent NI | {fmt(income['FY2026E']['parent_ni_recurring'])} | {fmt(income['FY2027E']['parent_ni_recurring'])} | {fmt(income['FY2028E']['parent_ni_recurring'])} | ex VIS |
| Free cash flow | {fmt(cashflow['FY2026E']['fcf'])} | {fmt(cashflow['FY2027E']['fcf'])} | {fmt(cashflow['FY2028E']['fcf'])} | cashflow.md |

## Equity DCF cross-check (recurring FCF)

| [VIEW] item | value | note |
|---|---|---|
| WACC | {DCF_WACC*100:.1f}% | Foundry leader with net cash; Taiwan/ADR listing; not observed from market data |
| Terminal growth | {DCF_TERMINAL_GROWTH*100:.0f}% | Perpetuity on FY2028E FCF [VIEW] |
| Mid-year convention | {DCF_MID_YEAR_OFFSETS[0]:.1f} / {DCF_MID_YEAR_OFFSETS[1]:.1f} / {DCF_MID_YEAR_OFFSETS[2]:.1f} years | FY2026E–FY2028E FCF from cashflow.md |
| PV of forecast FCF | {fmt(pv_fcfs)} | Sum of three `[VIEW]` years |
| Terminal FCF (FY2028E × (1+g)) | {fmt(terminal_fcf)} | `{fmt(cashflow['FY2028E']['fcf'])}` base FCF |
| PV of terminal | {fmt(pv_terminal)} | Gordon `{DCF_TERMINAL_GROWTH*100:.0f}%` / WACC `{DCF_WACC*100:.1f}%` |
| DCF equity value | {fmt(dcf_equity)} | PV(FCF) + terminal + 2026-06-30 net cash (R7.4); **not** the official method |
| Implied DCF PT / ADR | ${dcf_adr_pt:.2f} | vs official ${adr_pt:.2f}; FCF path is capex-heavy (R7.3) so DCF can sit below EBIT-multiple EV |

Heavy **capex** in the `[VIEW]` forecast (see [`cashflow.md`](cashflow.md)) compresses near-term FCF versus recurring EBIT; the DCF cross-check is therefore expected to land **below** the EV/EBIT official bridge unless terminal growth or WACC is retuned.

{markdown_table(["period", "recurring FCF (NT$bn)", "discount year", "WACC"], dcf_rows)}

## Checks — not additional official targets

{markdown_table(["check", "method", "PT / ADR (USD)"], check_rows)}

Bear and bull rows scale only the **EV/EBIT multiple** on the same `{OFFICIAL_EBIT_PERIOD}` operating income and net cash. DCF rows re-run the same FCF path with **±1.0pp WACC** around the {DCF_WACC*100:.1f}% base.

## Comparable-company framing

Peer foundry/semi manufacturing multiples were **not obtained** in this gate; do not treat the table as valuation anchors.

{markdown_table(["peer / frame", "metric sought", "status", "note"], comps_rows)}

Samsung and Intel filings mix foundry with large product businesses; GlobalFoundries and UMC would require a separate sourced comp pull (R10.8–R10.9).

## Gaps and what would move the official PT

- Sourced **peer EV/EBIT** for pure-play foundries (R10.8) to test the {OFFICIAL_EBIT_MULTIPLE:.0f}× `[VIEW]` vs the tape-implied {implied_ev_ebit_fy27:.1f}×.
- **Packaging economics** (R10.3) if CoWoS becomes a separately measurable profit pool.
- **IASB/TIFRS bridge** before splicing interim TIFRS into IASB valuation history (R10.13).
- **Street consensus** (R10.9) for external PT distribution — not used here.
- A change in `{OFFICIAL_EBIT_PERIOD}` recurring **operating income** path, **{OFFICIAL_EBIT_MULTIPLE:.0f}×** multiple, **net cash** roll-forward, **USD/NTD [VIEW]**, or **diluted share** path.
"""
    return content, summary


def main() -> None:
    segments = {**derived_segments(), **build_forecast_segments()}
    balances, income, cashflow = build_income_and_forecast(segments)
    checks = build_checks(segments, income, balances, cashflow)

    valuation_md, valuation_summary = build_valuation(income, balances, cashflow)

    outputs = {
        "segments.md": render_segments(segments, checks),
        "income.md": render_income(income, checks),
        "balance.md": render_balance(balances, income, checks),
        "cashflow.md": render_cashflow(balances, cashflow, checks),
        "valuation.md": valuation_md,
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
    print("\nValuation (ADR USD / common NT$)")
    print(
        f"Last close ${LAST_PRICE:.2f} ({LAST_PRICE_DATE}) | "
        f"Official PT ${valuation_summary['adr_pt']:.2f} / "
        f"NT${valuation_summary['common_pt_ntd']:.2f}"
    )
    print(
        f"Bear ${valuation_summary['bear_adr_pt']:.2f} | "
        f"Bull ${valuation_summary['bull_adr_pt']:.2f} | "
        f"DCF ${valuation_summary['dcf_adr_pt']:.2f} | "
        f"Tape residual ${valuation_summary['residual_adr']:.2f}"
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
