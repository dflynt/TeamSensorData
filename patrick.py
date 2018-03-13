import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.figure as fig
import numpy as np

import pandas as pd
import csv as cs

x = []
y = []

file_name = ".\\DrivingData.csv"

with open(file_name) as csvfile:
    next(csvfile)
    plots =  cs.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[20]))
        y.append(float(row[21]))
plt.plot(x, y, label='Loaded from file')
plt.xlabel('Atmospheric Pressure')
plt.ylabel('Sound Level')
plt.title('Atmospheric Pressure vs Sound Level')
plt.legend()
plt.show()      
