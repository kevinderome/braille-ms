#!/usr/bin/env python3.4

import time
import brlapi

def brl_print(txt, pos):
    b = brlapi.Connection()
    b.enterTtyMode()
    size = getattr(b, "displaySize")
    
    if (len(txt) - pos) < size[0]:
        b.writeText(txt[pos:])
    else:
        b.writeText(txt[pos:pos+size[0]])
    return 0
