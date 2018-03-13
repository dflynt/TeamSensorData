import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# import csv file to a dataframe as df using pandas
df = pd.read_csv("DrivingData.csv", sep=",")
# Setting Time column as index
time = df.iloc[:, 31]
df.set_index(time, inplace=True)

# Storing light, sound, acceleration column in an array. Using iloc() to find the location of the column
light = df.iloc[:, 12]
sound = df.iloc[:, 21]
accelx = df.iloc[:, 0]
accely = df.iloc[:, 1]
accelz = df.iloc[:, 2]

#creating numpy arrays for acceleration metrics
naccelx = np.array(accelx)
naccely = np.array(accely)
naccelz = np.array(accelz)

#calculating the acceleration
accel = np.sqrt(np.square(naccelx)+np.square(naccely)+np.square(naccelz))

# Calculating the features
avg_sound = sound.mean()
max_sound = sound.max()
avg_light = light.mean()
max_accel = accel.max()
avg_accel = accel.mean()

print("Average Light in Lux: ", avg_light)
print("Average Sound in dB: ", avg_sound)
print("Maximum Sound in dB: ", max_sound)
print("Maximum Acceleration in m/s2: ", max_accel)
print("Average Acceleration in m/s2: ", avg_accel)

# Plotting the graph with the help of subplots in matplotlib
# Sharing the same X-axis as Time with all 3 graphs
f, ax = plt.subplots(3, sharex=True)
ax[0].set_title('Graph which represents Light, Sound and Acceleration')
ax[0].plot(light)
ax[0].set_ylabel("Lux")
ax[1].plot(sound)
ax[1].set_ylabel("dB")
ax[2].plot(accelx,accely,accelz)
ax[2].set_ylabel("m/s2")
plt.xlabel('Time in ms')

plt.show()