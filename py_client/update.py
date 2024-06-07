import requests

endpoint = "http://127.0.0.1:8000/api/products/1/update/" # http://localhost:8000/

data = {
    "title": "I am Updated",
    "price": 120.22
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
