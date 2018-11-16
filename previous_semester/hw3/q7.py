import numpy as np
from sfs import sfs
from score_wrapper import score_wrapper
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# knn neighbors
k = 5
# number of features
b = 8

# load data
data = np.genfromtxt('flare.csv', delimiter=",", dtype=None, names=True)
data_classification = data['classification']
data_features = []
for row in data:
    data_features.append([col for col in row][:-1])

# split data to 75% train and 25% test
features_train, features_test, classification_train, classification_test = \
    train_test_split(data_features, data_classification, test_size=0.25, random_state=4)

# train KNN with all features
estimator_knn = neighbors.KNeighborsClassifier(n_neighbors=k)
estimator_knn.fit(features_train, classification_train)
classification_predict = estimator_knn.predict(features_test)
print(accuracy_score(classification_test, classification_predict))

# use KNN with sfs
features_idx = sfs(features_train, classification_train, b, estimator_knn, score_wrapper)

# remove unselected features from data
selected_features_train = [[row[i] for i in features_idx] for row in features_train]
selected_features_test = [[row[i] for i in features_idx] for row in features_test]

# train new knn with selected features
estimator_knn.fit(selected_features_train, classification_train)
classification_predict = estimator_knn.predict(selected_features_test)
print(accuracy_score(classification_test, classification_predict))
