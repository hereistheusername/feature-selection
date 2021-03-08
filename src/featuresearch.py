import numpy as np

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
        feature_to_add_at_this_level = np.nan
        best_so_far_accuracy = -np.inf

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

def forward_feature_search(data):
    # the 0th value in each line is the lable
    # Im going to use integers to represent features 
    # current_set_of_features is a set object
    current_set_of_features = set()
    best_features = set()

    (n,m) = data.shape
    last_accuracy = -np.inf
    best_accuracy = -np.inf
    for i in range(1,m):
        feature_to_add_at_this_level = np.nan
        best_so_far_accuracy = -np.inf

        for k in range(1,m):
            # only consider adding this feature if it was not already added
            if k not in current_set_of_features:
                accuracy = leave_one_out_cross_validation(data, current_set_of_features, k)

                print(
                    '--Considering adding the ',
                    str(k),
                    ' feature, and accuracy is ',
                    str(accuracy*100),
                    '%'
                )

                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add_at_this_level = k
            
        if best_so_far_accuracy < last_accuracy:
            print(
                'Warning, Accuracy has decreased! Continuing search in case of local maxima'
            )
        last_accuracy = best_so_far_accuracy
        current_set_of_features.add(feature_to_add_at_this_level)
        if best_accuracy < best_so_far_accuracy:
            best_accuracy = last_accuracy
            best_features = current_set_of_features.copy()
        print(
            'Feature set ',
            str(current_set_of_features),
            ' was best, accuracy is ',
            str(best_so_far_accuracy*100),
            '%\n'
        )
        
    print(
        'Finished search!! The best feauture subset is ',
        str(best_features),
        ', which has an accuracy of ',
        str(best_accuracy*100),
        '%'
    )

def backward_feature_search(data):
    # the 0th value in each line is the lable
    # Im going to use integers to represent features 
    # current_set_of_features is a set object

    (n,m) = data.shape

    current_set_of_features = set([n for n in range(1, m)])

    for i in range(1,m):
        feature_to_eliminate_at_this_level = np.nan
        best_so_far_accuracy = -np.inf
        last_accuracy = -np.inf

        for k in range(1,m):
            # only consider adding this feature if it was not already added
            if k in current_set_of_features:
                accuracy = leave_one_out_cross_validation(data, current_set_of_features, k)

                print(
                    '--Considering eliminating the ',
                    str(k),
                    ' feature, and accuracy is ',
                    str(accuracy*100),
                    '%'
                )

                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_eliminate_at_this_level = k
                    
            
        if best_so_far_accuracy < last_accuracy:
            print(
                'Warning, Accuracy has decreased! Continuing search in case of local maxima'
            )
        last_accuracy = best_so_far_accuracy
        current_set_of_features.remove(feature_to_eliminate_at_this_level)
        print(
            'Feature set ',
            str(current_set_of_features),
            ' was best, accuracy is ',
            str(best_so_far_accuracy*100),
            '%\n'
        )
        