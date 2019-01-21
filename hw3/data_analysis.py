import numpy as np
from hw3_utils import load_data
from matplotlib import pyplot as plt
from sklearn.feature_selection import SelectKBest, f_classif


train_set, train_tags, test_set = load_data('data/Data.pickle')
k_best = 187
train_set_new = SelectKBest(f_classif, k=k_best).fit_transform(train_set, train_tags)

best_scores = 0
best_classifier = []

good = train_set[train_tags]
bad = np.asarray([exmp for exmp in train_set if exmp not in train_set[train_tags]])
good_new = train_set_new[train_tags]
bad_new = np.asarray([exmp for exmp in train_set_new if exmp not in train_set_new[train_tags]])

print(np.var(good_new, axis=0))
print(np.var(bad_new, axis=0))

plt.figure()
plt.plot(range(k_best), np.mean(good_new, axis=0), 'g')
plt.plot(range(k_best), np.var(good_new, axis=0), 'g-')
plt.plot(range(k_best), np.mean(bad_new, axis=0), 'r')
plt.plot(range(k_best), np.var(bad_new, axis=0), 'r-')
plt.grid()
plt.show()

plt.figure(figsize=(12, 4))
plt.subplot(121)
plt.plot(range(187), good[0, :], 'g')
plt.plot(range(187), good[400, :], 'g')
plt.grid()
plt.subplot(122)
plt.plot(range(187), bad[0, :], 'r')
plt.plot(range(187), bad[90, :], 'r')
plt.grid()
plt.show()
