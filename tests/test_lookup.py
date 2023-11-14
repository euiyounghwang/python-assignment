
import pytest

@pytest.mark.skip(reason="no way of currently testing this")
def test_skip():
    assert 1 != 1
    
    
def test_mock_api(mock_client):
    response = mock_client.get("/v1")
    assert response is not None
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}