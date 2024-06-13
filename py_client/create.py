import requests

endpoint = "http://127.0.0.1:8005/api/products/"

get_response = requests.post(endpoint, json={"owner":2,"title":"Shorts","price":200})

print(get_response.json())
