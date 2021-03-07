import numpy as np

# use ndarray to represent data
def read_data(path):
    file = open(path, 'r')
    lines  = file.readlines()
    file.close()
    data = []
    for line in lines:
        data.append([ float(feature) for feature in line.split() ])
    return np.array(data)
