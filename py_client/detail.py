import requests

endpoint = "http://127.0.0.1:8005/api/products/1/"

get_response = requests.get(endpoint)

print(get_response.json())
