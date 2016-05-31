#!/usr/bin/python3
import configparser
import os
from mylib.braille import *


def load_conf():
    keyboard = {}
    config = configparser.RawConfigParser()
    config.read('/home/derome_k/.braille-ms/keyboard.conf')
    keyboard ={
        'key_left':int(config.get('keyboard', 'key_left')),
        'key_right': int(config.get('keyboard', 'key_right')),
        'key_up': int(config.get('keyboard', 'key_up')),
        'key_down': int(config.get('keyboard', 'key_down')),
        'key_ok': int(config.get('keyboard', 'key_ok')),
        'first_cursor': int(config.get('braille_display', 'first_cursor')),
        'last_cursor': int(config.get('braille_display', 'last_cursor'))
    }
    return keyboard


def new_conf():
    printb("press any key for begining     configuration", 0)
    config = configparser.RawConfigParser()
    config.add_section('keyboard')
    config.set('keyboard', 'key_left', get_funckey("Press key left ..."))
    config.set('keyboard', 'key_right', get_funckey("Press key right ..."))
    config.set('keyboard', 'key_up', get_funckey("Press key up ..."))
    config.set('keyboard', 'key_down', get_funckey("Press key down ..."))
    config.set('keyboard', 'key_ok', get_funckey("Press key OK ..."))
    config.add_section('braille_display')
    config.set('braille_display', 'first_cursor', get_funckey("Press a first cursor ..."))
    config.set('braille_display', 'last_cursor', get_funckey("Now, Press last cursor ..."))
    try:
        with open('/home/derome_k/.braille-ms/keyboard.conf', 'w') as conf_file:
            config.write(conf_file)
            flashb("You have finish")
    finally:
        return 0

def     init_bms():
    ch = os.path.expanduser("~")
    if os.path.exists(ch + "/.braille-ms/") != True:
        os.mkdir(ch + "/.braille-ms")
    if os.path.exists(ch + "/.braille-ms/keyboard.conf") != True:
        new_conf()
    return load_conf()
            
