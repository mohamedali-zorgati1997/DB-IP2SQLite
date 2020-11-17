#!/usr/bin/env python3

from utils import *
from os import walk
from os.path import splitext, getsize
import sqlite3



#get file list to detect available CSV files
def get_csv_file_list(directory="."):
    csv_files = []
    for file in next(walk(directory))[2]:
        if splitext(file)[1].lower() == ".csv":
            csv_files.append(file)
    return csv_files

def compile_city(database, csv_file):
    cursor = database.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS CITY_4 (start_ip INTEGER, end_ip INTEGER, \
    continent TEXT, country TEXT, region TEXT, city TEXT, longitude REAL, latitude REAL,\
    PRIMARY KEY(start_ip, end_ip))")
    fd = open(csv_file)
    print("Inserting data in CITY_4 table from csv: {}".format(csv_file))
    line = fd.readline()
    current_progress = len(line)
    filesize = getsize(csv_file)
    step = filesize // 20
    number_step = 0
    next_step = step
    print("-"*20, end="")
    while line:
        current_progress += len(line)
        if current_progress > next_step :
            number_step += 1
            next_step += step
            print("\r" + "|"*number_step + "-"*(20-number_step), end="")
            from time import sleep
            sleep(30)
        data = line.strip().split(",")
        if":" in data[0]: #ipv6 require different processing
            pass
        else:
            cursor.execute("INSERT INTO CITY_4 VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (ip4_2_int(data[0]), ip4_2_int(data[1]),
                            data[2].strip("'\""), data[3].strip("'\""), data[4].strip("'\""),
                            data[5].strip("'\""), float(data[6]), float(data[7])))
        line = fd.readline()

    database.commit()
    cursor.close()

def compile_asn(database, csv_file):
    cursor = database.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS ASN_4 (start_ip INTEGER, end_ip INTEGER, \
        number INTEGER, name TEXT, Primary KEY (start_ip, end_ip))")
    fd = open(csv_file)
    print("Inserting data in ASN_4 table from csv: {}".format(csv_file))
    line = fd.readline()
    current_progress = len(line)
    filesize = getsize(csv_file)
    step = filesize // 20
    number_step = 0
    next_step = step
    print("-" * 20, end="")
    while line:
        current_progress += len(line)
        if current_progress > next_step:
            number_step += 1
            next_step += step
            print("\r" + "|" * number_step + "-" * (20 - number_step), end="")
        data = line.strip().split(",")
        if ":" in data[0]:  # ipv6 require different processing
            pass
        else:
            cursor.execute("INSERT INTO ASN_4 VALUES (?, ?, ?, ?)",
                           (ip4_2_int(data[0]), ip4_2_int(data[1]),
                            int(data[2]), data[3].strip("'\"")))
        line = fd.readline()
    print("\r" + "|" * 20, end="")
    database.commit()
    cursor.close()




if __name__ == "__main__":
    csvFiles = get_csv_file_list()
    sqlite = sqlite3.connect("ip_locator.db")

    for file in csvFiles:
        if "dbip" in file:
            if "city" in file:
                compile_city(sqlite, file)
            elif "country" in file:
                compile_country()
            elif "asn" in file:
                compile_asn(sqlite, file)


