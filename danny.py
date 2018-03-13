"""Danny's collected data"""
import util
import pandas as p
import matplotlib as plot

def is_low_light(frame):
    """Microsoft's usability guidelines say that dim
    lighting starts at 200 lux."""
    return frame[LUX_INDEX] < 200

def is_close(frame):
    """My particular phone sensor is binary, either 5cm or 0cm.
    I can't vouch for others."""
    return frame[PROXIMITY_INDEX] < 5

def is_audible(frame):
    """60 decibels is roughly the noise level of conversation"""
    return frame[DECIBEL_INDEX] > 60

def is_active(frame):
    """Just an arbitrary threshhold for "Yeah, it looks like this person is moving"
    via the sensors"""
    return (abs(frame[LAT_X_INDEX]) + abs(frame[LAT_Y_INDEX]) + abs(frame[LAT_Z_INDEX])) > 1

def run():
    DATA = p.read_csv("DrivingData.csv", sep=";")
    NUM = DATA.values
    
    """Entry point and print the real metrics."""
    # The time column is the X axis for practically every graph
    TIME = column(NUM, TIME_INDEX)

    # Time is recorded in milliseconds, convert to seconds.
    TIME = [TIME / 1000.0 for TIME in TIME]

    # Extract all of our sensor snapshots which are in low light.
    LOW_LIGHT_FRAMES = [frame for frame in NUM if is_low_light(frame)]

    # If the light is low and there's something right next to us,
    #we're probably either on the phone or it's in the pocket.
    POCKET = [frame for frame in LOW_LIGHT_FRAMES if is_close(frame)]


    # Extract all frames which were above the conversation threshhold
    NOISY = [frame for frame in POCKET if is_audible(frame)]


    print("There are " + str(len(NUM)) + " frames of data in total, each frame is 0.5s")

    print("There are " + str(len(LOW_LIGHT_FRAMES)) + " frames with low light")

    print("Of those, it was probably in my pocket " + str(len(POCKET)) + " frames")

    print("The average light level overall was "
          + str(sum(column(NUM, LUX_INDEX))/len(NUM)) + ".")

    # Just get the total time from the first and last frames quickly.
    TOTAL_TIME = (NUM[-1][TIME_INDEX] - NUM[0][TIME_INDEX]) / 1000.0

    # Pull all frames during which we were active (above a linear acceleration threshhold.)
    ACTIVE_TIME = [frame for frame in NUM if is_active(frame)]

    print("Of those frames when it was probably in a pocket, we probably were able to pick "
          + "up on conversation for " + str(len(NOISY)) + " of them.")

    print("The total amount of time spent recording was " + str(TOTAL_TIME) + " S")

    # Each frame is 500 milliseconds.
    ACTIVE_TIME = (500 * len(ACTIVE_TIME)) / 1000.0


    print("Which means there was an active percentage of " + str((ACTIVE_TIME / TOTAL_ITME) * 100) + ".")

    show_plots(NUM, TIME)

def show_plots(NUM, TIME):
    """Display the data to be plotted"""
    # Plot various relevant metrics.
    plot.plot(TIME, column(NUM, LUX_INDEX))
    plot.title("Lux (light level) vs time.")
    plot.show()

    plot.plot(TIME, column(NUM, DECIBEL_INDEX))
    plot.title("Decibels (sound level) vs time.")
    plot.show()

    # Take every frame and sum the X, Y, and Z acceleration magnitudes in those frames.
    MOVEMENT_SUMS = []
    for sensor_frame in NUM:
        MOVEMENT_SUMS.append((abs(sensor_frame[LAT_X_INDEX]) + abs(sensor_frame[LAT_Y_INDEX])
                              + abs(sensor_frame[LAT_Z_INDEX])))

        plot.plot(TIME, MOVEMENT_SUMS)
        plot.title("Total movement vs time.")
        plot.show()

        # Just show a binary chart: either the user is active or the user is not,
        # as determined by our threshhold that we decided on before.
        ACTIVE = []
        for sensor_frame in NUM:
            if (abs(sensor_frame[LAT_X_INDEX]) + abs(sensor_frame[LAT_Y_INDEX])
                + abs(sensor_frame[LAT_Z_INDEX])) > 1:
                ACTIVE.append(1)
            else:
                ACTIVE.append(0)

        plot.bar(TIME, ACTIVE)
        plot.title("Blocks of active time.")
        plot.show()
