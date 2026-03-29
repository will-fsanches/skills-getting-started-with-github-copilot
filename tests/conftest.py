import pytest
from fastapi.testclient import TestClient
import copy
from src.app import app, ORIGINAL_ACTIVITIES


@pytest.fixture(autouse=True)
def reset_activities(monkeypatch):
    """Reset the activities dict to original state before each test"""
    monkeypatch.setattr("src.app.activities", copy.deepcopy(ORIGINAL_ACTIVITIES))


@pytest.fixture
def client():
    """FastAPI test client"""
    return TestClient(app)