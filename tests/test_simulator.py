from app.engine.simulator import simulate_pricing_scenarios


def test_scenario_simulator():
    res = simulate_pricing_scenarios(
        baseline_price=50.0,
        unit_cost=25.0,
        baseline_volume=1000.0,
        fixed_costs=5000.0,
        elasticity_assumed=-1.2,
    )
    assert len(res.scenarios) > 0
    assert res.baseline_price == 50.0
    assert res.optimal_profit_scenario is not None
    assert res.optimal_roi_scenario is not None
    assert "Maximum net profit" in res.summary
