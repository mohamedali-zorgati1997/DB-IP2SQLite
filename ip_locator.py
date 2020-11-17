#!/usr/bin/env python3

import sqlite3
from utils import *

def find_asn_by_ip(ip, database):
    if ":" in ip:
        print("IPv6 is not supported yet.")
        return
    else :
        ip = ip4_2_int(ip)
        cursor = database.cursor()
        cursor.execute("SELECT name FROM ASN_4 WHERE ? >= start_ip AND ? <= end_ip", (ip, ip))
        fetch = cursor.fetchall()
        print(fetch)

def find_asn_by_ip(ip, database):
    if ":" in ip:
        print("IPv6 is not supported yet.")
        return
    else :
        ip = ip4_2_int(ip)
        cursor = database.cursor()
        cursor.execute("SELECT name FROM ASN_4 WHERE ? >= start_ip AND ? <= end_ip", (ip, ip))
        fetch = cursor.fetchall()
        print(fetch)


def find_city_by_ip(ip, database):
    if ":" in ip:
        print("IPv6 is not supported yet.")
        return
    else :
        ip = ip4_2_int(ip)
        cursor = database.cursor()
        cursor.execute("SELECT * FROM CITY_4 WHERE ? >= start_ip AND ? <= end_ip", (ip, ip))
        fetch = cursor.fetchall()
        print(fetch)


if __name__ == "__main__":
    try:
        sqlite = sqlite3.connect("ip_locator.db")
    except: # TODO: show error msg in case of error (suggest to generate new database)
        pass
    while True:
        ip = input("type ip you want to find information about: ")
        #do input control to avoid errors
        find_asn_by_ip(ip, sqlite)
        find_city_by_ip(ip, sqlite)
