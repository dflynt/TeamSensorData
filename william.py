##import pytest
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import math

LAccelX = 6
LAccelY = 7
Duration = 30


# LINEAR_ACCEL_X =  6
# LINEAR_ACCEL_Y = 7
# TIME = 30

df = pd.read_csv("DrivingData.csv", sep = ",")

def column(arr,lst):
    ret = []
    print(len(arr))
    for i in range(0, len(arr)):
        ret.append(arr[i][lst])
    return ret

def run():
    number = df.values
    
    time = column(number, Duration)
    movement_time = []
    for frame in number:
        movement_time.append((abs(frame[LAccelX]) + abs(frame[LAccelY])))

    plt.plot(time,movement_time)
    plt.title("Toal movement vs time.")
    plt.show()
    print(plt)
run()


