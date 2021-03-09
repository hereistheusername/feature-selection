import numpy as np

def normalize(data):
    sum_along_axis_0 = np.sum(data,axis=0)
    # keep labels same
    sum_along_axis_0[0] = 1
    return data/sum_along_axis_0