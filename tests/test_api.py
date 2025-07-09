from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_ask_endpoint():
    response = client.post("/ask", json={"question": "2+2"})
    assert response.status_code == 200
    assert "agent" in response.json()
    assert "answer" in response.json()