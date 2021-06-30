import requests

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

payload = None

user = 'devnetuser'
password = 'Cisco123!'

headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE=",
    "Accept": "application/json"
}

response = requests.request('POST', url, headers=headers, data = payload)

print(response.text)




