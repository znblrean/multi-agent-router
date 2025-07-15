import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ask_endpoint():
    response = client.post("/ask", json={"question": "۲ به علاوه ۲"})
    assert response.status_code == 200
    assert "answer" in response.json()
    assert "agent" in response.json()

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}