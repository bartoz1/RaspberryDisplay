#!/usr/bin/python
import socket
import sys
import urllib2

def internet_on():
    pass


def handle_internet_info():
    pass


def main():
    handle_internet_info()


if __name__ == '__main__':
  main()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_adress = s.getsockname()[0]

print(ip_adress)