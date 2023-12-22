"""Test API Routes

Usage
    In an activated virtual environment run:
        python -m pytest tests/test_api_routes.py
"""
from fastapi.testclient import TestClient
from compare.api_service.api_routes import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_read_item():
    response = client.get("/components/some_component?q=test_query")
    assert response.status_code == 200
    assert response.json() == {"component_name": "some_component", "q": "test_query"}