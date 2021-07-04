import requests
import json

url = "https://sandbox-sdwan-1.cisco.com/"
auth_endpoint = "j_security_check"

login = {
    "j_username":"devnetuser",
    "j_password":"RG!_Yw919_83"
}

_session = requests.session()
_response = _session.post(url=f"{url}{auth_endpoint}", data=login, verify=False)

print(_response)    

if not _response.ok or _response.text:
    print('login failed')
    import sys
    sys.exit(1)
else:
    print('login succeeded')