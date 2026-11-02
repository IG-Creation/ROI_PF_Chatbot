import pytest
from app.engine.roi import calculate_roi, calculate_npv


def test_calculate_simple_roi_positive():
    res = calculate_roi(cost=1000.0, gain=1500.0)
    assert res.initial_cost == 1000.0
    assert res.total_gain == 1500.0
    assert res.net_profit == 500.0
    assert res.roi_percent == 50.0
    assert res.is_profitable is True


def test_calculate_simple_roi_loss():
    res = calculate_roi(cost=1000.0, gain=800.0)
    assert res.net_profit == -200.0
    assert res.roi_percent == -20.0
    assert res.is_profitable is False


def test_calculate_annualized_roi():
    res = calculate_roi(cost=1000.0, gain=1440.0, years=2.0)
    assert res.annualized_roi_percent is not None
    # (1440 / 1000)**0.5 - 1 = 1.2 - 1 = 20%
    assert pytest.approx(res.annualized_roi_percent, rel=1e-2) == 20.0


def test_roi_zero_or_negative_cost_raises():
    with pytest.raises(ValueError):
        calculate_roi(cost=0.0, gain=500.0)
    with pytest.raises(ValueError):
        calculate_roi(cost=-100.0, gain=500.0)


def test_calculate_npv():
    res = calculate_npv(initial_investment=1000.0, discount_rate_percent=10.0, cash_flows=[600.0, 600.0])
    # PV = 600 / 1.1 + 600 / 1.21 = 545.45 + 495.87 = 1041.32 - 1000 = ~41.32
    assert res.is_viable is True
    assert pytest.approx(res.npv, rel=1e-2) == 41.32
