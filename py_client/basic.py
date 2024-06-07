import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/" # http://localhost:8000/

get_response = requests.post(endpoint, json={"title": "hey", "content": "hello user", "price": "abc"}) # HTTP request
# print(get_response.text) # print raw text response
# print(get_response.status_code)
print(get_response.json())
# print(get_response.status_code)