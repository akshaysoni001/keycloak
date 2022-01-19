import requests
from requests.auth import HTTPBasicAuth
import json

def get_token():
    url = "http://127.0.0.1:8080/auth/realms/opcito/protocol/openid-connect/token"
    
    payload = 'grant_type=client_credentials'
    headers ={
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    response = requests.request("POST",url,headers=headers, data=payload,auth=HTTPBasicAuth("backend-client","m5qe1pSUyIa0VhZOW4dnDUlHccg1cSyM")
                        )
    token = json.loads(response.text)
    # print(token)
    return token["access_token"]


def get_user(token):
    url = "http://127.0.0.1:8080/auth/admin/realms/opcito/users"
    payload={}
    headers={
        'Authorization': 'Bearer '+token
    }
    print(headers)
    response = requests.request("GET",url,headers=headers,data=payload)
    users = json.loads(response.text)
    return users

print(get_user(get_token()))
    