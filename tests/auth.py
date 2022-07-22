import requests
import json.decoder


env = 'http://localhost:83'
auth_data = {
        "UserName": "Supervisor",
        "UserPassword": "Supervisor"
    }
url2 = "http://localhost:83/0/rest/SapErpIntegrationService/v1/UpdateFinPosition"

url = env + '/ServiceModel/AuthService.svc/Login'

header1 = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.29.0",
        'Accept': "*/*",
        'Cache-Control': "Cache-Control",
        'Host': "localhost:83",
        'Accept-Encoding': "gzip, deflate, br",
        'Connection': "keep-alive",
        'Content-Length': "69"
    }
response = requests.post(url,  json=auth_data, headers=header1)
jar = response.cookies
bpmcsrf = response.cookies["BPMCSRF"]
header = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.29.0",
        'Accept': "*/*",
        'Cache-Control': "Cache-Control",
        'Host': "localhost:83",
        'Accept-Encoding': "gzip, deflate, br",
        'Connection': "keep-alive",
        'Content-Length': "69",
        'BPMCSRF': bpmcsrf
    }

json_data = {
    "currentPage": "1",
    "pageCount": "1",
    "delta": "F",
    "item": [
        {
            "row": "4",
            "FIPEX": "main test code 1",
            "BEZEI": "IteFPName 1",
            "TEXT1": "IteFPDescription 1",
            "DATAB": "01.01.20",
            "DATBIS": "31.12.21",
            "deleted": ""
        }
    ]
}

response = requests.post(url,   json=json_data, headers=header, cookies=jar)
obj = json.loads(response.text)
print(obj)
