import requests

def test_hello_world():
    url = "http://<YOUR_FUNCTION_URL>"
    response = requests.get(url, params={"name": "World"})
    assert response.status_code == 200
    assert response.text == "Hello, World!"
