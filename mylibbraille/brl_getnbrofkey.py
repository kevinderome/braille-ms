#!/usr/bin/env python3.4
import brlapi

b = brlapi.Connection()

b.enterTtyMode()
key = 0
while key != 65293:
    key = b.readKey()
    b.writeText(str(key))
print(key)
