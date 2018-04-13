#!/usr/local/bin/python3

import vim
from requests import get


def get_root():
    url = "http://localhost:8080"
    request = get(url)
    return request.text


def take_marker():
    """
    Taker
    """
    buff = vim.current.buffer
    buff[0] = get_root()


def get_country():
    try:
        resp = get("http://api.ip2country.info/ip?101.228.124.30")
        my_location = resp.json()
        return my_location['countryName']
    except Exception as e:
        print('Error in hello.get_country() %s' % e.msg)


def print_country():
    print('I am in %s.' % get_country())
