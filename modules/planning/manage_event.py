#!/usr/bin/env python3.4
import brlapi
import time
import os
import re
import sqlite3
import datetime
import re
def     msgb(txt):
    try:
        b = brlapi.Connection()
        b.enterTtyMode()
        b.writeText(txt)
        b.readKey()
    finally:
        return 0

def     flashb(txt):
    try:
        b = brlapi.Connection()
        b.enterTtyMode()
        b.writeText(str(txt))
        time.sleep(2)
        del(b)
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

def     add_event():
    bdd = sqlite3.connect('agenda.db')
    time = ""
    cursor = bdd.cursor()
    verif = 0
    while verif != 2:
        if verif == 0:
            date = inputb("AAAA-MM-JJ : ")
            if date == -1:
                return 0
            if re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", date):
                verif = verif + 1
        if verif == 1:
            time = inputb("HH:MM : ")
            if time == -1:
                return 0
            if re.match("^[0-9]{2}\:[0-9]{2}$", time):
                verif = verif + 1
    note = inputb("note:")
    if note == -1:
        return 0
    # insert to db : agenda -> planing
    cursor.execute("""
    INSERT INTO planning(id, note) VALUES( ?, ?)""", [date+' '+time+':00',note])
    flashb("ajout réussie :)")
    bdd.commit()
    bdd.close()
    return 0
def     count_event(date):
    date = date.split(" ")
    date = date[0]
    bdd = sqlite3.connect('agenda.db')
    cursor = bdd.cursor()
    count = cursor.execute("SELECT COUNT(id) FROM planning WHERE id >= ? AND id <= ?", (date+" 00:00:00", date+" 23:59:59"))
    count = count.fetchall()
    bdd.close()
    return int(count[0][0])

def     consult_event():
    print(count_event("2016-05-07 12:30:00"))
    b = brlapi.Connection()
    b.enterTtyMode()
    bdd = sqlite3.connect('agenda.db')
    cursor = bdd.cursor()
    infos = cursor.execute("SELECT * FROM planning")
    infos = infos.fetchall()
    if len(infos) > 0:
        b.writeText(infos[0][0])
        b.readKey()
    else:
        flashb("Aucun évênement.")
    bdd.close()
    return 0

def     reset_event():
    b = brlapi.Connection()
    b.enterTtyMode()
    choix = 0
    while choix != 'o' and choix != 'n':
        b.writeText("2tes-vous sure ? (O/N ?)")
        choix = b.readKey()
        if choix < 128:
            choix = chr(choix)
    if choix == 'o':
        bdd = sqlite3.connect('agenda.db')
        cursor = bdd.cursor()
        cursor.execute("DELETE FROM planning")
        bdd.commit()
        bdd.close()
        flashb("Réinitialisation réussie :)")
    return 0

def     init_event():
    bdd = sqlite3.connect("agenda.db")
    cursor = bdd.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS planning(
    id DATETIME PRIMARY KEY UNIQUE,
    note TEXT)""")
    bdd.commit()
    bdd.close()
    return 0

