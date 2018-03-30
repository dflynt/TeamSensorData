"""Danny's collected data"""
import util

import pandas as p
import matplotlib.pyplot as plot



def is_low_light(frame):
    """Microsoft's usability guidelines say that dim
    lighting starts at 200 lux."""
    return frame[util.LUX_INDEX] < 200

def is_close(frame):
    """My particular phone sensor is binary, either 5cm or 0cm.
    I can't vouch for others."""
    return frame[util.PROXIMITY_INDEX] < 5

def is_audible(frame):
    """60 decibels is roughly the noise level of conversation"""
    return frame[util.DECIBEL_INDEX] > 60

def is_active(frame):
    """Just an arbitrary threshhold for "Yeah, it looks like this person is moving"
    via the sensors"""
    return (abs(frame[util.LAT_X_INDEX])
            + abs(frame[util.LAT_Y_INDEX])
            + abs(frame[util.LAT_Z_INDEX])) > 1

def run():
    """Entry point and print the real metrics."""
    data = p.read_csv("DrivingData.csv")
    num = data.values


    # The time column is the X axis for practically every graph
    time = util.column(num, util.TIME_INDEX)

    # Time is recorded in milliseconds, convert to seconds.
    time = [time / 1000.0 for time in time]

    # Extract all of our sensor snapshots which are in low light.
    low_light_frames = [frame for frame in num if is_low_light(frame)]

    # If the light is low and there's something right next to us,
    #we're probably either on the phone or it's in the pocket.
    pocket = [frame for frame in low_light_frames if is_close(frame)]


    # Extract all frames which were above the conversation threshhold
    noisy = [frame for frame in pocket if is_audible(frame)]



    print("There are " + str(len(num)) + " frames of data in total, each frame is 0.5s")

    print("There are " + str(len(low_light_frames)) + " frames with low light")

    print("Of those, it was probably in my pocket " + str(len(pocket)) + " frames")

    print("The average light level overall was "
          + str(sum(util.column(num, util.LUX_INDEX))/len(num)) + ".")

    # Just get the total time from the first and last frames quickly.
    total_time = (num[-1][util.TIME_INDEX] - num[0][util.TIME_INDEX]) / 1000.0

    # Pull all frames during which we were active (above a linear acceleration threshhold.)
    active_time = [frame for frame in num if is_active(frame)]

    print("Of those frames when it was probably in a pocket, we probably were able to pick "
          + "up on conversation for " + str(len(noisy)) + " of them.")

    print("The total amount of time spent recording was " + str(total_time) + " S")

    # Each frame is 500 milliseconds.
    active_time = (500 * len(active_time)) / 1000.0


    print("Which means there was an active percentage of "
          + str((active_time / total_time) * 100) + ".")

    show_plots(num, time)

def show_plots(num, time):
    """Display the data to be plotted"""
    # Plot various relevant metrics.
    plot.plot(time, util.column(num, util.LUX_INDEX))
    plot.title("Lux (light level) vs time.")
    plot.show()

    plot.plot(time, util.column(num, util.DECIBEL_INDEX))
    plot.title("Decibels (sound level) vs time.")
    plot.show()

    # Take every frame and sum the X, Y, and Z acceleration magnitudes in those frames.
    movement_sums = []
    for sensor_frame in num:
        movement_sums.append((abs(sensor_frame[util.LAT_X_INDEX])
                              + abs(sensor_frame[util.LAT_Y_INDEX])
                              + abs(sensor_frame[util.LAT_Z_INDEX])))

    plot.plot(time, movement_sums)
    plot.title("Total movement vs time.")
    plot.show()

    # Just show a binary chart: either the user is active or the user is not,
    # as determined by our threshhold that we decided on before.
    active = []
    for sensor_frame in num:
        if (abs(sensor_frame[util.LAT_X_INDEX]) + abs(sensor_frame[util.LAT_Y_INDEX])
                + abs(sensor_frame[util.LAT_Z_INDEX])) > 1:
            active.append(1)
        else:
            active.append(0)

    plot.bar(time, active)
    plot.title("Blocks of active time.")
    plot.show()
