import pytest
from app.engine.pricing import (
    calculate_break_even,
    calculate_target_roi_pricing,
    calculate_price_elasticity,
    simulate_markdown_impact,
)


def test_break_even():
    # Fixed = 20,000, Var = 10, Price = 30 -> CM = 20, Units = 1000, Revenue = 30,000
    res = calculate_break_even(fixed_costs=20000.0, variable_cost_per_unit=10.0, selling_price=30.0)
    assert res.contribution_margin == 20.0
    assert res.break_even_units == 1000.0
    assert res.break_even_revenue == 30000.0


def test_break_even_invalid_price():
    with pytest.raises(ValueError):
        calculate_break_even(fixed_costs=1000.0, variable_cost_per_unit=20.0, selling_price=15.0)


def test_target_roi_pricing():
    # Fixed = 10000, Var = 10, Units = 1000, Capital = 20000, Target ROI = 25% (Profit = 5000)
    # Price = 10 + (10000 + 5000)/1000 = 10 + 15 = 25
    res = calculate_target_roi_pricing(
        fixed_costs=10000.0,
        variable_cost_per_unit=10.0,
        expected_units=1000.0,
        invested_capital=20000.0,
        target_roi_percent=25.0,
    )
    assert res.recommended_price == 25.0
    assert res.projected_profit == 5000.0
    assert pytest.approx(res.projected_roi_percent, rel=1e-2) == 25.0


def test_price_elasticity():
    # P1 = 50, P2 = 60, Q1 = 1000, Q2 = 800
    res = calculate_price_elasticity(old_price=50.0, new_price=60.0, old_quantity=1000.0, new_quantity=800.0)
    assert res.elasticity < 0
    assert "Elastic" in res.elasticity_type


def test_markdown_simulation():
    # Price = 100, Cost = 60, Volume = 500, Discount = 20% -> New Price = 80
    # Base margin = 40, New margin = 20 -> Base gross profit = 20,000 -> Required units = 1000 (100% surge)
    res = simulate_markdown_impact(base_price=100.0, unit_cost=60.0, base_units=500.0, discount_percent=20.0)
    assert res.discounted_price == 80.0
    assert res.new_unit_margin == 20.0
    assert res.required_units_to_maintain_profit == 1000.0
    assert res.volume_increase_needed_percent == 100.0
