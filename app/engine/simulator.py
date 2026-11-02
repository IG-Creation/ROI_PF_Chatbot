"""
Pricing & ROI Scenario Simulator.
Generates what-if pricing grids across varied price adjustments and volume elasticity responses.
"""

from typing import List, Optional
from pydantic import BaseModel


class ScenarioRow(BaseModel):
    label: str
    price_change_percent: float
    price: float
    estimated_volume: float
    revenue: float
    total_cost: float
    net_profit: float
    roi_percent: float
    pricing_factor: float
    gross_margin_percent: float


class SimulationResult(BaseModel):
    baseline_price: float
    baseline_volume: float
    unit_cost: float
    fixed_costs: float
    elasticity_assumed: float
    scenarios: List[ScenarioRow]
    optimal_profit_scenario: ScenarioRow
    optimal_roi_scenario: ScenarioRow
    summary: str


def simulate_pricing_scenarios(
    baseline_price: float,
    unit_cost: float,
    baseline_volume: float,
    fixed_costs: float = 0.0,
    elasticity_assumed: float = -1.2,
    price_variations: Optional[List[float]] = None,
) -> SimulationResult:
    """
    Run multi-scenario pricing simulation.

    :param baseline_price: Current product or service price.
    :param unit_cost: Variable unit cost.
    :param baseline_volume: Current units sold.
    :param fixed_costs: Fixed operating costs allocated.
    :param elasticity_assumed: Price elasticity of demand (negative number, e.g. -1.2).
    :param price_variations: List of percentage changes, e.g. [-20, -10, -5, 0, 5, 10, 20].
    """
    if baseline_price <= 0 or unit_cost <= 0 or baseline_volume <= 0:
        raise ValueError("Price, cost, and baseline volume must be strictly positive.")

    if price_variations is None:
        price_variations = [-20.0, -15.0, -10.0, -5.0, 0.0, 5.0, 10.0, 15.0, 20.0]

    scenarios: List[ScenarioRow] = []

    for delta_p in price_variations:
        new_price = baseline_price * (1.0 + (delta_p / 100.0))
        # Volume change = elasticity * price change %
        volume_change_pct = elasticity_assumed * delta_p
        new_volume = max(0.0, baseline_volume * (1.0 + (volume_change_pct / 100.0)))

        revenue = new_price * new_volume
        total_cost = fixed_costs + (unit_cost * new_volume)
        net_profit = revenue - total_cost

        roi_pct = (net_profit / total_cost * 100.0) if total_cost > 0 else 0.0
        pf = (new_price / unit_cost) if unit_cost > 0 else 0.0
        gross_margin_pct = ((new_price - unit_cost) / new_price * 100.0) if new_price > 0 else 0.0

        label = f"{delta_p:+.0f}%" if delta_p != 0 else "Baseline"

        row = ScenarioRow(
            label=label,
            price_change_percent=delta_p,
            price=round(new_price, 2),
            estimated_volume=round(new_volume, 1),
            revenue=round(revenue, 2),
            total_cost=round(total_cost, 2),
            net_profit=round(net_profit, 2),
            roi_percent=round(roi_pct, 2),
            pricing_factor=round(pf, 2),
            gross_margin_percent=round(gross_margin_pct, 2),
        )
        scenarios.append(row)

    optimal_profit = max(scenarios, key=lambda s: s.net_profit)
    optimal_roi = max(scenarios, key=lambda s: s.roi_percent)

    summary = (
        f"Maximum net profit of ${optimal_profit.net_profit:,.2f} is reached at "
        f"{optimal_profit.label} price (${optimal_profit.price:.2f}, volume: {optimal_profit.estimated_volume:,.0f}). "
        f"Maximum ROI of {optimal_roi.roi_percent:.1f}% occurs at {optimal_roi.label} price."
    )

    return SimulationResult(
        baseline_price=round(baseline_price, 2),
        baseline_volume=round(baseline_volume, 2),
        unit_cost=round(unit_cost, 2),
        fixed_costs=round(fixed_costs, 2),
        elasticity_assumed=round(elasticity_assumed, 2),
        scenarios=scenarios,
        optimal_profit_scenario=optimal_profit,
        optimal_roi_scenario=optimal_roi,
        summary=summary,
    )
