import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from id3 import Id3Estimator

min_samples = 20

# load data
data = np.genfromtxt('flare.csv', delimiter=",", dtype=None, names=True)
data_classification = data['classification']
data_features = []
for row in data:
    data_features.append([col for col in row][:-1])

# split data to 75% train and 25% test
features_train, features_test, classification_train, classification_test = \
    train_test_split(data_features, data_classification, test_size=0.25, random_state=4)

# train without cut
estimator = Id3Estimator()
estimator.fit(features_train, classification_train)
classification_predict = estimator.predict(features_test)
print(accuracy_score(classification_test, classification_predict))

# train with cut
estimator_cut = Id3Estimator(min_samples_split=min_samples)
estimator_cut.fit(features_train, classification_train)
classification_predict = estimator_cut.predict(features_test)
print(accuracy_score(classification_test, classification_predict))

