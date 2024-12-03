import pytest
from fastapi.testclient import TestClient
from app import app  # Asegúrate de que 'app' se importe correctamente desde tu archivo principal

client = TestClient(app)

# Prueba para la ruta "/"
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Welcome to WordPlay API ;)"}

# Prueba para la ruta "/add_word/"
def test_add_word():
    payload = {
        "table_name": "test_table",
        "word": "example"
    }
    response = client.post("/add_word/", json=payload)
    assert response.status_code == 200
    assert "message" in response.json()
    assert "flag" in response.json()

# Prueba para la ruta "/remove_word/"
def test_remove_word():
    payload = {
        "table_name": "test_table",
        "word": "example"
    }
    response = client.delete("/remove_word/", json=payload)
    assert response.status_code == 200
    assert "message" in response.json()
    assert "flag" in response.json()

# Prueba para la ruta "/get_all_words/"
def test_get_all_words():
    payload = {"table_name": "test_table"}
    response = client.get("/get_all_words/", json=payload)
    assert response.status_code == 200
    assert "words" in response.json()

# Prueba para la ruta "/get_a_word/"
def test_get_a_word():
    payload = {"table_name": "test_table"}
    response = client.get("/get_a_word/", json=payload)
    assert response.status_code == 200
    assert "word" in response.json()

# Prueba para la ruta "/get_model_response/"
def test_get_model_response():
    payload = {"sentence": "This is a test sentence"}
    response = client.post("/get_model_response/", json=payload)
    assert response.status_code == 200
    assert "response" in response.json()
