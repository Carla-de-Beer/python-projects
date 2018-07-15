# Carla de Beer
# Created: July 2018
# Converts .properties file to a CSV file format.
# To ensure that special charaters are correctly displayed inside Excel, with the correct UTF-8 encoding, do the following:
# Open Excel, import the file using UTF-encoding and set commas as delimiters.
# Note that multiline text is not yet supported.

import csv

writeFile = open("i18n_en.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(writeFile)

with open("sourceFiles/i18n_en.properties", "r", ) as propertiesFile:
    for line in propertiesFile.readlines():
        line = line.strip()  # removes the newline characters
        parts = line.split("=")  # creates a (key, value) tuple

        # Create a multidimensional list for csv insertion
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
