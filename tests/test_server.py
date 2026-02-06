from fastapi.testclient import TestClient
from app.server import app

client = TestClient(app, raise_server_exceptions=False)

def test_health_returns_200():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status" : "OK"}

def test_process_valid_returns_200():
    response = client.post("/process" , json ={"value" : 5})
    assert response.status_code == 200
    assert response.json() == {"received" : 5}
    
def test_process_missing_value_returns_400():
    response = client.post("/process" , json = {"key" : 5})
    assert response.status_code == 400

def test_error_endpoint_returns_500():
    response = client.get("/error")
    assert response.status_code == 500