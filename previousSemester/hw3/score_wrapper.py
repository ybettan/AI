import numpy as np
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score

def score_wrapper(clf, features, classification):

    # K fold training
    fold_index = KFold(n_splits=4)
    accuracy = []

    for train_index, test_index in fold_index.split(features):
        # split data
        features_train = [features[i] for i in train_index]
        classification_train = [classification[i] for i in train_index]
        features_test = [features[i] for i in test_index]
        classification_test = [classification[i] for i in test_index]
        # train tree
        clf.fit(features_train, classification_train)
        # predict with tree
        classification_predict = clf.predict(features_test)
        # calculate accuracy and confusion matrix
        accuracy.append(accuracy_score(classification_test, classification_predict))

    # calculate final results and print
    acc = np.mean(accuracy)

    return acc
