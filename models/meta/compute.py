#!/usr/bin/env python3
"""Meta Platforms combined-segment three-statement model.

Running this file rewrites segments.md, income.md, balance.md, cashflow.md,
and valuation.md, then prints tie-out checks. USD millions except per-share
data, people, percentages, and share counts.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
HIST_PERIODS = ["FY2023A", "FY2024A", "FY2025A", "1H2026A"]
FORECAST_PERIODS = ["FY2026E", "FY2027E", "FY2028E"]
ALL_PERIODS = HIST_PERIODS + FORECAST_PERIODS

S1 = "https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm"
S2 = "https://www.sec.gov/Archives/edgar/data/1326801/000132680125000017/meta-20241231.htm"
S3 = "https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm"
S4 = "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Second-Quarter-2026-Results/"
REGISTER = "../../memory/meta/register.md"


# Raw filed values only; no derived values are typed in these dictionaries.
HIST_SEGMENTS = {
    "FY2023A": {
        "ads_revenue": 131_948.0,
        "other_revenue": 1_058.0,
        "foa_revenue": 133_006.0,
        "foa_oi": 62_871.0,
        "rl_revenue": 1_896.0,
        "rl_oi": -16_120.0,
    },
    "FY2024A": {
        "ads_revenue": 160_633.0,
        "other_revenue": 1_722.0,
        "foa_revenue": 162_355.0,
        "foa_oi": 87_109.0,
        "rl_revenue": 2_146.0,
        "rl_oi": -17_729.0,
    },
    "FY2025A": {
        "ads_revenue": 196_175.0,
        "other_revenue": 2_584.0,
        "foa_revenue": 198_759.0,
        "foa_oi": 102_469.0,
        "rl_revenue": 2_207.0,
        "rl_oi": -19_193.0,
    },
    "1H2026A": {
        "ads_revenue": 114_387.0,
        "other_revenue": 1_891.0,
        "foa_revenue": 116_278.0,
        "foa_oi": 50_294.0,
        "rl_revenue": 833.0,
        "rl_oi": -8_647.0,
    },
}

HIST_INCOME = {
    "FY2023A": {
        "cost_of_revenue": 25_959.0,
        "rd": 38_483.0,
        "marketing_sales": 12_301.0,
        "ga": 11_408.0,
        "interest_other": 677.0,
        "tax": 8_330.0,
        "net_income": 39_098.0,
        "diluted_shares": 2_629.0,
    },
    "FY2024A": {
        "cost_of_revenue": 30_161.0,
        "rd": 43_873.0,
        "marketing_sales": 11_347.0,
        "ga": 9_740.0,
        "interest_other": 1_283.0,
        "tax": 8_303.0,
        "net_income": 62_360.0,
        "diluted_shares": 2_614.0,
    },
    "FY2025A": {
        "cost_of_revenue": 36_175.0,
        "rd": 57_372.0,
        "marketing_sales": 11_991.0,
        "ga": 12_152.0,
        "interest_other": 2_656.0,
        "tax": 25_474.0,
        "net_income": 60_458.0,
        "diluted_shares": 2_574.0,
    },
    "1H2026A": {
        "cost_of_revenue": 21_549.0,
        "rd": 39_354.0,
        "marketing_sales": 6_339.0,
        "ga": 8_222.0,
        "interest_other": -1_139.0,
        "tax": -2_113.0,
        "net_income": 42_621.0,
        "diluted_shares": 2_565.0,
    },
}

HIST_BALANCE = {
    "FY2023A": {
        "cash": 41_862.0,
        "marketable": 23_541.0,
        "ar": 16_169.0,
        "nonmarketable": 6_141.0,
        "ppe": 96_587.0,
        "lease_assets": 13_294.0,
        "goodwill": 20_654.0,
        "total_assets": 229_623.0,
        "ap": 4_849.0,
        "lease_liabilities": 18_849.0,
        "debt": 18_385.0,
        "income_taxes": 7_514.0,
        "other_liabilities": 26_858.0,
        "total_liabilities": 76_455.0,
        "equity": 153_168.0,
        "shares_out": 2_561.0,
    },
    "FY2024A": {
        "cash": 43_889.0,
        "marketable": 33_926.0,
        "ar": 16_994.0,
        "nonmarketable": 6_070.0,
        "ppe": 121_346.0,
        "lease_assets": 14_922.0,
        "goodwill": 20_654.0,
        "total_assets": 276_054.0,
        "ap": 7_687.0,
        "lease_liabilities": 20_234.0,
        "debt": 28_826.0,
        "income_taxes": 9_987.0,
        "other_liabilities": 26_683.0,
        "total_liabilities": 93_417.0,
        "equity": 182_637.0,
        "shares_out": 2_534.0,
    },
    "FY2025A": {
        "cash": 35_873.0,
        "marketable": 45_719.0,
        "ar": 19_769.0,
        "nonmarketable": 27_524.0,
        "ppe": 176_400.0,
        "lease_assets": 20_404.0,
        "goodwill": 24_534.0,
        "total_assets": 366_021.0,
        "ap": 8_894.0,
        "lease_liabilities": 25_153.0,
        "debt": 58_744.0,
        "income_taxes": 21_005.0,
        "other_liabilities": 34_982.0,
        "total_liabilities": 148_778.0,
        "equity": 217_243.0,
        "shares_out": 2_530.0,
    },
    "1H2026A": {
        "cash": 15_462.0,
        "marketable": 74_798.0,
        "ar": 21_752.0,
        "nonmarketable": 30_157.0,
        "ppe": 225_724.0,
        "lease_assets": 23_985.0,
        "goodwill": 23_406.0,
        "total_assets": 449_956.0,
        "ap": 15_889.0,
        "lease_liabilities": 28_654.0,
        "debt": 83_664.0,
        "income_taxes": 18_326.0,
        "other_liabilities": 42_202.0,
        "total_liabilities": 188_735.0,
        "equity": 261_221.0,
        "shares_out": 2_548.0,
    },
}

HIST_CASHFLOW = {
    "FY2023A": {"net_income": 39_098.0, "da": 11_178.0, "sbc": 14_027.0, "ocf": 71_113.0, "ppe_capex": 27_045.0, "lease_principal": 1_058.0},
    "FY2024A": {"net_income": 62_360.0, "da": 15_498.0, "sbc": 16_690.0, "ocf": 91_328.0, "ppe_capex": 37_256.0, "lease_principal": 1_969.0},
    "FY2025A": {"net_income": 60_458.0, "da": 18_616.0, "sbc": 20_427.0, "ocf": 115_800.0, "ppe_capex": 69_691.0, "lease_principal": 2_524.0},
    "1H2026A": {"net_income": 42_621.0, "da": 12_355.0, "sbc": 13_690.0, "ocf": 64_088.0, "ppe_capex": 49_113.0, "lease_principal": 1_805.0},
}

# Every value below is a researcher [VIEW].
ASSUMPTIONS = {
    "FY2026E": {
        "ads_revenue": 249_000.0,
        "other_revenue": 4_200.0,
        "rl_revenue": 2_500.0,
        "foa_oi_margin": 0.419,
        "rl_oi": -19_100.0,
        "cost_of_revenue": 49_000.0,
        "rd": 86_000.0,
        "marketing_sales": 14_000.0,
        "interest_other": -2_000.0,
        "tax_rate": 0.16,
        "diluted_shares": 2_565.0,
        "da": 26_000.0,
        "sbc": 28_000.0,
        "ppe_capex": 134_000.0,
        "lease_principal": 4_000.0,
        "marketable": 50_000.0,
        "debt": 83_664.0,
        "dividends": 5_500.0,
        "buybacks": 0.0,
        "share_tax": 17_000.0,
    },
    "FY2027E": {
        "ads_revenue": 289_000.0,
        "other_revenue": 5_500.0,
        "rl_revenue": 3_400.0,
        "foa_oi_margin": 0.440,
        "rl_oi": -20_000.0,
        "cost_of_revenue": 55_000.0,
        "rd": 99_000.0,
        "marketing_sales": 15_000.0,
        "interest_other": -2_500.0,
        "tax_rate": 0.16,
        "diluted_shares": 2_565.0,
        "da": 38_000.0,
        "sbc": 32_000.0,
        "ppe_capex": 121_000.0,
        "lease_principal": 4_000.0,
        "marketable": 45_000.0,
        "debt": 83_664.0,
        "dividends": 5_800.0,
        "buybacks": 0.0,
        "share_tax": 18_000.0,
    },
    "FY2028E": {
        "ads_revenue": 329_500.0,
        "other_revenue": 7_200.0,
        "rl_revenue": 4_800.0,
        "foa_oi_margin": 0.460,
        "rl_oi": -18_500.0,
        "cost_of_revenue": 61_000.0,
        "rd": 108_000.0,
        "marketing_sales": 16_000.0,
        "interest_other": -2_000.0,
        "tax_rate": 0.17,
        "diluted_shares": 2_565.0,
        "da": 52_000.0,
        "sbc": 35_000.0,
        "ppe_capex": 101_000.0,
        "lease_principal": 4_000.0,
        "marketable": 60_000.0,
        "debt": 83_664.0,
        "dividends": 6_100.0,
        "buybacks": 25_000.0,
        "share_tax": 20_000.0,
    },
}

VALUATION_DATE = date(2026, 9, 29)
LAST_PRICE_DATE = date(2026, 9, 25)
LAST_PRICE = 751.66
NASDAQ_HISTORY = "https://www.nasdaq.com/market-activity/stocks/meta/historical-nocp"
CLASS_A_COVER_SHARES = 2_205_128_509
CLASS_B_COVER_SHARES = 342_377_716
OFFICIAL_EV_EBIT = 19.0
BEAR_EV_EBIT = 15.0
BULL_EV_EBIT = 23.0
DCF_WACC = 0.09
DCF_TERMINAL_GROWTH = 0.03


def fmt(value: Any, decimals: int = 0) -> str:
    if value is None:
        return "not obtained"
    if isinstance(value, str):
        return value
    if abs(value) < 0.0000001:
        return "—"
    out = f"{abs(value):,.{decimals}f}"
    return f"({out})" if value < 0 else out


def pct(value: float) -> str:
    return f"{value * 100:.1f}%"


def table(headers: list[str], rows: list[list[Any]]) -> str:
    return "\n".join(
        [
            "| " + " | ".join(headers) + " |",
            "|" + "|".join("---" for _ in headers) + "|",
            *["| " + " | ".join(str(c) for c in row) + " |" for row in rows],
        ]
    )


def build_segments() -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    for period, raw in HIST_SEGMENTS.items():
        output[period] = {
            **raw,
            "total_revenue": raw["foa_revenue"] + raw["rl_revenue"],
            "operating_income": raw["foa_oi"] + raw["rl_oi"],
        }
    for period, view in ASSUMPTIONS.items():
        foa_revenue = view["ads_revenue"] + view["other_revenue"]
        foa_oi = foa_revenue * view["foa_oi_margin"]
        output[period] = {
            "ads_revenue": view["ads_revenue"],
            "other_revenue": view["other_revenue"],
            "foa_revenue": foa_revenue,
            "foa_oi": foa_oi,
            "rl_revenue": view["rl_revenue"],
            "rl_oi": view["rl_oi"],
            "total_revenue": foa_revenue + view["rl_revenue"],
            "operating_income": foa_oi + view["rl_oi"],
        }
    return output


def build_income(segments: dict[str, dict[str, float]]) -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    for period in HIST_PERIODS:
        raw = HIST_INCOME[period]
        total_expenses = raw["cost_of_revenue"] + raw["rd"] + raw["marketing_sales"] + raw["ga"]
        pretax = segments[period]["operating_income"] + raw["interest_other"]
        output[period] = {
            **raw,
            **segments[period],
            "ga": raw["ga"],
            "total_expenses": total_expenses,
            "pretax": pretax,
            "diluted_eps": raw["net_income"] / raw["diluted_shares"],
        }
    for period in FORECAST_PERIODS:
        view = ASSUMPTIONS[period]
        segment = segments[period]
        total_expenses = segment["total_revenue"] - segment["operating_income"]
        ga = total_expenses - view["cost_of_revenue"] - view["rd"] - view["marketing_sales"]
        pretax = segment["operating_income"] + view["interest_other"]
        tax = max(pretax, 0.0) * view["tax_rate"]
        net_income = pretax - tax
        output[period] = {
            **segment,
            "cost_of_revenue": view["cost_of_revenue"],
            "rd": view["rd"],
            "marketing_sales": view["marketing_sales"],
            "ga": ga,
            "total_expenses": total_expenses,
            "interest_other": view["interest_other"],
            "pretax": pretax,
            "tax": tax,
            "net_income": net_income,
            "diluted_shares": view["diluted_shares"],
            "diluted_eps": net_income / view["diluted_shares"],
        }
    return output


def historical_balance() -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    for period, raw in HIST_BALANCE.items():
        named_assets = (
            raw["cash"] + raw["marketable"] + raw["ar"] + raw["nonmarketable"]
            + raw["ppe"] + raw["lease_assets"] + raw["goodwill"]
        )
        output[period] = {
            **raw,
            "other_assets": raw["total_assets"] - named_assets,
            "total_liabilities_equity": raw["total_liabilities"] + raw["equity"],
        }
    return output


def build_forecast(
    segments: dict[str, dict[str, float]],
    income: dict[str, dict[str, float]],
) -> tuple[dict[str, dict[str, float]], dict[str, dict[str, float]]]:
    balances = historical_balance()
    cashflows: dict[str, dict[str, float]] = {}
    ar_ratio = HIST_BALANCE["FY2025A"]["ar"] / HIST_SEGMENTS["FY2025A"]["foa_revenue"]
    ap_ratio = HIST_BALANCE["FY2025A"]["ap"] / (
        HIST_INCOME["FY2025A"]["cost_of_revenue"]
        + HIST_INCOME["FY2025A"]["rd"]
        + HIST_INCOME["FY2025A"]["marketing_sales"]
        + HIST_INCOME["FY2025A"]["ga"]
    )
    previous = balances["FY2025A"]
    previous_nwc = previous["ar"] - previous["ap"]
    for period in FORECAST_PERIODS:
        view = ASSUMPTIONS[period]
        ar = segments[period]["foa_revenue"] * ar_ratio
        ap = income[period]["total_expenses"] * ap_ratio
        nwc = ar - ap
        delta_nwc = nwc - previous_nwc
        ocf = income[period]["net_income"] + view["da"] + view["sbc"] - delta_nwc
        fcf = ocf - view["ppe_capex"] - view["lease_principal"]
        net_market_purchases = view["marketable"] - previous["marketable"]
        debt_issuance = view["debt"] - previous["debt"]
        cash_change = (
            fcf
            - net_market_purchases
            + debt_issuance
            - view["dividends"]
            - view["buybacks"]
            - view["share_tax"]
        )
        cash = previous["cash"] + cash_change
        ppe = previous["ppe"] + view["ppe_capex"] - view["da"]
        equity = (
            previous["equity"] + income[period]["net_income"] + view["sbc"]
            - view["dividends"] - view["buybacks"] - view["share_tax"]
        )
        lease_assets = previous["lease_assets"]
        goodwill = previous["goodwill"]
        nonmarketable = previous["nonmarketable"]
        lease_liabilities = previous["lease_liabilities"]
        income_taxes = previous["income_taxes"]
        other_liabilities = previous["other_liabilities"]
        total_liabilities = (
            ap + lease_liabilities + view["debt"] + income_taxes + other_liabilities
        )
        total_assets = total_liabilities + equity
        named_assets = (
            cash + view["marketable"] + ar + nonmarketable + ppe
            + lease_assets + goodwill
        )
        other_assets = total_assets - named_assets
        balances[period] = {
            "cash": cash,
            "marketable": view["marketable"],
            "ar": ar,
            "nonmarketable": nonmarketable,
            "ppe": ppe,
            "lease_assets": lease_assets,
            "goodwill": goodwill,
            "other_assets": other_assets,
            "total_assets": total_assets,
            "ap": ap,
            "lease_liabilities": lease_liabilities,
            "debt": view["debt"],
            "income_taxes": income_taxes,
            "other_liabilities": other_liabilities,
            "total_liabilities": total_liabilities,
            "equity": equity,
            "total_liabilities_equity": total_liabilities + equity,
            "shares_out": None,
        }
        cashflows[period] = {
            "net_income": income[period]["net_income"],
            "da": view["da"],
            "sbc": view["sbc"],
            "delta_nwc": delta_nwc,
            "ocf": ocf,
            "ppe_capex": view["ppe_capex"],
            "lease_principal": view["lease_principal"],
            "fcf": fcf,
            "net_market_purchases": net_market_purchases,
            "debt_issuance": debt_issuance,
            "dividends": view["dividends"],
            "buybacks": view["buybacks"],
            "share_tax": view["share_tax"],
            "cash_change": cash_change,
            "ending_cash": cash,
        }
        previous = balances[period]
        previous_nwc = nwc
    cashflows["_ratios"] = {"ar_ratio": ar_ratio, "ap_ratio": ap_ratio}
    return balances, cashflows


def build_checks(
    segments: dict[str, dict[str, float]],
    income: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
    cashflows: dict[str, dict[str, float]],
) -> list[tuple[str, bool, float]]:
    checks: list[tuple[str, bool, float]] = []
    tol = 0.02
    for period in ALL_PERIODS:
        segment = segments[period]
        checks.append((f"{period}: FoA revenue components", abs(segment["ads_revenue"] + segment["other_revenue"] - segment["foa_revenue"]) < tol, segment["ads_revenue"] + segment["other_revenue"] - segment["foa_revenue"]))
        checks.append((f"{period}: combined segment revenue", abs(segment["foa_revenue"] + segment["rl_revenue"] - segment["total_revenue"]) < tol, segment["foa_revenue"] + segment["rl_revenue"] - segment["total_revenue"]))
        checks.append((f"{period}: combined segment operating income", abs(segment["foa_oi"] + segment["rl_oi"] - segment["operating_income"]) < tol, segment["foa_oi"] + segment["rl_oi"] - segment["operating_income"]))
        functional_oi = income[period]["total_revenue"] - income[period]["total_expenses"]
        checks.append((f"{period}: functional expenses reconcile to segment OI", abs(functional_oi - segment["operating_income"]) < tol, functional_oi - segment["operating_income"]))
    expected = {
        "FY2023A": (134_902.0, 46_751.0, 39_098.0),
        "FY2024A": (164_501.0, 69_380.0, 62_360.0),
        "FY2025A": (200_966.0, 83_276.0, 60_458.0),
        "1H2026A": (117_111.0, 41_647.0, 42_621.0),
    }
    for period, values in expected.items():
        actual = (income[period]["total_revenue"], income[period]["operating_income"], income[period]["net_income"])
        difference = max(abs(a - b) for a, b in zip(actual, values))
        checks.append((f"{period}: historical IS matches filing", difference < tol, difference))
    previous = balances["FY2025A"]
    for period in FORECAST_PERIODS:
        balance = balances[period]
        cf = cashflows[period]
        checks.append((f"{period}: balance sheet balances", abs(balance["total_assets"] - balance["total_liabilities_equity"]) < tol, balance["total_assets"] - balance["total_liabilities_equity"]))
        checks.append((f"{period}: CF ending cash equals BS cash", abs(cf["ending_cash"] - balance["cash"]) < tol, cf["ending_cash"] - balance["cash"]))
        bridge = cf["fcf"] - cf["net_market_purchases"] + cf["debt_issuance"] - cf["dividends"] - cf["buybacks"] - cf["share_tax"]
        checks.append((f"{period}: cash bridge equals change in cash", abs(bridge - cf["cash_change"]) < tol, bridge - cf["cash_change"]))
        ppe_bridge = previous["ppe"] + cf["ppe_capex"] - cf["da"]
        checks.append((f"{period}: PP&E roll-forward", abs(ppe_bridge - balance["ppe"]) < tol, ppe_bridge - balance["ppe"]))
        checks.append((f"{period}: other assets remain non-negative", balance["other_assets"] >= 0.0, balance["other_assets"]))
        previous = balance
    return checks


def render_segments(segments: dict[str, dict[str, float]], checks: list[tuple[str, bool, float]]) -> str:
    rows = []
    lines = [
        ("Advertising revenue", "ads_revenue"),
        ("FoA Other revenue", "other_revenue"),
        ("Family of Apps revenue", "foa_revenue"),
        ("Family of Apps operating income", "foa_oi"),
        ("Reality Labs revenue", "rl_revenue"),
        ("Reality Labs operating income / (loss)", "rl_oi"),
        ("Company revenue", "total_revenue"),
        ("Company operating income", "operating_income"),
    ]
    for label, key in lines:
        values = [
            (f"[FACT] {fmt(segments[p][key])}" if p in HIST_PERIODS else f"[VIEW] {fmt(segments[p][key])}")
            for p in ALL_PERIODS
        ]
        rows.append([label, *values])
    drivers = []
    for period in ALL_PERIODS:
        segment = segments[period]
        drivers.append([
            period,
            "[FACT]" if period in HIST_PERIODS else "[VIEW]",
            pct(segment["foa_oi"] / segment["foa_revenue"]),
            pct(segment["rl_oi"] / segment["rl_revenue"]),
            pct(segment["operating_income"] / segment["total_revenue"]),
        ])
    check_rows = [[n, "OK" if ok else "ERROR", fmt(d, 2)] for n, ok, d in checks if "segment" in n or "FoA revenue" in n]
    return f"""# Meta Platforms segment model

Generated by `compute.py`; do not hand-edit. USD millions except percentages.

## Combined-segment build

{table(["line", *ALL_PERIODS], rows)}

Historical source: [register R2]({REGISTER}), [S1]({S1}), and [S3]({S3}). Company revenue and operating income are built from FoA plus RL in every period; no corporate operating-profit plug is used.

## Segment operating drivers

{table(["period", "class", "FoA operating margin", "RL operating margin", "company operating margin"], drivers)}

Forecast Advertising embeds the `[VIEW]` that AI-assisted recommendation and ad tools sustain growth while the rate decelerates. FoA Other embeds paid messaging and subscriptions without an unsupported product split. RL embeds growing hardware/ecosystem revenue, a loss near the FY2026 company frame, and narrowing only in FY2028E.

## Tie checks

{table(["check", "status", "difference"], check_rows)}
"""


def render_income(income: dict[str, dict[str, float]], checks: list[tuple[str, bool, float]]) -> str:
    lines = [
        ("Advertising revenue", "ads_revenue"),
        ("FoA Other revenue", "other_revenue"),
        ("Family of Apps revenue", "foa_revenue"),
        ("Reality Labs revenue", "rl_revenue"),
        ("Total revenue", "total_revenue"),
        ("Cost of revenue", "cost_of_revenue"),
        ("Research and development", "rd"),
        ("Marketing and sales", "marketing_sales"),
        ("General and administrative", "ga"),
        ("Total costs and expenses", "total_expenses"),
        ("Family of Apps operating income", "foa_oi"),
        ("Reality Labs operating income / (loss)", "rl_oi"),
        ("Operating income", "operating_income"),
        ("Interest and other income / (expense)", "interest_other"),
        ("Pre-tax income", "pretax"),
        ("Tax provision / (benefit)", "tax"),
        ("Net income", "net_income"),
        ("Diluted weighted-average shares", "diluted_shares"),
        ("Diluted EPS", "diluted_eps"),
    ]
    rows = []
    for label, key in lines:
        vals = []
        for p in ALL_PERIODS:
            number = fmt(income[p][key], 2 if key == "diluted_eps" else 0)
            vals.append(f"[FACT] {number}" if p in HIST_PERIODS else f"[VIEW] {number}")
        rows.append([label, *vals])
    check_rows = [[n, "OK" if ok else "ERROR", fmt(d, 2)] for n, ok, d in checks if "functional expenses" in n or "historical IS" in n]
    return f"""# Meta Platforms income statement

Generated by `compute.py`; do not hand-edit. USD millions except per-share data.

{table(["line", *ALL_PERIODS], rows)}

`1H2026A` is a six-month period. Historical company operating income equals the two disclosed segment contributions. Forecast functional G&A is the computed residual required for company functional expenses to reconcile exactly to that combined-segment operating income; it is not a segment allocation. Forecast taxes use normalized `[VIEW]` rates rather than FY2025's enactment-date valuation-allowance distortion.

## Reconciliation checks

{table(["check", "status", "difference"], check_rows)}
"""


def render_balance(balances: dict[str, dict[str, float]], income: dict[str, dict[str, float]], checks: list[tuple[str, bool, float]]) -> str:
    lines = [
        ("Cash and cash equivalents", "cash"),
        ("Marketable securities", "marketable"),
        ("Accounts receivable", "ar"),
        ("Non-marketable equity investments", "nonmarketable"),
        ("Property and equipment, net", "ppe"),
        ("Operating-lease right-of-use assets", "lease_assets"),
        ("Goodwill", "goodwill"),
        ("Other assets / balance completion", "other_assets"),
        ("Total assets", "total_assets"),
        ("Accounts payable", "ap"),
        ("Operating-lease liabilities", "lease_liabilities"),
        ("Long-term debt", "debt"),
        ("Long-term income taxes", "income_taxes"),
        ("Accrued and other liabilities", "other_liabilities"),
        ("Total liabilities", "total_liabilities"),
        ("Stockholders' equity", "equity"),
        ("Total liabilities and equity", "total_liabilities_equity"),
        ("Period-end shares", "shares_out"),
    ]
    rows = []
    for label, key in lines:
        vals = []
        for p in ALL_PERIODS:
            rendered = fmt(balances[p][key])
            vals.append(f"[FACT] {rendered}" if p in HIST_PERIODS else f"[VIEW] {rendered}")
        rows.append([label, *vals])
    rows.append(["Diluted WAS used in model", *[f"[FACT] {fmt(income[p]['diluted_shares'])}" if p in HIST_PERIODS else f"[VIEW] {fmt(income[p]['diluted_shares'])}" for p in ALL_PERIODS]])
    check_rows = [[n, "OK" if ok else "ERROR", fmt(d, 2)] for n, ok, d in checks if "balance sheet" in n or "PP&E" in n or "other assets" in n]
    return f"""# Meta Platforms balance sheet

Generated by `compute.py`; do not hand-edit. USD millions except shares.

{table(["line", *ALL_PERIODS], rows)}

Historical FY2023 comes from [S2]({S2}); FY2024–FY2025 from [S1]({S1}); and 1H2026 from [S3]({S3}). Forecast cash is generated by the cash-flow bridge. PP&E rolls by property purchases less D&A. Forecast marketable securities, debt, capital return, and share-settlement taxes are explicit `[VIEW]`s. “Other assets / balance completion” is the transparent residual needed to carry unmodeled prepaid, restricted-cash, tax, intangible, and other asset lines; it is not used in valuation.

## Tie checks

{table(["check", "status", "difference"], check_rows)}
"""


def render_cashflow(balances: dict[str, dict[str, float]], cashflows: dict[str, dict[str, float]], checks: list[tuple[str, bool, float]]) -> str:
    rows = []
    hist_lines = [
        ("Net income", "net_income"),
        ("D&A", "da"),
        ("SBC", "sbc"),
        ("Operating cash flow", "ocf"),
        ("Property and equipment purchases", "ppe_capex"),
        ("Finance-lease principal", "lease_principal"),
    ]
    for label, key in hist_lines:
        vals = [f"[FACT] {fmt(HIST_CASHFLOW[p][key])}" for p in HIST_PERIODS]
        rows.append([label, *vals, "—", "—", "—"])
    rows.append(["Free cash flow", *[f"[DEDUCTED] {fmt(HIST_CASHFLOW[p]['ocf'] - HIST_CASHFLOW[p]['ppe_capex'] - HIST_CASHFLOW[p]['lease_principal'])}" for p in HIST_PERIODS], "—", "—", "—"])
    forecast_lines = [
        ("Net income", "net_income", 1),
        ("D&A", "da", 1),
        ("SBC", "sbc", 1),
        ("Less: increase in core NWC", "delta_nwc", -1),
        ("Operating cash flow", "ocf", 1),
        ("Less: property and equipment purchases", "ppe_capex", -1),
        ("Less: finance-lease principal", "lease_principal", -1),
        ("Free cash flow", "fcf", 1),
        ("Net purchases / (sales) of marketable securities", "net_market_purchases", -1),
        ("Net debt issuance", "debt_issuance", 1),
        ("Dividends", "dividends", -1),
        ("Share repurchases", "buybacks", -1),
        ("Taxes paid for net share settlement", "share_tax", -1),
        ("Change in cash", "cash_change", 1),
        ("Ending cash", "ending_cash", 1),
    ]
    for label, key, sign in forecast_lines:
        vals = [f"[VIEW] {fmt(cashflows[p][key] * sign)}" for p in FORECAST_PERIODS]
        rows.append([label, "—", "—", "—", "—", *vals])
    ratios = cashflows["_ratios"]
    check_rows = [[n, "OK" if ok else "ERROR", fmt(d, 2)] for n, ok, d in checks if "CF ending cash" in n or "cash bridge" in n]
    return f"""# Meta Platforms cash-flow statement

Generated by `compute.py`; do not hand-edit. USD millions.

{table(["line", *ALL_PERIODS], rows)}

Historical free cash flow follows Meta's definition: OCF less property purchases and finance-lease principal. Forecast OCF is `net income + D&A + SBC − change in core NWC`; core NWC is accounts receivable less accounts payable. The `[DEDUCTED]/[VIEW]` completion ratios seeded from FY2025 are AR/FoA revenue `{pct(ratios['ar_ratio'])}` and AP/total expenses `{pct(ratios['ap_ratio'])}`. Purchases or sales of marketable securities, debt, dividends, repurchases, and net-share-settlement taxes complete the cash bridge.

## Cash tie checks

{table(["check", "status", "difference"], check_rows)}
"""


def render_valuation(
    income: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
    cashflows: dict[str, dict[str, float]],
) -> tuple[str, dict[str, float]]:
    shares_m = (CLASS_A_COVER_SHARES + CLASS_B_COVER_SHARES) / 1_000_000.0
    ebit = income["FY2027E"]["operating_income"]
    operating_ev = ebit * OFFICIAL_EV_EBIT
    net_cash = balances["FY2027E"]["cash"] + balances["FY2027E"]["marketable"] - balances["FY2027E"]["debt"]
    equity_value = operating_ev + net_cash
    raw_pt = equity_value / shares_m
    official_pt = round(raw_pt / 5.0) * 5.0
    bear = (ebit * BEAR_EV_EBIT + net_cash) / shares_m
    bull = (ebit * BULL_EV_EBIT + net_cash) / shares_m
    upside = official_pt / LAST_PRICE - 1.0
    market_cap = LAST_PRICE * shares_m
    current_net_cash = HIST_BALANCE["1H2026A"]["cash"] + HIST_BALANCE["1H2026A"]["marketable"] - HIST_BALANCE["1H2026A"]["debt"]
    current_ev = market_cap - current_net_cash
    current_multiple = current_ev / ebit
    forecast_fcff = []
    for p in FORECAST_PERIODS:
        after_tax_ebit = income[p]["operating_income"] * (1.0 - ASSUMPTIONS[p]["tax_rate"])
        fcff = after_tax_ebit + cashflows[p]["da"] - cashflows[p]["ppe_capex"] - cashflows[p]["lease_principal"] - cashflows[p]["delta_nwc"]
        forecast_fcff.append((p, fcff))
    pv_fcff = sum(v / ((1.0 + DCF_WACC) ** i) for i, (_, v) in enumerate(forecast_fcff, start=1))
    terminal_fcff = forecast_fcff[-1][1] * (1.0 + DCF_TERMINAL_GROWTH)
    terminal_value = terminal_fcff / (DCF_WACC - DCF_TERMINAL_GROWTH)
    pv_terminal = terminal_value / ((1.0 + DCF_WACC) ** len(FORECAST_PERIODS))
    dcf_equity = pv_fcff + pv_terminal + current_net_cash
    dcf_per_share = dcf_equity / shares_m
    setup = [
        ["Valuation as-of", f"[FACT] {VALUATION_DATE.isoformat()}"],
        ["Last close", f"[FACT] ${LAST_PRICE:.2f} on {LAST_PRICE_DATE.isoformat()}"],
        ["Last-close source", f"[Nasdaq historical NOCP]({NASDAQ_HISTORY})"],
        ["Share denominator", f"[DEDUCTED] {shares_m:,.3f}m from the two S3 cover counts"],
        ["Official method", "[VIEW] 19.0× FY2027E company operating income plus FY2027E net cash"],
    ]
    bridge = [
        ["FY2027E operating income", "income.md", f"[VIEW] {fmt(ebit, 1)}"],
        ["Selected EV / EBIT", "researcher assumption", f"[VIEW] {OFFICIAL_EV_EBIT:.1f}x"],
        ["Operating enterprise value", "EBIT × multiple", f"[DEDUCTED] {fmt(operating_ev, 1)}"],
        ["FY2027E net cash / (debt)", "cash + marketable securities − debt", f"[VIEW] {fmt(net_cash, 1)}"],
        ["Equity value", "EV + net cash", f"[DEDUCTED] {fmt(equity_value, 1)}"],
        ["Unrounded value / share", "equity value ÷ cover shares", f"[DEDUCTED] ${raw_pt:.2f}"],
        ["Official 12-month PT", "nearest $5", f"[VIEW] ${official_pt:.0f}"],
    ]
    checks = [
        ["Bear", f"[VIEW] {BEAR_EV_EBIT:.1f}× FY2027E EBIT + net cash", f"[VIEW] ${bear:.2f}"],
        ["Base / official", f"[VIEW] {OFFICIAL_EV_EBIT:.1f}× FY2027E EBIT + net cash", f"[VIEW] ${official_pt:.0f}"],
        ["Bull", f"[VIEW] {BULL_EV_EBIT:.1f}× FY2027E EBIT + net cash", f"[VIEW] ${bull:.2f}"],
        ["Three-year DCF check", f"[VIEW] {pct(DCF_WACC)} WACC / {pct(DCF_TERMINAL_GROWTH)} terminal growth", f"[VIEW] ${dcf_per_share:.2f}"],
    ]
    dcf_rows = [[p, f"[VIEW] {fmt(v, 1)}"] for p, v in forecast_fcff]
    tape = [
        ["Last-close market capitalization", "last close × cover shares", f"[DEDUCTED] {fmt(market_cap, 1)}"],
        ["2026-06-30 net cash / (debt)", "cash + marketable securities − debt", f"[DEDUCTED] {fmt(current_net_cash, 1)}"],
        ["Last-close enterprise value", "market cap − net cash", f"[DEDUCTED] {fmt(current_ev, 1)}"],
        ["EV / FY2027E operating income", "current EV ÷ FY2027E EBIT", f"[DEDUCTED] {current_multiple:.1f}x"],
        ["Official PT change from last close", "PT ÷ last close − 1", f"[DEDUCTED] {pct(upside)}"],
    ]
    content = f"""# Meta Platforms valuation

The official 12-month PT is **[VIEW] ${official_pt:.0f}**. The idea is visible in the target: FoA ad and Other growth rebuilds company operating leverage through FY2027E despite a still-large RL loss, while the selected multiple does not require RL breakeven.

## Official method and as-of

{table(["item", "value"], setup)}

## Official bridge

{table(["item", "basis", "$m except per share"], bridge)}

The target is generated from the operating model, not fitted to the last close. The multiple is applied to combined FoA plus RL operating income, so RL's modeled loss is already deducted. Net cash includes marketable securities and debt; non-marketable equity investments receive no separate value.

## Tape check

{table(["item", "formula", "value"], tape)}

## Bull / bear and DCF checks — not additional official targets

{table(["case", "method", "value / share"], checks)}

### DCF cash flows

{table(["period", "unlevered FCF"], dcf_rows)}

Unlevered FCF is `[VIEW]` after-tax operating income plus D&A less property purchases, finance-lease principal, and change in core NWC. The DCF is a capital-intensity check: it gives no separate credit for RL optionality and exposes the near-term AI infrastructure burden.

## What moves value

- **[VIEW]** Advertising growth and FoA operating margin change FY2027E operating income.
- **[VIEW]** AI infrastructure timing changes D&A, capex, cash conversion, and the warranted multiple.
- **[VIEW]** RL revenue and operating loss flow directly through combined operating income; no hidden RL value is added.
- **[VIEW]** Capital return, debt, and marketable-security balances change net cash and the share denominator.
"""
    return content, {"official_pt": official_pt, "bear": bear, "bull": bull, "dcf": dcf_per_share}


def main() -> None:
    segments = build_segments()
    income = build_income(segments)
    balances, cashflows = build_forecast(segments, income)
    checks = build_checks(segments, income, balances, cashflows)
    valuation_md, valuation_summary = render_valuation(income, balances, cashflows)
    outputs = {
        "segments.md": render_segments(segments, checks),
        "income.md": render_income(income, checks),
        "balance.md": render_balance(balances, income, checks),
        "cashflow.md": render_cashflow(balances, cashflows, checks),
        "valuation.md": valuation_md,
    }
    for filename, content in outputs.items():
        (ROOT / filename).write_text(content.rstrip() + "\n", encoding="utf-8")

    print("Meta Platforms model outputs")
    print("period | revenue | operating income | net income | FCF | diluted EPS")
    for period in FORECAST_PERIODS:
        print(
            f"{period} | {income[period]['total_revenue']:.1f} | "
            f"{income[period]['operating_income']:.1f} | "
            f"{income[period]['net_income']:.1f} | "
            f"{cashflows[period]['fcf']:.1f} | "
            f"{income[period]['diluted_eps']:.2f}"
        )
    print("\nValuation outputs")
    print(f"Official 12-month PT | ${valuation_summary['official_pt']:.0f}")
    print(f"Bear check | ${valuation_summary['bear']:.2f}")
    print(f"Bull check | ${valuation_summary['bull']:.2f}")
    print(f"DCF check | ${valuation_summary['dcf']:.2f}")
    print("\nTie-out checks")
    failed = False
    for name, passed, difference in checks:
        print(f"{'OK' if passed else 'ERROR'}: {name} (difference {difference:.6f})")
        failed = failed or not passed
    if failed:
        raise SystemExit("One or more model checks failed")


if __name__ == "__main__":
    main()
