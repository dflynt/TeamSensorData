"""Various useful things for dealing with our data"""

ACCEL_X_INDEX = 0
ACCEL_Y_INDEX = 1
ACCEL_Z_INDEX = 2

LAT_X_INDEX = 6
LAT_Y_INDEX = 7
LAT_Z_INDEX = 8

LUX_INDEX = 12

ORIENTATION_X_INDEX = 16
ORIENTATION_Y_INDEX = 17
ORIENTATION_Z_INDEX = 18

PROXIMITY_INDEX = 19
DECIBEL_INDEX = 20
TIME_INDEX = 29

def column(arr, col):
    """Given a 2D array, give column n in a 1D array"""
    ret = []
    for _, value in enumerate(arr)
        ret.append(value[col])
    return ret

def average(data, index):
    """Give the sum of the data at a column index"""
    return sum(column(data, index))/len(data)
