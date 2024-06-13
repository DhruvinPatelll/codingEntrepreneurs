import requests

headers = {'Authorization': 'Bearer affa5ee19e0e587fb58e599f1563d314e3420ba2'}
endpoint = "http://127.0.0.1:8005/api/products/"

get_response = requests.post(
    endpoint, json={"owner": 2, "title": "Shorts", "price": 200}, headers=headers
)

print(get_response.json())
