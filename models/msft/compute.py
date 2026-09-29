#!/usr/bin/env python3
"""Microsoft segment three-statement model and DCF.

Running this file rewrites segments.md, income.md, balance.md, cashflow.md,
and valuation.md in that order, then prints tie-out checks. USD millions
except per-share data and percentages.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
HIST_PERIODS = ["FY2024A", "FY2025A", "FY2026A"]
FORECAST_PERIODS = ["FY2027E", "FY2028E", "FY2029E"]
ALL_PERIODS = HIST_PERIODS + FORECAST_PERIODS
BALANCE_PERIODS = ["FY2025A", "FY2026A", *FORECAST_PERIODS]

S1 = "https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm"
S2_INCOME = "https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R2.htm"
S2_BALANCE = "https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R4.htm"
S2_CASHFLOW = "https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R6.htm"
S2_SEGMENTS = "https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R45.htm"
S5 = "https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4"
STOCK_LOOKUP = "https://www.microsoft.com/en-us/investor/stock-lookup"
REGISTER = "../../memory/msft/register.md"


HIST_SEGMENTS = {
    "FY2024A": {
        "pbp_revenue": 106_820.0,
        "pbp_cost": 19_611.0,
        "pbp_opex": 27_548.0,
        "pbp_oi": 59_661.0,
        "ic_revenue": 87_464.0,
        "ic_cost": 29_611.0,
        "ic_opex": 20_040.0,
        "ic_oi": 37_813.0,
        "mpc_revenue": 50_838.0,
        "mpc_cost": 24_892.0,
        "mpc_opex": 13_987.0,
        "mpc_oi": 11_959.0,
    },
    "FY2025A": {
        "pbp_revenue": 120_810.0,
        "pbp_cost": 22_422.0,
        "pbp_opex": 28_615.0,
        "pbp_oi": 69_773.0,
        "ic_revenue": 106_265.0,
        "ic_cost": 40_171.0,
        "ic_opex": 21_505.0,
        "ic_oi": 44_589.0,
        "mpc_revenue": 54_649.0,
        "mpc_cost": 25_238.0,
        "mpc_opex": 15_245.0,
        "mpc_oi": 14_166.0,
    },
    "FY2026A": {
        "pbp_revenue": 139_996.0,
        "pbp_cost": 25_017.0,
        "pbp_opex": 31_100.0,
        "pbp_oi": 83_879.0,
        "ic_revenue": 137_791.0,
        "ic_cost": 57_876.0,
        "ic_opex": 22_943.0,
        "ic_oi": 56_972.0,
        "mpc_revenue": 54_052.0,
        "mpc_cost": 23_481.0,
        "mpc_opex": 16_185.0,
        "mpc_oi": 14_386.0,
    },
}

HIST_INCOME = {
    "FY2024A": {
        "rd": 29_510.0,
        "sales_marketing": 24_456.0,
        "ga": 7_609.0,
        "other_income": -1_646.0,
        "pretax": 107_787.0,
        "tax": 19_651.0,
        "net_income": 88_136.0,
        "diluted_shares": 7_469.0,
        "diluted_eps": 11.80,
    },
    "FY2025A": {
        "rd": 32_488.0,
        "sales_marketing": 25_654.0,
        "ga": 7_223.0,
        "other_income": -4_901.0,
        "pretax": 123_627.0,
        "tax": 21_795.0,
        "net_income": 101_832.0,
        "diluted_shares": 7_465.0,
        "diluted_eps": 13.64,
    },
    "FY2026A": {
        "rd": 35_562.0,
        "sales_marketing": 26_710.0,
        "ga": 7_956.0,
        "other_income": 10_697.0,
        "pretax": 165_934.0,
        "tax": 32_185.0,
        "net_income": 133_749.0,
        "diluted_shares": 7_453.0,
        "diluted_eps": 17.95,
    },
}

HIST_BALANCE = {
    "FY2025A": {
        "cash": 30_242.0,
        "short_investments": 64_323.0,
        "ar": 69_905.0,
        "inventory": 938.0,
        "other_operating_assets": 25_723.0 + 24_823.0 + 40_565.0,
        "ppe": 204_966.0,
        "equity_investments": 15_405.0,
        "goodwill_intangibles": 119_509.0 + 22_604.0,
        "total_assets": 619_003.0,
        "ap": 27_724.0,
        "debt": 2_999.0 + 40_152.0,
        "unearned_revenue": 64_555.0 + 2_710.0,
        "other_operating_liabilities": (
            13_709.0
            + 7_211.0
            + 25_020.0
            + 25_986.0
            + 2_835.0
            + 17_437.0
            + 45_186.0
        ),
        "total_liabilities": 275_524.0,
        "equity": 343_479.0,
        "shares_out": 7_434.0,
    },
    "FY2026A": {
        "cash": 20_935.0,
        "short_investments": 55_908.0,
        "ar": 80_876.0,
        "inventory": 1_397.0,
        "other_operating_assets": 48_594.0 + 24_177.0 + 38_805.0,
        "ppe": 313_076.0,
        "equity_investments": 36_348.0,
        "goodwill_intangibles": 119_651.0 + 18_609.0,
        "total_assets": 758_376.0,
        "ap": 42_416.0,
        "debt": 9_227.0 + 31_067.0,
        "unearned_revenue": 72_965.0 + 2_747.0,
        "other_operating_liabilities": (
            14_945.0
            + 2_534.0
            + 26_738.0
            + 28_647.0
            + 3_054.0
            + 16_532.0
            + 65_117.0
        ),
        "total_liabilities": 315_989.0,
        "equity": 442_387.0,
        "shares_out": 7_427.0,
    },
}

HIST_CASHFLOW = {
    "FY2024A": {
        "net_income": 88_136.0,
        "da_other": 20_958.0,
        "sbc": 10_734.0,
        "ocf": 118_548.0,
        "capex": 44_477.0,
        "net_investing": -96_970.0,
        "buybacks": 17_254.0,
        "dividends": 21_771.0,
        "debt_repayment": 29_070.0,
        "net_financing": -37_757.0,
        "cash_change": -16_389.0,
        "ending_cash": 18_315.0,
    },
    "FY2025A": {
        "net_income": 101_832.0,
        "da_other": 29_433.0,
        "sbc": 11_974.0,
        "ocf": 136_162.0,
        "capex": 64_551.0,
        "net_investing": -72_599.0,
        "buybacks": 18_420.0,
        "dividends": 24_082.0,
        "debt_repayment": 3_216.0,
        "net_financing": -51_699.0,
        "cash_change": 11_927.0,
        "ending_cash": 30_242.0,
    },
    "FY2026A": {
        "net_income": 133_749.0,
        "da_other": 38_534.0,
        "sbc": 12_405.0,
        "ocf": 182_935.0,
        "capex": 115_948.0,
        "net_investing": -139_500.0,
        "buybacks": 22_271.0,
        "dividends": 26_445.0,
        "debt_repayment": 3_000.0,
        "net_financing": -52_546.0,
        "cash_change": -9_307.0,
        "ending_cash": 20_935.0,
    },
}

ASSUMPTIONS = {
    "FY2027E": {
        "pbp_growth": 0.13,
        "ic_growth": 0.30,
        "mpc_growth": -0.08,
        "pbp_gm": 0.817,
        "ic_gm": 0.560,
        "mpc_gm": 0.550,
        "pbp_om": 0.595,
        "ic_om": 0.410,
        "mpc_om": 0.220,
        "other_income": -400.0,
        "tax_rate": 0.20,
        "capex": 140_000.0,
        "da_rate": 0.13,
        "sbc_percent_revenue": 0.037,
        "dividends": 30_000.0,
        "buybacks": 20_000.0,
        "debt_repayment": 3_000.0,
    },
    "FY2028E": {
        "pbp_growth": 0.14,
        "ic_growth": 0.24,
        "mpc_growth": 0.01,
        "pbp_gm": 0.820,
        "ic_gm": 0.550,
        "mpc_gm": 0.555,
        "pbp_om": 0.600,
        "ic_om": 0.410,
        "mpc_om": 0.230,
        "other_income": -400.0,
        "tax_rate": 0.20,
        "capex": 155_000.0,
        "da_rate": 0.13,
        "sbc_percent_revenue": 0.036,
        "dividends": 33_000.0,
        "buybacks": 20_000.0,
        "debt_repayment": 3_000.0,
    },
    "FY2029E": {
        "pbp_growth": 0.13,
        "ic_growth": 0.20,
        "mpc_growth": 0.03,
        "pbp_gm": 0.823,
        "ic_gm": 0.560,
        "mpc_gm": 0.560,
        "pbp_om": 0.605,
        "ic_om": 0.420,
        "mpc_om": 0.240,
        "other_income": -400.0,
        "tax_rate": 0.20,
        "capex": 150_000.0,
        "da_rate": 0.13,
        "sbc_percent_revenue": 0.035,
        "dividends": 36_000.0,
        "buybacks": 20_000.0,
        "debt_repayment": 3_000.0,
    },
}

FORECAST_DILUTED_SHARES = 7_453.0
FORECAST_PERIOD_END_SHARES = 7_427.0
VALUATION_DATE = date(2026, 9, 29)
LAST_PRICE_DATE = date(2026, 9, 28)
LAST_PRICE = 509.22
WACC = 0.085
TERMINAL_GROWTH = 0.040


def fmt(value: Any, decimals: int = 0) -> str:
    if value is None:
        return "not obtained"
    if isinstance(value, str):
        return value
    if abs(value) < 0.0000001:
        return "—"
    rendered = f"{abs(value):,.{decimals}f}"
    return f"({rendered})" if value < 0 else rendered


def pct(value: float, decimals: int = 1) -> str:
    return f"{value * 100:.{decimals}f}%"


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    top = "| " + " | ".join(headers) + " |"
    separator = "|" + "|".join("---" for _ in headers) + "|"
    body = ["| " + " | ".join(str(cell) for cell in row) + " |" for row in rows]
    return "\n".join([top, separator, *body])


def enrich_segment(raw: dict[str, float]) -> dict[str, float]:
    output = dict(raw)
    for segment in ("pbp", "ic", "mpc"):
        revenue = output[f"{segment}_revenue"]
        cost = output[f"{segment}_cost"]
        gp = revenue - cost
        output[f"{segment}_gp"] = gp
        output[f"{segment}_gm"] = gp / revenue
        output[f"{segment}_om"] = output[f"{segment}_oi"] / revenue
    output["revenue"] = sum(output[f"{s}_revenue"] for s in ("pbp", "ic", "mpc"))
    output["cost"] = sum(output[f"{s}_cost"] for s in ("pbp", "ic", "mpc"))
    output["gp"] = output["revenue"] - output["cost"]
    output["opex"] = sum(output[f"{s}_opex"] for s in ("pbp", "ic", "mpc"))
    output["oi"] = sum(output[f"{s}_oi"] for s in ("pbp", "ic", "mpc"))
    output["gm"] = output["gp"] / output["revenue"]
    output["om"] = output["oi"] / output["revenue"]
    return output


def build_segments() -> dict[str, dict[str, float]]:
    segments = {p: enrich_segment(raw) for p, raw in HIST_SEGMENTS.items()}
    previous = segments["FY2026A"]
    for period in FORECAST_PERIODS:
        assumption = ASSUMPTIONS[period]
        raw: dict[str, float] = {}
        for segment in ("pbp", "ic", "mpc"):
            revenue = previous[f"{segment}_revenue"] * (
                1.0 + assumption[f"{segment}_growth"]
            )
            gp = revenue * assumption[f"{segment}_gm"]
            oi = revenue * assumption[f"{segment}_om"]
            raw[f"{segment}_revenue"] = revenue
            raw[f"{segment}_cost"] = revenue - gp
            raw[f"{segment}_opex"] = gp - oi
            raw[f"{segment}_oi"] = oi
        segments[period] = enrich_segment(raw)
        previous = segments[period]
    return segments


def build_income(
    segments: dict[str, dict[str, float]]
) -> dict[str, dict[str, float]]:
    income: dict[str, dict[str, float]] = {}
    for period in HIST_PERIODS:
        segment = segments[period]
        raw = HIST_INCOME[period]
        income[period] = {
            "revenue": segment["revenue"],
            "cost": segment["cost"],
            "gp": segment["gp"],
            "rd": raw["rd"],
            "sales_marketing": raw["sales_marketing"],
            "ga": raw["ga"],
            "opex": segment["opex"],
            "oi": segment["oi"],
            "other_income": raw["other_income"],
            "pretax": raw["pretax"],
            "tax": raw["tax"],
            "tax_rate": raw["tax"] / raw["pretax"],
            "net_income": raw["net_income"],
            "diluted_shares": raw["diluted_shares"],
            "diluted_eps": raw["diluted_eps"],
        }
    for period in FORECAST_PERIODS:
        segment = segments[period]
        assumption = ASSUMPTIONS[period]
        pretax = segment["oi"] + assumption["other_income"]
        tax = pretax * assumption["tax_rate"]
        net_income = pretax - tax
        income[period] = {
            "revenue": segment["revenue"],
            "cost": segment["cost"],
            "gp": segment["gp"],
            "rd": None,
            "sales_marketing": None,
            "ga": None,
            "opex": segment["opex"],
            "oi": segment["oi"],
            "other_income": assumption["other_income"],
            "pretax": pretax,
            "tax": tax,
            "tax_rate": assumption["tax_rate"],
            "net_income": net_income,
            "diluted_shares": FORECAST_DILUTED_SHARES,
            "diluted_eps": net_income / FORECAST_DILUTED_SHARES,
        }
    return income


def operating_capital(balance: dict[str, float]) -> float:
    return (
        balance["ar"]
        + balance["inventory"]
        + balance["other_operating_assets"]
        - balance["ap"]
        - balance["unearned_revenue"]
        - balance["other_operating_liabilities"]
    )


def build_balance_and_cashflow(
    segments: dict[str, dict[str, float]],
    income: dict[str, dict[str, float]],
) -> tuple[
    dict[str, dict[str, float]],
    dict[str, dict[str, float]],
    dict[str, float],
]:
    balances = {p: dict(raw) for p, raw in HIST_BALANCE.items()}
    cashflow = {
        p: {**raw, "fcf": raw["ocf"] - raw["capex"]}
        for p, raw in HIST_CASHFLOW.items()
    }

    fy26 = balances["FY2026A"]
    fy26_segment = segments["FY2026A"]
    ar_days = fy26["ar"] / fy26_segment["revenue"] * 365.0
    inventory_days = fy26["inventory"] / fy26_segment["cost"] * 365.0
    ap_days = fy26["ap"] / fy26_segment["cost"] * 365.0
    unearned_ratio = fy26["unearned_revenue"] / fy26_segment["revenue"]
    other_asset_ratio = fy26["other_operating_assets"] / fy26_segment["revenue"]
    other_liability_ratio = (
        fy26["other_operating_liabilities"] / fy26_segment["revenue"]
    )
    working_capital = {
        "ar_days": ar_days,
        "inventory_days": inventory_days,
        "ap_days": ap_days,
        "unearned_ratio": unearned_ratio,
        "other_asset_ratio": other_asset_ratio,
        "other_liability_ratio": other_liability_ratio,
    }

    previous = balances["FY2026A"]
    for period in FORECAST_PERIODS:
        segment = segments[period]
        assumption = ASSUMPTIONS[period]
        revenue = segment["revenue"]
        cost = segment["cost"]

        ar = revenue * ar_days / 365.0
        inventory = cost * inventory_days / 365.0
        ap = cost * ap_days / 365.0
        unearned = revenue * unearned_ratio
        other_operating_assets = revenue * other_asset_ratio
        other_operating_liabilities = revenue * other_liability_ratio

        da_rate = assumption["da_rate"]
        da = (
            da_rate * (previous["ppe"] + assumption["capex"] / 2.0)
            / (1.0 + da_rate / 2.0)
        )
        ppe = previous["ppe"] + assumption["capex"] - da
        sbc = revenue * assumption["sbc_percent_revenue"]

        provisional = {
            "ar": ar,
            "inventory": inventory,
            "other_operating_assets": other_operating_assets,
            "ap": ap,
            "unearned_revenue": unearned,
            "other_operating_liabilities": other_operating_liabilities,
        }
        delta_operating_capital = (
            operating_capital(provisional) - operating_capital(previous)
        )
        ocf = income[period]["net_income"] + da + sbc - delta_operating_capital
        fcf = ocf - assumption["capex"]
        financing_after_fcf = -(
            assumption["debt_repayment"]
            + assumption["dividends"]
            + assumption["buybacks"]
        )
        cash_change = fcf + financing_after_fcf
        cash = previous["cash"] + cash_change
        debt = previous["debt"] - assumption["debt_repayment"]
        equity = (
            previous["equity"]
            + income[period]["net_income"]
            + sbc
            - assumption["dividends"]
            - assumption["buybacks"]
        )
        total_assets = (
            cash
            + previous["short_investments"]
            + ar
            + inventory
            + other_operating_assets
            + ppe
            + previous["equity_investments"]
            + previous["goodwill_intangibles"]
        )
        total_liabilities = ap + debt + unearned + other_operating_liabilities
        balances[period] = {
            "cash": cash,
            "short_investments": previous["short_investments"],
            "ar": ar,
            "inventory": inventory,
            "other_operating_assets": other_operating_assets,
            "ppe": ppe,
            "equity_investments": previous["equity_investments"],
            "goodwill_intangibles": previous["goodwill_intangibles"],
            "total_assets": total_assets,
            "ap": ap,
            "debt": debt,
            "unearned_revenue": unearned,
            "other_operating_liabilities": other_operating_liabilities,
            "total_liabilities": total_liabilities,
            "equity": equity,
            "shares_out": FORECAST_PERIOD_END_SHARES,
        }
        cashflow[period] = {
            "net_income": income[period]["net_income"],
            "da_other": da,
            "sbc": sbc,
            "delta_operating_capital": delta_operating_capital,
            "ocf": ocf,
            "capex": assumption["capex"],
            "fcf": fcf,
            "net_investing": None,
            "buybacks": assumption["buybacks"],
            "dividends": assumption["dividends"],
            "debt_repayment": assumption["debt_repayment"],
            "net_financing": financing_after_fcf,
            "cash_change": cash_change,
            "ending_cash": cash,
        }
        previous = balances[period]

    return balances, cashflow, working_capital


def build_checks(
    segments: dict[str, dict[str, float]],
    income: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
    cashflow: dict[str, dict[str, float]],
) -> list[tuple[str, bool, float]]:
    tolerance = 0.02
    checks: list[tuple[str, bool, float]] = []
    expected = {
        "FY2024A": (245_122.0, 171_008.0, 109_433.0, 88_136.0),
        "FY2025A": (281_724.0, 193_893.0, 128_528.0, 101_832.0),
        "FY2026A": (331_839.0, 225_465.0, 155_237.0, 133_749.0),
    }
    for period in ALL_PERIODS:
        segment = segments[period]
        segment_revenue = sum(
            segment[f"{s}_revenue"] for s in ("pbp", "ic", "mpc")
        )
        segment_oi = sum(segment[f"{s}_oi"] for s in ("pbp", "ic", "mpc"))
        checks.append(
            (
                f"{period}: segment revenue = company revenue",
                abs(segment_revenue - income[period]["revenue"]) < tolerance,
                segment_revenue - income[period]["revenue"],
            )
        )
        checks.append(
            (
                f"{period}: segment operating income = company operating income",
                abs(segment_oi - income[period]["oi"]) < tolerance,
                segment_oi - income[period]["oi"],
            )
        )
        if period in HIST_PERIODS:
            actual = (
                income[period]["revenue"],
                income[period]["gp"],
                income[period]["oi"],
                income[period]["net_income"],
            )
            difference = max(
                abs(a - b) for a, b in zip(actual, expected[period])
            )
            checks.append(
                (
                    f"{period}: historical income statement matches filing",
                    difference < tolerance,
                    difference,
                )
            )

    fy27_revenue_growth = (
        income["FY2027E"]["revenue"] / income["FY2026A"]["revenue"] - 1.0
    )
    fy27_oi_growth = income["FY2027E"]["oi"] / income["FY2026A"]["oi"] - 1.0
    fy27_margin_change = (
        income["FY2027E"]["oi"] / income["FY2027E"]["revenue"]
        - income["FY2026A"]["oi"] / income["FY2026A"]["revenue"]
    )
    checks.extend(
        [
            (
                "FY2027E: revenue growth meets management double-digit bar",
                fy27_revenue_growth >= 0.10,
                fy27_revenue_growth,
            ),
            (
                "FY2027E: operating-income growth meets management double-digit bar",
                fy27_oi_growth >= 0.10,
                fy27_oi_growth,
            ),
            (
                "FY2027E: operating-margin decline is less than one point",
                -0.01 < fy27_margin_change <= 0.0,
                fy27_margin_change,
            ),
            (
                "FY2027E: cash capex grows year over year",
                cashflow["FY2027E"]["capex"] > cashflow["FY2026A"]["capex"],
                cashflow["FY2027E"]["capex"] - cashflow["FY2026A"]["capex"],
            ),
            (
                "FY2027E: free cash flow remains positive",
                cashflow["FY2027E"]["fcf"] > 0.0,
                cashflow["FY2027E"]["fcf"],
            ),
        ]
    )

    previous = balances["FY2026A"]
    for period in FORECAST_PERIODS:
        balance = balances[period]
        cf = cashflow[period]
        difference = balance["total_assets"] - (
            balance["total_liabilities"] + balance["equity"]
        )
        checks.append(
            (
                f"{period}: balance sheet balances",
                abs(difference) < tolerance,
                difference,
            )
        )
        checks.append(
            (
                f"{period}: cash-flow ending cash = balance-sheet cash",
                abs(cf["ending_cash"] - balance["cash"]) < tolerance,
                cf["ending_cash"] - balance["cash"],
            )
        )
        checks.append(
            (
                f"{period}: cash-flow change = balance-sheet cash change",
                abs(cf["cash_change"] - (balance["cash"] - previous["cash"]))
                < tolerance,
                cf["cash_change"] - (balance["cash"] - previous["cash"]),
            )
        )
        previous = balance
    return checks


def render_segments(
    segments: dict[str, dict[str, float]],
    checks: list[tuple[str, bool, float]],
) -> str:
    rows: list[list[str]] = []
    labels = (
        ("PBP revenue", "pbp_revenue"),
        ("PBP gross profit", "pbp_gp"),
        ("PBP operating expense", "pbp_opex"),
        ("PBP operating income", "pbp_oi"),
        ("Intelligent Cloud revenue", "ic_revenue"),
        ("Intelligent Cloud gross profit", "ic_gp"),
        ("Intelligent Cloud operating expense", "ic_opex"),
        ("Intelligent Cloud operating income", "ic_oi"),
        ("MPC revenue", "mpc_revenue"),
        ("MPC gross profit", "mpc_gp"),
        ("MPC operating expense", "mpc_opex"),
        ("MPC operating income", "mpc_oi"),
        ("Company revenue", "revenue"),
        ("Company gross profit", "gp"),
        ("Company operating expense", "opex"),
        ("Company operating income", "oi"),
    )
    for label, key in labels:
        rows.append([label, *[fmt(segments[p][key]) for p in ALL_PERIODS]])

    margin_rows = []
    for period in ALL_PERIODS:
        segment = segments[period]
        margin_rows.append(
            [
                period,
                pct(segment["pbp_gm"]),
                pct(segment["pbp_om"]),
                pct(segment["ic_gm"]),
                pct(segment["ic_om"]),
                pct(segment["mpc_gm"]),
                pct(segment["mpc_om"]),
                pct(segment["gm"]),
                pct(segment["om"]),
            ]
        )
    check_rows = [
        [name, "OK" if passed else "ERROR", fmt(difference, 4)]
        for name, passed, difference in checks
        if "segment revenue" in name or "segment operating income" in name
    ]
    return f"""# Microsoft segment model

Generated by `compute.py`; do not hand-edit. USD millions except percentages.

The consolidated income statement is built from the three reported segments. Microsoft Cloud and product-revenue disclosures are overlapping KPIs and are not added as extra segments.

## Revenue, gross profit, operating expense, and operating income

{markdown_table(["line", *ALL_PERIODS], rows)}

Historical source: [register R2]({REGISTER}) and the [FY2026 10-K segment table]({S2_SEGMENTS}). Historical gross profit is `[DEDUCTED]` as segment revenue less disclosed segment cost of revenue. Forecast revenue, gross margin, and operating margin assumptions are `[VIEW]`s in [`inputs.md`](inputs.md); forecast cost and operating expense are computed residuals, not plugs to consolidated totals.

## Segment margins

{markdown_table(["period", "PBP GM", "PBP OM", "IC GM", "IC OM", "MPC GM", "MPC OM", "Company GM", "Company OM"], margin_rows)}

IC gross margin falls before recovering because the model embeds the filed mix/infrastructure pressure and then utilization/efficiency. PBP carries Copilot usage cost before modest leverage. MPC contracts in FY2027 before Search/mix and expense recovery. No separate unreported AI revenue or profit wedge is added.

## Tie checks

{markdown_table(["check", "status", "difference"], check_rows)}
"""


def render_income(
    income: dict[str, dict[str, float]],
    checks: list[tuple[str, bool, float]],
) -> str:
    rows = []
    labels = (
        ("Revenue", "revenue"),
        ("Cost of revenue", "cost"),
        ("Gross profit", "gp"),
        ("Research and development", "rd"),
        ("Sales and marketing", "sales_marketing"),
        ("General and administrative", "ga"),
        ("Total operating expense", "opex"),
        ("Operating income", "oi"),
        ("Other income / (expense), net", "other_income"),
        ("Income before tax", "pretax"),
        ("Tax provision", "tax"),
        ("Net income", "net_income"),
        ("Diluted weighted-average shares", "diluted_shares"),
        ("Diluted EPS", "diluted_eps"),
    )
    for label, key in labels:
        decimals = 2 if key == "diluted_eps" else 0
        rows.append([label, *[fmt(income[p][key], decimals) for p in ALL_PERIODS]])
    check_rows = [
        [name, "OK" if passed else "ERROR", fmt(difference, 4)]
        for name, passed, difference in checks
        if "historical income statement" in name
        or "management double-digit" in name
        or "operating-margin decline" in name
    ]
    return f"""# Microsoft income statement

Generated by `compute.py`; do not hand-edit. USD millions except per-share data.

Revenue, gross profit, operating expense, and operating income sum the three segment lines in [`segments.md`](segments.md); there is no consolidated operating plug.

{markdown_table(["line", *ALL_PERIODS], rows)}

Historical source: [FY2026 10-K income statement]({S2_INCOME}). R&D, sales and marketing, and G&A are `not obtained` individually for forecast years because segment opex—not corporate function—is the model architecture. Forecast other expense is `[VIEW]` $400 million annually and does not forecast OpenAI marks. Forecast tax is the approximately 20% management FY2027 bar held flat.

## Filing and guidance checks

{markdown_table(["check", "status", "difference / rate"], check_rows)}
"""


def render_balance(
    balances: dict[str, dict[str, float]],
    checks: list[tuple[str, bool, float]],
) -> str:
    rows = []
    labels = (
        ("Cash and cash equivalents", "cash"),
        ("Short-term investments", "short_investments"),
        ("Accounts receivable", "ar"),
        ("Inventory", "inventory"),
        ("Other operating assets", "other_operating_assets"),
        ("PP&E, net", "ppe"),
        ("Equity and other investments", "equity_investments"),
        ("Goodwill and intangible assets", "goodwill_intangibles"),
        ("Total assets", "total_assets"),
        ("Accounts payable", "ap"),
        ("Debt", "debt"),
        ("Unearned revenue", "unearned_revenue"),
        ("Other operating liabilities", "other_operating_liabilities"),
        ("Total liabilities", "total_liabilities"),
        ("Stockholders' equity", "equity"),
        ("Total liabilities and equity", "liabilities_and_equity"),
        ("Period-end shares", "shares_out"),
    )
    for label, key in labels:
        values = []
        for period in BALANCE_PERIODS:
            value = (
                balances[period]["total_liabilities"] + balances[period]["equity"]
                if key == "liabilities_and_equity"
                else balances[period][key]
            )
            values.append(fmt(value))
        rows.append([label, *values])
    check_rows = [
        [name, "OK" if passed else "ERROR", fmt(difference, 2)]
        for name, passed, difference in checks
        if "balance sheet balances" in name
    ]
    return f"""# Microsoft balance sheet

Generated by `compute.py`; do not hand-edit. USD millions except shares.

{markdown_table(["line", *BALANCE_PERIODS], rows)}

Historical source: [FY2026 10-K balance sheet]({S2_BALANCE}). “Other operating assets” aggregates other current assets, operating-lease ROU assets, and other long-term assets. “Other operating liabilities” aggregates compensation, tax, lease, deferred-tax, and other current/long-term liabilities.

Forecast receivable/inventory/payable days and other operating-asset/liability ratios hold the FY2026 filing relationships. PP&E rolls as beginning PP&E plus cash capex less D&A. Equity rolls with net income plus SBC less dividends and repurchases. Every corresponding working-capital movement is included in [`cashflow.md`](cashflow.md), so cash is not a balance-sheet plug.

## Tie checks

{markdown_table(["check", "status", "difference"], check_rows)}
"""


def render_cashflow(
    cashflow: dict[str, dict[str, float]],
    working_capital: dict[str, float],
    checks: list[tuple[str, bool, float]],
) -> str:
    rows = []
    labels = (
        ("Net income", "net_income"),
        ("D&A and other", "da_other"),
        ("Stock-based compensation", "sbc"),
        ("Cash effect of operating-capital change", "delta_operating_capital"),
        ("Operating cash flow", "ocf"),
        ("Additions to PP&E", "capex"),
        ("Free cash flow", "fcf"),
        ("Reported net investing cash flow", "net_investing"),
        ("Common-stock repurchases", "buybacks"),
        ("Cash dividends", "dividends"),
        ("Debt repayments", "debt_repayment"),
        ("Reported / modeled financing after FCF", "net_financing"),
        ("Change in cash", "cash_change"),
        ("Ending cash", "ending_cash"),
    )
    for label, key in labels:
        values = []
        for period in ALL_PERIODS:
            value = cashflow[period].get(key)
            if key in {
                "delta_operating_capital",
                "capex",
                "buybacks",
                "dividends",
                "debt_repayment",
            } and value is not None:
                value = -value
            values.append(fmt(value))
        rows.append([label, *values])
    check_rows = [
        [name, "OK" if passed else "ERROR", fmt(difference, 2)]
        for name, passed, difference in checks
        if "cash-flow" in name
        or "cash capex" in name
        or "free cash flow remains" in name
    ]
    return f"""# Microsoft cash-flow statement

Generated by `compute.py`; do not hand-edit. USD millions.

{markdown_table(["line", *ALL_PERIODS], rows)}

Historical source: [FY2026 10-K cash flow]({S2_CASHFLOW}). Historical free cash flow is `[DEDUCTED]` as operating cash flow less additions to PP&E.

Forecast OCF equals `net income + D&A + SBC − change in operating capital`. Operating capital is `AR + inventory + other operating assets − AP − unearned revenue − other operating liabilities`. FY2026 seed relationships held in the forecast are: receivable days `{working_capital["ar_days"]:.2f}`, inventory days `{working_capital["inventory_days"]:.2f}`, payable days `{working_capital["ap_days"]:.2f}`, unearned revenue `{pct(working_capital["unearned_ratio"])}` of revenue, other operating assets `{pct(working_capital["other_asset_ratio"])}` of revenue, and other operating liabilities `{pct(working_capital["other_liability_ratio"])}` of revenue.

Forecast D&A uses 13% of average net PP&E and therefore reflects the PP&E roll mechanically. Forecast free cash flow remains OCF less cash additions to PP&E; dividends, repurchases, and debt repayment are financing uses after FCF.

## Cash and management-bar checks

{markdown_table(["check", "status", "difference / amount"], check_rows)}
"""


def dcf_value(
    fcff: dict[str, float],
    net_cash: float,
    shares: float,
    wacc: float,
    terminal_growth: float,
) -> tuple[float, float, float, dict[str, float]]:
    fiscal_dates = {
        "FY2027E": date(2027, 6, 30),
        "FY2028E": date(2028, 6, 30),
        "FY2029E": date(2029, 6, 30),
    }
    discount_years = {
        p: (fiscal_dates[p] - VALUATION_DATE).days / 365.0
        for p in FORECAST_PERIODS
    }
    pv_explicit = sum(
        fcff[p] / ((1.0 + wacc) ** discount_years[p])
        for p in FORECAST_PERIODS
    )
    terminal_value = (
        fcff["FY2029E"] * (1.0 + terminal_growth) / (wacc - terminal_growth)
    )
    pv_terminal = terminal_value / (
        (1.0 + wacc) ** discount_years["FY2029E"]
    )
    enterprise_value = pv_explicit + pv_terminal
    equity_value = enterprise_value + net_cash
    per_share = equity_value / shares
    return per_share, enterprise_value, equity_value, {
        "pv_explicit": pv_explicit,
        "terminal_value": terminal_value,
        "pv_terminal": pv_terminal,
        **{f"years_{p}": discount_years[p] for p in FORECAST_PERIODS},
    }


def render_valuation(
    segments: dict[str, dict[str, float]],
    income: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
    cashflow: dict[str, dict[str, float]],
) -> tuple[str, dict[str, float]]:
    fcff: dict[str, float] = {}
    fcff_rows = []
    for period in FORECAST_PERIODS:
        assumption = ASSUMPTIONS[period]
        nopat = income[period]["oi"] * (1.0 - assumption["tax_rate"])
        delta_operating_capital = cashflow[period]["delta_operating_capital"]
        fcff[period] = (
            nopat
            + cashflow[period]["da_other"]
            - cashflow[period]["capex"]
            - delta_operating_capital
        )
        fcff_rows.append(
            [
                period,
                fmt(income[period]["oi"], 1),
                fmt(nopat, 1),
                fmt(cashflow[period]["da_other"], 1),
                fmt(-cashflow[period]["capex"], 1),
                fmt(-delta_operating_capital, 1),
                fmt(fcff[period], 1),
            ]
        )

    base = balances["FY2026A"]
    net_cash = base["cash"] + base["short_investments"] - base["debt"]
    pt, enterprise_value, equity_value, dcf = dcf_value(
        fcff, net_cash, FORECAST_PERIOD_END_SHARES, WACC, TERMINAL_GROWTH
    )

    market_cap = LAST_PRICE * FORECAST_PERIOD_END_SHARES
    market_ev = market_cap - net_cash
    terminal_discount_factor = (
        (1.0 + WACC) ** dcf["years_FY2029E"]
    )
    market_terminal_value = (
        market_ev - dcf["pv_explicit"]
    ) * terminal_discount_factor
    implied_terminal_growth = (
        market_terminal_value * WACC - fcff["FY2029E"]
    ) / (market_terminal_value + fcff["FY2029E"])
    residual = pt - LAST_PRICE

    setup_rows = [
        ["Valuation as-of", VALUATION_DATE.isoformat()],
        ["Last close", f"${LAST_PRICE:.2f} on {LAST_PRICE_DATE.isoformat()}"],
        ["Last-price source", f"[Microsoft IR stock lookup]({STOCK_LOOKUP})"],
        ["Method", "Enterprise DCF; three explicit forecast years + terminal value"],
        ["WACC", pct(WACC)],
        ["Terminal growth", pct(TERMINAL_GROWTH)],
        ["PT denominator", f"{FORECAST_PERIOD_END_SHARES:,.0f}m FY2026 shares outstanding"],
    ]
    bridge_rows = [
        ["PV FY2027E–FY2029E FCFF", "Explicit period", fmt(dcf["pv_explicit"], 1)],
        ["FY2029E terminal value", "FY2029E FCFF × (1+g) ÷ (WACC−g)", fmt(dcf["terminal_value"], 1)],
        ["PV terminal value", "Discounted to valuation date", fmt(dcf["pv_terminal"], 1)],
        ["Enterprise value", "Explicit PV + terminal PV", fmt(enterprise_value, 1)],
        ["FY2026 net cash", "Cash + short investments − debt", fmt(net_cash, 1)],
        ["Equity value", "Enterprise value + net cash", fmt(equity_value, 1)],
        ["Shares outstanding (m)", "FY2026 filing", fmt(FORECAST_PERIOD_END_SHARES, 1)],
        ["Official 12-month price target / share", "Equity value ÷ shares", f"${pt:.2f}"],
    ]
    tape_rows = [
        ["Market capitalization", "Last close × FY2026 shares", fmt(market_cap, 1)],
        ["Market enterprise value", "Market cap − FY2026 net cash", fmt(market_ev, 1)],
        ["EV / FY2026A revenue", "Market EV ÷ revenue", f"{market_ev / income['FY2026A']['revenue']:.1f}x"],
        ["EV / FY2026A operating income", "Market EV ÷ operating income", f"{market_ev / income['FY2026A']['oi']:.1f}x"],
        ["Price / FY2026A diluted EPS", "Last close ÷ diluted EPS", f"{LAST_PRICE / income['FY2026A']['diluted_eps']:.1f}x"],
        ["EV / FY2027E revenue", "Market EV ÷ modeled revenue", f"{market_ev / income['FY2027E']['revenue']:.1f}x"],
        ["EV / FY2027E operating income", "Market EV ÷ modeled operating income", f"{market_ev / income['FY2027E']['oi']:.1f}x"],
        ["Market-implied terminal growth", "Solve DCF to last close, hold explicit FCFF/WACC", pct(implied_terminal_growth)],
    ]
    milestones = []
    for period in FORECAST_PERIODS:
        milestones.append(
            [
                period,
                fmt(segments[period]["pbp_revenue"], 1),
                fmt(segments[period]["ic_revenue"], 1),
                fmt(segments[period]["mpc_revenue"], 1),
                fmt(income[period]["oi"], 1),
                pct(income[period]["oi"] / income[period]["revenue"]),
                fmt(cashflow[period]["capex"], 1),
                fmt(cashflow[period]["fcf"], 1),
            ]
        )

    sensitivity_rows = []
    for wacc in (0.080, 0.085, 0.090):
        row = [pct(wacc)]
        for terminal_growth in (0.035, 0.040, 0.045):
            value, _, _, _ = dcf_value(
                fcff,
                net_cash,
                FORECAST_PERIOD_END_SHARES,
                wacc,
                terminal_growth,
            )
            row.append(f"${value:.2f}")
        sensitivity_rows.append(row)

    terminal_share = dcf["pv_terminal"] / enterprise_value
    content = f"""# Microsoft valuation

The official DCF values the filed three-segment business without a separate unreported “AI” wedge. The operating statement is that Azure/AI and Microsoft 365 monetization sustain double-digit company growth while FY2027 operating margin declines by less than one point and cash capex remains elevated.

## Official method and as-of

{markdown_table(["item", "value"], setup_rows)}

## Unlevered free cash flow

{markdown_table(["period", "Operating income", "NOPAT", "D&A", "Cash capex", "Cash effect of Δ operating capital", "FCFF"], fcff_rows)}

FCFF is `NOPAT + D&A − cash capex − change in operating capital`. SBC is not added back in valuation because it is treated as an economic cost. No OpenAI mark is forecast.

## Official price-target bridge

{markdown_table(["item", "basis", "$m except per share"], bridge_rows)}

**Official price-target line:** **${pt:.2f} per share.** This is the DCF output from the operating assumptions in [`inputs.md`](inputs.md); it is not fitted to the last close.

The target requires the following segment and cash milestones:

{markdown_table(["period", "PBP revenue", "IC revenue", "MPC revenue", "Operating income", "Operating margin", "Cash capex", "Equity FCF"], milestones)}

“Equity FCF” in the milestone table is consolidated OCF less cash capex from [`cashflow.md`](cashflow.md); the DCF uses the unlevered FCFF table above.

## What the last close already requires

{markdown_table(["item", "formula", "value"], tape_rows)}

**[DEDUCTED] Signed target spread:** `${pt:.2f} − ${LAST_PRICE:.2f} = ${residual:.2f}` per share. The market-implied terminal growth solves only one variable while holding the explicit operating path and 8.5% WACC fixed; it is not a claim that the market literally uses that terminal rate.

## Sensitivity — diagnostics, not additional official targets

{markdown_table(["WACC / terminal growth", "3.5%", "4.0%", "4.5%"], sensitivity_rows)}

The terminal value is {pct(terminal_share)} of enterprise value. That concentration makes IC growth, steady-state AI/cloud margins, capex normalization, and the discount rate the primary valuation risks.

## What would move the official value

- Segment growth or margin that changes consolidated operating income and FCFF.
- Cash capex, useful-life economics, or working-capital conversion.
- WACC or terminal growth.
- A sourced standalone AI/Copilot P&L that changes—not double counts—the reported segment cash flows.
"""
    return content, {
        "pt": pt,
        "enterprise_value": enterprise_value,
        "equity_value": equity_value,
        "net_cash": net_cash,
        "market_ev": market_ev,
        "implied_terminal_growth": implied_terminal_growth,
        "residual": residual,
        "terminal_share": terminal_share,
    }


def main() -> None:
    segments = build_segments()
    income = build_income(segments)
    balances, cashflow, working_capital = build_balance_and_cashflow(
        segments, income
    )
    checks = build_checks(segments, income, balances, cashflow)
    valuation_markdown, valuation_summary = render_valuation(
        segments, income, balances, cashflow
    )

    outputs = [
        ("segments.md", render_segments(segments, checks)),
        ("income.md", render_income(income, checks)),
        ("balance.md", render_balance(balances, checks)),
        ("cashflow.md", render_cashflow(cashflow, working_capital, checks)),
        ("valuation.md", valuation_markdown),
    ]
    for filename, content in outputs:
        (ROOT / filename).write_text(content.rstrip() + "\n", encoding="utf-8")

    print("Microsoft model outputs")
    print("period | revenue | gross profit | operating income | net income | equity FCF | diluted EPS")
    for period in FORECAST_PERIODS:
        print(
            f"{period} | {income[period]['revenue']:.1f} | "
            f"{income[period]['gp']:.1f} | {income[period]['oi']:.1f} | "
            f"{income[period]['net_income']:.1f} | "
            f"{cashflow[period]['fcf']:.1f} | "
            f"{income[period]['diluted_eps']:.2f}"
        )
    print("\nValuation outputs")
    print(f"Enterprise value | ${valuation_summary['enterprise_value']:.1f}m")
    print(f"Net cash | ${valuation_summary['net_cash']:.1f}m")
    print(f"Equity value | ${valuation_summary['equity_value']:.1f}m")
    print(f"Official 12-month PT | ${valuation_summary['pt']:.2f}")
    print(f"Signed spread to last close | ${valuation_summary['residual']:.2f}")
    print(
        "Market-implied terminal growth | "
        f"{valuation_summary['implied_terminal_growth'] * 100:.2f}%"
    )
    print(
        f"Terminal value share of EV | "
        f"{valuation_summary['terminal_share'] * 100:.1f}%"
    )

    print("\nTie-out checks")
    failed = False
    for name, passed, difference in checks:
        status = "OK" if passed else "ERROR"
        print(f"{status}: {name} (difference/rate {difference:.6f})")
        failed = failed or not passed
    if failed:
        raise SystemExit("One or more model checks failed")


if __name__ == "__main__":
    main()
