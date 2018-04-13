#!/usr/local/bin/python3

import vim
import requests


def get_root():
    url = "http://localhost:8080"
    request = requests.get(url)
    return request.text


def take_marker():
    """
    Taker
    """
    buff = vim.current.buffer
    buff[0] = get_root()
