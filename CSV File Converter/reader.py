"""
Carla de Beer
Created: July 2018
Converts a CVS file to a .properties file format.
UTF-8 character encoding is preserved.
"""

import csv

WRITE_FILE = open("i18n_en.properties", "w", newline="", encoding="utf-8")

try:
    with open("sourceFiles/i18n_en.csv") as csvfile:
        READ_CSV = csv.reader(csvfile, delimiter=",")
        for row in READ_CSV:
            print(row[0] + "=" + row[1])

            WRITE_FILE.write(row[0])
            WRITE_FILE.write("=")
            WRITE_FILE.write(row[1])
            WRITE_FILE.write("\n")

    WRITE_FILE.close()

except IOError:
    print("Error: can\'t find file or read data")
