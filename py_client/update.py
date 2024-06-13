import requests

endpoint = "http://127.0.0.1:8005/api/products/1/update"

data = {
    "title": "Shorts",
    "price": 300,
}

get_response = requests.put(endpoint, json=data)

print(get_response.json())
