
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
    # Case#1: Lookup the different keys
    # --
    sample_payload ={
        "first_input_array_lookup": [
            "xyz"
        ],
        "second_input_array_lookup": [
            "test"
        ]
    }
    
    # Create Post Method API
    response = mock_client.post("/v1/process_lookup", json=sample_payload)
    assert response.status_code == 200
    assert response.json() == {"result" : sample_payload}
    
     # --
    # Case#2: Lookup the different keys
    # --
    sample_payload ={
        "first_input_array": [
            
        ],
        "second_input_array": [
            "abc",
            "xyz"
        ]
    }
    
    # Create Post Method API
    response = mock_client.post("/v1/process_lookup", json=sample_payload)
    assert response.status_code == 200
    assert response.json() == {
        "result" : {
            "first_input_array_lookup": [
                "abc",
                "xyz"
            ],
            "second_input_array_lookup": [
            ]
        }
    }
    