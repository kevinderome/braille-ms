#!/usr/bin/env python3.4
import brlapi
import os
def brl_input():
    b = brlapi.Connection()
    b.enterTtyMode()
    r = 0
    key = ""
    i = 1
    tmp = 0
    while tmp != 65293:
        b.writeText(key, i)
        tmp = b.readKey()
        if len(key) > 39:
            ts = key[40:]
            b.writeText(ts, i)
        if tmp <= 255:
            key += chr(tmp) + chr(brlapi.Dot7)
            i += 1
        elif tmp == 65288:
            key = key[:-1]
            i -= 1
            if len(key) == 0:
                b.writeText(" ", i)
                key = ""
                if i == 0:
                    i = 1
                elif i == 41:
                    exit()
    return key

a = brl_input()
print(a)
