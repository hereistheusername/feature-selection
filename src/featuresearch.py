
from src.cross_validation import leave_one_out_cross_validation

def feature_search_demo(data):
    # the 0th value in each line is the lable
    # Im going to use integers to represent features 
    # current_set_of_features is a set object
    current_set_of_features = set()

    (n,m) = data.shape
    for i in range(1,m):
        print(
            'On the ',
            str(i),
            'th level of the search three'
            )
        feature_to_add_at_this_level = 0
        best_so_far_accuracy = 0

        for k in range(1,m):
            # only consider adding this feature if it was not already added
            if k not in current_set_of_features:
                print(
                    '--Considering adding the ',
                    str(k),
                    ' feature'
                )
            accuracy = leave_one_out_cross_validation(data, current_set_of_features, k)

            if accuracy > best_so_far_accuracy:
                best_so_far_accuracy = accuracy
                feature_to_add_at_this_level = k
            
        current_set_of_features.add(feature_to_add_at_this_level)
        print(
            'On level ',
            str(i),
            ' i added feature ',
            str(feature_to_add_at_this_level),
            ' to current set'
        )
