import random
import numpy as np

# accuracy is between 0 and 1
# def leave_one_out_cross_validation(data, current_set, feature_to_add):
#     return random.random()

def leave_one_out_cross_validation(data, current_set, feature_to_add, add_or_delete=1):

    (n, m) = data.shape
    # copy data and set irrelevant features as 0s

    # add_or_delete equals 1 means current_set adds the feature_to_add, otherwise the set delete it
    __set = current_set.copy()
    # keep labels
    __set.add(0)

    if add_or_delete:
        __set.add(feature_to_add)
    else:
        __set.remove(feature_to_add)
    
    filter = np.zeros([m])
    for feature in __set:
        filter[feature] = 1
    __data = data*filter

    number_correctly_classified = 0

    for i in range(n):
        object_to_classity = __data[i, 1:]
        label_object_to_classify = __data[i, 0]

        nearest_neighbor_distance = np.inf
        nearest_neighbor_location = np.inf
        nearest_neighbor_label = np.nan

        distances = np.sqrt(np.sum((object_to_classity[np.newaxis,:] - __data[:,1:])**2, axis=1))
        min_distance = np.where(np.min(distances[distances>0]) == distances)
        min_distance_label = min_distance[0][0]

        if label_object_to_classify == __data[min_distance_label,0]:
            number_correctly_classified += 1

    accuracy = number_correctly_classified / n
    return accuracy