#!/usr/bin/env python3.4

import time
import brlapi

b = brlapi.Connection()
b.enterTtyMode()
text = "bonjour les amies ceci un test en python :) je vous aime tous xxxxxxxxxxxxxxxxxttttttttttttttttttttttoooooooooooooooooooooooooooooooooooooooooooooooooozzzzzzzzzzzzzzzzz fin"
pos = 0
size = getattr(b, "displaySize")
while 42:
    if (len(text) - pos) < size[0]:
        break
    else:
        b.writeText(text[pos:pos+size[0]])
        time.sleep(0.01)
    pos = pos + size[0]
b.writeText(text[pos:])
time.sleep(8)
