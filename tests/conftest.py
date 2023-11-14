import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app


@pytest.fixture(scope="class")
def mock_client():
    client = TestClient(app)
    
    return client