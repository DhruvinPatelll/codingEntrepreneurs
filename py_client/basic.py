import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/"

get_response = requests.get(endpoint)
print(get_response.text)


# HTTP REQUEST -> HTML
# REST API HTTP REQUEST -> JSON

print(get_response.json)