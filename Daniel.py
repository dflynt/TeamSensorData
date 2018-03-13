import pandas as p
import util
def is_active(frame):
    return (abs(frame[LAT_X_INDEX]) + abs(frame[LAT_Y_INDEX]) +
            abs(frame[LAT_Z_INDEX])) > 1

def run():
    DATA = p.read_csv("DrivingData.csv", sep=",")
    NUM = DATA.values
    ACTIVE_TIME = [frame for frame in NUM if is_active(frame)]

    print("Of those frames when it was probably in a pocket, we probably" + 
    " were able to pick up on conversation for "+str(len(NOISY))+" of them.")

    ACTIVE_TIME = (500 * len(ACTIVE_TIME)) / 1000.0
    print("The active time was " + str(ACTIVE_TIME) + ".")
    print("Which means there was an active percentage of " + 
            str((ACTIVE_TIME / TOTAL_ITME) * 100) + ".")


