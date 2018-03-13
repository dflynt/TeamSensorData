'''
A program that extracts information from the data gathered
from AndroSenser.

Author: Colleen Britt

NOTE: Unable to reach 100% pass on pylint because the
imports must be in that order for this program to
work.

Python 3.6
'''

import math
import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(DIR, 'DrivingData.csv')

def calculate_stops(d_f, row):
    '''
    Calculates the number of stops that occurred.
    '''
    stopped = False
    number_of_stops = 0
    for i in range(0, row):
        if d_f.iloc[i][27] == 0 and stopped:
            continue
        elif d_f.iloc[i][27] == 0:
            number_of_stops += 1
            stopped = True
        else:
            stopped = False
    return number_of_stops

def calculate_total_distance(d_f, row):
    '''
    Calcuates the total distance travelled.
    '''

    distance = 0

    # approximate radius of earth in km
    radius = 6373.0

    for i in range(0, row-1):
        # algorithm taken from:
        # https://stackoverflow.com/questions/19412462/
        # getting-distance-between-two-points-based-on-latitude-longitude
        lat1 = math.radians(d_f.iloc[i][22])
        lon1 = math.radians(d_f.iloc[i][23])
        lat2 = math.radians(d_f.iloc[i+1][22])
        lon2 = math.radians(d_f.iloc[i+1][23])

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        calc_a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        calc_c = 2 * math.atan2(math.sqrt(calc_a), math.sqrt(1 - calc_a))

        distance += radius * calc_c

    return distance

def calculate_distances(d_f, row):
    '''
    Calculates each distance between 2 pairs of longitude and
    latitude coordinates.
    '''
    distances = []
    distance = 0

    # approximate radius of earth in km
    radius = 6373.0

    for i in range(0, row-1):
        # algorithm taken from:
        # https://stackoverflow.com/questions/19412462/
        # getting-distance-between-two-points-based-on-latitude-longitude
        lat1 = math.radians(d_f.iloc[i][22])
        lon1 = math.radians(d_f.iloc[i][23])
        lat2 = math.radians(d_f.iloc[i+1][22])
        lon2 = math.radians(d_f.iloc[i+1][23])

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        calc_a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        calc_c = 2 * math.atan2(math.sqrt(calc_a), math.sqrt(1 - calc_a))

        distance += radius * calc_c
        distances.append(distance * .621371)

    return distances

def print_features(time, number_of_stops, distance, average_light):
    '''
    Prints the features that were calculated.
    '''
    print('\nTotal time: ' + str((time/(1000*60)%60)) + ' minutes')
    print('Number of stops: ' + str(number_of_stops))
    print('Distance travelled: ' + str(distance) + ' km or ' + str(distance * .621371) + ' miles')
    print('Average Light: ' + str(average_light) + " lux\n")


def plot_distance(distances):
    '''
    Creates a graph of the distances between each pair of latitude
    and longitude coordinates. It is saved to a .png file.
    '''

    plt.plot(distances)
    plt.ylabel('Cumulative Distance (miles)')
    plt.xlabel('Number of distances calculated from long. and lat.')
    out_png = 'distances.png'
    plt.savefig(out_png, dpi=150)
    plt.clf()

def plot_light(d_f, average_light):
    '''
    Creates a graph of the average light amount and compares it
    to all of the entries of the light data. It is saved to a .png
    file.
    '''
    plt.plot(d_f.iloc[:, 12])
    plt.axhline(average_light, color='r', linestyle='dashed', linewidth=2)
    plt.ylabel('Lux')
    plt.xlabel('Number of entries')
    out_png = 'light.png'
    plt.savefig(out_png, dpi=150)
    plt.clf()

def run():
    '''
    Reads data from .cvs file and calls other function to
    extract information.
    '''
    d_f = pd.read_csv(CSV_FILE, skiprows=0, sep=',')

    # total number of rows
    row = d_f.shape[0]
    # total number of columns
    col = d_f.shape[1]
    # column containing light data
    light = d_f.iloc[:, 12]

    # gets the total time from the specific entry in .csv file
    time = d_f.iloc[row-1][col-2]
    # calculates average light
    average_light = light.mean()
    # total number of stops
    number_of_stops = calculate_stops(d_f, row)
    # total distance travelled
    distance = calculate_total_distance(d_f, row)
    # array of distances between pairs of longitude and latitude coordinates
    distances = calculate_distances(d_f, row)

    print_features(time, number_of_stops, distance, average_light)

    plot_distance(distances)
    plot_light(d_f, average_light)
