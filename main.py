from apiGoDaddy import get_ip, set_ip
import socket
import time


def get_current_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address


if __name__ == "__main__":
    while True:
        previous_ip = get_ip()
        current_ip = get_current_ip()

        if current_ip != previous_ip:
            set_ip(current_ip)

        time.sleep(60)
