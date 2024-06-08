import requests

endpoint = "http://127.0.0.1:8000/api/products/" # http://localhost:8000/
# http://localhost:8000/admin/
# session -> post data

data = {
    "title": "this is the title",
    "price": "50"
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())
