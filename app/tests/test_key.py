from starlette.testclient import TestClient

from main import app

client = TestClient(app)


def test_set_key_value():
    payload = {"key": "key1", "value": "value1"}
    response = client.post("/set", json=payload)
    assert response.status_code == 201
    assert response.json() == payload

def test_get_key_value():
    key = "key1"
    expected_response = {"key": "key1", "value": "value1"}
    response = client.get(f"/get/{key}")
    assert response.status_code == 200
    assert response.json() == expected_response

def test_search_keys_prefix():
    expected_response = ["key1"]
    response = client.get("/search", params={"prefix": "key"})
    assert response.status_code == 200
    assert response.json() == expected_response

def test_search_keys_suffix():
    expected_response = ["key1"]
    response = client.get("/search", params={"suffix": "y1"})
    assert response.status_code == 200
    assert response.json() == expected_response

def test_set_key_value_negative():
    expected_response = {"detail": "key already exists"}
    payload = {"key": "key1", "value": "value1"}
    response = client.post("/set", json=payload)
    assert response.status_code == 409
    assert response.json() == expected_response

def test_get_key_value_negative():
    key = "key123"
    expected_response = {"detail": "key not found"}
    response = client.get(f"/get/{key}")
    assert response.status_code == 404
    assert response.json() == expected_response

def test_search_keys_prefix_negative():
    expected_response = []
    response = client.get("/search", params={"prefix": "key123"})
    assert response.status_code == 200
    assert response.json() == expected_response

def test_search_keys_suffix_negative():
    expected_response = []
    response = client.get("/search", params={"suffix": "key123"})
    assert response.status_code == 200
    assert response.json() == expected_response