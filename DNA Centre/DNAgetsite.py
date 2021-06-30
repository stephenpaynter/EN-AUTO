import requests
import json

base_url = 'https://sandboxdnac.cisco.com/dna/'
auth_endpoint = 'system/api/v1/auth/token'

user = 'devnetuser'
password = 'Cisco123!'

auth_response = requests.post(url=f"{base_url}{auth_endpoint}", auth=(user,password)).json()

token = auth_response['Token']

headers = {
    "x-auth-token":token,
    "Accept":"application/json",
    "Content-Type":"application/json"
}

payload = None

site_endpoint = "https://sandboxdnac.cisco.com/dna/intent/api/v1/site"

site_response = requests.request('GET', site_endpoint, headers=headers, data=payload)

print(site_response.text)