#!/usr/bin/python3
import brlapi
import time
from .load_conf import *

keyboard = init_bms()

def     printb(txt, pos):
    try:
        b = brlapi.Connection()
        b.enterTtyMode()
        size = getattr(b, "displaySize")    
        if len(txt) < size[0]:
            b.writeText(txt[0:])
        elif (len(txt) - pos) < size[0]:
            b.writeText(txt[pos:])
        else:
            b.writeText(txt[(pos * size[0]):(pos+1 * size[0])])
    finally:
        return 0

def     get_key():
    key = -1
    try:
        b = brlapi.Connection()
        b.enterTtyMode()
        key = b.readKey()
    finally:
        if key < 256 and key > 0:
            key = chr(key)
        return key

def     flashb(txt):
    try:
        b = brlapi.Connection()
        b.enterTtyMode()
        b.writeText(str(txt))
        time.sleep(2)
        del(b)
    finally:
        return 0

def     msgb(txt):
    try:
        b = brlapi.Connection()
        b.enterTtyMode()
        b.writeText(txt)
        b.readKey()
    finally:
        return 0

def     inputb(txt):
    b = brlapi.Connection()
    b.enterTtyMode()
    r = 0
    key = ""
    i = len(txt)+1 
    tmp = 0
    while tmp != 65293:
        b.writeText(txt+key, i)
        tmp = b.readKey()
        if len(key) > 39:
            ts = key[41:]
            b.writeText(ts, i)
        if tmp <= 255:
            key += chr(tmp)
            i += 1
        elif tmp == 65288 and (len(key)) < i:
            key = key[:-1]
            i -= 1
            if len(key) == 0:
                b.writeText(txt+" ", i)
                key = ""
                if i == len(txt):
                    i = len(txt)+1
                elif i == 41:
                    return key
        elif tmp == 536936448:
            return -1
    return key
