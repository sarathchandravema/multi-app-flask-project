import requests

BASE_URL = "http://127.0.0.1:5000/"

def test_hw_success():
    response = requests.get(BASE_URL + "hw")
    assert response.json() == {"hello": "world"}

def test_hw_fail():
    response = requests.post(BASE_URL + "hw")
    assert response.json() == {'message': 'The method is not allowed for the requested URL.'}