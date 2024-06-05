import requests

endpoint = "http://127.0.0.1:8005/api_home"
# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/"

get_response = requests.get(endpoint, json={"id": 123})
print(get_response.text)
# print(get_response.headers)


# HTTP REQUEST -> HTML
# REST API HTTP REQUEST -> JSON

# print(get_response.json())
# print(get_response.status_code)
