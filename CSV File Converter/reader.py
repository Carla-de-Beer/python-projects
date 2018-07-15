# Carla de Beer
# Created: July 2018
# Converts a CVS file to a .properties file format.
# UTF-8 character encoding is preserved.

import csv

writeFile = open("i18n_en.properties", "w", newline="", encoding="utf-8")

with open("sourceFiles/i18n_en.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    for row in readCSV:
        print(row[0] + "=" + row[1])

        writeFile.write(row[0])
        writeFile.write("=")
        writeFile.write(row[1])
        writeFile.write("\n")

writeFile.close()