#!/usr/local/bin/python3

import vim


def take_marker():
    """
    Taker 
    """
    print("Hello World!")
    buff = vim.current.buffer
    for idx, line in enumerate(buff):
        buff[idx] = line + "\t" + "mark"
