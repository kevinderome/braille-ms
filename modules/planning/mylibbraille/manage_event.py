#!/usr/bin/env python3.4
import brlapi
import time
import os
import re
import sqlite3
import datetime
from .braille import *

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
    INSERT INTO planning(date_e, time_e, note) VALUES( ?, ?, ?)""", [date, time+':00', note])
    flashb("ajout réussie :)")
    bdd.commit()
    bdd.close()
    return 0

def     consult_event():
    i = 0
    bdd = sqlite3.connect('agenda.db')
    cursor = bdd.cursor()
    planning = cursor.execute("""select date_e,count(time_e) from planning group by date_e""")
    planning = planning.fetchall()
    print(planning)
    bdd.close()
    max = len(planning)
    print(max)
    if max > 0:
        while 42:
            printb(str(planning[i][0])+" --------------> "+str(planning[i][1])+" event(s)", 0)
            key = get_key()
            if key == 97 and i != 0:
                i = i - 1
            elif key == 98 and i < max:
                i = i + 1
            elif key == 99:
                return planning[i][0]
    else:
        flashb("Aucun évênement.")
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
    date_e DATE NOT NULL,
    time_e TIME NOT NULL,
    note TEXT NOT NULL, PRIMARY KEY(date_e, time_e))""")
    bdd.commit()
    bdd.close()
    return 0

