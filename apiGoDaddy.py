from dotenv import load_dotenv
from logger import Logger
import requests
import datetime
import logging
import json

load_dotenv()


class ApiGoDaddy:
    domains_url = "https://api.godaddy.com/v1/domains/{}/records/{}/{}"

    def __init__(self, api_key: str, api_secret: str, logger=Logger("ApiGoDaddy")):
        self.logger = logger
        self.headers = {
            "Authorization": "sso-key {}:{}"
            .format(api_key, api_secret),
        }

    def get_host_ip(self, domain_name: str, record_type: str, record_name: str) -> dict | None:
        response = requests.get(
            url=self.domains_url.format(domain_name, record_type, record_name),
            headers=self.headers
        )

        if response.status_code == 200:
            response_json = response.json()[0]

            print(f"[{datetime.datetime.now().isoformat()}] - GET Host IP Succeed.")
            self.logger.log(logging.INFO, f"GET Host Ip - {response_json}")
            return response_json["data"]

        else:
            print(f"[{datetime.datetime.now().isoformat()}] - GET Host IP FAIL!!!")
            print("\t", response.status_code, response.text)
            self.logger.log(logging.ERROR, f"GET Host Ip - {response.status_code}, {response.text}")

    def set_host_ip(self, new_ip: str, domain_name: str, record_type: str, record_name: str):
        new_ip = "192.168.1.124"

        headers = self.headers.copy()
        headers["Content-Type"] = "application/json"

        response = requests.put(
            url=self.domains_url.format(domain_name, record_type, record_name),
            headers=headers,
            data=json.dumps([{
                "data": new_ip
            }])
        )

        if response.status_code == 200:
            print("PUT Succeed")

        else:
            print("PUT Fail.")
            print(response.status_code, response.text)
