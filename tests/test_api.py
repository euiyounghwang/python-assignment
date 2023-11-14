
import pytest


def test_mock_api(mock_client):
    response = mock_client.get("/v1")
    assert response is not None
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello World"
    }
    
    
def test_mock_lookup_api(mock_client):
    response = mock_client.get("/v1")
    assert response is not None
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello World"
    }
    
    # --
    # Lookup the different keys
    sample_payload ={
        "first_input_array": [
            "test",
            "abc"
        ],
        "second_input_array": [
            "abc",
            "xyz"
        ]
    }
    
    # Create Item
    response = mock_client.post("/v1/process_lookup", json=sample_payload)
    assert response.status_code == 200
    assert response.json() == {"result" : sample_payload}
    