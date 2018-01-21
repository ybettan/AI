import numpy as np
from id3 import Id3Estimator
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, confusion_matrix

estimator = Id3Estimator()
data = np.genfromtxt('flare.csv', delimiter=",", dtype=None, names=True)
data_classification = data['classification']
data_features = []
for row in data:
    data_features.append([col for col in row][:-1])

# K fold training
fold_index = KFold(n_splits=4)
accuracy = []
confusion_mat = []

for train_index, test_index in fold_index.split(data_features):
    # split data
    features_train = [data_features[i] for i in train_index]
    classification_train = [data_classification[i] for i in train_index]
    features_test = [data_features[i] for i in test_index]
    classification_test = [data_classification[i] for i in test_index]
    # train tree
    estimator.fit(features_train, classification_train)
    # predict with tree
    classification_predict = estimator.predict(features_test)
    # calculate accuracy and confusion matrix
    accuracy.append(accuracy_score(classification_test, classification_predict))
    confusion_mat.append(confusion_matrix(classification_test, classification_predict))

# calculate final results and print
acc = np.mean(accuracy)
mat = confusion_mat[0] + confusion_mat[1] + confusion_mat[2] + confusion_mat[3]

print(acc)
print(mat)


