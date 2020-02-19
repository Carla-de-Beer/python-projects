"""
Carla de Beer
Created: February 2018
Python program that reads in a set of text files and
calculates the frequency occurrences of each alphabet letter,
where the alphabet letters are listed in descending order of frequency.
The results are plotted on a plot.ly graph.
"""

import os
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

# NB: Add relevant credentials here in order to display the graph
plotly.tools.set_credentials_file(username='ENTER_USERNAME_HERE', api_key='ENTER_TOKEN_HERE')

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
COUNT_ARRAY = []
PLOT_DATA = []


# ------------------------------------------------------
# Helper methods
# ------------------------------------------------------

def init_arrays():
    for char in ALPHABET:
        COUNT_ARRAY.append({'letter': char, 'count': 0})

    # Get the filenames from the 'texts' folder
    file_names = os.listdir('texts')
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


def calculate(input_file, array):
    for line in input_file:
        line = line.lower()

        # Count the number of occurrences of each alphabet letter, for each incoming line
        char = ''
        for index in range(len(array)):
            for key in array[index]:
                if key == 'letter':
                    char = key
                if key == 'count':
                    array[index][key] += line.count(array[index][char])

    sum_value = 0
    for index in range(len(array)):
        for key in array[index]:
            if key == 'count':
                sum_value += array[index][key]

    # Sort the array by count value, descending
    return sorted(array, key=lambda k: k['count'], reverse=True), sum_value


def print_results(file_name, array, sum_value):
    print("Letter frequencies for '{0}':".format(file_name))

    c = ''
    for index in range(len(array)):
        for key in array[index]:
            if key == 'letter':
                c = key
            if key == 'count':
                percentage = round(array[index][key] / sum_value * 100, 3)
                print('{0}: {1} occurrences => {2}%'.format(array[index][c],
                                                            array[index][key], percentage))
    print('\n')


def get_plot_results(array, sum_value):
    c_array = []
    y_array = []
    for index in range(len(array)):
        for key in COUNT_ARRAY[index]:
            if key == 'letter':
                c_array.append(array[index][key])
            if key == 'count':
                percentage = round(array[index][key] / sum_value * 100, 3)
                y_array.append(percentage)

    x_array = []
    for i in range(1, 27):
        x_array.append(i)

        data = go.Scatter(
            x=x_array,
            y=y_array,
            mode='lines+markers+text',
            text=c_array,
            name=i,
            textposition='middle center',
            marker=dict(
                opacity=0.4,
                size=y_array,
                sizemode='area',
                sizeref=2. * max(y_array) / (40. ** 2),
                sizemin=4
            )
        )

    PLOT_DATA.append(data)
    return PLOT_DATA


def plot_results(plot_data):
    layout = go.Layout(title='Letter frequencies (%)', showlegend=True)
    fig = go.Figure(data=plot_data, layout=layout)
    py.plot(fig, filename='Letter frequencies')


# ------------------------------------------------------
# Read file and parse text
# ------------------------------------------------------

FILE_NAMES, TEXT_POSITION = init_arrays()

try:

    for f in FILE_NAMES:
        path = 'texts/' + f
        file = open(path, 'r')

        COUNT_ARRAY, SUM_TOTAL = calculate(file, COUNT_ARRAY)

        print_results(f, COUNT_ARRAY, SUM_TOTAL)

        plot = get_plot_results(COUNT_ARRAY, SUM_TOTAL)

        file.close()

    plot_results(PLOT_DATA)

except IOError as e:
    print('I/O error({0}): {1}'.format(e.errno, e.strerror))
