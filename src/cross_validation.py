import random
import numpy as np

# accuracy is between 0 and 1
# def leave_one_out_cross_validation(data, current_set, feature_to_add):
#     return random.random()

def leave_one_out_cross_validation(data, current_set, feature_to_add, add_or_delete=1):

    # copy data and set irrelevant features as 0s
    __data = data.copy()

    # add_or_delete equals 1 means current_set adds the feature_to_add, otherwise the set delete it
    __set = current_set.copy()
    if add_or_delete:
        __set.add(feature_to_add)
    else:
        __set.remove(feature_to_add)

    for feature in __set:
        __data[:, feature] = 0

    number_correctly_classified = 0

    (n, m) = __data.shape
    for i in range(n):
        object_to_classity = __data[i, 1:]
        label_object_to_classify = __data[i, 0]

        nearest_neighbor_distance = np.inf
        nearest_neighbor_location = np.inf
        nearest_neighbor_label = np.nan

        for k in range(n):
            if k != i:
                distance = np.sqrt(np.sum((object_to_classity - __data[k, 1:])**2))
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = k
                    nearest_neighbor_label = __data[k, 0]

        if label_object_to_classify == nearest_neighbor_label:
            number_correctly_classified += 1

    accuracy = number_correctly_classified / n
    return accuracy