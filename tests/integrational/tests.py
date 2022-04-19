import requests
from src.config import settings


def test_flask_server_quick_sort():
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'seq': [1, 2, 7, 4, 2, 7, 0, 1, 4, ]
    }
    response = requests.post(f"http://{settings.HOST}:{settings.PORT}/sort/quick", json=data, headers=headers)
    assert response.status_code == 200


def test_flask_server_shaker_sort():
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'seq': [1, 2,7, 4, 2, 7, 0, 1, 4, ]
    }
    response = requests.post(f"http://{settings.HOST}:{settings.PORT}/sort/shaker", json=data, headers=headers)
    assert response.status_code == 200


def test_flask_server_insertion_sort():
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'seq': [1, 2, 7, 4, 2, 7, 0, 1, 4, ]
    }
    response = requests.post(f"http://{settings.HOST}:{settings.PORT}/sort/insertion", json=data, headers=headers)
    assert response.status_code == 200


def test_flask_server_selection_sort():
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'seq': [1, 2, 7, 4, 2, 7, 0, 1, 4, ]
    }
    response = requests.post(f"http://{settings.HOST}:{settings.PORT}/sort/selection", json=data, headers=headers)
    assert response.status_code == 200


def test_flask_server_incorrect_seq_sort():
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'seq': [1, 2, 7, 4, 2, 'value', 0, 1, 4, ]
    }
    response = requests.post(f"http://{settings.HOST}:{settings.PORT}/sort/shaker", json=data, headers=headers)
    assert response.status_code == 200


def test_flask_server_incorrect_endpoint():
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'seq': [1, 2, 7, 4, 2, 7, 0, 1, 4, ]
    }
    response = requests.post(f"http://{settings.HOST}:{settings.PORT}/sort/another", json=data, headers=headers)
    assert response.status_code == 200


def test_flask_server_empty_endpoint():
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'seq': [1, 2, 7, 4, 2, 7, 0, 1, 4, ]
    }
    response = requests.post(f"http://{settings.HOST}:{settings.PORT}/sort/", json=data, headers=headers)
    assert response.status_code == 404

