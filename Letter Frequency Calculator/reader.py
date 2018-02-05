# Python program that reads in a set of text files and calculates the frequency occurrences of each alphabet letter,
# where the alphabet letters are listed in descending order of frequency.
# The results are plotted on a plot.ly graph.
# Carla de Beer
# Created: February 2018

#!/usr/bin/python

import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import os

plotly.tools.set_credentials_file(username='ENTER_USERNAME_HERE', api_key='ENTER_TOKEN_HERE')

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
count_array = []
plot_data = []


# ----------------------------------------------------------------------------------------------------
# Helper methods
# ----------------------------------------------------------------------------------------------------

def init_arrays():
    for c in ALPHABET:
        count_array.append({'letter': c, 'count': 0})

    # Get the filenames from the 'Texts' folder
    file_names = os.listdir('Texts')
    file_names = [x for x in file_names if ".txt" in x]

    text_position = []
    for i in range(len(file_names)):
        if i % 4 == 0:
            text_position.append('top')
        elif i % 3 == 0:
            text_position.append('bottom')
        elif i % 2 == 0:
            text_position.append('left')
        else:
            text_position.append('right')

    return file_names, text_position

def calculate(file, array):
    for line in file:
        line = line.lower()

        # Count the number of occurrences of each alphabet letter, for each incoming line
        c = ''
        for index in range(len(array)):
            for key in array[index]:
                if key == 'letter':
                    c = key
                if key == 'count':
                    array[index][key] += line.count(array[index][c])

    sum = 0
    for index in range(len(array)):
        for key in array[index]:
            if key == 'count':
                sum += array[index][key]

    # Sort the array by count value, descending
    return sorted(array, key=lambda k: k['count'], reverse=True), sum

def print_results(fileName, array, sum):
    print("Letter frequencies for '{0}':".format(fileName))

    c = ''
    for index in range(len(array)):
        for key in array[index]:
            if key == 'letter':
                c = key
            if key == 'count':
                percentage = round(array[index][key]/sum * 100, 3)
                print('{0}: {1} occurrences => {2}%'.format(array[index][c], array[index][key], percentage))
    print('\n')


def get_plot_results(array, file_names, text_position, sum):
    c_array = []
    y_array = []
    for index in range(len(array)):
        for key in count_array[index]:
            if key == 'letter':
                c_array.append(array[index][key])
            if key == 'count':
                percentage = round(array[index][key] / sum * 100, 3)
                y_array.append(percentage)

    x_array = []
    for i in range(1, 27):
        x_array.append(i)

        data = go.Scatter(
            x=x_array,
            y=y_array,
            mode='lines+markers+text',
            text=c_array,
            name=f,
            textposition=text_position[file_names.index(f)],
            marker=dict(
                opacity=0.4,
                size=y_array,
                sizemode='area',
                sizeref=2. * max(y_array) / (40. ** 2),
                sizemin=4
            )
        )


    plot_data.append(data)
    return plot_data

def plot_results(plot_data):
    layout = go.Layout(title='Letter frequencies (%)', showlegend=True)
    fig = go.Figure(data=plot_data, layout=layout)
    plot_url = py.plot(fig, filename='Letter frequencies')


# ----------------------------------------------------------------------------------------------------
# Read file and parse text
# ----------------------------------------------------------------------------------------------------

file_names, text_position = init_arrays()

try:

    for f in file_names:

        path = 'Texts/' + f
        file = open(path, 'r')

        count_array, sum = calculate(file, count_array)

        print_results(f, count_array, sum)

        plot = get_plot_results(count_array, file_names, text_position, sum)

        file.close()

    plot_results(plot_data)

except IOError as e:
    print('I/O error({0}): {1}'.format(e.errno, e.strerror))
