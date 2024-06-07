import requests

endpoint = "http://127.0.0.1:8005/api/products/create"

get_response = requests.post(endpoint, json={"title":"Socks","price":100})

print(get_response.status_code==204)
