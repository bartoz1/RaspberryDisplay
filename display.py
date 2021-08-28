#!/usr/bin/python
import socket
import urllib.error
import urllib.request


def internet_on():
    try:
        urllib.request.urlopen('http://www.google.com', timeout=1)
        return True
    except urllib.error.URLError as err:
        return False


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    return ip


def handle_internet_info():
    if internet_on():
        ip = get_local_ip()
        print('jest internet', ip)
    pass


def main():
    handle_internet_info()


if __name__ == '__main__':
    main()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_adress = s.getsockname()[0]

print(ip_adress)