from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_activity_list_response_is_not_cached():
    response = client.get("/activities")

    assert response.status_code == 200
    assert "no-store" in response.headers.get("cache-control", "").lower()
