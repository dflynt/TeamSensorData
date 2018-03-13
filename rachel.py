import numpy
import matplotlib.pyplot as plt
import traceback

# Change this to point to your specific AndroSensor CSV file
FILE_LOCATION = ".\\DrivingData.csv"

def runaccelmagovertime(DATA):
    try:
        # abs(Magnitude) = sqrt(x^2 + y^2 + z^2)
        magnitude_x_column = numpy.square(DATA["AccelX"])
        magnitude_y_column = numpy.square(DATA["AccelY"])
        magnitude_z_column = numpy.square(DATA["AccelZ"])
        magnitude_column = numpy.add(magnitude_x_column, magnitude_y_column)
        magnitude_column = numpy.add(magnitude_column, magnitude_z_column)
        magnitude_column = numpy.sqrt(magnitude_column)

        plt.plot((DATA["Duration"]/1000), magnitude_column)
        plt.xlabel("Duration (Seconds)")
        plt.ylabel("Acceleration Magnitude Sensed")
        plt.savefig("Acceleration_Mag_Over_Time.png")
        plt.show()
    except:
        print("Something went wrong with printing the plot in rachel.py...")
        # The next line is for debugging only, leave commented out for delivery
        print(traceback.format_exc())
    print("Acceleration Magnitude over Time plot attempt complete.\n")
    print("If a plot did not disply, please check for Acceleration_Mag_Over_Time.png.")
    plt.gcf().clear()

def run():
    try:
        NAMES_LIST = ["AccelX", "AccelY", "AccelZ", "GravX", "GravY", "GravZ", "LAccelX", "LAccelY", "LAccelZ", "GyroX", "GyroY", "GyroZ", "Light", "MagX", "MagY", "MagZ", "OrienX", "OrienY", "OrienZ", "Proximity", "Pressure", "Sound", "Latitude", "Longitude", "Altitude", "GoogleAlt", "GoogleATM", "Speed", "Accuracy", "Orientation", "SatelliteCount", "Duration", "Date"]
        DATA = numpy.genfromtxt(FILE_LOCATION, delimiter=',', names=NAMES_LIST, skip_header=1)
        runaccelmagovertime(DATA)
    except:
        print("There was an issue with reading in the data from rachel.py...")

# Comment out when not using
# run()