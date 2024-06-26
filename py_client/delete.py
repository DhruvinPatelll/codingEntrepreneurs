import requests

product_id = input("What is your product ID?\n")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} is Invalid")

if product_id:
    endpoint = f"http://127.0.0.1:8005/api/products/{product_id}/delete"

    get_response = requests.delete(endpoint)
    print(get_response.json())
