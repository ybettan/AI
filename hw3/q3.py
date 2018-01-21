import numpy as np
from id3 import Id3Estimator
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# load data
data = np.genfromtxt('flare.csv', delimiter=",", dtype=None, names=True)
data_classification = data['classification']
data_features = []
for row in data:
    data_features.append([col for col in row][:-1])

# split data to 75% train and 25% test
features_train, features_test, classification_train, classification_test = \
    train_test_split(data_features, data_classification, test_size=0.25, random_state=1)


# create estimators
estimator_underFitting = Id3Estimator(max_depth=1)
estimator_overFitting = Id3Estimator(max_depth=32)

# train over fitting with 75% data
estimator_overFitting.fit(features_train, classification_train)

# predict over fitting on test data and print accuracy FIXME - remove print (FAQ)
classification_predict = estimator_overFitting.predict(features_test)
# print(accuracy_score(classification_test, classification_predict))

# predict over fitting on train data and print accuracy
classification_predict = estimator_overFitting.predict(features_train)
print(accuracy_score(classification_train, classification_predict))

# train under fitting with 75% data
estimator_underFitting.fit(features_train, classification_train)

# predict under fitting on test data and print accuracy FIXME - remove print (FAQ)
classification_predict = estimator_underFitting.predict(features_test)
# print(accuracy_score(classification_test, classification_predict))

# predict under fitting on train data and print accuracy
classification_predict = estimator_underFitting.predict(features_train)
print(accuracy_score(classification_train, classification_predict))
