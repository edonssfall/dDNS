import json

from dotenv import load_dotenv
import requests
import os

load_dotenv()

domain_name = os.environ["DOMAIN_NAME"]
record_type = os.environ["RECORD_TYPE"]
record_name = os.environ["RECORD_NAME"]

url = (
    "https://api.godaddy.com/v1/domains/{}/records/{}/{}"
    .format(os.environ["DOMAIN_NAME"], os.environ["RECORD_TYPE"], os.environ["RECORD_NAME"])
)

headers = {
    "Authorization": "sso-key {}:{}"
    .format(os.environ['APIKey'], os.environ['APISecret']),
}


def get_ip():
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("GET Succeed")
        return response.json()[0]['data']

    else:
        print("GET Fail.")
        print(response.status_code, response.text)


def set_ip(current_ip: str):
    # data = [{"data": current_ip}]
    data = [{"data": "192.168.1.124"}]

    headers["Content-Type"] = "application/json"

    response = requests.put(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("PUT Succeed")
        print(response.json())

    else:
        print("PUT Fail.")
        print(response.status_code, response.text)
