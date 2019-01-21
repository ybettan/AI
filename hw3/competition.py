from sklearn.feature_selection import SelectKBest, f_classif
from sklearn import svm, neighbors
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from hw3_utils import load_data, write_prediction

train_set_full, train_tags, test_set_full = load_data('data/Data.pickle')

# ### Pre-processing ###
# Trim data
train_set_full[train_set_full < 0] = 0
train_set_full[train_set_full > 1] = 1
test_set_full[test_set_full < 0] = 0
test_set_full[test_set_full > 1] = 1
# Select 70 best features
feature_sel_1 = SelectKBest(f_classif, k=70)
feature_sel_1.fit(train_set_full, train_tags)
train_set_1 = feature_sel_1.transform(train_set_full)
test_set_1 = feature_sel_1.transform(test_set_full)

# ### Train classifiers ###
clf_1 = neighbors.KNeighborsClassifier(n_neighbors=1, weights='uniform', p=2).fit(train_set_1, train_tags)
clf_2 = neighbors.KNeighborsClassifier(n_neighbors=3, weights='distance', p=2).fit(train_set_1, train_tags)
clf_3 = neighbors.KNeighborsClassifier(n_neighbors=5, weights='distance', p=1).fit(train_set_1, train_tags)
clf_4 = svm.SVC(kernel='poly', C=0.78, degree=11, coef0=2, gamma='auto').fit(train_set_1, train_tags)
clf_5 = RandomForestClassifier(n_estimators=200, criterion='entropy', max_depth=None).fit(train_set_1, train_tags)

# create voting classifier
final_clf = VotingClassifier(estimators=[('knn1', clf_1), ('knn3', clf_2), ('knn5', clf_3),
                                         ('svm', clf_4), ('rf', clf_5)], voting='hard')
final_clf.fit(train_set_1, train_tags)
write_prediction(final_clf.predict(test_set_1).astype(int))
