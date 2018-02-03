# Simple program to count letter frequencies in a text file
# Carla de Beer
# Created: February 2018

#!/usr/bin/python

import sys
import getopt

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
count_array = []
count_word = 0
count_letter = 0

# Set filename from incoming parameters
try:
    opts, args = getopt.getopt(sys.argv,'hi',['ifile='])
    fileName = sys.argv[1]

except getopt.GetoptError as err:
    print(str(err))
    sys.exit(2)

# ----------------------------------------------------------------------------------------------------
# Helper methods
# ----------------------------------------------------------------------------------------------------

def print_results():
    print("Letter frequencies for '{0}':".format(fileName))

    c = ''
    for index in range(len(count_array)):
        for key in count_array[index]:

            if key == 'letter':
                c = key
            if key == 'count':
                percentage = round(count_array[index][key]/sum * 100, 3)
                print('{0}: {1} occurrences => {2}%'.format(count_array[index][c], count_array[index][key], percentage))

def init_array():
    for c in ALPHABET:
        count_array.append({'letter': c, 'count': 0})

# ----------------------------------------------------------------------------------------------------
# Read file and parse text
# ----------------------------------------------------------------------------------------------------

init_array()

try:

    file = open(fileName, 'r')

    list = []
    for line in file:
        line = line.lower()
        # Count the number of occurrences of each alphabet letter, for each incoming line
        c = ''
        for index in range(len(count_array)):
            for key in count_array[index]:
                if key == 'letter':
                    c = key
                if key == 'count':
                    count_array[index][key] += line.count(count_array[index][c])
    sum = 0
    for index in range(len(count_array)):
        for key in count_array[index]:
            if key == 'count':
                sum += count_array[index][key]

    # Sort the array by count value, descending
    count_array = sorted(count_array, key=lambda k: k['count'], reverse=True)

    print_results()

    file.close()

except IOError as e:
    print('I/O error({0}): {1}'.format(e.errno, e.strerror))
