#!/usr/bin/env python3.4
import brlapi
import time
def brl_rt():
    """this fonction put the time on the braille display"""
    b = brlapi.Connection()
    b.enterTtyMode()
    while 1:
        tmp = time.localtime()
        y = str(tmp.tm_hour)+':'+str(tmp.tm_min)
        b.writeText(y)
        if b.readKey(False) == 97:
            break
    return 0

brl_rt()