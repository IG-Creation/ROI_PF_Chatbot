from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    res = client.get("/api/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"


def test_api_chat():
    res = client.post("/api/chat", json={"message": "Calculate ROI for cost 1000 and return 2000"})
    assert res.status_code == 200
    data = res.json()
    assert data["intent"] == "CALCULATE_ROI"
    assert data["data"]["roi_percent"] == 100.0


def test_api_direct_roi():
    res = client.post("/api/roi", json={"cost": 5000, "gain": 7500})
    assert res.status_code == 200
    assert res.json()["roi_percent"] == 50.0


def test_api_direct_break_even():
    res = client.post("/api/pricing/break-even", json={
        "fixed_costs": 10000,
        "variable_cost_per_unit": 5,
        "selling_price": 15
    })
    assert res.status_code == 200
    assert res.json()["break_even_units"] == 1000.0


def test_api_catalog_upload():
    csv_content = "product,cost,price,volume\nWidget A,10,25,100\nWidget B,20,50,200\n"
    res = client.post(
        "/api/upload/catalog",
        files={"file": ("test.csv", csv_content.encode("utf-8"), "text/csv")},
    )
    assert res.status_code == 200
    data = res.json()
    assert data["count"] == 2
    assert len(data["products"]) == 2
    assert data["total_revenue"] == 12500.0
