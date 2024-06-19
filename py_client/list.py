import requests
from getpass import getpass

endpoint = "http://127.0.0.1:8005/api/auth/"
username = input("Enter your username:\n")
password = getpass("Enter your password:\n")
auth_response = requests.post(
    endpoint, json={"username": username, "password": password}
)
print(auth_response.json())
if auth_response.status_code == 200:
    token = auth_response.json().get("token")
    if token:
        headers = {"Authorization": f"Bearer {token}"}
        endpoint = "http://127.0.0.1:8005/api/products/"
        get_response = requests.get(endpoint, headers=headers)
        print(get_response.json())
    else:
        print("Token not found in the response")
else:
    print(f"Authentication failed: {auth_response.status_code}")
