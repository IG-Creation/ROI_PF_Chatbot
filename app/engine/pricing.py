"""
Managed Pricing Engine.
Covers:
1. Break-even analysis (units & revenue)
2. Target ROI Pricing
3. Price Elasticity of Demand (PED)
4. Markdown & Discount Impact Simulation
"""

from typing import Optional
from pydantic import BaseModel


class BreakEvenResult(BaseModel):
    fixed_costs: float
    variable_cost_per_unit: float
    selling_price: float
    contribution_margin: float
    contribution_margin_ratio: float
    break_even_units: float
    break_even_revenue: float
    interpretation: str


class TargetROIPricingResult(BaseModel):
    fixed_costs: float
    variable_cost_per_unit: float
    expected_units: float
    invested_capital: float
    target_roi_percent: float
    recommended_price: float
    total_cost: float
    total_revenue: float
    projected_profit: float
    projected_roi_percent: float
    markup_on_cost_percent: float


class ElasticityResult(BaseModel):
    old_price: float
    new_price: float
    old_quantity: float
    new_quantity: float
    price_change_percent: float
    quantity_change_percent: float
    elasticity: float
    elasticity_type: str
    revenue_impact_summary: str


class MarkdownImpactResult(BaseModel):
    base_price: float
    unit_cost: float
    base_units: float
    discount_percent: float
    discounted_price: float
    base_gross_profit: float
    new_unit_margin: float
    required_units_to_maintain_profit: float
    volume_increase_needed_percent: float
    is_feasible: bool
    warning: Optional[str] = None


def calculate_break_even(
    fixed_costs: float,
    variable_cost_per_unit: float,
    selling_price: float,
) -> BreakEvenResult:
    """
    Calculate break-even point in units and revenue.
    """
    if fixed_costs < 0:
        raise ValueError("Fixed costs cannot be negative.")
    if variable_cost_per_unit < 0:
        raise ValueError("Variable cost cannot be negative.")
    if selling_price <= variable_cost_per_unit:
        raise ValueError("Selling price must exceed variable cost per unit to achieve break-even.")

    contribution_margin = selling_price - variable_cost_per_unit
    cm_ratio = (contribution_margin / selling_price) * 100.0
    break_even_units = fixed_costs / contribution_margin
    break_even_revenue = break_even_units * selling_price

    interpretation = (
        f"You must sell {int(break_even_units) + 1:,} units (${break_even_revenue:,.2f} revenue) "
        f"to cover ${fixed_costs:,.2f} in fixed overhead. Every unit beyond generates ${contribution_margin:,.2f} pure profit."
    )

    return BreakEvenResult(
        fixed_costs=round(fixed_costs, 2),
        variable_cost_per_unit=round(variable_cost_per_unit, 2),
        selling_price=round(selling_price, 2),
        contribution_margin=round(contribution_margin, 2),
        contribution_margin_ratio=round(cm_ratio, 2),
        break_even_units=round(break_even_units, 2),
        break_even_revenue=round(break_even_revenue, 2),
        interpretation=interpretation,
    )


def calculate_target_roi_pricing(
    fixed_costs: float,
    variable_cost_per_unit: float,
    expected_units: float,
    invested_capital: float,
    target_roi_percent: float,
) -> TargetROIPricingResult:
    """
    Determine selling price required to achieve a target ROI on capital invested.
    Price = VariableCost + (FixedCosts + (TargetROI% * Capital)) / ExpectedUnits
    """
    if expected_units <= 0:
        raise ValueError("Expected units must be greater than zero.")
    if invested_capital < 0:
        raise ValueError("Invested capital cannot be negative.")

    target_profit = (target_roi_percent / 100.0) * invested_capital
    required_price = variable_cost_per_unit + ((fixed_costs + target_profit) / expected_units)

    total_cost = fixed_costs + (variable_cost_per_unit * expected_units)
    unit_total_cost = total_cost / expected_units
    markup_percent = ((required_price - unit_total_cost) / unit_total_cost) * 100.0 if unit_total_cost > 0 else 0.0

    total_revenue = required_price * expected_units
    projected_profit = total_revenue - total_cost
    projected_roi = (projected_profit / invested_capital * 100.0) if invested_capital > 0 else 0.0

    return TargetROIPricingResult(
        fixed_costs=round(fixed_costs, 2),
        variable_cost_per_unit=round(variable_cost_per_unit, 2),
        expected_units=round(expected_units, 2),
        invested_capital=round(invested_capital, 2),
        target_roi_percent=round(target_roi_percent, 2),
        recommended_price=round(required_price, 2),
        total_cost=round(total_cost, 2),
        total_revenue=round(total_revenue, 2),
        projected_profit=round(projected_profit, 2),
        projected_roi_percent=round(projected_roi, 2),
        markup_on_cost_percent=round(markup_percent, 2),
    )


def calculate_price_elasticity(
    old_price: float,
    new_price: float,
    old_quantity: float,
    new_quantity: float,
) -> ElasticityResult:
    """
    Calculate Price Elasticity of Demand (PED) using the midpoint formula.
    """
    if old_price <= 0 or new_price <= 0 or old_quantity <= 0 or new_quantity <= 0:
        raise ValueError("Prices and quantities must be positive numbers greater than 0.")

    delta_p = new_price - old_price
    avg_p = (old_price + new_price) / 2.0
    pct_p = (delta_p / avg_p) * 100.0

    delta_q = new_quantity - old_quantity
    avg_q = (old_quantity + new_quantity) / 2.0
    pct_q = (delta_q / avg_q) * 100.0

    if pct_p == 0:
        elasticity = 0.0
    else:
        elasticity = pct_q / pct_p

    abs_e = abs(elasticity)
    if abs_e > 1.05:
        e_type = "Elastic (|Ed| > 1)"
        if delta_p > 0:
            summary = "Demand drops faster than price increases. Raising prices reduced total revenue."
        else:
            summary = "Demand expands faster than price discount. Price cuts boost total revenue."
    elif abs_e < 0.95:
        e_type = "Inelastic (|Ed| < 1)"
        if delta_p > 0:
            summary = "Customers are relatively price-insensitive. Raising price increases total revenue."
        else:
            summary = "Price discount generated weak demand response. Cutting price hurt total revenue."
    else:
        e_type = "Unitary Elastic (|Ed| ≈ 1)"
        summary = "Proportional reaction. Total revenue remains largely neutral."

    return ElasticityResult(
        old_price=round(old_price, 2),
        new_price=round(new_price, 2),
        old_quantity=round(old_quantity, 2),
        new_quantity=round(new_quantity, 2),
        price_change_percent=round(pct_p, 2),
        quantity_change_percent=round(pct_q, 2),
        elasticity=round(elasticity, 3),
        elasticity_type=e_type,
        revenue_impact_summary=summary,
    )


def simulate_markdown_impact(
    base_price: float,
    unit_cost: float,
    base_units: float,
    discount_percent: float,
) -> MarkdownImpactResult:
    """
    Simulate the effect of a price markdown / discount.
    Calculates the exact volume boost required to keep gross dollar profit unchanged.
    """
    if base_price <= unit_cost:
        raise ValueError("Base price must be greater than unit cost.")
    if base_units <= 0:
        raise ValueError("Base units must be greater than zero.")
    if discount_percent < 0 or discount_percent >= 100:
        raise ValueError("Discount percent must be between 0 and 100.")

    discounted_price = base_price * (1.0 - (discount_percent / 100.0))
    base_unit_margin = base_price - unit_cost
    new_unit_margin = discounted_price - unit_cost
    base_gross_profit = base_unit_margin * base_units

    if new_unit_margin <= 0:
        return MarkdownImpactResult(
            base_price=round(base_price, 2),
            unit_cost=round(unit_cost, 2),
            base_units=round(base_units, 2),
            discount_percent=round(discount_percent, 2),
            discounted_price=round(discounted_price, 2),
            base_gross_profit=round(base_gross_profit, 2),
            new_unit_margin=round(new_unit_margin, 2),
            required_units_to_maintain_profit=float("inf"),
            volume_increase_needed_percent=float("inf"),
            is_feasible=False,
            warning="Discounted price falls below unit cost. Every sale will generate a net loss.",
        )

    required_units = base_gross_profit / new_unit_margin
    vol_increase_pct = ((required_units - base_units) / base_units) * 100.0

    warning = None
    if vol_increase_pct > 50:
        warning = f"High hurdle: Requires a {vol_increase_pct:.1f}% surge in sales volume just to stay even."

    return MarkdownImpactResult(
        base_price=round(base_price, 2),
        unit_cost=round(unit_cost, 2),
        base_units=round(base_units, 2),
        discount_percent=round(discount_percent, 2),
        discounted_price=round(discounted_price, 2),
        base_gross_profit=round(base_gross_profit, 2),
        new_unit_margin=round(new_unit_margin, 2),
        required_units_to_maintain_profit=round(required_units, 2),
        volume_increase_needed_percent=round(vol_increase_pct, 2),
        is_feasible=True,
        warning=warning,
    )
