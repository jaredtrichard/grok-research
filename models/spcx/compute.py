#!/usr/bin/env python3
"""Build the SpaceX segment-led three-statement model.

All material arithmetic is performed here. The script writes the four markdown
workbook files beside itself and exits non-zero if a reconciliation fails.
Units are USD millions unless a driver explicitly says otherwise.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Iterable


D = Decimal
ROOT = Path(__file__).resolve().parent
TOLERANCE = D("0.000001")
VIEW_TAG = "[VIEW; as_of 2026-08-30; not a filing line]"


@dataclass(frozen=True)
class Formula:
    formula_id: str
    output: str
    expression: str
    inputs: dict[str, Decimal]
    result: Decimal


FORMULAS: list[Formula] = []


def derive(
    output: str,
    expression: str,
    inputs: dict[str, Decimal],
    result: Decimal,
) -> Decimal:
    """Record a derived value and the named inputs used to compute it."""
    formula_id = f"F{len(FORMULAS) + 1:03d}"
    FORMULAS.append(Formula(formula_id, output, expression, dict(inputs), result))
    return result


def formula_id(output: str) -> str:
    matches = [item.formula_id for item in FORMULAS if item.output == output]
    if len(matches) != 1:
        raise ValueError(f"Expected one formula for {output}, found {len(matches)}")
    return matches[0]


def sum_named(output: str, inputs: dict[str, Decimal]) -> Decimal:
    return derive(output, " + ".join(inputs), inputs, sum(inputs.values(), D("0")))


def subtract(output: str, minuend_name: str, minuend: Decimal, subtrahend_name: str, subtrahend: Decimal) -> Decimal:
    return derive(
        output,
        f"{minuend_name} - {subtrahend_name}",
        {minuend_name: minuend, subtrahend_name: subtrahend},
        minuend - subtrahend,
    )


def multiply(output: str, left_name: str, left: Decimal, right_name: str, right: Decimal) -> Decimal:
    return derive(
        output,
        f"{left_name} × {right_name}",
        {left_name: left, right_name: right},
        left * right,
    )


def divide(output: str, numerator_name: str, numerator: Decimal, denominator_name: str, denominator: Decimal) -> Decimal:
    return derive(
        output,
        f"{numerator_name} ÷ {denominator_name}",
        {numerator_name: numerator, denominator_name: denominator},
        numerator / denominator,
    )


def power(output: str, base_name: str, base: Decimal, exponent_name: str, exponent: Decimal) -> Decimal:
    return derive(
        output,
        f"{base_name} ^ {exponent_name}",
        {base_name: base, exponent_name: exponent},
        base ** exponent,
    )


def q(value: Decimal, places: str = "0.1") -> Decimal:
    return value.quantize(D(places), rounding=ROUND_HALF_UP)


def number(value: Decimal, places: str = "0.1") -> str:
    rounded = q(value, places)
    return f"{rounded:,.{abs(D(places).as_tuple().exponent)}f}"


def money(value: Decimal, places: str = "0.1") -> str:
    if value < 0:
        return f"$({number(-value, places)})"
    return f"${number(value, places)}"


def plain(value: Decimal, places: str = "0.1") -> str:
    if value < 0:
        return f"({number(-value, places)})"
    return number(value, places)


def exact(value: Decimal) -> str:
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return f"({text})" if value < 0 else text


def tagged(value: Decimal, classification: str, output: str | None = None, unit: str = "money") -> str:
    rendered = money(value) if unit == "money" else plain(value)
    if classification == "DEDUCTED":
        if output is None:
            raise ValueError("Derived cells require an output/formula name")
        return f"{rendered} [DEDUCTED {formula_id(output)}]"
    return f"{rendered} [{classification}]"


def not_obtained() -> str:
    return "**not obtained**"


def markdown_table(headers: list[str], rows: Iterable[list[str]], aligns: list[str] | None = None) -> str:
    if aligns is None:
        aligns = ["---"] * len(headers)
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(aligns) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(lines)


def formula_appendix(title: str, prefixes: tuple[str, ...]) -> str:
    selected = [item for item in FORMULAS if item.output.startswith(prefixes)]
    rows: list[list[str]] = []
    for item in selected:
        inputs = "; ".join(f"{name}={exact(value)}" for name, value in item.inputs.items())
        rows.append([item.formula_id, f"`{item.output}`", item.expression, inputs, plain(item.result)])
    return f"""## {title}

Every `[DEDUCTED]` cell above points to one of these formulas.

{markdown_table(["id", "output", "expression", "named inputs", "result"], rows)}
"""


def close(left: Decimal, right: Decimal) -> bool:
    return abs(left - right) <= TOLERANCE


# ---------------------------------------------------------------------------
# Source facts: register.md and its catalogued 424B4 / 10-Q / 8-K sources.
# ---------------------------------------------------------------------------

ACTUAL_SEGMENTS: dict[str, dict[str, dict[str, Decimal]]] = {
    "FY2023": {
        "Space": {"revenue": D("3557"), "cor": D("1669"), "rd": D("1538"), "sga": D("351"), "restruct": D("0"), "impairment": D("0")},
        "Connectivity": {"revenue": D("3869"), "cor": D("2786"), "rd": D("381"), "sga": D("233"), "restruct": D("0"), "impairment": D("0")},
        "AI": {"revenue": D("2961"), "cor": D("1655"), "rd": D("186"), "sga": D("1081"), "restruct": D("237"), "impairment": D("3775")},
    },
    "FY2024": {
        "Space": {"revenue": D("3796"), "cor": D("1541"), "rd": D("1835"), "sga": D("375"), "restruct": D("0"), "impairment": D("24")},
        "Connectivity": {"revenue": D("7599"), "cor": D("4768"), "rd": D("453"), "sga": D("333"), "restruct": D("0"), "impairment": D("39")},
        "AI": {"revenue": D("2620"), "cor": D("1687"), "rd": D("1176"), "sga": D("1105"), "restruct": D("213"), "impairment": D("0")},
    },
    "FY2025": {
        "Space": {"revenue": D("4086"), "cor": D("1352"), "rd": D("3004"), "sga": D("349"), "restruct": D("0"), "impairment": D("38")},
        "Connectivity": {"revenue": D("11387"), "cor": D("5921"), "rd": D("575"), "sga": D("468"), "restruct": D("0"), "impairment": D("0")},
        "AI": {"revenue": D("3201"), "cor": D("2178"), "rd": D("5064"), "sga": D("1827"), "restruct": D("487"), "impairment": D("0")},
    },
    "H1 2026A": {
        "Space": {"revenue": D("1581"), "cor": D("610"), "rd": D("2006"), "sga": D("169"), "restruct": D("0"), "impairment": D("0")},
        "Connectivity": {"revenue": D("7548"), "cor": D("3711"), "rd": D("499"), "sga": D("494"), "restruct": D("0"), "impairment": D("0")},
        "AI": {"revenue": D("3379"), "cor": D("1562"), "rd": D("4557"), "sga": D("995"), "restruct": D("-9"), "impairment": D("0")},
    },
}

REPORTED_CONSOLIDATED: dict[str, dict[str, Decimal]] = {
    "FY2023": {"revenue": D("10387"), "cor": D("6110"), "rd": D("2105"), "sga": D("1665"), "restruct": D("237"), "impairment": D("3775"), "ebit": D("-3505")},
    "FY2024": {"revenue": D("14015"), "cor": D("7996"), "rd": D("3464"), "sga": D("1813"), "restruct": D("213"), "impairment": D("63"), "ebit": D("466")},
    "FY2025": {"revenue": D("18674"), "cor": D("9451"), "rd": D("8643"), "sga": D("2644"), "restruct": D("487"), "impairment": D("38"), "ebit": D("-2589")},
    "H1 2026A": {"revenue": D("12508"), "cor": D("5883"), "rd": D("7062"), "sga": D("1658"), "restruct": D("-9"), "impairment": D("0"), "ebit": D("-2086")},
}

ACTUAL_FINANCE: dict[str, dict[str, Decimal]] = {
    "FY2023": {"interest_expense": D("1693"), "interest_income": D("249"), "other_income": D("-42"), "tax": D("-363"), "net_income": D("-4628")},
    "FY2024": {"interest_expense": D("1580"), "interest_income": D("371"), "other_income": D("985"), "tax": D("-549"), "net_income": D("791")},
    "FY2025": {"interest_expense": D("1945"), "interest_income": D("492"), "other_income": D("-177"), "tax": D("718"), "net_income": D("-4937")},
    "H1 2026A": {"interest_expense": D("1293"), "interest_income": D("553"), "other_income": D("-1962"), "tax": D("29"), "net_income": D("-4817")},
}

ACTUAL_CASHFLOW: dict[str, dict[str, Decimal]] = {
    "FY2023": {"ocf": D("4520"), "capex": D("4415")},
    "FY2024": {"ocf": D("5776"), "capex": D("11163")},
    "FY2025": {"ocf": D("6785"), "capex": D("20737")},
    "H1 2026A": {"ocf": D("3466"), "capex": D("28476")},
}

ACTUAL_BALANCE: dict[str, dict[str, Decimal]] = {
    "FY2025": {
        "cash": D("24747"), "securities": D("0"), "ar": D("1579"), "inventory": D("2416"),
        "ppe": D("42602"), "spectrum_assets": D("0"), "total_assets": D("92079"), "debt": D("22896"),
        "deferred_revenue": D("12116"), "total_liabilities": D("50754"),
        "redeemable_preferred": D("38752"), "equity": D("2573"),
    },
    "H1 2026A": {
        "cash": D("93522"), "securities": D("6487"), "ar": D("3596"), "inventory": D("2718"),
        "ppe": D("65736"), "spectrum_assets": D("0"), "total_assets": D("192770"), "debt": D("39364"),
        "deferred_revenue": D("14286"), "total_liabilities": D("65546"),
        "redeemable_preferred": D("0"), "equity": D("127224"),
    },
}


# ---------------------------------------------------------------------------
# Forecast drivers. Every forecast driver is a [VIEW] implementing research.md.
# ---------------------------------------------------------------------------

DRIVERS: dict[str, dict[str, Decimal]] = {
    "H2 2026E": {
        "customer_falcon_launches": D("22"), "internal_falcon_launches": D("58"), "starship_launches": D("2"),
        "launch_revenue_per_customer_launch": D("65"), "launch_development_revenue": D("700"),
        "starship_commercial_flights": D("1"), "starship_revenue_per_flight": D("150"), "starship_cor_pct": D("0.60"),
        "ending_subscribers_m": D("14"), "arpu_monthly": D("64"), "enterprise_government_revenue": D("3300"), "spectrum_mobile_revenue": D("100"), "spectrum_mobile_cor_pct": D("0.50"),
        "advertising_revenue": D("760"), "solutions_infrastructure_revenue": D("5000"), "cursor_revenue": D("1000"),
        "cursor_cor_pct": D("0.25"), "cursor_rd_pct": D("0.70"), "cursor_sga_pct": D("0.25"),
        "space_launch_cor_pct": D("0.35"), "space_development_cor_pct": D("0.45"), "space_rd": D("2200"), "space_sga": D("200"),
        "consumer_cor_pct": D("0.50"), "enterprise_cor_pct": D("0.32"), "connectivity_rd": D("350"), "connectivity_sga": D("350"),
        "advertising_cor_pct": D("0.30"), "solutions_cor_pct": D("0.45"), "ai_rd": D("4500"), "ai_sga": D("1100"), "ai_restruct": D("0"),
        "interest_expense": D("1500"), "interest_income": D("1800"), "other_income": D("0"), "tax": D("0"),
        "da": D("6500"), "sbc": D("1800"), "other_operating_items": D("-3000"),
        "space_capex_per_launch": D("28.54"), "connectivity_capex_per_net_add": D("822"), "ai_capex": D("18000"),
        "ar_pct_revenue": D("0.15"), "inventory_pct_revenue": D("0.10"),
        "deferred_revenue": D("16000"), "other_liabilities": D("13000"),
        "cursor_equity_consideration": D("60000"), "echostar_equity_consideration": D("11100.32"),
        "echostar_spectrum_assets": D("19600"), "echostar_cash_consideration": D("8500"), "noncapex_cash_flows": D("-8500"),
    },
    "FY2027E": {
        "customer_falcon_launches": D("45"), "internal_falcon_launches": D("130"), "starship_launches": D("20"),
        "launch_revenue_per_customer_launch": D("67"), "launch_development_growth": D("0.12"),
        "starship_commercial_flights": D("12"), "starship_revenue_per_flight": D("150"), "starship_cor_pct": D("0.50"),
        "ending_subscribers_m": D("18"), "arpu_monthly": D("61"), "enterprise_government_growth": D("0.30"), "spectrum_mobile_revenue": D("1000"), "spectrum_mobile_cor_pct": D("0.40"),
        "advertising_growth": D("0.10"), "solutions_infrastructure_growth": D("0.45"), "cursor_revenue": D("3000"),
        "cursor_cor_pct": D("0.25"), "cursor_rd_pct": D("0.50"), "cursor_sga_pct": D("0.25"),
        "space_launch_cor_pct": D("0.34"), "space_development_cor_pct": D("0.44"), "space_rd": D("4200"), "space_sga": D("220"),
        "consumer_cor_pct": D("0.47"), "enterprise_cor_pct": D("0.30"), "connectivity_rd": D("1000"), "connectivity_sga": D("1100"),
        "advertising_cor_pct": D("0.28"), "solutions_cor_pct": D("0.40"), "ai_rd": D("8000"), "ai_sga": D("2500"), "ai_restruct": D("0"),
        "interest_expense": D("2500"), "interest_income": D("3000"), "other_income": D("0"), "tax_rate": D("0.17"),
        "da": D("15000"), "sbc": D("4000"), "other_operating_items": D("-2000"),
        "space_capex_per_launch": D("27"), "connectivity_capex_per_net_add": D("800"), "ai_capex": D("30000"),
        "ar_pct_revenue": D("0.14"), "inventory_pct_revenue": D("0.09"),
        "deferred_revenue": D("18500"), "other_liabilities": D("15000"), "echostar_spectrum_assets": D("19600"), "noncapex_cash_flows": D("0"),
    },
    "FY2028E": {
        "customer_falcon_launches": D("50"), "internal_falcon_launches": D("140"), "starship_launches": D("60"),
        "launch_revenue_per_customer_launch": D("69"), "launch_development_growth": D("0.12"),
        "starship_commercial_flights": D("50"), "starship_revenue_per_flight": D("140"), "starship_cor_pct": D("0.40"),
        "ending_subscribers_m": D("22.5"), "arpu_monthly": D("59"), "enterprise_government_growth": D("0.25"), "spectrum_mobile_revenue": D("2500"), "spectrum_mobile_cor_pct": D("0.35"),
        "advertising_growth": D("0.08"), "solutions_infrastructure_growth": D("0.30"), "cursor_revenue": D("5000"),
        "cursor_cor_pct": D("0.25"), "cursor_rd_pct": D("0.40"), "cursor_sga_pct": D("0.20"),
        "space_launch_cor_pct": D("0.32"), "space_development_cor_pct": D("0.42"), "space_rd": D("3600"), "space_sga": D("230"),
        "consumer_cor_pct": D("0.45"), "enterprise_cor_pct": D("0.29"), "connectivity_rd": D("1200"), "connectivity_sga": D("1300"),
        "advertising_cor_pct": D("0.27"), "solutions_cor_pct": D("0.36"), "ai_rd": D("8500"), "ai_sga": D("2900"), "ai_restruct": D("0"),
        "interest_expense": D("2400"), "interest_income": D("2500"), "other_income": D("0"), "tax_rate": D("0.20"),
        "da": D("18000"), "sbc": D("5000"), "other_operating_items": D("-2000"),
        "space_capex_per_launch": D("25"), "connectivity_capex_per_net_add": D("750"), "ai_capex": D("25000"),
        "ar_pct_revenue": D("0.13"), "inventory_pct_revenue": D("0.08"),
        "deferred_revenue": D("21000"), "other_liabilities": D("17000"), "echostar_spectrum_assets": D("19600"), "noncapex_cash_flows": D("0"),
    },
}


# ---------------------------------------------------------------------------
# Revenue build.
# ---------------------------------------------------------------------------

REVENUE_LINES: dict[str, dict[str, Decimal | None]] = {}

for period, launch_mix in (("FY2023", D("0.552")), ("FY2024", D("0.682")), ("FY2025", D("0.630"))):
    space_revenue = ACTUAL_SEGMENTS[period]["Space"]["revenue"]
    launch_services = multiply(
        f"segment.{period}.launch_services_revenue",
        "reported_space_revenue",
        space_revenue,
        "rounded_launch_services_mix",
        launch_mix,
    )
    launch_development = subtract(
        f"segment.{period}.launch_development_revenue",
        "reported_space_revenue",
        space_revenue,
        "derived_launch_services_revenue",
        launch_services,
    )
    REVENUE_LINES[period] = {
        "Launch Services": launch_services,
        "Launch & Development": launch_development,
        "Starship Commercial": None,
        "Consumer": None,
        "Enterprise & Government": None,
        "Spectrum / Mobile Overlay": None,
        "Advertising": None,
        "Solutions & Infrastructure": None,
        "Cursor": None,
    }

REVENUE_LINES["H1 2026A"] = {
    "Launch Services": D("978"),
    "Launch & Development": D("603"),
    "Starship Commercial": D("0"),
    "Consumer": D("4633"),
    "Enterprise & Government": D("2915"),
    "Spectrum / Mobile Overlay": D("0"),
    "Advertising": D("710"),
    "Solutions & Infrastructure": D("2669"),
    "Cursor": D("0"),
}

H1_SUBSCRIBERS = D("12")
H2 = DRIVERS["H2 2026E"]
H2_LAUNCH_SERVICES = multiply(
    "segment.H2 2026E.launch_services_revenue",
    "customer_falcon_launches",
    H2["customer_falcon_launches"],
    "launch_revenue_per_customer_launch",
    H2["launch_revenue_per_customer_launch"],
)
H2_STARSHIP_REVENUE = multiply(
    "segment.H2 2026E.starship_commercial_revenue",
    "commercial_Starship_flights",
    H2["starship_commercial_flights"],
    "assumed_revenue_per_flight",
    H2["starship_revenue_per_flight"],
)
H2_AVG_SUBSCRIBERS = divide(
    "segment.H2 2026E.average_subscribers_m",
    "opening_plus_ending_subscribers",
    H1_SUBSCRIBERS + H2["ending_subscribers_m"],
    "two",
    D("2"),
)
H2_CONSUMER = derive(
    "segment.H2 2026E.consumer_revenue",
    "average_subscribers_m × monthly_ARPU × six_months",
    {
        "average_subscribers_m": H2_AVG_SUBSCRIBERS,
        "monthly_ARPU": H2["arpu_monthly"],
        "six_months": D("6"),
    },
    H2_AVG_SUBSCRIBERS * H2["arpu_monthly"] * D("6"),
)
REVENUE_LINES["H2 2026E"] = {
    "Launch Services": H2_LAUNCH_SERVICES,
    "Launch & Development": H2["launch_development_revenue"],
    "Starship Commercial": H2_STARSHIP_REVENUE,
    "Consumer": H2_CONSUMER,
    "Enterprise & Government": H2["enterprise_government_revenue"],
    "Spectrum / Mobile Overlay": H2["spectrum_mobile_revenue"],
    "Advertising": H2["advertising_revenue"],
    "Solutions & Infrastructure": H2["solutions_infrastructure_revenue"],
    "Cursor": H2["cursor_revenue"],
}

REVENUE_LINES["FY2026E"] = {}
for line in REVENUE_LINES["H1 2026A"]:
    REVENUE_LINES["FY2026E"][line] = sum_named(
        f"segment.FY2026E.{line.lower().replace(' ', '_').replace('&', 'and')}",
        {"H1_2026_actual": REVENUE_LINES["H1 2026A"][line] or D("0"), "H2_2026_forecast": REVENUE_LINES["H2 2026E"][line] or D("0")},
    )

previous_subscribers = H2["ending_subscribers_m"]
for period, previous_period in (("FY2027E", "FY2026E"), ("FY2028E", "FY2027E")):
    driver = DRIVERS[period]
    launch_services = multiply(
        f"segment.{period}.launch_services_revenue",
        "customer_falcon_launches",
        driver["customer_falcon_launches"],
        "launch_revenue_per_customer_launch",
        driver["launch_revenue_per_customer_launch"],
    )
    launch_development = derive(
        f"segment.{period}.launch_development_revenue",
        "prior_launch_development_revenue × (one + growth)",
        {
            "prior_launch_development_revenue": REVENUE_LINES[previous_period]["Launch & Development"] or D("0"),
            "one_plus_growth": D("1") + driver["launch_development_growth"],
        },
        (REVENUE_LINES[previous_period]["Launch & Development"] or D("0")) * (D("1") + driver["launch_development_growth"]),
    )
    avg_subscribers = divide(
        f"segment.{period}.average_subscribers_m",
        "opening_plus_ending_subscribers",
        previous_subscribers + driver["ending_subscribers_m"],
        "two",
        D("2"),
    )
    consumer = derive(
        f"segment.{period}.consumer_revenue",
        "average_subscribers_m × monthly_ARPU × twelve_months",
        {"average_subscribers_m": avg_subscribers, "monthly_ARPU": driver["arpu_monthly"], "twelve_months": D("12")},
        avg_subscribers * driver["arpu_monthly"] * D("12"),
    )
    enterprise = derive(
        f"segment.{period}.enterprise_government_revenue",
        "prior_enterprise_government_revenue × (one + growth)",
        {
            "prior_enterprise_government_revenue": REVENUE_LINES[previous_period]["Enterprise & Government"] or D("0"),
            "one_plus_growth": D("1") + driver["enterprise_government_growth"],
        },
        (REVENUE_LINES[previous_period]["Enterprise & Government"] or D("0")) * (D("1") + driver["enterprise_government_growth"]),
    )
    advertising = derive(
        f"segment.{period}.advertising_revenue",
        "prior_advertising_revenue × (one + growth)",
        {
            "prior_advertising_revenue": REVENUE_LINES[previous_period]["Advertising"] or D("0"),
            "one_plus_growth": D("1") + driver["advertising_growth"],
        },
        (REVENUE_LINES[previous_period]["Advertising"] or D("0")) * (D("1") + driver["advertising_growth"]),
    )
    solutions = derive(
        f"segment.{period}.solutions_infrastructure_revenue",
        "prior_solutions_infrastructure_revenue × (one + growth)",
        {
            "prior_solutions_infrastructure_revenue": REVENUE_LINES[previous_period]["Solutions & Infrastructure"] or D("0"),
            "one_plus_growth": D("1") + driver["solutions_infrastructure_growth"],
        },
        (REVENUE_LINES[previous_period]["Solutions & Infrastructure"] or D("0")) * (D("1") + driver["solutions_infrastructure_growth"]),
    )
    starship_revenue = multiply(
        f"segment.{period}.starship_commercial_revenue",
        "commercial_Starship_flights",
        driver["starship_commercial_flights"],
        "assumed_revenue_per_flight",
        driver["starship_revenue_per_flight"],
    )
    REVENUE_LINES[period] = {
        "Launch Services": launch_services,
        "Launch & Development": launch_development,
        "Starship Commercial": starship_revenue,
        "Consumer": consumer,
        "Enterprise & Government": enterprise,
        "Spectrum / Mobile Overlay": driver["spectrum_mobile_revenue"],
        "Advertising": advertising,
        "Solutions & Infrastructure": solutions,
        "Cursor": driver["cursor_revenue"],
    }
    previous_subscribers = driver["ending_subscribers_m"]


# ---------------------------------------------------------------------------
# Forecast segment income statements.
# ---------------------------------------------------------------------------

def forecast_segment_period(period: str, revenue_lines: dict[str, Decimal | None]) -> dict[str, dict[str, Decimal]]:
    driver = DRIVERS[period if period != "FY2026E" else "H2 2026E"]
    output: dict[str, dict[str, Decimal]] = {}

    if period == "FY2026E":
        h1 = ACTUAL_SEGMENTS["H1 2026A"]
        h2_lines = REVENUE_LINES["H2 2026E"]
        h2_space_cor = sum_named(
            "segment.H2 2026E.space_cor",
            {
                "launch_services_cor": multiply(
                    "segment.H2 2026E.launch_services_cor",
                    "launch_services_revenue",
                    h2_lines["Launch Services"] or D("0"),
                    "launch_services_cor_pct",
                    driver["space_launch_cor_pct"],
                ),
                "launch_development_cor": multiply(
                    "segment.H2 2026E.launch_development_cor",
                    "launch_development_revenue",
                    h2_lines["Launch & Development"] or D("0"),
                    "launch_development_cor_pct",
                    driver["space_development_cor_pct"],
                ),
                "starship_commercial_cor": multiply(
                    "segment.H2 2026E.starship_commercial_cor",
                    "starship_commercial_revenue",
                    h2_lines["Starship Commercial"] or D("0"),
                    "starship_commercial_cor_pct",
                    driver["starship_cor_pct"],
                ),
            },
        )
        h2_connectivity_cor = sum_named(
            "segment.H2 2026E.connectivity_cor",
            {
                "consumer_cor": multiply(
                    "segment.H2 2026E.consumer_cor",
                    "consumer_revenue",
                    h2_lines["Consumer"] or D("0"),
                    "consumer_cor_pct",
                    driver["consumer_cor_pct"],
                ),
                "enterprise_government_cor": multiply(
                    "segment.H2 2026E.enterprise_government_cor",
                    "enterprise_government_revenue",
                    h2_lines["Enterprise & Government"] or D("0"),
                    "enterprise_government_cor_pct",
                    driver["enterprise_cor_pct"],
                ),
                "spectrum_mobile_cor": multiply(
                    "segment.H2 2026E.spectrum_mobile_cor",
                    "spectrum_mobile_revenue",
                    h2_lines["Spectrum / Mobile Overlay"] or D("0"),
                    "spectrum_mobile_cor_pct",
                    driver["spectrum_mobile_cor_pct"],
                ),
            },
        )
        h2_ai_cor = sum_named(
            "segment.H2 2026E.ai_cor",
            {
                "advertising_cor": multiply(
                    "segment.H2 2026E.advertising_cor",
                    "advertising_revenue",
                    h2_lines["Advertising"] or D("0"),
                    "advertising_cor_pct",
                    driver["advertising_cor_pct"],
                ),
                "solutions_infrastructure_cor": multiply(
                    "segment.H2 2026E.solutions_infrastructure_cor",
                    "solutions_infrastructure_revenue",
                    h2_lines["Solutions & Infrastructure"] or D("0"),
                    "solutions_cor_pct",
                    driver["solutions_cor_pct"],
                ),
                "cursor_cor": multiply(
                    "segment.H2 2026E.cursor_cor",
                    "Cursor_revenue",
                    h2_lines["Cursor"] or D("0"),
                    "Cursor_cor_pct",
                    driver["cursor_cor_pct"],
                ),
            },
        )
        h2_cursor_rd = multiply("segment.H2 2026E.cursor_rd", "Cursor_revenue", h2_lines["Cursor"] or D("0"), "Cursor_rd_pct", driver["cursor_rd_pct"])
        h2_cursor_sga = multiply("segment.H2 2026E.cursor_sga", "Cursor_revenue", h2_lines["Cursor"] or D("0"), "Cursor_sga_pct", driver["cursor_sga_pct"])
        output["Space"] = {
            "revenue": sum_named("segment.FY2026E.space_revenue", {"launch_services": revenue_lines["Launch Services"] or D("0"), "launch_development": revenue_lines["Launch & Development"] or D("0"), "starship_commercial": revenue_lines["Starship Commercial"] or D("0")}),
            "cor": sum_named("segment.FY2026E.space_cor", {"H1_actual": h1["Space"]["cor"], "H2_forecast": h2_space_cor}),
            "rd": sum_named("segment.FY2026E.space_rd", {"H1_actual": h1["Space"]["rd"], "H2_forecast": driver["space_rd"]}),
            "sga": sum_named("segment.FY2026E.space_sga", {"H1_actual": h1["Space"]["sga"], "H2_forecast": driver["space_sga"]}),
            "restruct": D("0"), "impairment": D("0"),
        }
        output["Connectivity"] = {
            "revenue": sum_named("segment.FY2026E.connectivity_revenue", {"consumer": revenue_lines["Consumer"] or D("0"), "enterprise_government": revenue_lines["Enterprise & Government"] or D("0"), "spectrum_mobile_overlay": revenue_lines["Spectrum / Mobile Overlay"] or D("0")}),
            "cor": sum_named("segment.FY2026E.connectivity_cor", {"H1_actual": h1["Connectivity"]["cor"], "H2_forecast": h2_connectivity_cor}),
            "rd": sum_named("segment.FY2026E.connectivity_rd", {"H1_actual": h1["Connectivity"]["rd"], "H2_forecast": driver["connectivity_rd"]}),
            "sga": sum_named("segment.FY2026E.connectivity_sga", {"H1_actual": h1["Connectivity"]["sga"], "H2_forecast": driver["connectivity_sga"]}),
            "restruct": D("0"), "impairment": D("0"),
        }
        output["AI"] = {
            "revenue": sum_named("segment.FY2026E.ai_revenue", {"advertising": revenue_lines["Advertising"] or D("0"), "solutions_infrastructure": revenue_lines["Solutions & Infrastructure"] or D("0"), "Cursor": revenue_lines["Cursor"] or D("0")}),
            "cor": sum_named("segment.FY2026E.ai_cor", {"H1_actual": h1["AI"]["cor"], "H2_forecast": h2_ai_cor}),
            "rd": sum_named("segment.FY2026E.ai_rd", {"H1_actual": h1["AI"]["rd"], "H2_xAI_X_forecast": driver["ai_rd"], "H2_Cursor_forecast": h2_cursor_rd}),
            "sga": sum_named("segment.FY2026E.ai_sga", {"H1_actual": h1["AI"]["sga"], "H2_xAI_X_forecast": driver["ai_sga"], "H2_Cursor_forecast": h2_cursor_sga}),
            "restruct": sum_named("segment.FY2026E.ai_restruct", {"H1_actual": h1["AI"]["restruct"], "H2_forecast": driver["ai_restruct"]}),
            "impairment": D("0"),
        }
    else:
        starship_cor = multiply(f"segment.{period}.starship_commercial_cor", "starship_commercial_revenue", revenue_lines["Starship Commercial"] or D("0"), "starship_commercial_cor_pct", driver["starship_cor_pct"])
        spectrum_cor = multiply(f"segment.{period}.spectrum_mobile_cor", "spectrum_mobile_revenue", revenue_lines["Spectrum / Mobile Overlay"] or D("0"), "spectrum_mobile_cor_pct", driver["spectrum_mobile_cor_pct"])
        cursor_cor = multiply(f"segment.{period}.cursor_cor", "Cursor_revenue", revenue_lines["Cursor"] or D("0"), "Cursor_cor_pct", driver["cursor_cor_pct"])
        cursor_rd = multiply(f"segment.{period}.cursor_rd", "Cursor_revenue", revenue_lines["Cursor"] or D("0"), "Cursor_rd_pct", driver["cursor_rd_pct"])
        cursor_sga = multiply(f"segment.{period}.cursor_sga", "Cursor_revenue", revenue_lines["Cursor"] or D("0"), "Cursor_sga_pct", driver["cursor_sga_pct"])
        output["Space"] = {
            "revenue": sum_named(f"segment.{period}.space_revenue", {"launch_services": revenue_lines["Launch Services"] or D("0"), "launch_development": revenue_lines["Launch & Development"] or D("0"), "starship_commercial": revenue_lines["Starship Commercial"] or D("0")}),
            "cor": sum_named(
                f"segment.{period}.space_cor",
                {
                    "launch_services_cor": multiply(f"segment.{period}.launch_services_cor", "launch_services_revenue", revenue_lines["Launch Services"] or D("0"), "launch_services_cor_pct", driver["space_launch_cor_pct"]),
                    "launch_development_cor": multiply(f"segment.{period}.launch_development_cor", "launch_development_revenue", revenue_lines["Launch & Development"] or D("0"), "launch_development_cor_pct", driver["space_development_cor_pct"]),
                    "starship_commercial_cor": starship_cor,
                },
            ),
            "rd": driver["space_rd"], "sga": driver["space_sga"], "restruct": D("0"), "impairment": D("0"),
        }
        output["Connectivity"] = {
            "revenue": sum_named(f"segment.{period}.connectivity_revenue", {"consumer": revenue_lines["Consumer"] or D("0"), "enterprise_government": revenue_lines["Enterprise & Government"] or D("0"), "spectrum_mobile_overlay": revenue_lines["Spectrum / Mobile Overlay"] or D("0")}),
            "cor": sum_named(
                f"segment.{period}.connectivity_cor",
                {
                    "consumer_cor": multiply(f"segment.{period}.consumer_cor", "consumer_revenue", revenue_lines["Consumer"] or D("0"), "consumer_cor_pct", driver["consumer_cor_pct"]),
                    "enterprise_government_cor": multiply(f"segment.{period}.enterprise_government_cor", "enterprise_government_revenue", revenue_lines["Enterprise & Government"] or D("0"), "enterprise_government_cor_pct", driver["enterprise_cor_pct"]),
                    "spectrum_mobile_cor": spectrum_cor,
                },
            ),
            "rd": driver["connectivity_rd"], "sga": driver["connectivity_sga"], "restruct": D("0"), "impairment": D("0"),
        }
        output["AI"] = {
            "revenue": sum_named(f"segment.{period}.ai_revenue", {"advertising": revenue_lines["Advertising"] or D("0"), "solutions_infrastructure": revenue_lines["Solutions & Infrastructure"] or D("0"), "Cursor": revenue_lines["Cursor"] or D("0")}),
            "cor": sum_named(
                f"segment.{period}.ai_cor",
                {
                    "advertising_cor": multiply(f"segment.{period}.advertising_cor", "advertising_revenue", revenue_lines["Advertising"] or D("0"), "advertising_cor_pct", driver["advertising_cor_pct"]),
                    "solutions_infrastructure_cor": multiply(f"segment.{period}.solutions_infrastructure_cor", "solutions_infrastructure_revenue", revenue_lines["Solutions & Infrastructure"] or D("0"), "solutions_cor_pct", driver["solutions_cor_pct"]),
                    "Cursor_cor": cursor_cor,
                },
            ),
            "rd": sum_named(f"segment.{period}.ai_rd", {"xAI_X_R&D": driver["ai_rd"], "Cursor_R&D": cursor_rd}),
            "sga": sum_named(f"segment.{period}.ai_sga", {"xAI_X_SG&A": driver["ai_sga"], "Cursor_SG&A": cursor_sga}),
            "restruct": driver["ai_restruct"], "impairment": D("0"),
        }

    for segment, values in output.items():
        expenses = sum_named(
            f"segment.{period}.{segment.lower()}.operating_expenses",
            {"cost_of_revenue": values["cor"], "rd": values["rd"], "sga": values["sga"], "restructuring": values["restruct"], "impairment": values["impairment"]},
        )
        values["ebit"] = subtract(f"segment.{period}.{segment.lower()}.ebit", "revenue", values["revenue"], "operating_expenses", expenses)
    return output


FORECAST_SEGMENTS = {
    period: forecast_segment_period(period, REVENUE_LINES[period])
    for period in ("FY2026E", "FY2027E", "FY2028E")
}
ALL_SEGMENTS = {**ACTUAL_SEGMENTS, **FORECAST_SEGMENTS}

for period in ACTUAL_SEGMENTS:
    for segment, values in ACTUAL_SEGMENTS[period].items():
        expenses = values["cor"] + values["rd"] + values["sga"] + values["restruct"] + values["impairment"]
        values["ebit"] = values["revenue"] - expenses


# ---------------------------------------------------------------------------
# Consolidated income statement, calculated from segments.
# ---------------------------------------------------------------------------

INCOME: dict[str, dict[str, Decimal]] = {}
for period, segments in ALL_SEGMENTS.items():
    statement: dict[str, Decimal] = {}
    for metric in ("revenue", "cor", "rd", "sga", "restruct", "impairment", "ebit"):
        statement[metric] = sum_named(
            f"income.{period}.{metric}",
            {segment.lower(): values[metric] for segment, values in segments.items()},
        )
    statement["gross_profit"] = subtract(f"income.{period}.gross_profit", "revenue", statement["revenue"], "cost_of_revenue", statement["cor"])
    INCOME[period] = statement

H2_SEGMENTS: dict[str, dict[str, Decimal]] = {}
for segment in ("Space", "Connectivity", "AI"):
    H2_SEGMENTS[segment] = {}
    for metric in ("revenue", "cor", "rd", "sga", "restruct", "impairment", "ebit"):
        H2_SEGMENTS[segment][metric] = subtract(
            f"segment.H2 2026E.{segment.lower()}.{metric}",
            "FY2026_forecast",
            FORECAST_SEGMENTS["FY2026E"][segment][metric],
            "H1_2026_actual",
            ACTUAL_SEGMENTS["H1 2026A"][segment][metric],
        )

INCOME["H2 2026E"] = {}
for metric in ("revenue", "cor", "rd", "sga", "restruct", "impairment", "ebit"):
    INCOME["H2 2026E"][metric] = sum_named(
        f"income.H2 2026E.{metric}",
        {segment.lower(): values[metric] for segment, values in H2_SEGMENTS.items()},
    )
INCOME["H2 2026E"]["gross_profit"] = subtract(
    "income.H2 2026E.gross_profit",
    "revenue",
    INCOME["H2 2026E"]["revenue"],
    "cost_of_revenue",
    INCOME["H2 2026E"]["cor"],
)

for period in ("FY2023", "FY2024", "FY2025", "H1 2026A"):
    finance = ACTUAL_FINANCE[period]
    INCOME[period].update(finance)
    INCOME[period]["pretax"] = derive(
        f"income.{period}.pretax",
        "EBIT - interest_expense + interest_income + other_income",
        {
            "EBIT": INCOME[period]["ebit"], "interest_expense": finance["interest_expense"],
            "interest_income": finance["interest_income"], "other_income": finance["other_income"],
        },
        INCOME[period]["ebit"] - finance["interest_expense"] + finance["interest_income"] + finance["other_income"],
    )

H2_FINANCE = {key: H2[key] for key in ("interest_expense", "interest_income", "other_income", "tax")}
H2_PRETAX = derive(
    "income.H2 2026E.pretax",
    "EBIT - interest_expense + interest_income + other_income",
    {"EBIT": INCOME["H2 2026E"]["ebit"], **{k: H2_FINANCE[k] for k in ("interest_expense", "interest_income", "other_income")}},
    INCOME["H2 2026E"]["ebit"] - H2_FINANCE["interest_expense"] + H2_FINANCE["interest_income"] + H2_FINANCE["other_income"],
)
H2_NET_INCOME = subtract("income.H2 2026E.net_income", "pretax_income", H2_PRETAX, "tax_provision", H2_FINANCE["tax"])
INCOME["H2 2026E"].update(H2_FINANCE | {"pretax": H2_PRETAX, "net_income": H2_NET_INCOME})

for key in ("interest_expense", "interest_income", "other_income", "tax", "net_income"):
    INCOME["FY2026E"][key] = sum_named(
        f"income.FY2026E.{key}",
        {"H1_2026_actual": INCOME["H1 2026A"][key], "H2_2026_forecast": INCOME["H2 2026E"][key]},
    )
INCOME["FY2026E"]["pretax"] = derive(
    "income.FY2026E.pretax",
    "EBIT - interest_expense + interest_income + other_income",
    {
        "EBIT": INCOME["FY2026E"]["ebit"], "interest_expense": INCOME["FY2026E"]["interest_expense"],
        "interest_income": INCOME["FY2026E"]["interest_income"], "other_income": INCOME["FY2026E"]["other_income"],
    },
    INCOME["FY2026E"]["ebit"] - INCOME["FY2026E"]["interest_expense"] + INCOME["FY2026E"]["interest_income"] + INCOME["FY2026E"]["other_income"],
)

for period in ("FY2027E", "FY2028E"):
    driver = DRIVERS[period]
    INCOME[period]["interest_expense"] = driver["interest_expense"]
    INCOME[period]["interest_income"] = driver["interest_income"]
    INCOME[period]["other_income"] = driver["other_income"]
    pretax = derive(
        f"income.{period}.pretax",
        "EBIT - interest_expense + interest_income + other_income",
        {
            "EBIT": INCOME[period]["ebit"], "interest_expense": driver["interest_expense"],
            "interest_income": driver["interest_income"], "other_income": driver["other_income"],
        },
        INCOME[period]["ebit"] - driver["interest_expense"] + driver["interest_income"] + driver["other_income"],
    )
    tax = multiply(f"income.{period}.tax", "positive_pretax_income", max(pretax, D("0")), "tax_rate", driver["tax_rate"])
    net_income = subtract(f"income.{period}.net_income", "pretax_income", pretax, "tax_provision", tax)
    INCOME[period].update({"pretax": pretax, "tax": tax, "net_income": net_income})


# ---------------------------------------------------------------------------
# Capex, cash flow and balance sheet.
# ---------------------------------------------------------------------------

CAPEX: dict[str, dict[str, Decimal]] = {
    "H1 2026A": {"Space": D("2226"), "Connectivity": D("2699"), "AI": D("23551")},
}

subscriber_openings = {"H2 2026E": H1_SUBSCRIBERS, "FY2027E": H2["ending_subscribers_m"], "FY2028E": DRIVERS["FY2027E"]["ending_subscribers_m"]}
for period in ("H2 2026E", "FY2027E", "FY2028E"):
    driver = DRIVERS[period]
    total_launches = sum_named(
        f"cashflow.{period}.total_launches",
        {
            "customer_falcon_launches": driver["customer_falcon_launches"],
            "internal_falcon_launches": driver["internal_falcon_launches"],
            "starship_launches": driver["starship_launches"],
        },
    )
    space_capex = multiply(
        f"cashflow.{period}.space_capex",
        "total_launches",
        total_launches,
        "space_capex_per_launch",
        driver["space_capex_per_launch"],
    )
    net_adds = subtract(
        f"cashflow.{period}.subscriber_net_adds_m",
        "ending_subscribers_m",
        driver["ending_subscribers_m"],
        "opening_subscribers_m",
        subscriber_openings[period],
    )
    connectivity_capex = multiply(
        f"cashflow.{period}.connectivity_capex",
        "subscriber_net_adds_m",
        net_adds,
        "capex_per_net_add",
        driver["connectivity_capex_per_net_add"],
    )
    CAPEX[period] = {"Space": space_capex, "Connectivity": connectivity_capex, "AI": driver["ai_capex"]}

CAPEX["FY2026E"] = {
    segment: sum_named(
        f"cashflow.FY2026E.{segment.lower()}_capex",
        {"H1_2026_actual": CAPEX["H1 2026A"][segment], "H2_2026_forecast": CAPEX["H2 2026E"][segment]},
    )
    for segment in ("Space", "Connectivity", "AI")
}

BALANCE: dict[str, dict[str, Decimal]] = {}
for period, values in ACTUAL_BALANCE.items():
    other_assets = derive(
        f"balance.{period}.other_assets",
        "total_assets - cash - securities - accounts_receivable - inventory - PP&E - spectrum_assets",
        {
            "total_assets": values["total_assets"], "cash": values["cash"], "securities": values["securities"],
            "accounts_receivable": values["ar"], "inventory": values["inventory"], "PP&E": values["ppe"], "spectrum_assets": values["spectrum_assets"],
        },
        values["total_assets"] - values["cash"] - values["securities"] - values["ar"] - values["inventory"] - values["ppe"] - values["spectrum_assets"],
    )
    other_liabilities = derive(
        f"balance.{period}.other_liabilities",
        "total_liabilities - debt_and_finance_leases - deferred_revenue",
        {
            "total_liabilities": values["total_liabilities"], "debt_and_finance_leases": values["debt"],
            "deferred_revenue": values["deferred_revenue"],
        },
        values["total_liabilities"] - values["debt"] - values["deferred_revenue"],
    )
    BALANCE[period] = values | {"other_assets": other_assets, "other_liabilities": other_liabilities}

H1_OTHER_NONCASH = sum_named(
    "cashflow.H1 2026A.other_noncash",
    {"deferred_tax": D("-9"), "digital_asset_loss": D("539"), "impairment_disposals": D("40"), "debt_extinguishment": D("1545"), "other": D("-72")},
)
H1_PREPAIDS_AP = sum_named(
    "cashflow.H1 2026A.prepaids_ap_contribution",
    {"prepaids_and_other_assets": D("102"), "accounts_payable": D("-88")},
)
H1_CF_DETAIL = {
    "net_income": D("-4817"), "da": D("5290"), "sbc": D("1470"), "other_noncash": H1_OTHER_NONCASH,
    "ar_contribution": D("-2003"), "inventory_contribution": D("-827"), "prepaids_ap_contribution": H1_PREPAIDS_AP,
    "deferred_revenue_contribution": D("2169"), "other_liabilities_contribution": D("127"),
}
H1_CF_DETAIL["ocf"] = sum_named("cashflow.H1 2026A.ocf", H1_CF_DETAIL)
H1_CF_DETAIL["total_capex"] = sum_named("cashflow.H1 2026A.total_capex", {k.lower(): v for k, v in CAPEX["H1 2026A"].items()})
H1_CF_DETAIL["fcf"] = subtract("cashflow.H1 2026A.fcf", "operating_cash_flow", H1_CF_DETAIL["ocf"], "capital_expenditures", H1_CF_DETAIL["total_capex"])

CASHFLOW: dict[str, dict[str, Decimal]] = {"H1 2026A": H1_CF_DETAIL}

START_BALANCE_PERIOD = {"H2 2026E": "H1 2026A", "FY2027E": "FY2026E", "FY2028E": "FY2027E"}
START_CASH = {"H2 2026E": BALANCE["H1 2026A"]["cash"]}
START_SECURITIES = {"H2 2026E": BALANCE["H1 2026A"]["securities"]}
START_EQUITY = {"H2 2026E": BALANCE["H1 2026A"]["equity"]}
START_PPE = {"H2 2026E": BALANCE["H1 2026A"]["ppe"]}

for period in ("H2 2026E", "FY2027E", "FY2028E"):
    driver = DRIVERS[period]
    income_period = "H2 2026E" if period == "H2 2026E" else period
    prior_balance_key = START_BALANCE_PERIOD[period]
    prior = BALANCE[prior_balance_key]
    annual_revenue = INCOME["FY2026E"]["revenue"] if period == "H2 2026E" else INCOME[period]["revenue"]
    ending_ar = multiply(f"balance.{period}.accounts_receivable", "annual_revenue", annual_revenue, "accounts_receivable_pct_revenue", driver["ar_pct_revenue"])
    ending_inventory = multiply(f"balance.{period}.inventory", "annual_revenue", annual_revenue, "inventory_pct_revenue", driver["inventory_pct_revenue"])
    ar_contribution = derive(
        f"cashflow.{period}.accounts_receivable_contribution",
        "negative(ending_accounts_receivable - opening_accounts_receivable)",
        {"ending_accounts_receivable": ending_ar, "opening_accounts_receivable": prior["ar"]},
        -(ending_ar - prior["ar"]),
    )
    inventory_contribution = derive(
        f"cashflow.{period}.inventory_contribution",
        "negative(ending_inventory - opening_inventory)",
        {"ending_inventory": ending_inventory, "opening_inventory": prior["inventory"]},
        -(ending_inventory - prior["inventory"]),
    )
    deferred_contribution = subtract(
        f"cashflow.{period}.deferred_revenue_contribution",
        "ending_deferred_revenue",
        driver["deferred_revenue"],
        "opening_deferred_revenue",
        prior["deferred_revenue"],
    )
    other_liability_contribution = subtract(
        f"cashflow.{period}.other_liabilities_contribution",
        "ending_other_liabilities",
        driver["other_liabilities"],
        "opening_other_liabilities",
        prior["other_liabilities"],
    )
    ocf = sum_named(
        f"cashflow.{period}.ocf",
        {
            "net_income": INCOME[income_period]["net_income"], "depreciation_and_amortization": driver["da"],
            "share_based_compensation": driver["sbc"], "accounts_receivable_contribution": ar_contribution,
            "inventory_contribution": inventory_contribution, "deferred_revenue_contribution": deferred_contribution,
            "other_liabilities_contribution": other_liability_contribution, "other_operating_items": driver["other_operating_items"],
        },
    )
    total_capex = sum_named(f"cashflow.{period}.total_capex", {k.lower(): v for k, v in CAPEX[period].items()})
    fcf = subtract(f"cashflow.{period}.fcf", "operating_cash_flow", ocf, "capital_expenditures", total_capex)
    opening_cash = START_CASH[period]
    ending_cash = sum_named(
        f"cashflow.{period}.ending_cash",
        {"opening_cash": opening_cash, "free_cash_flow": fcf, "net_financing_noncapex_investing": driver["noncapex_cash_flows"]},
    )
    ending_securities = START_SECURITIES[period]
    ending_liquidity = sum_named(
        f"cashflow.{period}.ending_liquidity",
        {"ending_cash": ending_cash, "marketable_securities": ending_securities},
    )
    ppe = derive(
        f"balance.{period}.PP&E",
        "opening_PP&E + capital_expenditures - depreciation_and_amortization",
        {"opening_PP&E": START_PPE[period], "capital_expenditures": total_capex, "depreciation_and_amortization": driver["da"]},
        START_PPE[period] + total_capex - driver["da"],
    )
    cursor_equity_issuance = driver.get("cursor_equity_consideration", D("0"))
    echostar_equity_issuance = driver.get("echostar_equity_consideration", D("0"))
    spectrum_assets = driver["echostar_spectrum_assets"]
    equity = sum_named(
        f"balance.{period}.equity",
        {
            "opening_equity": START_EQUITY[period], "net_income": INCOME[income_period]["net_income"],
            "share_based_compensation": driver["sbc"], "stock_issued_for_Cursor": cursor_equity_issuance,
            "pending_stock_issued_for_EchoStar": echostar_equity_issuance,
        },
    )
    debt = prior["debt"]
    preferred = D("0")
    total_liabilities = sum_named(
        f"balance.{period}.total_liabilities",
        {"debt_and_finance_leases": debt, "deferred_revenue": driver["deferred_revenue"], "other_liabilities": driver["other_liabilities"]},
    )
    total_liabilities_equity = sum_named(
        f"balance.{period}.total_liabilities_and_equity",
        {"total_liabilities": total_liabilities, "redeemable_preferred": preferred, "shareholders_equity": equity},
    )
    other_assets = derive(
        f"balance.{period}.other_assets",
        "total_liabilities_and_equity - cash - securities - accounts_receivable - inventory - PP&E - spectrum_assets",
        {
            "total_liabilities_and_equity": total_liabilities_equity, "cash": ending_cash, "securities": ending_securities,
            "accounts_receivable": ending_ar, "inventory": ending_inventory, "PP&E": ppe, "spectrum_assets": spectrum_assets,
        },
        total_liabilities_equity - ending_cash - ending_securities - ending_ar - ending_inventory - ppe - spectrum_assets,
    )
    total_assets = sum_named(
        f"balance.{period}.total_assets",
        {"cash": ending_cash, "securities": ending_securities, "accounts_receivable": ending_ar, "inventory": ending_inventory, "PP&E": ppe, "spectrum_assets": spectrum_assets, "other_assets": other_assets},
    )
    BALANCE[period] = {
        "cash": ending_cash, "securities": ending_securities, "ar": ending_ar, "inventory": ending_inventory,
        "ppe": ppe, "spectrum_assets": spectrum_assets, "other_assets": other_assets, "total_assets": total_assets, "debt": debt,
        "deferred_revenue": driver["deferred_revenue"], "other_liabilities": driver["other_liabilities"],
        "total_liabilities": total_liabilities, "redeemable_preferred": preferred, "equity": equity,
    }
    CASHFLOW[period] = {
        "net_income": INCOME[income_period]["net_income"], "da": driver["da"], "sbc": driver["sbc"],
        "other_noncash": D("0"), "ar_contribution": ar_contribution, "inventory_contribution": inventory_contribution,
        "prepaids_ap_contribution": D("0"), "deferred_revenue_contribution": deferred_contribution,
        "other_liabilities_contribution": other_liability_contribution, "other_operating_items": driver["other_operating_items"],
        "ocf": ocf, "total_capex": total_capex, "fcf": fcf, "noncapex_cash_flows": driver["noncapex_cash_flows"],
        "ending_cash": ending_cash, "ending_securities": ending_securities, "ending_liquidity": ending_liquidity,
    }
    if period == "H2 2026E":
        BALANCE["FY2026E"] = BALANCE.pop(period)
        CASHFLOW["H2 2026E"] = CASHFLOW.pop(period)
        balance_key = "FY2026E"
    else:
        balance_key = period
    if period == "H2 2026E":
        START_CASH["FY2027E"] = BALANCE[balance_key]["cash"]
        START_SECURITIES["FY2027E"] = BALANCE[balance_key]["securities"]
        START_EQUITY["FY2027E"] = BALANCE[balance_key]["equity"]
        START_PPE["FY2027E"] = BALANCE[balance_key]["ppe"]
    elif period == "FY2027E":
        START_CASH["FY2028E"] = BALANCE[balance_key]["cash"]
        START_SECURITIES["FY2028E"] = BALANCE[balance_key]["securities"]
        START_EQUITY["FY2028E"] = BALANCE[balance_key]["equity"]
        START_PPE["FY2028E"] = BALANCE[balance_key]["ppe"]

# FY2026 cash flow equals H1 actual plus H2 forecast.
CASHFLOW["FY2026E"] = {}
for metric in ("net_income", "da", "sbc", "other_noncash", "ar_contribution", "inventory_contribution", "prepaids_ap_contribution", "deferred_revenue_contribution", "other_liabilities_contribution", "ocf", "total_capex", "fcf"):
    CASHFLOW["FY2026E"][metric] = sum_named(
        f"cashflow.FY2026E.{metric}",
        {"H1_2026_actual": CASHFLOW["H1 2026A"][metric], "H2_2026_forecast": CASHFLOW["H2 2026E"][metric]},
    )
CASHFLOW["FY2026E"]["other_operating_items"] = CASHFLOW["H2 2026E"]["other_operating_items"]
H1_NONCAPEX = derive(
    "cashflow.H1 2026A.noncapex_cash_flows",
    "ending_cash - opening_cash - free_cash_flow",
    {"ending_cash": D("93522"), "opening_cash": D("24747"), "free_cash_flow": CASHFLOW["H1 2026A"]["fcf"]},
    D("93522") - D("24747") - CASHFLOW["H1 2026A"]["fcf"],
)
CASHFLOW["H1 2026A"]["noncapex_cash_flows"] = H1_NONCAPEX
CASHFLOW["H1 2026A"]["ending_cash"] = BALANCE["H1 2026A"]["cash"]
CASHFLOW["H1 2026A"]["ending_securities"] = BALANCE["H1 2026A"]["securities"]
CASHFLOW["H1 2026A"]["ending_liquidity"] = sum_named(
    "cashflow.H1 2026A.ending_liquidity",
    {"ending_cash": BALANCE["H1 2026A"]["cash"], "marketable_securities": BALANCE["H1 2026A"]["securities"]},
)
CASHFLOW["FY2026E"]["noncapex_cash_flows"] = sum_named(
    "cashflow.FY2026E.noncapex_cash_flows",
    {"H1_actual_derived": H1_NONCAPEX, "H2_forecast": CASHFLOW["H2 2026E"]["noncapex_cash_flows"]},
)
CASHFLOW["FY2026E"]["ending_cash"] = BALANCE["FY2026E"]["cash"]
CASHFLOW["FY2026E"]["ending_securities"] = BALANCE["FY2026E"]["securities"]
CASHFLOW["FY2026E"]["ending_liquidity"] = sum_named(
    "cashflow.FY2026E.ending_liquidity",
    {"ending_cash": BALANCE["FY2026E"]["cash"], "marketable_securities": BALANCE["FY2026E"]["securities"]},
)

BASIC_SHARES = {
    "H1 2026A": D("13176"),
    "FY2026E": sum_named(
        "balance.FY2026E.basic_shares",
        {
            "July_28_basic_shares_m": D("13181.779945"),
            "Cursor_merger_shares_m": D("389.289254"),
            "Cursor_vested_RSU_shares_m": D("1.752426"),
            "pending_EchoStar_shares_m": D("261.8"),
        },
    ),
    "FY2027E": D("13834.621625"),
    "FY2028E": D("13834.621625"),
}


# ---------------------------------------------------------------------------
# Reconciliation checks.
# ---------------------------------------------------------------------------

CHECKS: list[tuple[str, bool, str]] = []
for period in ("FY2023", "FY2024", "FY2025", "H1 2026A"):
    for metric in ("revenue", "cor", "rd", "sga", "restruct", "impairment", "ebit"):
        CHECKS.append((
            f"{period} segment {metric} equals reported consolidated",
            close(INCOME[period][metric], REPORTED_CONSOLIDATED[period][metric]),
            f"segments={plain(INCOME[period][metric])}; reported={plain(REPORTED_CONSOLIDATED[period][metric])}",
        ))

for period in ("FY2026E", "FY2027E", "FY2028E"):
    revenue_sum = sum((REVENUE_LINES[period][line] or D("0")) for line in REVENUE_LINES[period])
    CHECKS.append((f"{period} segment revenue lines equal consolidated revenue", close(revenue_sum, INCOME[period]["revenue"]), f"lines={plain(revenue_sum)}; consolidated={plain(INCOME[period]['revenue'])}"))
    ebit_sum = sum(FORECAST_SEGMENTS[period][segment]["ebit"] for segment in FORECAST_SEGMENTS[period])
    CHECKS.append((f"{period} segment EBIT equals consolidated EBIT", close(ebit_sum, INCOME[period]["ebit"]), f"segments={plain(ebit_sum)}; consolidated={plain(INCOME[period]['ebit'])}"))
    calculated_ebit = INCOME[period]["revenue"] - INCOME[period]["cor"] - INCOME[period]["rd"] - INCOME[period]["sga"] - INCOME[period]["restruct"] - INCOME[period]["impairment"]
    CHECKS.append((f"{period} income statement operating lines reconcile", close(calculated_ebit, INCOME[period]["ebit"]), f"calculated={plain(calculated_ebit)}; EBIT={plain(INCOME[period]['ebit'])}"))
    CHECKS.append((f"{period} income net income equals cash-flow net income", close(INCOME[period]["net_income"], CASHFLOW[period]["net_income"]), f"income={plain(INCOME[period]['net_income'])}; cashflow={plain(CASHFLOW[period]['net_income'])}"))
    CHECKS.append((f"{period} balance cash equals cash-flow ending cash", close(BALANCE[period]["cash"], CASHFLOW[period]["ending_cash"]), f"balance={plain(BALANCE[period]['cash'])}; cashflow={plain(CASHFLOW[period]['ending_cash'])}"))
    CHECKS.append((f"{period} balance sheet balances", close(BALANCE[period]["total_assets"], BALANCE[period]["total_liabilities"] + BALANCE[period]["redeemable_preferred"] + BALANCE[period]["equity"]), f"assets={plain(BALANCE[period]['total_assets'])}; liabilities+equity={plain(BALANCE[period]['total_liabilities'] + BALANCE[period]['redeemable_preferred'] + BALANCE[period]['equity'])}"))
    fcf_check = CASHFLOW[period]["ocf"] - CASHFLOW[period]["total_capex"]
    CHECKS.append((f"{period} FCF equals operating cash flow less capex", close(fcf_check, CASHFLOW[period]["fcf"]), f"calculated={plain(fcf_check)}; FCF={plain(CASHFLOW[period]['fcf'])}"))

CHECKS.append((
    "FY2026E equals H1 actual plus H2 forecast",
    all(close(INCOME["FY2026E"][metric], INCOME["H1 2026A"][metric] + INCOME["H2 2026E"][metric]) for metric in ("revenue", "cor", "rd", "sga", "restruct", "impairment", "ebit", "net_income")),
    "income statement key lines checked",
))
CHECKS.append((
    "Launch Services revenue uses customer launches only",
    close(H2_LAUNCH_SERVICES, H2["customer_falcon_launches"] * H2["launch_revenue_per_customer_launch"]),
    "internal Falcon and Starship launches excluded from revenue formula",
))


# ---------------------------------------------------------------------------
# Markdown writers.
# ---------------------------------------------------------------------------

def build_segments_md() -> str:
    periods = ["FY2023", "FY2024", "FY2025", "H1 2026A", "FY2026E", "FY2027E", "FY2028E"]
    revenue_rows: list[list[str]] = []
    historical_formula_slug = {
        "Launch Services": "launch_services_revenue",
        "Launch & Development": "launch_development_revenue",
    }
    fy2026_formula_slug = {
        "Launch Services": "launch_services",
        "Launch & Development": "launch_and_development",
        "Starship Commercial": "starship_commercial",
        "Consumer": "consumer",
        "Enterprise & Government": "enterprise_and_government",
        "Spectrum / Mobile Overlay": "spectrum_/_mobile_overlay",
        "Advertising": "advertising",
        "Solutions & Infrastructure": "solutions_and_infrastructure",
        "Cursor": "cursor",
    }
    outer_year_formula_slug = {
        "Launch Services": "launch_services_revenue",
        "Launch & Development": "launch_development_revenue",
        "Starship Commercial": "starship_commercial_revenue",
        "Consumer": "consumer_revenue",
        "Enterprise & Government": "enterprise_government_revenue",
        "Spectrum / Mobile Overlay": "spectrum_mobile_revenue",
        "Advertising": "advertising_revenue",
        "Solutions & Infrastructure": "solutions_infrastructure_revenue",
        "Cursor": "cursor_revenue",
    }
    for line in ("Launch Services", "Launch & Development", "Starship Commercial", "Consumer", "Enterprise & Government", "Spectrum / Mobile Overlay", "Advertising", "Solutions & Infrastructure", "Cursor"):
        row = [line]
        for period in periods:
            value = REVENUE_LINES[period][line]
            if value is None:
                row.append(not_obtained())
            elif period in ("H1 2026A",):
                row.append(tagged(value, "FACT"))
            elif period.startswith("FY202") and period.endswith(("3", "4", "5")) and line.startswith("Launch"):
                row.append(tagged(value, "DEDUCTED", f"segment.{period}.{historical_formula_slug[line]}"))
            elif period in ("FY2027E", "FY2028E") and line in ("Spectrum / Mobile Overlay", "Cursor"):
                row.append(tagged(value, "VIEW"))
            else:
                slug = fy2026_formula_slug[line] if period == "FY2026E" else outer_year_formula_slug[line]
                key = f"segment.{period}.{slug}"
                row.append(tagged(value, "DEDUCTED", key))
        revenue_rows.append(row)
    for segment, label in (("Space", "Space revenue"), ("Connectivity", "Connectivity revenue"), ("AI", "AI revenue")):
        row = [f"**{label}**"]
        for period in periods:
            if period in ACTUAL_SEGMENTS:
                row.append(tagged(ACTUAL_SEGMENTS[period][segment]["revenue"], "FACT"))
            else:
                row.append(tagged(FORECAST_SEGMENTS[period][segment]["revenue"], "DEDUCTED", f"segment.{period}.{segment.lower()}_revenue"))
        revenue_rows.append(row)

    driver_rows: list[list[str]] = []
    cost_driver_rows: list[list[str]] = []
    for period in ("H2 2026E", "FY2027E", "FY2028E"):
        d = DRIVERS[period]
        driver_rows.extend([
            [period, "Customer / internal Falcon / Starship launches", f"{plain(d['customer_falcon_launches'])} / {plain(d['internal_falcon_launches'])} / {plain(d['starship_launches'])} [VIEW]", "`research.md` Space — Launch Services / Starship overlay"],
            [period, "Launch revenue per customer launch", f"{money(d['launch_revenue_per_customer_launch'])} [VIEW]", "`research.md` recognized revenue per customer launch; list price remains not obtained"],
            [period, "Starship commercial flights / assumed revenue per flight", f"{plain(d['starship_commercial_flights'])} / {money(d['starship_revenue_per_flight'])} [VIEW]", "Commercial overlay; prospectus H2 2026 payload-to-orbit expectation is the start, but this is not a filing line"],
            [period, "Ending subscribers / monthly ARPU", f"{plain(d['ending_subscribers_m'])}m / {money(d['arpu_monthly'])} [VIEW]", "`research.md` Connectivity — Consumer"],
            [period, "Enterprise & Government", (money(d["enterprise_government_revenue"]) if period == "H2 2026E" else f"{number(d['enterprise_government_growth'] * D('100'))}% growth") + " [VIEW]", "`research.md` Connectivity — Enterprise & Government; no Starshield split"],
            [period, "Pending EchoStar spectrum/mobile revenue", f"{money(d['spectrum_mobile_revenue'])} [VIEW]", "Pending spectrum-enabled mobile overlay; not a filing line"],
            [period, "Advertising", (money(d["advertising_revenue"]) if period == "H2 2026E" else f"{number(d['advertising_growth'] * D('100'))}% growth") + " [VIEW]", "`research.md` AI — Advertising"],
            [period, "Solutions & Infrastructure", (money(d["solutions_infrastructure_revenue"]) if period == "H2 2026E" else f"{number(d['solutions_infrastructure_growth'] * D('100'))}% growth") + " [VIEW]", "`research.md` AI — Solutions & Infrastructure; Customer B concentration is the named downside"],
            [period, "Cursor revenue", f"{money(d['cursor_revenue'])} [VIEW]", "Cursor memo line rolls into AI; revenue is not obtained from a filing"],
        ])
        cost_driver_rows.extend([
            [period, "Space cost of revenue", f"{number(d['space_launch_cor_pct'] * D('100'))}% Launch Services / {number(d['space_development_cor_pct'] * D('100'))}% Launch & Development [VIEW]", "`research.md` Space segment drivers"],
            [period, "Starship commercial cost of revenue", f"{number(d['starship_cor_pct'] * D('100'))}% of Starship commercial revenue [VIEW]", "Commercial overlay economics; not a filing line"],
            [period, "Space R&D / SG&A", f"{money(d['space_rd'])} / {money(d['space_sga'])} [VIEW]", "`research.md` Starship overlay and Corporate"],
            [period, "Connectivity cost of revenue", f"{number(d['consumer_cor_pct'] * D('100'))}% Consumer / {number(d['enterprise_cor_pct'] * D('100'))}% Enterprise & Government [VIEW]", "`research.md` Connectivity segment drivers"],
            [period, "Connectivity R&D / SG&A", f"{money(d['connectivity_rd'])} / {money(d['connectivity_sga'])} [VIEW]", "`research.md` Connectivity segment drivers"],
            [period, "Spectrum/mobile cost of revenue", f"{number(d['spectrum_mobile_cor_pct'] * D('100'))}% of spectrum/mobile revenue [VIEW]", "Pending EchoStar overlay; not a filing line"],
            [period, "AI cost of revenue", f"{number(d['advertising_cor_pct'] * D('100'))}% Advertising / {number(d['solutions_cor_pct'] * D('100'))}% Solutions & Infrastructure [VIEW]", "`research.md` AI segment drivers"],
            [period, "AI R&D / SG&A", f"{money(d['ai_rd'])} / {money(d['ai_sga'])} [VIEW]", "`research.md` AI segment drivers"],
            [period, "Cursor cost / R&D / SG&A", f"{number(d['cursor_cor_pct'] * D('100'))}% / {number(d['cursor_rd_pct'] * D('100'))}% / {number(d['cursor_sga_pct'] * D('100'))}% of Cursor revenue [VIEW]", "Cursor P&L view; not a filing line"],
            [period, "Capex unit drivers", f"{money(d['space_capex_per_launch'])}/launch; {money(d['connectivity_capex_per_net_add'])}/net add; AI {money(d['ai_capex'])} [VIEW]", "`research.md` Capital cycle"],
        ])

    segment_rows: list[list[str]] = []
    for period in periods:
        for segment in ("Space", "Connectivity", "AI"):
            values = ALL_SEGMENTS[period][segment]
            is_actual = period in ACTUAL_SEGMENTS
            cells = [period, segment]
            for metric in ("revenue", "cor", "rd", "sga", "restruct", "impairment", "ebit"):
                if is_actual:
                    cells.append(tagged(values[metric], "FACT"))
                elif period == "FY2026E" and metric in ("revenue", "cor", "rd", "sga"):
                    cells.append(tagged(values[metric], "DEDUCTED", f"segment.{period}.{segment.lower()}_{metric}"))
                elif period == "FY2026E" and segment == "AI" and metric == "restruct":
                    cells.append(tagged(values[metric], "DEDUCTED", f"segment.{period}.ai_restruct"))
                elif metric == "ebit":
                    cells.append(tagged(values[metric], "DEDUCTED", f"segment.{period}.{segment.lower()}.ebit"))
                elif metric in ("revenue", "cor"):
                    cells.append(tagged(values[metric], "DEDUCTED", f"segment.{period}.{segment.lower()}_{metric}"))
                elif segment == "AI" and metric in ("rd", "sga"):
                    cells.append(tagged(values[metric], "DEDUCTED", f"segment.{period}.ai_{metric}"))
                else:
                    cells.append(tagged(values[metric], "VIEW"))
            segment_rows.append(cells)

    starship_rows = [
        ["FY2025", "Starship-specific R&D", "$3,004 [FACT]", "`research.md` Starship overlay"],
        ["H1 2026A", "Space R&D, mainly Starship", "$2,006 [FACT]", "Exact Starship-only amount not obtained"],
        ["FY2026E", "Commercial overlay", f"{plain(H2['starship_commercial_flights'])} flight × {money(H2['starship_revenue_per_flight'])} = {tagged(REVENUE_LINES['FY2026E']['Starship Commercial'] or D('0'), 'DEDUCTED', 'segment.FY2026E.starship_commercial')}", "View anchored to the prospectus H2 2026 payload-to-orbit expectation; not a filing revenue line"],
        ["FY2027E", "Commercial overlay", f"{plain(DRIVERS['FY2027E']['starship_commercial_flights'])} flights × {money(DRIVERS['FY2027E']['starship_revenue_per_flight'])} = {tagged(REVENUE_LINES['FY2027E']['Starship Commercial'] or D('0'), 'DEDUCTED', 'segment.FY2027E.starship_commercial_revenue')}", "Assumed cadence and yield; list price not obtained"],
        ["FY2028E", "Commercial overlay", f"{plain(DRIVERS['FY2028E']['starship_commercial_flights'])} flights × {money(DRIVERS['FY2028E']['starship_revenue_per_flight'])} = {tagged(REVENUE_LINES['FY2028E']['Starship Commercial'] or D('0'), 'DEDUCTED', 'segment.FY2028E.starship_commercial_revenue')}", "Assumed cadence and yield; list price not obtained"],
        ["FY2026E", "Space R&D / Starship overlay", tagged(FORECAST_SEGMENTS["FY2026E"]["Space"]["rd"], "DEDUCTED", "segment.FY2026E.space_rd"), "H1 actual plus H2 view"],
        ["FY2027E", "Space R&D / Starship overlay", "$4,200 [VIEW]", "Commercial revenue does not remove development spend"],
        ["FY2028E", "Space R&D / Starship overlay", "$3,600 [VIEW]", "Commercial revenue does not remove development spend"],
    ]
    cursor_rows: list[list[str]] = []
    for display_period, driver_period in (("FY2026E", "H2 2026E"), ("FY2027E", "FY2027E"), ("FY2028E", "FY2028E")):
        d = DRIVERS[driver_period]
        revenue = d["cursor_revenue"]
        cursor_cor = revenue * d["cursor_cor_pct"]
        cursor_rd = revenue * d["cursor_rd_pct"]
        cursor_sga = revenue * d["cursor_sga_pct"]
        cursor_ebit = derive(
            f"segment.{display_period}.cursor_memo_ebit",
            "Cursor_revenue - Cursor_cost_of_revenue - Cursor_R&D - Cursor_SG&A",
            {"Cursor_revenue": revenue, "Cursor_cost_of_revenue": cursor_cor, "Cursor_R&D": cursor_rd, "Cursor_SG&A": cursor_sga},
            revenue - cursor_cor - cursor_rd - cursor_sga,
        )
        cursor_rows.append([
            display_period,
            tagged(revenue, "VIEW"),
            tagged(cursor_cor, "DEDUCTED", f"segment.{driver_period}.cursor_cor"),
            tagged(cursor_rd, "DEDUCTED", f"segment.{driver_period}.cursor_rd"),
            tagged(cursor_sga, "DEDUCTED", f"segment.{driver_period}.cursor_sga"),
            tagged(cursor_ebit, "DEDUCTED", f"segment.{display_period}.cursor_memo_ebit"),
        ])

    capex_rows: list[list[str]] = []
    for period in ("H1 2026A", "H2 2026E", "FY2026E", "FY2027E", "FY2028E"):
        row = [period]
        for segment in ("Space", "Connectivity", "AI"):
            if period == "H1 2026A":
                row.append(tagged(CAPEX[period][segment], "FACT"))
            else:
                row.append(tagged(CAPEX[period][segment], "DEDUCTED" if segment != "AI" or period == "FY2026E" else "VIEW", f"cashflow.{period}.{segment.lower()}_capex" if not (segment == "AI" and period != "FY2026E") else None))
        capex_rows.append(row)

    return f"""# SpaceX segment model

as_of: 2026-08-30
units: USD millions unless stated otherwise
generator: `compute.py`

Forecast drivers are `[VIEW]` and implement the captain's 2026-08-30 overlay on `memory/spcx/research.md`. Historical facts point to `memory/spcx/register.md`. Internal Falcon launches do not create Launch Services revenue. Starship commercial revenue is a separate view. Starshield remains a memo inside Enterprise & Government; standalone P&L is {not_obtained()}.

## Explicit forecast drivers

{markdown_table(["period", "driver", "assumption", "research instruction"], driver_rows)}

## Forecast cost and capital drivers

{markdown_table(["period", "driver", "assumption", "research instruction"], cost_driver_rows)}

Kit revenue, churn, launch list price, Falcon 9/Heavy mix, Starshield standalone results, GPU-hours and utilization remain {not_obtained()}. Consumer revenue therefore models service revenue only; kit contribution is zero `[VIEW]`, not a claim that kits have no value. Cursor revenue and costs are explicit `[VIEW]` memo lines inside AI from H2 2026 onward; Cursor is not back-cast into Q2.

## Revenue lines

{markdown_table(["line", *periods], revenue_rows, ["---", *["---:"] * len(periods)])}

Historical Connectivity and AI sub-lines that were not disclosed as absolute annual values remain {not_obtained()}; reportable-segment totals are shown as `[FACT]`. Historical Launch Services uses the rounded disclosed mix and is therefore `[DEDUCTED]`.

## Reportable-segment operating statements

{markdown_table(["period", "segment", "revenue", "cost of revenue", "R&D", "SG&A", "restructuring", "impairment", "EBIT"], segment_rows, ["---", "---", *["---:"] * 7])}

Corporate / eliminations operating revenue and expense are zero `[FACT]` because the filed reportable segments reconcile to consolidated EBIT. Financing sits below EBIT in `income.md`.

## Starship overlay

{markdown_table(["period", "line", "value", "treatment"], starship_rows)}

Starship filing revenue, standalone capex, list price, payload economics and cost per test remain {not_obtained()}. The forecast's non-zero commercial revenue is a labeled cadence × assumed revenue-per-flight view.

## Cursor memo P&L — rolls into AI

{markdown_table(["period", "revenue", "cost of revenue", "R&D", "SG&A", "EBIT"], cursor_rows, ["---", "---:", "---:", "---:", "---:", "---:"])}

Cursor filing revenue and margins are {not_obtained()}. These are explicit forecast views, not filing lines. The 8-K discloses the closing share consideration and implied equity value, not Cursor P&L.

## Segment capex

{markdown_table(["period", "Space", "Connectivity", "AI"], capex_rows, ["---", "---:", "---:", "---:"])}

Space capex = total launches × capex per launch. Connectivity capex = subscriber net adds × capex per net add. AI capex is the residual cash bid `[VIEW]` from `research.md` Capital cycle.

{formula_appendix("Formula register", ("segment.", "cashflow.H2 2026E.total_launches", "cashflow.FY2027E.total_launches", "cashflow.FY2028E.total_launches", "cashflow.H2 2026E.subscriber", "cashflow.FY2027E.subscriber", "cashflow.FY2028E.subscriber", "cashflow.H2 2026E.space_capex", "cashflow.FY2027E.space_capex", "cashflow.FY2028E.space_capex", "cashflow.H2 2026E.connectivity_capex", "cashflow.FY2027E.connectivity_capex", "cashflow.FY2028E.connectivity_capex", "cashflow.FY2026E.space_capex", "cashflow.FY2026E.connectivity_capex", "cashflow.FY2026E.ai_capex"))}
"""


def build_income_md() -> str:
    periods = ["FY2023", "FY2024", "FY2025", "H1 2026A", "FY2026E", "FY2027E", "FY2028E"]
    labels = [
        ("revenue", "Revenue"), ("cor", "Cost of revenue"), ("gross_profit", "Gross profit"),
        ("rd", "Research and development"), ("sga", "Selling, general and administrative"),
        ("restruct", "Restructuring"), ("impairment", "Impairment"), ("ebit", "Operating income / EBIT"),
        ("interest_expense", "Interest expense"), ("interest_income", "Interest income"),
        ("other_income", "Other income / (expense)"), ("pretax", "Pretax income"),
        ("tax", "Tax provision / (benefit)"), ("net_income", "Net income"),
    ]
    rows: list[list[str]] = []
    for metric, label in labels:
        row = [label]
        for period in periods:
            value = INCOME[period][metric]
            if period in ("FY2023", "FY2024", "FY2025", "H1 2026A") and metric not in ("gross_profit", "pretax"):
                row.append(tagged(value, "FACT"))
            elif period in ("FY2027E", "FY2028E") and metric in ("interest_expense", "interest_income", "other_income"):
                row.append(tagged(value, "VIEW"))
            else:
                row.append(tagged(value, "DEDUCTED", f"income.{period}.{metric}"))
        rows.append(row)

    source_rows: list[list[str]] = []
    for period in periods:
        values = ALL_SEGMENTS[period]
        source_rows.append([
            period,
            tagged(values["Space"]["revenue"], "FACT") if period in ACTUAL_SEGMENTS else tagged(values["Space"]["revenue"], "DEDUCTED", f"segment.{period}.space_revenue"),
            tagged(values["Connectivity"]["revenue"], "FACT") if period in ACTUAL_SEGMENTS else tagged(values["Connectivity"]["revenue"], "DEDUCTED", f"segment.{period}.connectivity_revenue"),
            tagged(values["AI"]["revenue"], "FACT") if period in ACTUAL_SEGMENTS else tagged(values["AI"]["revenue"], "DEDUCTED", f"segment.{period}.ai_revenue"),
            tagged(INCOME[period]["revenue"], "DEDUCTED", f"income.{period}.revenue"),
        ])

    finance_rows = [
        ["H2 2026E", "Interest expense / income / other income / tax", f"{money(H2['interest_expense'])} / {money(H2['interest_income'])} / {money(H2['other_income'])} / {money(H2['tax'])} [VIEW]", "`research.md` Corporate / financing; tax attributes not obtained"],
        ["FY2027E", "Interest expense / income / other income / tax rate", f"{money(DRIVERS['FY2027E']['interest_expense'])} / {money(DRIVERS['FY2027E']['interest_income'])} / {money(DRIVERS['FY2027E']['other_income'])} / {number(DRIVERS['FY2027E']['tax_rate'] * D('100'))}% [VIEW]", "`research.md` Corporate / financing"],
        ["FY2028E", "Interest expense / income / other income / tax rate", f"{money(DRIVERS['FY2028E']['interest_expense'])} / {money(DRIVERS['FY2028E']['interest_income'])} / {money(DRIVERS['FY2028E']['other_income'])} / {number(DRIVERS['FY2028E']['tax_rate'] * D('100'))}% [VIEW]", "`research.md` Corporate / financing"],
    ]

    return f"""# SpaceX consolidated income statement

as_of: 2026-08-30
units: USD millions
generator: `compute.py`

The forecast is built from the combined segment statements in `segments.md`; consolidated revenue and EBIT are not separate plugs. FY2023–FY2025 remain retrospectively recast for xAI/X. FY2026E equals H1 actual plus H2 forecast. Cursor P&L is a non-zero `[VIEW]` from H2 2026 onward and is not back-cast into Q2. Starship commercial and pending EchoStar spectrum/mobile overlays are also explicit forecast views.

## Segment revenue bridge

{markdown_table(["period", "Space", "Connectivity", "AI", "consolidated"], source_rows, ["---", "---:", "---:", "---:", "---:"])}

## Consolidated statement

{markdown_table(["line", *periods], rows, ["---", *["---:"] * len(periods)])}

## Below-EBIT forecast drivers

{markdown_table(["period", "driver", "assumption", "research instruction"], finance_rows)}

FY2027E and FY2028E tax provisions apply the explicit `[VIEW]` rates in `compute.py` to positive pretax income. FY2026E includes the H1 actual tax provision plus a zero H2 cash/book provision `[VIEW]` because utilization of tax attributes is not obtained. Fully diluted EPS is not presented because fully diluted shares are {not_obtained()}.

{formula_appendix("Formula register", ("income.",))}
"""


def build_balance_md() -> str:
    periods = ["FY2025", "H1 2026A", "FY2026E", "FY2027E", "FY2028E"]
    labels = [
        ("cash", "Cash"), ("securities", "Marketable securities"), ("ar", "Accounts receivable"),
        ("inventory", "Inventory"), ("ppe", "PP&E, net"), ("spectrum_assets", "Pending EchoStar spectrum assets"), ("other_assets", "Other assets / purchase-accounting residual"),
        ("total_assets", "Total assets"), ("debt", "Debt and finance leases"),
        ("deferred_revenue", "Deferred revenue"), ("other_liabilities", "Other liabilities"),
        ("total_liabilities", "Total liabilities"), ("redeemable_preferred", "Redeemable preferred stock"),
        ("equity", "Shareholders' equity"),
    ]
    rows: list[list[str]] = []
    for metric, label in labels:
        row = [label]
        for period in periods:
            value = BALANCE[period][metric]
            if period in ("FY2025", "H1 2026A") and metric not in ("other_assets", "other_liabilities"):
                row.append(tagged(value, "FACT"))
            elif period in ("FY2025", "H1 2026A"):
                row.append(tagged(value, "DEDUCTED", f"balance.{period}.{metric}"))
            elif metric == "cash":
                output_period = "H2 2026E" if period == "FY2026E" else period
                row.append(tagged(value, "DEDUCTED", f"cashflow.{output_period}.ending_cash"))
            elif metric == "securities":
                row.append(tagged(value, "VIEW"))
            elif metric == "ar":
                output_period = "H2 2026E" if period == "FY2026E" else period
                row.append(tagged(value, "DEDUCTED", f"balance.{output_period}.accounts_receivable"))
            elif metric == "inventory":
                output_period = "H2 2026E" if period == "FY2026E" else period
                row.append(tagged(value, "DEDUCTED", f"balance.{output_period}.inventory"))
            elif metric in ("deferred_revenue", "other_liabilities", "redeemable_preferred", "spectrum_assets"):
                row.append(tagged(value, "VIEW"))
            elif metric == "debt":
                row.append(tagged(value, "VIEW"))
            else:
                formula_name = f"balance.{period if period != 'FY2026E' else 'H2 2026E'}.{metric if metric != 'ppe' else 'PP&E'}"
                row.append(tagged(value, "DEDUCTED", formula_name))
        rows.append(row)

    total_rows: list[list[str]] = []
    for period in periods:
        if period in ("FY2025", "H1 2026A"):
            right = sum_named(
                f"balance.{period}.total_liabilities_and_equity",
                {
                    "total_liabilities": BALANCE[period]["total_liabilities"],
                    "redeemable_preferred": BALANCE[period]["redeemable_preferred"],
                    "shareholders_equity": BALANCE[period]["equity"],
                },
            )
        else:
            right = BALANCE[period]["total_liabilities"] + BALANCE[period]["redeemable_preferred"] + BALANCE[period]["equity"]
        if period in ("FY2025", "H1 2026A"):
            right_cell = tagged(right, "DEDUCTED", f"balance.{period}.total_liabilities_and_equity")
            asset_cell = tagged(BALANCE[period]["total_assets"], "FACT")
        else:
            output_period = "H2 2026E" if period == "FY2026E" else period
            right_cell = tagged(right, "DEDUCTED", f"balance.{output_period}.total_liabilities_and_equity")
            asset_cell = tagged(BALANCE[period]["total_assets"], "DEDUCTED", f"balance.{output_period}.total_assets")
        total_rows.append([period, asset_cell, right_cell, plain(BALANCE[period]["total_assets"] - right)])

    share_rows = [
        ["H1 2026A", "13,176.0 [FACT]", "June 30 issued Class A plus Class B; July 28 count is higher"],
        ["FY2026E", tagged(BASIC_SHARES["FY2026E"], "DEDUCTED", "balance.FY2026E.basic_shares", unit="plain"), "Post-Cursor plus 261.8 million pending EchoStar shares `[VIEW]`"],
        ["FY2027E", f"{plain(BASIC_SHARES['FY2027E'])} [VIEW]", "Held flat after pending EchoStar inclusion; exercises and fully diluted shares are not obtained"],
        ["FY2028E", f"{plain(BASIC_SHARES['FY2028E'])} [VIEW]", "Held flat after pending EchoStar inclusion; exercises and fully diluted shares are not obtained"],
    ]
    assumption_rows: list[list[str]] = []
    for period in ("H2 2026E", "FY2027E", "FY2028E"):
        d = DRIVERS[period]
        assumption_rows.extend([
            [period, "Accounts receivable / inventory", f"{number(d['ar_pct_revenue'] * D('100'))}% / {number(d['inventory_pct_revenue'] * D('100'))}% of annual revenue [VIEW]", "`research.md` Working capital"],
            [period, "Deferred revenue / other liabilities", f"{money(d['deferred_revenue'])} / {money(d['other_liabilities'])} [VIEW]", "`research.md` Backlog and deferred revenue as constraints"],
            [period, "Debt / marketable securities", "$39,364 / $6,487 held flat [VIEW]", "`research.md` Corporate / financing; new financing not obtained"],
        ])
    assumption_rows.append(["H2 2026E", "Cursor stock consideration", f"{money(H2['cursor_equity_consideration'])} [VIEW]", "Share step-up is required by `research.md`; final purchase accounting is not obtained"])
    assumption_rows.append(["H2 2026E", "Pending EchoStar consideration", f"{money(H2['echostar_spectrum_assets'])} spectrum asset / {money(H2['echostar_equity_consideration'])} equity / {money(H2['echostar_cash_consideration'])} cash [VIEW]", "Pending deal included in base; not a closed filing balance"])

    return f"""# SpaceX balance sheet

as_of: 2026-08-30
units: USD millions except shares
generator: `compute.py`

Cash ties to `cashflow.md`. Forecast PP&E uses opening PP&E + capex − D&A `[VIEW]`; this simplifying bridge treats all D&A as PP&E depreciation because an intangible-amortization forecast is {not_obtained()}. Other assets are the explicit balancing residual and include Cursor purchase accounting, goodwill/intangibles and other items not separately forecast.

## Balance sheet

{markdown_table(["line", *periods], rows, ["---", *["---:"] * len(periods)])}

## Forecast balance drivers

{markdown_table(["period", "driver", "assumption", "research instruction"], assumption_rows)}

The H2 2026 Cursor bridge assumes $60,000 of stock consideration `[VIEW]` in equity and the other-assets residual; final purchase accounting and Cursor standalone net assets are {not_obtained()}. Cursor P&L is modeled separately in AI. The pending EchoStar base view adds spectrum assets, equity shares and cash consideration while holding debt flat. Refinancing, repayment and new borrowing are not obtained.

## Balance check

{markdown_table(["period", "total assets", "liabilities + preferred + equity", "difference"], total_rows, ["---", "---:", "---:", "---:"])}

## Basic shares

{markdown_table(["period", "ending basic shares (millions)", "treatment"], share_rows)}

Point-in-time fully diluted shares and float remain {not_obtained()}. Share-based compensation is included in expense/cash-flow reconciliation, but no exercise issuance is modeled.

## EchoStar pending base treatment

The base includes approximately 261.8 million Class A shares and approximately $19,600 consideration: $11,100.32 equity at $42.40 and $8,500 cash `[VIEW]`. The transaction terms are `[FACT]` in `register.md`; including the pending close in forecast shares, cash and spectrum assets is a view. Closing date, final cash use and purchase accounting remain {not_obtained()}.

{formula_appendix("Formula register", ("balance.",))}
"""


def build_cashflow_md() -> str:
    periods = ["FY2023", "FY2024", "FY2025", "H1 2026A", "H2 2026E", "FY2026E", "FY2027E", "FY2028E"]
    labels = [
        ("net_income", "Net income"), ("da", "Depreciation and amortization"), ("sbc", "Share-based compensation"),
        ("other_noncash", "Other non-cash items"), ("ar_contribution", "Accounts receivable contribution"),
        ("inventory_contribution", "Inventory contribution"), ("prepaids_ap_contribution", "Prepaids / payables contribution"),
        ("deferred_revenue_contribution", "Deferred revenue contribution"),
        ("other_liabilities_contribution", "Other liabilities contribution"), ("other_operating_items", "Other operating items"),
        ("ocf", "Operating cash flow"), ("space_capex", "Space capex"), ("connectivity_capex", "Connectivity capex"),
        ("ai_capex", "AI capex"), ("total_capex", "Total capex"), ("fcf", "Free cash flow"),
        ("noncapex_cash_flows", "Financing and non-capex investing / FX"), ("ending_cash", "Ending cash"),
        ("ending_securities", "Ending marketable securities"), ("ending_liquidity", "Ending cash + securities"),
    ]

    rows: list[list[str]] = []
    for metric, label in labels:
        row = [label]
        for period in periods:
            if period in ("FY2023", "FY2024", "FY2025"):
                if metric == "net_income":
                    row.append(tagged(ACTUAL_FINANCE[period]["net_income"], "FACT"))
                elif metric == "ocf":
                    row.append(tagged(ACTUAL_CASHFLOW[period]["ocf"], "FACT"))
                elif metric == "total_capex":
                    row.append(tagged(ACTUAL_CASHFLOW[period]["capex"], "FACT"))
                elif metric == "fcf":
                    fcf = subtract(f"cashflow.{period}.fcf", "operating_cash_flow", ACTUAL_CASHFLOW[period]["ocf"], "capital_expenditures", ACTUAL_CASHFLOW[period]["capex"])
                    row.append(tagged(fcf, "DEDUCTED", f"cashflow.{period}.fcf"))
                elif metric == "ending_cash" and period == "FY2025":
                    row.append(tagged(BALANCE["FY2025"]["cash"], "FACT"))
                elif metric == "ending_securities" and period == "FY2025":
                    row.append(tagged(BALANCE["FY2025"]["securities"], "FACT"))
                elif metric == "ending_liquidity" and period == "FY2025":
                    liquidity = sum_named("cashflow.FY2025.ending_liquidity", {"cash": BALANCE["FY2025"]["cash"], "securities": BALANCE["FY2025"]["securities"]})
                    row.append(tagged(liquidity, "DEDUCTED", "cashflow.FY2025.ending_liquidity"))
                else:
                    row.append(not_obtained())
                continue

            data = CASHFLOW[period]
            if metric == "space_capex":
                capex_period = period
                value = CAPEX[capex_period]["Space"]
                if period == "H1 2026A":
                    row.append(tagged(value, "FACT"))
                else:
                    row.append(tagged(value, "DEDUCTED", f"cashflow.{period}.space_capex"))
            elif metric == "connectivity_capex":
                value = CAPEX[period]["Connectivity"]
                if period == "H1 2026A":
                    row.append(tagged(value, "FACT"))
                else:
                    row.append(tagged(value, "DEDUCTED", f"cashflow.{period}.connectivity_capex"))
            elif metric == "ai_capex":
                value = CAPEX[period]["AI"]
                if period == "H1 2026A":
                    row.append(tagged(value, "FACT"))
                elif period == "FY2026E":
                    row.append(tagged(value, "DEDUCTED", "cashflow.FY2026E.ai_capex"))
                else:
                    row.append(tagged(value, "VIEW"))
            elif metric in data:
                value = data[metric]
                if period == "H1 2026A":
                    if metric in ("net_income", "da", "sbc", "ar_contribution", "inventory_contribution", "deferred_revenue_contribution", "other_liabilities_contribution"):
                        row.append(tagged(value, "FACT"))
                    elif metric in ("other_noncash", "prepaids_ap_contribution"):
                        row.append(tagged(value, "DEDUCTED", f"cashflow.H1 2026A.{metric}"))
                    elif metric in ("ocf", "total_capex"):
                        row.append(tagged(value, "FACT"))
                    elif metric == "fcf":
                        row.append(tagged(value, "DEDUCTED", "cashflow.H1 2026A.fcf"))
                    elif metric == "noncapex_cash_flows":
                        row.append(tagged(value, "DEDUCTED", "cashflow.H1 2026A.noncapex_cash_flows"))
                    elif metric in ("ending_cash", "ending_securities"):
                        row.append(tagged(value, "FACT"))
                    elif metric == "ending_liquidity":
                        row.append(tagged(value, "DEDUCTED", "cashflow.H1 2026A.ending_liquidity"))
                    else:
                        row.append(not_obtained())
                elif metric == "net_income":
                    row.append(tagged(value, "DEDUCTED", f"income.{period}.net_income"))
                elif metric in ("da", "sbc", "other_noncash", "prepaids_ap_contribution", "other_operating_items", "noncapex_cash_flows") and period != "FY2026E":
                    row.append(tagged(value, "VIEW"))
                elif period == "FY2026E" and metric == "other_operating_items":
                    row.append(tagged(value, "VIEW"))
                elif metric in ("ending_cash", "ending_securities"):
                    if metric == "ending_securities":
                        row.append(tagged(value, "VIEW"))
                    else:
                        output_period = "H2 2026E" if period == "FY2026E" else period
                        row.append(tagged(value, "DEDUCTED", f"cashflow.{output_period}.ending_cash"))
                elif metric == "ending_liquidity":
                    row.append(tagged(value, "DEDUCTED", f"cashflow.{period}.ending_liquidity"))
                elif metric == "ar_contribution" and period != "FY2026E":
                    row.append(tagged(value, "DEDUCTED", f"cashflow.{period}.accounts_receivable_contribution"))
                else:
                    row.append(tagged(value, "DEDUCTED", f"cashflow.{period}.{metric}"))
            else:
                row.append(not_obtained())
        rows.append(row)

    runway_rows: list[list[str]] = []
    starting_liquidity = sum_named("cashflow.runway.starting_liquidity", {"cash": D("93522"), "marketable_securities": D("6487")})
    for period in ("FY2026E", "FY2027E", "FY2028E"):
        ending = CASHFLOW[period]["ending_liquidity"]
        used = subtract(f"cashflow.runway.{period}.liquidity_used", "starting_liquidity", starting_liquidity, "ending_liquidity", ending)
        runway_rows.append([period, tagged(starting_liquidity, "DEDUCTED", "cashflow.runway.starting_liquidity"), tagged(ending, "DEDUCTED", f"cashflow.{period}.ending_liquidity"), tagged(used, "DEDUCTED", f"cashflow.runway.{period}.liquidity_used"), "positive" if ending > 0 else "exhausted"])

    assumption_rows: list[list[str]] = []
    for period in ("H2 2026E", "FY2027E", "FY2028E"):
        d = DRIVERS[period]
        assumption_rows.extend([
            [period, "D&A / share-based compensation", f"{money(d['da'])} / {money(d['sbc'])} [VIEW]", "`research.md` Corporate / financing"],
            [period, "Other operating items", f"{money(d['other_operating_items'])} [VIEW]", "Explicit residual for cash taxes and operating items not separately obtained"],
            [period, "AI capex", f"{money(d['ai_capex'])} [VIEW]", "`research.md` AI as residual cash bid"],
            [period, "Incremental financing / non-capex investing", f"{money(d['noncapex_cash_flows'])} [VIEW]", "Pending EchoStar cash consideration included in H2 2026; no new financing"],
        ])

    return f"""# SpaceX cash flow

as_of: 2026-08-30
units: USD millions
generator: `compute.py`

Free cash flow is operating cash flow minus capex, matching `register.md`. Forecast working-capital contributions tie to the ending balance-sheet accounts. AI capex is the residual cash bid `[VIEW]`; Space capex is launch-driven and Connectivity capex is net-add-driven.

## Cash-flow statement and runway

{markdown_table(["line", *periods], rows, ["---", *["---:"] * len(periods)])}

## Forecast cash-flow drivers

{markdown_table(["period", "driver", "assumption", "research instruction"], assumption_rows)}

The H1 2026 financing/non-capex line is the derived cash bridge from 2025 year-end cash to 2026-06-30 cash after FCF; it aggregates IPO/debt proceeds, repayments, non-capex investing, securities purchases and FX. H2 2026 includes $8,500 pending EchoStar cash consideration `[VIEW]`; later periods assume zero incremental financing.

## Liquidity runway from 2026-06-30

{markdown_table(["through period", "starting cash + securities", "ending cash + securities", "cumulative liquidity used", "status"], runway_rows, ["---", "---:", "---:", "---:", "---"])}

The base case remains cash-positive through FY2028E after the pending EchoStar cash view. This is a liquidity schedule, not a financing commitment; minimum cash, new debt and final EchoStar closing mechanics remain {not_obtained()}.

{formula_appendix("Formula register", ("cashflow.",))}
"""


VALUATION_SUMMARY: dict[str, Decimal] = {}


def build_valuation_md() -> str:
    """Build a 12-month SOTP price target plus DCF and comps checks."""
    as_of = "2026-08-30"
    target_date = "2027-08-30"
    last_sale = D("141.50")
    current_market_cap = D("1920554.3")
    basic_shares = BASIC_SHARES["FY2026E"]
    potential_awards = D("564")
    target_years_from_fy2028 = D("1.3333333333")
    months_of_fy2027_burn_to_target = D("8")

    current_ev = derive(
        "valuation.current_enterprise_value",
        "current_market_cap + debt_and_finance_leases - cash - marketable_securities",
        {
            "current_market_cap": current_market_cap,
            "debt_and_finance_leases": D("39364"),
            "cash": D("93522"),
            "marketable_securities": D("6487"),
        },
        current_market_cap + D("39364") - D("93522") - D("6487"),
    )
    target_net_cash = derive(
        "valuation.target_net_cash",
        "FY2026_ending_liquidity - debt + FY2027_FCF × months_to_target ÷ twelve_months",
        {
            "FY2026_ending_liquidity": CASHFLOW["FY2026E"]["ending_liquidity"],
            "debt": BALANCE["FY2026E"]["debt"],
            "FY2027_FCF": CASHFLOW["FY2027E"]["fcf"],
            "months_to_target": months_of_fy2027_burn_to_target,
            "twelve_months": D("12"),
        },
        CASHFLOW["FY2026E"]["ending_liquidity"]
        - BALANCE["FY2026E"]["debt"]
        + CASHFLOW["FY2027E"]["fcf"] * months_of_fy2027_burn_to_target / D("12"),
    )
    ai_invested_capital = sum_named(
        "valuation.ai_invested_capital",
        {
            "FY2026E_AI_capex": CAPEX["FY2026E"]["AI"],
            "FY2027E_AI_capex": CAPEX["FY2027E"]["AI"],
            "FY2028E_AI_capex": CAPEX["FY2028E"]["AI"],
        },
    )

    scenarios: dict[str, dict[str, Decimal]] = {
        "Base": {
            "wacc": D("0.105"),
            "opening_subscribers_m": D("18"),
            "ending_subscribers_m": D("22.5"),
            "arpu": D("59"),
            "enterprise_factor": D("1.00"),
            "consumer_incremental_margin": D("0.55"),
            "enterprise_incremental_margin": D("0.60"),
            "connectivity_exit_ebit_multiple": D("70"),
            "space_exit_revenue_multiple": D("12"),
            "starship_commercial_flights": D("50"), "starship_revenue_per_flight": D("140"),
            "ai_capital_conversion_multiple": D("2"),
            "customer_b_haircut": D("0.20"),
            "cursor_revenue": D("5000"), "cursor_ebit_margin": D("0.15"), "cursor_exit_ebit_multiple": D("40"),
        },
        "Bull": {
            "wacc": D("0.09"),
            "opening_subscribers_m": D("19"),
            "ending_subscribers_m": D("25"),
            "arpu": D("65"),
            "enterprise_factor": D("1.15"),
            "consumer_incremental_margin": D("0.55"),
            "enterprise_incremental_margin": D("0.60"),
            "connectivity_exit_ebit_multiple": D("95"),
            "space_exit_revenue_multiple": D("20"),
            "starship_commercial_flights": D("100"), "starship_revenue_per_flight": D("160"),
            "ai_capital_conversion_multiple": D("7"),
            "customer_b_haircut": D("0.05"),
            "cursor_revenue": D("8000"), "cursor_ebit_margin": D("0.25"), "cursor_exit_ebit_multiple": D("60"),
        },
        "Bear": {
            "wacc": D("0.135"),
            "opening_subscribers_m": D("17"),
            "ending_subscribers_m": D("20"),
            "arpu": D("54"),
            "enterprise_factor": D("0.85"),
            "consumer_incremental_margin": D("0.55"),
            "enterprise_incremental_margin": D("0.60"),
            "connectivity_exit_ebit_multiple": D("40"),
            "space_exit_revenue_multiple": D("8"),
            "starship_commercial_flights": D("10"), "starship_revenue_per_flight": D("120"),
            "ai_capital_conversion_multiple": D("0.75"),
            "customer_b_haircut": D("0.40"),
            "cursor_revenue": D("2000"), "cursor_ebit_margin": D("-0.10"), "cursor_exit_ebit_multiple": D("20"),
        },
    }

    base_consumer_revenue = REVENUE_LINES["FY2028E"]["Consumer"] or D("0")
    base_enterprise_revenue = sum_named(
        "valuation.base_enterprise_and_spectrum_revenue",
        {
            "Enterprise_and_Government": REVENUE_LINES["FY2028E"]["Enterprise & Government"] or D("0"),
            "pending_spectrum_mobile_overlay": REVENUE_LINES["FY2028E"]["Spectrum / Mobile Overlay"] or D("0"),
        },
    )
    base_connectivity_ebit = FORECAST_SEGMENTS["FY2028E"]["Connectivity"]["ebit"]
    base_space_core_revenue = sum_named(
        "valuation.base_space_core_revenue",
        {
            "Launch_Services": REVENUE_LINES["FY2028E"]["Launch Services"] or D("0"),
            "Launch_and_Development": REVENUE_LINES["FY2028E"]["Launch & Development"] or D("0"),
        },
    )

    scenario_results: dict[str, dict[str, Decimal]] = {}
    for scenario, inputs in scenarios.items():
        slug = scenario.lower()
        average_subscribers = derive(
            f"valuation.{slug}.average_subscribers",
            "(opening_subscribers + ending_subscribers) ÷ two",
            {
                "opening_subscribers_m": inputs["opening_subscribers_m"],
                "ending_subscribers_m": inputs["ending_subscribers_m"],
                "two": D("2"),
            },
            (inputs["opening_subscribers_m"] + inputs["ending_subscribers_m"]) / D("2"),
        )
        consumer_revenue = derive(
            f"valuation.{slug}.consumer_revenue",
            "average_subscribers × ARPU × twelve_months",
            {"average_subscribers_m": average_subscribers, "ARPU": inputs["arpu"], "twelve_months": D("12")},
            average_subscribers * inputs["arpu"] * D("12"),
        )
        enterprise_revenue = multiply(
            f"valuation.{slug}.enterprise_revenue",
            "base_enterprise_revenue",
            base_enterprise_revenue,
            "scenario_factor",
            inputs["enterprise_factor"],
        )
        consumer_ebit_change = derive(
            f"valuation.{slug}.consumer_ebit_change",
            "(scenario_consumer_revenue - base_consumer_revenue) × incremental_margin",
            {
                "scenario_consumer_revenue": consumer_revenue,
                "base_consumer_revenue": base_consumer_revenue,
                "incremental_margin": inputs["consumer_incremental_margin"],
            },
            (consumer_revenue - base_consumer_revenue) * inputs["consumer_incremental_margin"],
        )
        enterprise_ebit_change = derive(
            f"valuation.{slug}.enterprise_ebit_change",
            "(scenario_enterprise_revenue - base_enterprise_revenue) × incremental_margin",
            {
                "scenario_enterprise_revenue": enterprise_revenue,
                "base_enterprise_revenue": base_enterprise_revenue,
                "incremental_margin": inputs["enterprise_incremental_margin"],
            },
            (enterprise_revenue - base_enterprise_revenue) * inputs["enterprise_incremental_margin"],
        )
        connectivity_ebit = sum_named(
            f"valuation.{slug}.connectivity_ebit",
            {
                "base_connectivity_EBIT": base_connectivity_ebit,
                "consumer_EBIT_change": consumer_ebit_change,
                "enterprise_EBIT_change": enterprise_ebit_change,
            },
        )
        connectivity_value = multiply(
            f"valuation.{slug}.connectivity_value_FY2028",
            "scenario_connectivity_EBIT",
            connectivity_ebit,
            "connectivity_exit_EBIT_multiple",
            inputs["connectivity_exit_ebit_multiple"],
        )
        starship_revenue = multiply(
            f"valuation.{slug}.starship_commercial_revenue",
            "commercial_Starship_flights",
            inputs["starship_commercial_flights"],
            "assumed_revenue_per_flight",
            inputs["starship_revenue_per_flight"],
        )
        space_revenue = sum_named(
            f"valuation.{slug}.space_revenue",
            {"modeled_launch_revenue": base_space_core_revenue, "Starship_commercial_revenue": starship_revenue},
        )
        space_value = multiply(
            f"valuation.{slug}.space_value_FY2028",
            "space_revenue",
            space_revenue,
            "space_exit_revenue_multiple",
            inputs["space_exit_revenue_multiple"],
        )
        ai_gross_value = multiply(
            f"valuation.{slug}.ai_gross_value_FY2028",
            "AI_invested_capital",
            ai_invested_capital,
            "AI_capital_conversion_multiple",
            inputs["ai_capital_conversion_multiple"],
        )
        ai_value = derive(
            f"valuation.{slug}.ai_value_FY2028",
            "AI_gross_value × (one - Customer_B_haircut)",
            {"AI_gross_value": ai_gross_value, "Customer_B_haircut": inputs["customer_b_haircut"]},
            ai_gross_value * (D("1") - inputs["customer_b_haircut"]),
        )
        cursor_ebit = multiply(
            f"valuation.{slug}.cursor_EBIT",
            "Cursor_revenue",
            inputs["cursor_revenue"],
            "Cursor_EBIT_margin",
            inputs["cursor_ebit_margin"],
        )
        cursor_value = multiply(
            f"valuation.{slug}.cursor_value_FY2028",
            "positive_Cursor_EBIT",
            max(cursor_ebit, D("0")),
            "Cursor_exit_EBIT_multiple",
            inputs["cursor_exit_ebit_multiple"],
        )
        end_fy2028_ev = sum_named(
            f"valuation.{slug}.end_FY2028_enterprise_value",
            {"Connectivity": connectivity_value, "Space": space_value, "AI_core": ai_value, "Cursor": cursor_value},
        )
        discount_factor = power(
            f"valuation.{slug}.discount_factor",
            "one_plus_WACC",
            D("1") + inputs["wacc"],
            "years_from_target_to_FY2028",
            target_years_from_fy2028,
        )
        target_ev = divide(
            f"valuation.{slug}.target_enterprise_value",
            "end_FY2028_enterprise_value",
            end_fy2028_ev,
            "discount_factor",
            discount_factor,
        )
        target_equity = sum_named(
            f"valuation.{slug}.target_equity_value",
            {"target_enterprise_value": target_ev, "target_net_cash": target_net_cash},
        )
        price_target = divide(
            f"valuation.{slug}.price_target",
            "target_equity_value",
            target_equity,
            "basic_shares_m",
            basic_shares,
        )
        implied_change = derive(
            f"valuation.{slug}.implied_change",
            "price_target ÷ last_sale - one",
            {"price_target": price_target, "last_sale": last_sale, "one": D("1")},
            price_target / last_sale - D("1"),
        )
        pv_connectivity = divide(f"valuation.{slug}.pv_connectivity", "FY2028_connectivity_value", connectivity_value, "discount_factor", discount_factor)
        pv_space = divide(f"valuation.{slug}.pv_space", "FY2028_space_value", space_value, "discount_factor", discount_factor)
        pv_ai = divide(f"valuation.{slug}.pv_ai", "FY2028_AI_value", ai_value, "discount_factor", discount_factor)
        pv_cursor = divide(f"valuation.{slug}.pv_cursor", "FY2028_Cursor_value", cursor_value, "discount_factor", discount_factor)
        scenario_results[scenario] = {
            "average_subscribers": average_subscribers,
            "consumer_revenue": consumer_revenue,
            "enterprise_revenue": enterprise_revenue,
            "connectivity_ebit": connectivity_ebit,
            "connectivity_value": connectivity_value,
            "starship_revenue": starship_revenue,
            "space_revenue": space_revenue,
            "space_value": space_value,
            "ai_value": ai_value,
            "cursor_ebit": cursor_ebit,
            "cursor_value": cursor_value,
            "end_ev": end_fy2028_ev,
            "discount_factor": discount_factor,
            "target_ev": target_ev,
            "target_equity": target_equity,
            "price_target": price_target,
            "implied_change": implied_change,
            "pv_connectivity": pv_connectivity,
            "pv_space": pv_space,
            "pv_ai": pv_ai,
            "pv_cursor": pv_cursor,
        }

    base = scenario_results["Base"]
    sensitivity_shares = sum_named(
        "valuation.dilution_sensitivity_shares",
        {"basic_shares_m": basic_shares, "potentially_dilutive_awards_m": potential_awards},
    )
    diluted_sensitivity_pt = divide(
        "valuation.dilution_sensitivity_price",
        "base_target_equity_value",
        base["target_equity"],
        "basic_plus_potential_awards_m",
        sensitivity_shares,
    )
    dilution_haircut = derive(
        "valuation.dilution_sensitivity_haircut",
        "one - sensitivity_price ÷ base_price_target",
        {"one": D("1"), "sensitivity_price": diluted_sensitivity_pt, "base_price_target": base["price_target"]},
        D("1") - diluted_sensitivity_pt / base["price_target"],
    )

    implied_target_ev_revenue = divide(
        "valuation.base.target_EV_to_FY2028_revenue",
        "target_enterprise_value",
        base["target_ev"],
        "FY2028_revenue",
        INCOME["FY2028E"]["revenue"],
    )
    implied_target_ev_ebit = divide(
        "valuation.base.target_EV_to_FY2028_EBIT",
        "target_enterprise_value",
        base["target_ev"],
        "FY2028_EBIT",
        INCOME["FY2028E"]["ebit"],
    )
    current_ev_revenue = divide(
        "valuation.current_EV_to_FY2028_revenue",
        "current_enterprise_value",
        current_ev,
        "FY2028_revenue",
        INCOME["FY2028E"]["revenue"],
    )
    current_ev_ebit = divide(
        "valuation.current_EV_to_FY2028_EBIT",
        "current_enterprise_value",
        current_ev,
        "FY2028_EBIT",
        INCOME["FY2028E"]["ebit"],
    )
    current_premium_to_base_ev = derive(
        "valuation.current_EV_premium_to_base_target_EV",
        "current_enterprise_value ÷ base_target_enterprise_value - one",
        {"current_enterprise_value": current_ev, "base_target_enterprise_value": base["target_ev"], "one": D("1")},
        current_ev / base["target_ev"] - D("1"),
    )

    # Consolidated DCF check. Explicit FCF is near zero in FY2028, so the
    # extension uses named revenue-growth and FCF-margin fade assumptions.
    dcf_wacc = scenarios["Base"]["wacc"]
    terminal_growth = D("0.035")
    exit_fcf_multiple = D("25")
    dcf_growth = {"FY2029E": D("0.20"), "FY2030E": D("0.16"), "FY2031E": D("0.12"), "FY2032E": D("0.09"), "FY2033E": D("0.06")}
    dcf_fcf_margin = {"FY2029E": D("0.08"), "FY2030E": D("0.16"), "FY2031E": D("0.23"), "FY2032E": D("0.28"), "FY2033E": D("0.31")}
    dcf_time = {"FY2028E": D("1.3333333333"), "FY2029E": D("2.3333333333"), "FY2030E": D("3.3333333333"), "FY2031E": D("4.3333333333"), "FY2032E": D("5.3333333333"), "FY2033E": D("6.3333333333")}
    dcf_rows: list[list[str]] = []
    dcf_pv: dict[str, Decimal] = {}
    fy2028_df = power("valuation.dcf.FY2028_discount_factor", "one_plus_WACC", D("1") + dcf_wacc, "years", dcf_time["FY2028E"])
    dcf_pv["FY2028E"] = divide("valuation.dcf.FY2028_PV_FCF", "FY2028_FCF", CASHFLOW["FY2028E"]["fcf"], "discount_factor", fy2028_df)
    dcf_rows.append(["FY2028E", tagged(INCOME["FY2028E"]["revenue"], "DEDUCTED", "income.FY2028E.revenue"), "model", tagged(CASHFLOW["FY2028E"]["fcf"], "DEDUCTED", "cashflow.FY2028E.fcf"), tagged(dcf_pv["FY2028E"], "DEDUCTED", "valuation.dcf.FY2028_PV_FCF")])
    previous_revenue = INCOME["FY2028E"]["revenue"]
    dcf_revenue: dict[str, Decimal] = {}
    dcf_fcf: dict[str, Decimal] = {"FY2028E": CASHFLOW["FY2028E"]["fcf"]}
    for period in ("FY2029E", "FY2030E", "FY2031E", "FY2032E", "FY2033E"):
        revenue = derive(
            f"valuation.dcf.{period}.revenue",
            "prior_revenue × (one + growth)",
            {"prior_revenue": previous_revenue, "one_plus_growth": D("1") + dcf_growth[period]},
            previous_revenue * (D("1") + dcf_growth[period]),
        )
        fcf = multiply(f"valuation.dcf.{period}.FCF", "revenue", revenue, "FCF_margin", dcf_fcf_margin[period])
        discount_factor = power(f"valuation.dcf.{period}.discount_factor", "one_plus_WACC", D("1") + dcf_wacc, "years", dcf_time[period])
        pv_fcf = divide(f"valuation.dcf.{period}.PV_FCF", "FCF", fcf, "discount_factor", discount_factor)
        dcf_revenue[period], dcf_fcf[period], dcf_pv[period] = revenue, fcf, pv_fcf
        dcf_rows.append([
            period,
            tagged(revenue, "DEDUCTED", f"valuation.dcf.{period}.revenue"),
            f"{number(dcf_growth[period] * D('100'))}% revenue growth / {number(dcf_fcf_margin[period] * D('100'))}% FCF margin [VIEW]",
            tagged(fcf, "DEDUCTED", f"valuation.dcf.{period}.FCF"),
            tagged(pv_fcf, "DEDUCTED", f"valuation.dcf.{period}.PV_FCF"),
        ])
        previous_revenue = revenue

    terminal_value = derive(
        "valuation.dcf.terminal_value",
        "FY2033_FCF × (one + terminal_growth) ÷ (WACC - terminal_growth)",
        {"FY2033_FCF": dcf_fcf["FY2033E"], "terminal_growth": terminal_growth, "WACC": dcf_wacc},
        dcf_fcf["FY2033E"] * (D("1") + terminal_growth) / (dcf_wacc - terminal_growth),
    )
    terminal_df = power("valuation.dcf.terminal_discount_factor", "one_plus_WACC", D("1") + dcf_wacc, "years", dcf_time["FY2033E"])
    pv_terminal = divide("valuation.dcf.PV_terminal_value", "terminal_value", terminal_value, "discount_factor", terminal_df)
    dcf_ev = sum_named("valuation.dcf.enterprise_value", {f"PV_{period}_FCF": value for period, value in dcf_pv.items()} | {"PV_terminal_value": pv_terminal})
    dcf_equity = sum_named("valuation.dcf.equity_value", {"enterprise_value": dcf_ev, "target_net_cash": target_net_cash})
    dcf_price = divide("valuation.dcf.price_per_share", "equity_value", dcf_equity, "basic_shares_m", basic_shares)
    terminal_share = divide("valuation.dcf.terminal_value_share", "PV_terminal_value", pv_terminal, "DCF_enterprise_value", dcf_ev)

    exit_terminal_value = multiply("valuation.dcf.exit_terminal_value", "FY2033_FCF", dcf_fcf["FY2033E"], "exit_FCF_multiple", exit_fcf_multiple)
    pv_exit_terminal = divide("valuation.dcf.PV_exit_terminal_value", "exit_terminal_value", exit_terminal_value, "discount_factor", terminal_df)
    dcf_exit_ev = sum_named("valuation.dcf.exit_enterprise_value", {f"PV_{period}_FCF": value for period, value in dcf_pv.items()} | {"PV_exit_terminal_value": pv_exit_terminal})
    dcf_exit_equity = sum_named("valuation.dcf.exit_equity_value", {"enterprise_value": dcf_exit_ev, "target_net_cash": target_net_cash})
    dcf_exit_price = divide("valuation.dcf.exit_price_per_share", "equity_value", dcf_exit_equity, "basic_shares_m", basic_shares)

    CHECKS.extend([
        ("Valuation base SOTP pieces equal target enterprise value", close(base["pv_connectivity"] + base["pv_space"] + base["pv_ai"] + base["pv_cursor"], base["target_ev"]), f"pieces={plain(base['pv_connectivity'] + base['pv_space'] + base['pv_ai'] + base['pv_cursor'])}; target_EV={plain(base['target_ev'])}"),
        ("Valuation base equity bridge equals enterprise value plus net cash", close(base["target_equity"], base["target_ev"] + target_net_cash), f"equity={plain(base['target_equity'])}"),
        ("Valuation scenario ordering", scenario_results["Bull"]["price_target"] > base["price_target"] > scenario_results["Bear"]["price_target"], "bull > base > bear"),
        ("DCF terminal formula denominator positive", dcf_wacc > terminal_growth, f"WACC={exact(dcf_wacc)}; terminal_growth={exact(terminal_growth)}"),
    ])

    VALUATION_SUMMARY.update({
        "base_pt": base["price_target"],
        "bull_pt": scenario_results["Bull"]["price_target"],
        "bear_pt": scenario_results["Bear"]["price_target"],
        "last_sale": last_sale,
    })

    scenario_assumption_rows: list[list[str]] = []
    for scenario in ("Bear", "Base", "Bull"):
        inputs = scenarios[scenario]
        scenario_assumption_rows.extend([
            [scenario, "Connectivity subscribers / ARPU", f"{plain(inputs['opening_subscribers_m'])}m → {plain(inputs['ending_subscribers_m'])}m / {money(inputs['arpu'])} [VIEW]", "`research.md` explicit subscriber and ARPU paths"],
            [scenario, "Enterprise & Government factor", f"{number(inputs['enterprise_factor'] * D('100'))}% of base [VIEW]", "Starshield remains embedded; standalone P&L not obtained"],
            [scenario, "Connectivity exit EBIT multiple", f"{plain(inputs['connectivity_exit_ebit_multiple'])}× [VIEW]", "Selected SOTP input; primary-source peer multiple not obtained"],
            [scenario, "Space multiple / Starship flights / $ per flight", f"{plain(inputs['space_exit_revenue_multiple'])}× / {plain(inputs['starship_commercial_flights'])} / {money(inputs['starship_revenue_per_flight'])} [VIEW]", "Non-zero Starship commercial view; list price not obtained"],
            [scenario, "AI capital conversion / Customer B haircut", f"{number(inputs['ai_capital_conversion_multiple'], '0.01') if scenario == 'Bear' else plain(inputs['ai_capital_conversion_multiple'])}× / {number(inputs['customer_b_haircut'] * D('100'))}% [VIEW]", "AI capex conversion with explicit concentration haircut"],
            [scenario, "Cursor revenue / EBIT margin / exit EBIT multiple", f"{money(inputs['cursor_revenue'])} / {number(inputs['cursor_ebit_margin'] * D('100'))}% / {plain(inputs['cursor_exit_ebit_multiple'])}× [VIEW]", "Cursor P&L and value view; no synergy premium"],
            [scenario, "WACC / years to FY2028", f"{number(inputs['wacc'] * D('100'))}% / {plain(target_years_from_fy2028)} [VIEW]", "Discount FY2028 segment values to the 12-month target date"],
        ])

    scenario_output_rows: list[list[str]] = []
    for scenario in ("Bear", "Base", "Bull"):
        slug = scenario.lower()
        result = scenario_results[scenario]
        scenario_output_rows.append([
            scenario,
            tagged(result["consumer_revenue"], "DEDUCTED", f"valuation.{slug}.consumer_revenue"),
            tagged(result["connectivity_ebit"], "DEDUCTED", f"valuation.{slug}.connectivity_ebit"),
            tagged(result["starship_revenue"], "DEDUCTED", f"valuation.{slug}.starship_commercial_revenue"),
            tagged(result["cursor_ebit"], "DEDUCTED", f"valuation.{slug}.cursor_EBIT"),
            tagged(result["target_ev"], "DEDUCTED", f"valuation.{slug}.target_enterprise_value"),
            tagged(result["target_equity"], "DEDUCTED", f"valuation.{slug}.target_equity_value"),
            tagged(result["price_target"], "DEDUCTED", f"valuation.{slug}.price_target"),
            f"{number(result['implied_change'] * D('100'))}% [DEDUCTED {formula_id(f'valuation.{slug}.implied_change')}]",
        ])

    base_bridge_rows = [
        ["Connectivity", "FY2028E scenario EBIT", tagged(base["connectivity_ebit"], "DEDUCTED", "valuation.base.connectivity_ebit"), "70× EBIT [VIEW]", tagged(base["connectivity_value"], "DEDUCTED", "valuation.base.connectivity_value_FY2028"), tagged(base["pv_connectivity"], "DEDUCTED", "valuation.base.pv_connectivity")],
        ["Space", "FY2028E launch plus Starship commercial revenue", tagged(base["space_revenue"], "DEDUCTED", "valuation.base.space_revenue"), "12× revenue [VIEW]", tagged(base["space_value"], "DEDUCTED", "valuation.base.space_value_FY2028"), tagged(base["pv_space"], "DEDUCTED", "valuation.base.pv_space")],
        ["AI core", "Cumulative FY2026E–FY2028E AI capex", tagged(ai_invested_capital, "DEDUCTED", "valuation.ai_invested_capital"), "2× capital, then 20% Customer B haircut [VIEW]", tagged(base["ai_value"], "DEDUCTED", "valuation.base.ai_value_FY2028"), tagged(base["pv_ai"], "DEDUCTED", "valuation.base.pv_ai")],
        ["Cursor", "FY2028E Cursor EBIT", tagged(base["cursor_ebit"], "DEDUCTED", "valuation.base.cursor_EBIT"), "40× EBIT [VIEW]", tagged(base["cursor_value"], "DEDUCTED", "valuation.base.cursor_value_FY2028"), tagged(base["pv_cursor"], "DEDUCTED", "valuation.base.pv_cursor")],
        ["**Enterprise value**", "Sum of pieces", "", "", tagged(base["end_ev"], "DEDUCTED", "valuation.base.end_FY2028_enterprise_value"), tagged(base["target_ev"], "DEDUCTED", "valuation.base.target_enterprise_value")],
        ["Net cash", "Target-date base cash bridge", "", "", "", tagged(target_net_cash, "DEDUCTED", "valuation.target_net_cash")],
        ["**Equity value**", "Target EV + net cash", "", "", "", tagged(base["target_equity"], "DEDUCTED", "valuation.base.target_equity_value")],
        ["**Price target**", "Equity value ÷ basic shares", tagged(basic_shares, "DEDUCTED", "balance.FY2026E.basic_shares", unit="plain"), "", "", tagged(base["price_target"], "DEDUCTED", "valuation.base.price_target")],
    ]

    already_priced_rows = [
        ["Last sale", money(last_sale, "0.01") + " [FACT]", "Nasdaq `lastTradeTimestamp` 2026-08-27"],
        ["Current market capitalization", tagged(current_market_cap, "FACT"), "`register.md` What is already priced"],
        ["Current mixed-date enterprise value", tagged(current_ev, "DEDUCTED", "valuation.current_enterprise_value"), "Market cap plus debt less cash and securities"],
        ["Base target implied enterprise value", tagged(base["target_ev"], "DEDUCTED", "valuation.base.target_enterprise_value"), "Discounted SOTP pieces"],
        ["Current EV / FY2028E revenue", f"{plain(current_ev_revenue)}× [DEDUCTED {formula_id('valuation.current_EV_to_FY2028_revenue')}]", "Current EV ÷ model revenue"],
        ["Base target EV / FY2028E revenue", f"{plain(implied_target_ev_revenue)}× [DEDUCTED {formula_id('valuation.base.target_EV_to_FY2028_revenue')}]", "Target EV ÷ model revenue"],
        ["Current EV / FY2028E EBIT", f"{plain(current_ev_ebit)}× [DEDUCTED {formula_id('valuation.current_EV_to_FY2028_EBIT')}]", "Current EV ÷ model EBIT"],
        ["Base target EV / FY2028E EBIT", f"{plain(implied_target_ev_ebit)}× [DEDUCTED {formula_id('valuation.base.target_EV_to_FY2028_EBIT')}]", "Target EV ÷ model EBIT"],
        ["Current EV premium to base target EV", f"{number(current_premium_to_base_ev * D('100'))}% [DEDUCTED {formula_id('valuation.current_EV_premium_to_base_target_EV')}]", "Same FY2028 model denominator"],
    ]

    dcf_output_rows = [
        ["WACC", f"{number(dcf_wacc * D('100'))}% [VIEW]", "Named discount-rate input"],
        ["Terminal growth", f"{number(terminal_growth * D('100'))}% [VIEW]", "Perpetuity-growth input"],
        ["Exit FCF multiple", f"{plain(exit_fcf_multiple)}× [VIEW]", "Alternative terminal-value check"],
        ["Perpetuity DCF enterprise value", tagged(dcf_ev, "DEDUCTED", "valuation.dcf.enterprise_value"), "Extended explicit fade plus terminal value"],
        ["Perpetuity DCF value / share", tagged(dcf_price, "DEDUCTED", "valuation.dcf.price_per_share"), "Basic shares"],
        ["PV terminal value / DCF EV", f"{number(terminal_share * D('100'))}% [DEDUCTED {formula_id('valuation.dcf.terminal_value_share')}]", "Shows terminal dependence"],
        ["Exit-multiple DCF enterprise value", tagged(dcf_exit_ev, "DEDUCTED", "valuation.dcf.exit_enterprise_value"), "25× FY2033E FCF terminal"],
        ["Exit-multiple DCF value / share", tagged(dcf_exit_price, "DEDUCTED", "valuation.dcf.exit_price_per_share"), "Basic shares"],
    ]

    return f"""# SpaceX valuation

as_of: {as_of}
target_date: {target_date}
units: USD millions except per-share data, shares and operating drivers
generator: `compute.py`

## Price target

| item | value | basis |
| --- | ---: | --- |
| **12-month base price target** | **{money(base['price_target'], '0.01')} [DEDUCTED {formula_id('valuation.base.price_target')}]** | Segment SOTP discounted to {target_date} |
| Last sale | {money(last_sale, '0.01')} [FACT] | Nasdaq `lastTradeTimestamp` 2026-08-27 |
| Implied change | {number(base['implied_change'] * D('100'))}% [DEDUCTED {formula_id('valuation.base.implied_change')}] | Price target ÷ last sale − one |
| Basic shares | {plain(basic_shares)} million [DEDUCTED {formula_id('balance.FY2026E.basic_shares')}] | Post-Cursor plus pending EchoStar shares; fully diluted shares not obtained |
| Load-bearing method | SOTP | Connectivity EBIT including pending spectrum/mobile, Space revenue including Starship, AI invested-capital conversion, and Cursor EBIT |

The target is generated from the segment model and named valuation inputs below. It is not fitted to the last sale.

## Load-bearing SOTP — base bridge

{markdown_table(["piece", "metric", "metric value", "valuation input", "FY2028 value", "12-month value"], base_bridge_rows, ["---", "---", "---:", "---", "---:", "---:"])}

Target net cash uses FY2026E ending liquidity less debt and eight months of FY2027E FCF, with no new financing. The pending EchoStar cash and share consideration is included. Cursor P&L is included; synergy premium is zero.

## Bear / base / bull assumptions

{markdown_table(["scenario", "driver", "assumption", "treatment"], scenario_assumption_rows)}

Starship commercial revenue is non-zero in every scenario. Bull and bear change Starship cadence/yield, Cursor revenue/margin, Connectivity ARPU/net adds, Enterprise & Government realization, AI capex conversion, Customer B concentration haircut, exit multiples and WACC.

## Scenario outputs

{markdown_table(["scenario", "FY2028 Consumer revenue", "FY2028 Connectivity EBIT", "Starship revenue", "Cursor EBIT", "target EV", "target equity", "price / share", "vs last sale"], scenario_output_rows, ["---", "---:", "---:", "---:", "---:", "---:", "---:", "---:", "---:"])}

## Dilution sensitivity — not known fully diluted shares

| item | value | treatment |
| --- | ---: | --- |
| Basic shares | {plain(basic_shares)} million [DEDUCTED {formula_id('balance.FY2026E.basic_shares')}] | Base denominator includes pending EchoStar shares |
| Potentially dilutive awards | {plain(potential_awards)} million [FACT] | Sensitivity only; treasury-stock-method dilution not obtained |
| Sensitivity shares | {tagged(sensitivity_shares, 'DEDUCTED', 'valuation.dilution_sensitivity_shares', unit='plain')} million | Basic plus all potentially dilutive awards |
| Sensitivity price / share | {tagged(diluted_sensitivity_pt, 'DEDUCTED', 'valuation.dilution_sensitivity_price')} | Same base equity value |
| Price haircut | {number(dilution_haircut * D('100'))}% [DEDUCTED {formula_id('valuation.dilution_sensitivity_haircut')}] | Sensitivity price versus base |

The sensitivity does not assert that the awards are fully dilutive.

## What the last sale already prices

{markdown_table(["measure", "value", "basis"], already_priced_rows, ["---", "---:", "---"])}

## Consolidated DCF check — not load-bearing

Explicit model FCF is negative through FY2027E and turns positive in FY2028E. The extension makes the terminal auditable by fading consolidated revenue growth and FCF margins explicitly.

{markdown_table(["period", "revenue", "fade assumption", "FCF", "PV FCF"], dcf_rows, ["---", "---:", "---", "---:", "---:"])}

{markdown_table(["item", "value", "basis"], dcf_output_rows, ["---", "---:", "---"])}

## Comps check

| peer set | primary-source trading multiple | treatment |
| --- | --- | --- |
| Listed launch providers | {not_obtained()} | No filing/exchange-derived comparable EV multiple obtained |
| Satellite connectivity providers | {not_obtained()} | No filing/exchange-derived comparable EV multiple obtained |
| AI infrastructure / platform providers | {not_obtained()} | No filing/exchange-derived comparable EV multiple obtained |

No peer EV/EBITDA multiple is invented. Current and target implied multiples are shown in “What the last sale already prices.”

## Exclusions and gaps

- EchoStar consideration and shares are pending `[VIEW]` base inputs; final closing mechanics remain {not_obtained()}.
- Cursor P&L is a forecast view inside AI; synergy premium is zero and filing revenue/margins remain {not_obtained()}.
- Starshield standalone P&L, launch list price, GPU-hours and utilization remain {not_obtained()}.
- Fully diluted shares remain {not_obtained()}; the award count is only a sensitivity.

{formula_appendix("Valuation formula register", ("valuation.",))}
"""


def write_outputs() -> None:
    outputs = {
        "segments.md": build_segments_md(),
        "income.md": build_income_md(),
        "balance.md": build_balance_md(),
        "cashflow.md": build_cashflow_md(),
        "valuation.md": build_valuation_md(),
    }
    for filename, content in outputs.items():
        rendered = content.replace("[VIEW]", VIEW_TAG)
        (ROOT / filename).write_text(rendered.rstrip() + "\n", encoding="utf-8")


def print_summary() -> None:
    for name, passed, detail in CHECKS:
        print(f"{'pass' if passed else 'fail'}: {name} ({detail})")
    print("\nForecast summary (USD millions except shares):")
    for period in ("FY2026E", "FY2027E", "FY2028E"):
        print(
            f"{period}: revenue={plain(INCOME[period]['revenue'])}; "
            f"EBIT={plain(INCOME[period]['ebit'])}; FCF={plain(CASHFLOW[period]['fcf'])}; "
            f"ending_cash={plain(CASHFLOW[period]['ending_cash'])}; "
            f"basic_shares_m={plain(BASIC_SHARES[period])}"
        )
    print(
        "\nValuation summary: "
        f"base_PT={money(VALUATION_SUMMARY['base_pt'], '0.01')}; "
        f"bull={money(VALUATION_SUMMARY['bull_pt'], '0.01')}; "
        f"bear={money(VALUATION_SUMMARY['bear_pt'], '0.01')}; "
        f"last_sale={money(VALUATION_SUMMARY['last_sale'], '0.01')}"
    )


if __name__ == "__main__":
    write_outputs()
    print_summary()
    if not all(passed for _, passed, _ in CHECKS):
        raise SystemExit(1)
