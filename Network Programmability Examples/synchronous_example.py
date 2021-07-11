import requests
import json

base_url = 'http://httpbin.org/'

def get_delay(seconds):
    endpoint = f"/delay/{seconds}"

    print(f"Getting with {seconds} delay...")

    response = requests.get(base_url + endpoint)
    data = response.json()
    print(json.dumps(data, indent=4))

get_delay(3)

print("Okay! Finished GETting.")