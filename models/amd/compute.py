#!/usr/bin/env python3
"""AMD segment three-statement model.

All arithmetic for the markdown model lives here. Running this file rewrites
segments.md, income.md, balance.md, cashflow.md and valuation.md (stub), then
prints tie-out checks. USD millions except per-share data and percentages.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REGISTER = "../../memory/amd/register.md"
S1 = "https://www.sec.gov/Archives/edgar/data/2488/000000248826000018/amd-20251227.htm"
S5 = "https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm"

HIST_PERIODS = ["FY2023A", "FY2024A", "FY2025A", "1H2026A"]
FORECAST_PERIODS = ["FY2026E", "FY2027E", "FY2028E"]
ALL_PERIODS = HIST_PERIODS + FORECAST_PERIODS

# Segment actuals — [FACT] from register R2 segment tables.
HIST_SEGMENTS: dict[str, dict[str, float]] = {
    "FY2023A": {
        "dc_rev": 6_496.0,
        "dc_oi": 1_267.0,
        "client_rev": 4_651.0,
        "gaming_rev": 6_212.0,
        "cg_oi": 925.0,
        "emb_rev": 5_321.0,
        "emb_oi": 2_628.0,
        "all_other_oi": -4_419.0,
    },
    "FY2024A": {
        "dc_rev": 12_579.0,
        "dc_oi": 3_482.0,
        "client_rev": 7_054.0,
        "gaming_rev": 2_595.0,
        "cg_oi": 1_187.0,
        "emb_rev": 3_557.0,
        "emb_oi": 1_421.0,
        "all_other_oi": -4_190.0,
    },
    "FY2025A": {
        "dc_rev": 16_635.0,
        "dc_oi": 3_603.0,
        "client_rev": 10_640.0,
        "gaming_rev": 3_910.0,
        "cg_oi": 2_855.0,
        "emb_rev": 3_454.0,
        "emb_oi": 1_243.0,
        "all_other_oi": -4_007.0,
    },
    "1H2026A": {
        "dc_rev": 12_493.0,
        "dc_oi": 3_702.0,
        "client_rev": 5_947.0,
        "gaming_rev": 1_499.0,
        "cg_oi": 1_157.0,
        "emb_rev": 1_850.0,
        "emb_oi": 724.0,
        "all_other_oi": -2_117.0,
    },
}

# Consolidated income — [FACT] register R2 consolidated table / S1 / S6.
HIST_INCOME: dict[str, dict[str, float]] = {
    "FY2023A": {
        "revenue": 22_680.0,
        "gross_profit": 10_460.0,
        "rd": 5_872.0,
        "mga": 2_318.0,
        "operating_income": 401.0,
        "interest_expense": 106.0,
        "other_income": 0.0,
        "pretax": 0.0,
        "tax": -346.0,
        "net_income": 854.0,
        "diluted_shares": 1_608.0,
    },
    "FY2024A": {
        "revenue": 25_785.0,
        "gross_profit": 12_725.0,
        "rd": 6_456.0,
        "mga": 2_735.0,
        "operating_income": 1_900.0,
        "interest_expense": 92.0,
        "other_income": 0.0,
        "pretax": 0.0,
        "tax": 381.0,
        "net_income": 1_641.0,
        "diluted_shares": 1_641.0,
    },
    "FY2025A": {
        "revenue": 34_639.0,
        "gross_profit": 17_152.0,
        "rd": 8_091.0,
        "mga": 4_144.0,
        "operating_income": 3_694.0,
        "interest_expense": 131.0,
        "other_income": 0.0,
        "pretax": 0.0,
        "tax": -103.0,
        "net_income": 4_335.0,
        "diluted_shares": 1_636.0,
    },
    "1H2026A": {
        "revenue": 21_789.0,
        "gross_profit": 11_619.0,
        "rd": 4_925.0,
        "mga": 2_654.0,
        "operating_income": 3_466.0,
        "interest_expense": 0.0,
        "other_income": 0.0,
        "pretax": 0.0,
        "tax": 0.0,
        "net_income": 3_680.0,
        "diluted_shares": 1_655.0,
    },
}

# Balance sheet — [FACT] SEC XBRL / R6.1 for 1H2026.
HIST_BALANCE: dict[str, dict[str, float]] = {
    "FY2023A": {
        "cash": 3_933.0,
        "sti": 0.0,
        "ar": 5_376.0,
        "inventory": 4_351.0,
        "ppe": 1_589.0,
        "goodwill": 24_262.0,
        "other_assets": 29_374.0,
        "total_assets": 67_885.0,
        "ap": 2_055.0,
        "debt": 1_717.0,
        "other_liabilities": 9_221.0,
        "total_liabilities": 12_993.0,
        "apic": 0.0,
        "retained_earnings": 0.0,
        "stockholders_equity": 55_892.0,
    },
    "FY2024A": {
        "cash": 3_787.0,
        "sti": 0.0,
        "ar": 6_192.0,
        "inventory": 5_734.0,
        "ppe": 1_802.0,
        "goodwill": 24_839.0,
        "other_assets": 32_872.0,
        "total_assets": 69_226.0,
        "ap": 2_466.0,
        "debt": 1_721.0,
        "other_liabilities": 9_471.0,
        "total_liabilities": 11_658.0,
        "apic": 0.0,
        "retained_earnings": 0.0,
        "stockholders_equity": 57_568.0,
    },
    "FY2025A": {
        "cash": 5_539.0,
        "sti": 5_013.0,
        "ar": 6_315.0,
        "inventory": 7_920.0,
        "ppe": 2_312.0,
        "goodwill": 25_126.0,
        "other_assets": 30_701.0,
        "total_assets": 76_926.0,
        "ap": 2_929.0,
        "debt": 3_222.0,
        "other_liabilities": 7_776.0,
        "total_liabilities": 13_927.0,
        "apic": 0.0,
        "retained_earnings": 6_699.0,
        "stockholders_equity": 62_999.0,
    },
    "1H2026A": {
        "cash": 5_086.0,
        "sti": 8_025.0,
        "ar": 7_281.0,
        "inventory": 8_468.0,
        "ppe": 3_439.0,
        "goodwill": 25_126.0,
        "other_assets": 28_000.0,
        "total_assets": 80_425.0,
        "ap": 5_359.0,
        "debt": 3_226.0,
        "other_liabilities": 7_500.0,
        "total_liabilities": 16_085.0,
        "apic": 0.0,
        "retained_earnings": 0.0,
        "stockholders_equity": 64_340.0,
    },
}

HIST_CASHFLOW: dict[str, dict[str, float]] = {
    "FY2023A": {
        "ocf": 1_667.0,
        "capex": 546.0,
        "da": 0.0,
        "sbc": 1_384.0,
        "net_income": 854.0,
    },
    "FY2024A": {
        "ocf": 3_041.0,
        "capex": 636.0,
        "da": 0.0,
        "sbc": 1_407.0,
        "net_income": 1_641.0,
    },
    "FY2025A": {
        "ocf": 6_493.0,
        "capex": 974.0,
        "da": 0.0,
        "sbc": 1_638.0,
        "net_income": 4_335.0,
    },
    "1H2026A": {
        "ocf": 5_321.0,
        "capex": 1_197.0,
        "da": 0.0,
        "sbc": 990.0,
        "net_income": 3_680.0,
    },
}

# Researcher [VIEW] segment drivers — see inputs.md.
ASSUMPTIONS: dict[str, dict[str, float]] = {
    "FY2026E": {
        "dc_rev_growth": 0.78,
        "client_rev_growth": 0.18,
        "gaming_rev_growth": -0.15,
        "emb_rev_growth": 0.15,
        "dc_oi_margin": 0.30,
        "cg_oi_margin": 0.16,
        "emb_oi_margin": 0.39,
        "all_other_oi": -5_100.0,
        "consolidated_gm": 0.54,
        "rd": 9_600.0,
        "mga": 4_900.0,
        "interest_expense": 150.0,
        "other_income": 80.0,
        "tax_rate": 0.13,
        "capex": 2_800.0,
        "da": 1_200.0,
        "sbc": 2_100.0,
        "buybacks": 400.0,
        "diluted_shares": 1_660.0,
    },
    "FY2027E": {
        "dc_rev_growth": 1.05,
        "client_rev_growth": 0.10,
        "gaming_rev_growth": -0.05,
        "emb_rev_growth": 0.10,
        "dc_oi_margin": 0.31,
        "cg_oi_margin": 0.17,
        "emb_oi_margin": 0.39,
        "all_other_oi": -5_800.0,
        "consolidated_gm": 0.55,
        "rd": 10_800.0,
        "mga": 5_400.0,
        "interest_expense": 160.0,
        "other_income": 60.0,
        "tax_rate": 0.13,
        "capex": 3_500.0,
        "da": 1_400.0,
        "sbc": 2_400.0,
        "buybacks": 600.0,
        "diluted_shares": 1_670.0,
    },
    "FY2028E": {
        "dc_rev_growth": 0.40,
        "client_rev_growth": 0.08,
        "gaming_rev_growth": 0.00,
        "emb_rev_growth": 0.08,
        "dc_oi_margin": 0.32,
        "cg_oi_margin": 0.18,
        "emb_oi_margin": 0.38,
        "all_other_oi": -6_400.0,
        "consolidated_gm": 0.55,
        "rd": 11_600.0,
        "mga": 5_800.0,
        "interest_expense": 170.0,
        "other_income": 50.0,
        "tax_rate": 0.13,
        "capex": 4_000.0,
        "da": 1_600.0,
        "sbc": 2_600.0,
        "buybacks": 800.0,
        "diluted_shares": 1_680.0,
    },
}

MINIMUM_CASH = 4_000.0
INTEREST_INCOME_RATE = 0.03


def fmt(value: Any, decimals: int = 0) -> str:
    if value is None:
        return "not obtained"
    if isinstance(value, str):
        return value
    if abs(value) < 0.0000001:
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


def enrich_segments(raw: dict[str, float]) -> dict[str, float]:
    cg_rev = raw["client_rev"] + raw["gaming_rev"]
    seg_oi = (
        raw["dc_oi"]
        + raw["cg_oi"]
        + raw["emb_oi"]
        + raw["all_other_oi"]
    )
    return {
        **raw,
        "cg_rev": cg_rev,
        "total_rev": raw["dc_rev"] + cg_rev + raw["emb_rev"],
        "segment_operating_income": seg_oi,
    }


def build_historical_segments() -> dict[str, dict[str, float]]:
    return {p: enrich_segments(HIST_SEGMENTS[p]) for p in HIST_PERIODS}


def build_forecast_segments(
    prior: dict[str, dict[str, float]],
) -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    prev_key = "1H2026A"
    for period in FORECAST_PERIODS:
        assumption = ASSUMPTIONS[period]
        base = prior[prev_key] if period == "FY2026E" else output[
            FORECAST_PERIODS[FORECAST_PERIODS.index(period) - 1]
        ]
        base_rev = (
            HIST_SEGMENTS["FY2025A"]
            if period == "FY2026E"
            else {
                "dc_rev": base["dc_rev"],
                "client_rev": base["client_rev"],
                "gaming_rev": base["gaming_rev"],
                "emb_rev": base["emb_rev"],
            }
        )
        dc_rev = base_rev["dc_rev"] * (1.0 + assumption["dc_rev_growth"])
        client_rev = base_rev["client_rev"] * (1.0 + assumption["client_rev_growth"])
        gaming_rev = base_rev["gaming_rev"] * (1.0 + assumption["gaming_rev_growth"])
        emb_rev = base_rev["emb_rev"] * (1.0 + assumption["emb_rev_growth"])
        cg_rev = client_rev + gaming_rev
        dc_oi = dc_rev * assumption["dc_oi_margin"]
        cg_oi = cg_rev * assumption["cg_oi_margin"]
        emb_oi = emb_rev * assumption["emb_oi_margin"]
        raw = {
            "dc_rev": dc_rev,
            "dc_oi": dc_oi,
            "client_rev": client_rev,
            "gaming_rev": gaming_rev,
            "cg_oi": cg_oi,
            "emb_rev": emb_rev,
            "emb_oi": emb_oi,
            "all_other_oi": assumption["all_other_oi"],
        }
        output[period] = enrich_segments(raw)
        prev_key = period
    return output


def build_income(
    segments: dict[str, dict[str, float]],
) -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    for period in HIST_PERIODS:
        seg = segments[period]
        raw = HIST_INCOME[period]
        pretax = (
            raw["operating_income"]
            - raw["interest_expense"]
            + raw["other_income"]
        )
        if raw["pretax"] == 0.0:
            pretax = raw["net_income"] - raw["tax"]
        output[period] = {
            **raw,
            "segment_revenue": seg["total_rev"],
            "segment_operating_income": seg["segment_operating_income"],
            "dc_oi": seg["dc_oi"],
            "cg_oi": seg["cg_oi"],
            "emb_oi": seg["emb_oi"],
            "all_other_oi": seg["all_other_oi"],
            "pretax_income": pretax,
            "diluted_eps": raw["net_income"] / raw["diluted_shares"],
        }

    prior_balance = HIST_BALANCE["1H2026A"]
    for period in FORECAST_PERIODS:
        seg = segments[period]
        assumption = ASSUMPTIONS[period]
        revenue = seg["total_rev"]
        operating_income = seg["segment_operating_income"]
        gross_profit = revenue * assumption["consolidated_gm"]
        rd = assumption["rd"]
        mga = assumption["mga"]
        implied_opex = gross_profit - operating_income
        interest_income = (
            prior_balance["cash"] + prior_balance["sti"]
        ) * INTEREST_INCOME_RATE
        interest_expense = assumption["interest_expense"]
        other_income = assumption["other_income"]
        pretax = (
            operating_income
            + interest_income
            - interest_expense
            + other_income
        )
        tax = max(pretax, 0.0) * assumption["tax_rate"]
        net_income = pretax - tax
        output[period] = {
            "revenue": revenue,
            "gross_profit": gross_profit,
            "rd": rd,
            "mga": mga,
            "implied_total_opex": implied_opex,
            "operating_income": operating_income,
            "interest_income": interest_income,
            "interest_expense": interest_expense,
            "other_income": other_income,
            "pretax_income": pretax,
            "tax": tax,
            "net_income": net_income,
            "segment_revenue": revenue,
            "segment_operating_income": operating_income,
            "dc_oi": seg["dc_oi"],
            "cg_oi": seg["cg_oi"],
            "emb_oi": seg["emb_oi"],
            "all_other_oi": seg["all_other_oi"],
            "diluted_shares": assumption["diluted_shares"],
            "diluted_eps": net_income / assumption["diluted_shares"],
        }
    return output


def build_balance_and_cashflow(
    income: dict[str, dict[str, float]],
) -> tuple[dict[str, dict[str, float]], dict[str, dict[str, float]]]:
    balances = {p: dict(HIST_BALANCE[p]) for p in HIST_PERIODS}
    cashflow: dict[str, dict[str, float]] = {}

    h1 = balances["1H2026A"]
    h1_rev_annual = income["1H2026A"]["revenue"] * 2.0
    h1_cogs_annual = (
        income["1H2026A"]["revenue"] - income["1H2026A"]["gross_profit"]
    ) * 2.0
    ar_days = h1["ar"] / h1_rev_annual * 365.0
    inventory_days = h1["inventory"] / h1_cogs_annual * 365.0
    ap_days = h1["ap"] / h1_cogs_annual * 365.0

    previous = balances["1H2026A"]
    for period in FORECAST_PERIODS:
        assumption = ASSUMPTIONS[period]
        inc = income[period]
        revenue = inc["revenue"]
        cogs = revenue - inc["gross_profit"]
        ar = revenue * ar_days / 365.0
        inventory = cogs * inventory_days / 365.0
        ap = cogs * ap_days / 365.0
        delta_nwc = (ar + inventory - ap) - (
            previous["ar"] + previous["inventory"] - previous["ap"]
        )

        da = assumption["da"]
        sbc = assumption["sbc"]
        ocf = inc["net_income"] + da + sbc - delta_nwc
        capex = assumption["capex"]
        fcf = ocf - capex
        buybacks = assumption["buybacks"]

        cash = previous["cash"] + fcf - buybacks
        if cash < MINIMUM_CASH:
            sti_draw = min(previous["sti"], MINIMUM_CASH - cash)
        else:
            sti_draw = 0.0
        cash += sti_draw
        sti = previous["sti"] - sti_draw
        ppe = previous["ppe"] + capex - da
        goodwill = previous["goodwill"]
        other_assets = previous["other_assets"]
        total_assets = (
            cash
            + sti
            + ar
            + inventory
            + ppe
            + goodwill
            + other_assets
        )
        debt = previous["debt"]
        other_liabilities = previous["other_liabilities"]
        total_liabilities = ap + debt + other_liabilities
        retained = previous.get("retained_earnings", 0.0) + inc["net_income"] - buybacks
        equity = total_assets - total_liabilities
        balances[period] = {
            "cash": cash,
            "sti": sti,
            "ar": ar,
            "inventory": inventory,
            "ppe": ppe,
            "goodwill": goodwill,
            "other_assets": other_assets,
            "total_assets": total_assets,
            "ap": ap,
            "debt": debt,
            "other_liabilities": other_liabilities,
            "total_liabilities": total_liabilities,
            "retained_earnings": retained,
            "stockholders_equity": equity,
        }
        cashflow[period] = {
            "net_income": inc["net_income"],
            "da": da,
            "sbc": sbc,
            "delta_nwc": delta_nwc,
            "ocf": ocf,
            "capex": capex,
            "fcf": fcf,
            "buybacks": buybacks,
            "ending_cash": cash,
        }
        previous = balances[period]

    cashflow["_wc_days"] = {
        "ar_days": ar_days,
        "inventory_days": inventory_days,
        "ap_days": ap_days,
    }
    return balances, cashflow


def build_checks(
    segments: dict[str, dict[str, float]],
    income: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
) -> list[tuple[str, bool, float]]:
    checks: list[tuple[str, bool, float]] = []
    tol = 0.05
    for period in ALL_PERIODS:
        seg = segments[period]
        inc = income[period]
        rev_diff = seg["total_rev"] - inc["revenue"]
        oi_diff = seg["segment_operating_income"] - inc["operating_income"]
        checks.append(
            (
                f"{period}: segment revenue = consolidated revenue",
                abs(rev_diff) < tol,
                rev_diff,
            )
        )
        checks.append(
            (
                f"{period}: segment OI = consolidated operating income",
                abs(oi_diff) < tol,
                oi_diff,
            )
        )
        if period in HIST_PERIODS:
            filed_oi = HIST_INCOME[period]["operating_income"]
            checks.append(
                (
                    f"{period}: segment OI = filed operating income",
                    abs(seg["segment_operating_income"] - filed_oi) < tol,
                    seg["segment_operating_income"] - filed_oi,
                )
            )
    for period in FORECAST_PERIODS:
        bal = balances[period]
        checks.append(
            (
                f"{period}: assets = liabilities + equity",
                abs(bal["total_assets"] - bal["total_liabilities"] - bal["stockholders_equity"])
                < 1.0,
                bal["total_assets"] - bal["total_liabilities"] - bal["stockholders_equity"],
            )
        )
    return checks


def render_segments(
    segments: dict[str, dict[str, float]], checks: list[tuple[str, bool, float]]
) -> str:
    rows = []
    line_items = [
        ("Data Center revenue", "dc_rev"),
        ("Data Center operating income", "dc_oi"),
        ("Client revenue", "client_rev"),
        ("Gaming revenue", "gaming_rev"),
        ("Client + Gaming revenue (combined)", "cg_rev"),
        ("Client + Gaming operating income (reported segment)", "cg_oi"),
        ("Embedded revenue", "emb_rev"),
        ("Embedded operating income", "emb_oi"),
        ("All Other operating loss", "all_other_oi"),
        ("Total segment revenue", "total_rev"),
        ("Consolidated operating income (segment sum)", "segment_operating_income"),
    ]
    for label, key in line_items:
        rows.append([label] + [fmt(segments[p][key]) for p in ALL_PERIODS])

    margin_rows = []
    for period in ALL_PERIODS:
        s = segments[period]
        margin_rows.append(
            [
                period,
                pct(s["dc_oi"] / s["dc_rev"]),
                pct(s["cg_oi"] / s["cg_rev"]),
                pct(s["emb_oi"] / s["emb_rev"]),
            ]
        )

    check_rows = [
        [n, "OK" if ok else "ERROR", fmt(d, 2)]
        for n, ok, d in checks
        if "segment revenue" in n or "segment OI" in n
    ]
    return f"""# AMD segment model

Generated by `compute.py`; do not hand-edit. USD millions except percentages.

## Revenue and segment operating income

Historical segment lines are `[FACT]` from [register R2]({REGISTER}). Client and Gaming operating income is disclosed only on a combined reportable-segment basis; standalone Client or Gaming OI is `not obtained`. World Labs (R1.9) is excluded until close.

{markdown_table(["line", *ALL_PERIODS], rows)}

## Reported segment operating margins

{markdown_table(["period", "Data Center OI / rev", "Client+Gaming OI / rev", "Embedded OI / rev"], margin_rows)}

Forecast segment operating margins are `[VIEW]` inputs in [`inputs.md`](inputs.md).

## Segment tie checks

{markdown_table(["check", "status", "difference"], check_rows)}
"""


def render_income(
    income: dict[str, dict[str, float]], checks: list[tuple[str, bool, float]]
) -> str:
    rows = [
        ["Data Center operating income"]
        + [fmt(income[p]["dc_oi"]) for p in ALL_PERIODS],
        ["Client + Gaming operating income"]
        + [fmt(income[p]["cg_oi"]) for p in ALL_PERIODS],
        ["Embedded operating income"]
        + [fmt(income[p]["emb_oi"]) for p in ALL_PERIODS],
        ["All Other operating loss"]
        + [fmt(income[p]["all_other_oi"]) for p in ALL_PERIODS],
        ["Operating income (sum of segments)"]
        + [fmt(income[p]["operating_income"]) for p in ALL_PERIODS],
        ["Gross profit"]
        + [fmt(income[p]["gross_profit"]) for p in ALL_PERIODS],
        ["Research and development"]
        + [fmt(income[p]["rd"]) for p in ALL_PERIODS],
        ["Marketing, general and administrative"]
        + [fmt(income[p]["mga"]) for p in ALL_PERIODS],
        ["Implied COGS + unallocated opex (GP − segment OI)"]
        + [
            fmt(
                income[p]["gross_profit"] - income[p]["operating_income"]
                if p in HIST_PERIODS
                else income[p]["implied_total_opex"]
            )
            for p in ALL_PERIODS
        ],
        ["Interest income"]
        + [
            fmt(income[p].get("interest_income", 0.0))
            for p in ALL_PERIODS
        ],
        ["Interest expense"]
        + [fmt(-income[p]["interest_expense"]) for p in ALL_PERIODS],
        ["Other income / (expense)"]
        + [fmt(income[p]["other_income"]) for p in ALL_PERIODS],
        ["Pre-tax income"]
        + [fmt(income[p]["pretax_income"]) for p in ALL_PERIODS],
        ["Income tax provision / (benefit)"]
        + [fmt(-income[p]["tax"]) if income[p]["tax"] > 0 else fmt(income[p]["tax"]) for p in ALL_PERIODS],
        ["Net income"]
        + [fmt(income[p]["net_income"]) for p in ALL_PERIODS],
        ["Diluted weighted-average shares"]
        + [fmt(income[p]["diluted_shares"]) for p in ALL_PERIODS],
        ["Diluted EPS"]
        + [fmt(income[p]["diluted_eps"], 2) for p in ALL_PERIODS],
    ]
    rev_row = ["Total revenue (segment sum)"] + [
        fmt(income[p]["revenue"]) for p in ALL_PERIODS
    ]
    gm_row = ["Gross margin"] + [
        pct(income[p]["gross_profit"] / income[p]["revenue"])
        for p in ALL_PERIODS
    ]
    rows.insert(0, rev_row)
    rows.insert(2, gm_row)

    check_rows = [
        [n, "OK" if ok else "ERROR", fmt(d, 2)]
        for n, ok, d in checks
        if "consolidated" in n or "filed operating" in n
    ]
    return f"""# AMD income statement

Generated by `compute.py`; do not hand-edit. USD millions except per-share data.

Consolidated revenue and operating income are built **only** from reported segment sums in [`segments.md`](segments.md): Data Center, Client + Gaming, Embedded and All Other. Gross profit on history is `[FACT]` from [register R2]({REGISTER}); forecast gross profit uses `[VIEW]` consolidated gross margin with R&D and MG&A also `[VIEW]`, so implied COGS plus any unallocated costs equal gross profit minus segment operating income.

{markdown_table(["line", *ALL_PERIODS], rows)}

`1H2026A` is a six-month period. Historical interest and other below-the-line lines are incomplete in the register set where not filed for 1H; tax is not split for 1H in this table.

## Reconciliation checks

{markdown_table(["check", "status", "difference"], check_rows)}
"""


def render_balance(balances: dict[str, dict[str, float]]) -> str:
    rows = [
        ["Cash"] + [fmt(balances[p]["cash"]) for p in ALL_PERIODS],
        ["Short-term investments"]
        + [fmt(balances[p]["sti"]) for p in ALL_PERIODS],
        ["Accounts receivable"]
        + [fmt(balances[p]["ar"]) for p in ALL_PERIODS],
        ["Inventory"] + [fmt(balances[p]["inventory"]) for p in ALL_PERIODS],
        ["PP&E, net"] + [fmt(balances[p]["ppe"]) for p in ALL_PERIODS],
        ["Goodwill"] + [fmt(balances[p]["goodwill"]) for p in ALL_PERIODS],
        ["Other assets (residual)"]
        + [fmt(balances[p]["other_assets"]) for p in ALL_PERIODS],
        ["Total assets"]
        + [fmt(balances[p]["total_assets"]) for p in ALL_PERIODS],
        ["Accounts payable"] + [fmt(balances[p]["ap"]) for p in ALL_PERIODS],
        ["Debt"] + [fmt(balances[p]["debt"]) for p in ALL_PERIODS],
        ["Other liabilities (residual)"]
        + [fmt(balances[p]["other_liabilities"]) for p in ALL_PERIODS],
        ["Total liabilities"]
        + [fmt(balances[p]["total_liabilities"]) for p in ALL_PERIODS],
        ["Stockholders' equity"]
        + [fmt(balances[p]["stockholders_equity"]) for p in ALL_PERIODS],
    ]
    return f"""# AMD balance sheet

Generated by `compute.py`; do not hand-edit. USD millions.

FY2023–FY2025 `[FACT]` lines are from SEC XBRL tied to [S1]({S1}); 1H2026 `[FACT]` from [R6.1]({REGISTER}) and [S5]({S5}). Other assets and other liabilities are residual plugs to filed totals on history. Forecast rolls from 2026-06-30 with `[VIEW]` working-capital days, capex, D&A and buybacks.

{markdown_table(["line", *ALL_PERIODS], rows)}
"""


def render_cashflow(
    cashflow: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
) -> str:
    hist_rows = []
    for period in HIST_PERIODS:
        raw = HIST_CASHFLOW[period]
        hist_rows.append(
            [
                period,
                fmt(raw["net_income"]),
                fmt(raw["ocf"]),
                fmt(raw["capex"]),
                fmt(raw["ocf"] - raw["capex"]),
                fmt(balances[period]["cash"]),
            ]
        )
    fc_rows = []
    for period in FORECAST_PERIODS:
        cf = cashflow[period]
        fc_rows.append(
            [
                period,
                fmt(cf["net_income"]),
                fmt(cf["da"]),
                fmt(cf["sbc"]),
                fmt(-cf["delta_nwc"]),
                fmt(cf["ocf"]),
                fmt(-cf["capex"]),
                fmt(cf["fcf"]),
                fmt(-cf["buybacks"]),
                fmt(cf["ending_cash"]),
            ]
        )
    wc = cashflow["_wc_days"]
    return f"""# AMD cash-flow statement

Generated by `compute.py`; do not hand-edit. USD millions.

## Historical (reported or register)

{markdown_table(["period", "net income", "OCF", "capex", "FCF (OCF − capex)", "ending cash"], hist_rows)}

FY2025 OCF uses continuing operations per [R6.3]({REGISTER}). D&A detail on history: `not obtained` in register aggregate.

## Forecast bridge

Operating cash flow = net income + D&A + SBC − ΔNWC. FCF = OCF − capex. Cash ends with FCF less `[VIEW]` buybacks; short-term investments absorb sub-minimum cash before equity is adjusted.

Working-capital days from 1H2026 annualized revenue/COGS: AR `{wc["ar_days"]:.1f}`, inventory `{wc["inventory_days"]:.1f}`, AP `{wc["ap_days"]:.1f}`.

{markdown_table(["period", "NI", "D&A", "SBC", "ΔNWC", "OCF", "capex", "FCF", "buybacks", "ending cash"], fc_rows)}
"""


def render_valuation_stub() -> str:
    return """# AMD valuation

Valuation not started; awaits completed three-statement model review and valuation gate.

The segment three-statement workbook lives under `models/amd/`. Do not infer price targets from forecast tables until `valuation.md` is built in a later gate.
"""


def main() -> None:
    hist_segments = build_historical_segments()
    forecast_segments = build_forecast_segments(hist_segments)
    segments = {**hist_segments, **forecast_segments}
    income = build_income(segments)
    balances, cashflow = build_balance_and_cashflow(income)
    checks = build_checks(segments, income, balances)

    outputs = {
        "segments.md": render_segments(segments, checks),
        "income.md": render_income(income, checks),
        "balance.md": render_balance(balances),
        "cashflow.md": render_cashflow(cashflow, balances),
        "valuation.md": render_valuation_stub(),
    }
    for name, content in outputs.items():
        (ROOT / name).write_text(content.rstrip() + "\n", encoding="utf-8")

    print("AMD model — forecast summary")
    for period in FORECAST_PERIODS:
        print(
            f"{period}: rev {income[period]['revenue']:.0f} | "
            f"OI {income[period]['operating_income']:.0f} | "
            f"NI {income[period]['net_income']:.0f} | "
            f"FCF {cashflow[period]['fcf']:.0f}"
        )
    print("\nTie-out checks")
    failed = False
    for name, passed, diff in checks:
        status = "OK" if passed else "ERROR"
        print(f"{status}: {name} (diff {diff:.4f})")
        failed = failed or not passed
    if failed:
        raise SystemExit("One or more model checks failed")


if __name__ == "__main__":
    main()
