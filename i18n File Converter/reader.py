# Carla de Beer
# Created: July 2018
# Converts .properties file to a csv format.
# To ensure that special charaters are correctly displayed inside Excel, with the correct UTF-8 encoding, do the following:
# Open Excel, import the file using UTF-encoding and set commas as delimiters.

import csv

writeFile = open("i18n_en.csv", "w", newline='', encoding='utf-8')
writer = csv.writer(writeFile)

with open("sourceFiles/i18n_en.properties", "r", ) as file:
    for line in file.readlines():
        line = line.strip()  # removes the newline characters
        parts = line.split("=")  # creates a (key, value) tuple

        # Create the multidimensional array for csv inclusion
        myData = []

        # Skip commented lines
        if line and line[0] != "#":
            # print(line)

            outgoingList = []
            outgoingList.append("<App name>")
            outgoingList.append("en")
            outgoingList.append(parts[0]) # key
            outgoingList.append(parts[1]) # value
            myData.append(outgoingList)

            print(outgoingList)

            writer = csv.writer(writeFile)
            writer.writerows(myData)
