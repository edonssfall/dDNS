from apiGoDaddy import ApiGoDaddy
from logger import Logger
import logging
import socket
import time
import os


def get_current_ip(logger: Logger):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip_address = str()
    try:
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        logger.log(logging.INFO, f"IP address: {ip_address}")
        s.close()
    except Exception as e:
        logger.log(logging.ERROR, str(e))
    return ip_address


if __name__ == "__main__":
    domain_name = os.environ["DOMAIN_NAME_0"]
    record_type = os.environ["RECORD_TYPE_0"]
    record_name = os.environ["RECORD_NAME_0"]

    api_key = os.environ['APIKey']
    api_secret = os.environ['APISecret']

    apiGoDaddy = ApiGoDaddy(api_key, api_secret)
    logger = Logger("ip")

    while True:
        current_ip = get_current_ip(logger)
        if not current_ip:
            while True:
                current_ip = get_current_ip(logger)
                time.sleep(1)
        host_ip = apiGoDaddy.get_host_ip(domain_name, record_type, record_name)

        if current_ip != host_ip:
            apiGoDaddy.set_host_ip(current_ip, domain_name, record_type, record_name)

        time.sleep(60)
