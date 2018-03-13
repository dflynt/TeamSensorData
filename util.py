"""Various useful things for dealing with our data"""

def column(arr, col):
    """Given a 2D array, give column n in a 1D array"""
    ret = []
    for _, val in enumerate(arr):
        ret.append(val[col])
    return ret

def average(data, index):
    """Give the sum of the data at a column index"""
    return sum(column(data, index))/len(data)
