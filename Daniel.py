import pandas as p
import util


def is_active(frame):
    return (abs(frame[util.LAT_X_INDEX]) + abs(frame[util.LAT_Y_INDEX]) +
            abs(frame[util.LAT_Z_INDEX])) > 1


def run():
    DATA = p.read_csv("DrivingData.csv", sep=",")
    NUM = DATA.values
    ACTIVE_TIME = [frame for frame in NUM if is_active(frame)]
    ACTIVE_TIME = (500 * len(ACTIVE_TIME)) / 1000.0
    print("The active time was " + str(ACTIVE_TIME) + ".")
