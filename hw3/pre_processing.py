import numpy as np
from sklearn import neighbors
from sklearn.model_selection import cross_val_score
from sklearn.feature_selection import SelectKBest, f_classif, mutual_info_classif, chi2
from hw3_utils import load_data

train_set, train_tags, _ = load_data('data/Data.pickle')
k_options = np.linspace(90, 140, 25, dtype=int)
max_k = [0, 0]
print("f_classif")
for num_of_features in k_options:
    train_set_new = SelectKBest(f_classif, k=num_of_features).fit_transform(train_set, train_tags)
    clf = neighbors.KNeighborsClassifier(n_neighbors=5, p=1)
    scores = cross_val_score(clf, train_set_new, train_tags, cv=4)
    avg_score = np.mean(scores)
    var = np.var(scores)
    if avg_score > max_k[1]:
        max_k[0] = num_of_features
        max_k[1] = avg_score
    print("k = " + str(num_of_features) + "| Accuracy = " + str(avg_score))
print(max_k)
max_k = [0, 0]
print("mutual_info_classif")
for num_of_features in k_options:
    train_set_new = SelectKBest(mutual_info_classif, k=num_of_features).fit_transform(abs(train_set), train_tags)
    clf = neighbors.KNeighborsClassifier(n_neighbors=5, p=1)
    scores = cross_val_score(clf, train_set_new, train_tags, cv=4)
    avg_score = np.mean(scores)
    if avg_score > max_k[1]:
        max_k[0] = num_of_features
        max_k[1] = avg_score
    print("k = " + str(num_of_features) + "| Accuracy = " + str(avg_score))
print(max_k)
max_k = [0, 0]
print("chi2")
for num_of_features in k_options:
    train_set_new = SelectKBest(chi2, k=num_of_features).fit_transform(abs(train_set), train_tags)
    clf = neighbors.KNeighborsClassifier(n_neighbors=5, p=1)
    scores = cross_val_score(clf, train_set_new, train_tags, cv=4)
    avg_score = np.mean(scores)
    if avg_score > max_k[1]:
        max_k[0] = num_of_features
        max_k[1] = avg_score
    print("k = " + str(num_of_features) + "| Accuracy = " + str(avg_score))
print(max_k)