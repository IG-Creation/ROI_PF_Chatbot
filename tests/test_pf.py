import pytest
from app.engine.pf import calculate_profit_factor, calculate_pricing_factor


def test_profit_factor_standard():
    res = calculate_profit_factor(gross_profit=15000.0, gross_loss=5000.0)
    assert res.profit_factor == 3.0
    assert res.net_profit == 10000.0
    assert res.is_profitable is True
    assert res.rating == "Exceptional"


def test_profit_factor_loss():
    res = calculate_profit_factor(gross_profit=5000.0, gross_loss=10000.0)
    assert res.profit_factor == 0.5
    assert res.net_profit == -5000.0
    assert res.is_profitable is False
    assert res.rating == "Unprofitable"


def test_profit_factor_zero_loss():
    res = calculate_profit_factor(gross_profit=10000.0, gross_loss=0.0)
    assert res.profit_factor == 999.99
    assert res.rating == "Flawless"


def test_pricing_factor_with_price():
    # Cost = 50, Price = 100 -> PF = 2.0 (Keystone)
    res = calculate_pricing_factor(unit_cost=50.0, selling_price=100.0)
    assert res.pricing_factor == 2.0
    assert res.markup_percent == 100.0
    assert res.gross_margin_percent == 50.0
    assert res.unit_margin == 50.0
    assert "Keystone" in res.rating


def test_pricing_factor_with_target():
    # Cost = 40, Target PF = 2.5 -> Price = 100
    res = calculate_pricing_factor(unit_cost=40.0, target_pricing_factor=2.5)
    assert res.selling_price == 100.0
    assert res.pricing_factor == 2.5
    assert res.markup_percent == 150.0
    assert res.gross_margin_percent == 60.0
