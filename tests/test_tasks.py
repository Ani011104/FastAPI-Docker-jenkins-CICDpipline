# tests/test_tasks.py
from fastapi.testclient import TestClient
from app.main import app
import pytest
from app.database import connections
import mongomock
import uuid

@pytest.fixture
def client():
    mock_client = mongomock.MongoClient()
    mock_db = mock_client["test_db"]
    mock_collection = mock_db["tasks"]
    connections.collection = mock_collection
    return TestClient(app)

@pytest.fixture
def payload():
    return {
        "user_id": f"test_user_{uuid.uuid4()}",
        "title": "Test Task",
        "description": "Testing payload works",
        "completed": False
    }

def test_create_task(client, payload):
    response = client.post('/tasks', json=payload)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "task_id" in response.json()

def test_get_tasks(client, payload):
    client.post("/tasks", json=payload)
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "tasks" in data
    assert isinstance(data["tasks"], list)
    assert len(data["tasks"]) >= 1
    assert "title" in data["tasks"][0]

def test_delete_task(client, payload):
    create_response = client.post('/tasks', json=payload)
    task_id = create_response.json()["task_id"]
    
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200