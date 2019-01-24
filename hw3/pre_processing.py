import numpy as np
from matplotlib import pyplot as plt
from sklearn import neighbors
from sklearn.model_selection import cross_val_score
from sklearn.feature_selection import SelectKBest, f_classif, mutual_info_classif, chi2
from hw3_utils import load_data


def main():
    train_set, train_tags, _ = load_data('data/Data.pickle')
    k_options = np.linspace(90, 140, 25, dtype=int)
    max_k = np.zeros((3, 2))
    selection_method = ['f_classif', 'mutual_info_classif', 'chi2']
    method_1, method_2, method_3 = [], [], []
    best_1, best_2, best_3 = 0, 0, 0
    rnd_idx = np.random.randint(0, train_set.shape[0])
    random_sample = train_set[rnd_idx, :]

    for num_of_features in k_options:
        train_set_new = SelectKBest(f_classif, k=num_of_features).fit_transform(train_set, train_tags)
        clf = neighbors.KNeighborsClassifier(n_neighbors=5, p=1)
        scores = cross_val_score(clf, train_set_new, train_tags, cv=3)
        avg_score = np.mean(scores)
        method_1.append(avg_score)
        if avg_score > max_k[0, 1]:
            max_k[0, 0] = num_of_features
            max_k[0, 1] = avg_score
            best_1 = np.copy(train_set_new[rnd_idx, :])

    for num_of_features in k_options:
        train_set_new = SelectKBest(mutual_info_classif, k=num_of_features).fit_transform(train_set, train_tags)
        clf = neighbors.KNeighborsClassifier(n_neighbors=5, p=1)
        scores = cross_val_score(clf, train_set_new, train_tags, cv=3)
        avg_score = np.mean(scores)
        method_2.append(avg_score)
        if avg_score > max_k[1, 1]:
            max_k[1, 0] = num_of_features
            max_k[1, 1] = avg_score
            best_2 = np.copy(train_set_new[rnd_idx, :])

    train_set[train_set < 0] = 0
    for num_of_features in k_options:
        train_set_new = SelectKBest(chi2, k=num_of_features).fit_transform(train_set, train_tags)
        clf = neighbors.KNeighborsClassifier(n_neighbors=5, p=1)
        scores = cross_val_score(clf, train_set_new, train_tags, cv=3)
        avg_score = np.mean(scores)
        method_3.append(avg_score)
        if avg_score > max_k[2, 1]:
            max_k[2, 0] = num_of_features
            max_k[2, 1] = avg_score
            best_3 = np.copy(train_set_new[rnd_idx, :])

    clf = neighbors.KNeighborsClassifier(n_neighbors=5, p=1)
    scores = cross_val_score(clf, train_set, train_tags, cv=3)
    avg_score = np.mean(scores)
    no_reduction = avg_score * np.ones(k_options.shape)

    plt.figure(figsize=(12, 6))
    plt.subplot(221)
    plt.title('Random sample - Original')
    plt.plot(range(len(random_sample)), random_sample, 'g')
    plt.grid()
    plt.subplot(222)
    plt.title('feature reduction using f_classif')
    plt.plot(range(len(best_1)), best_1, 'b')
    plt.grid()
    plt.subplot(223)
    plt.title('feature reduction using mutual_info_classif')
    plt.plot(range(len(best_2)), best_2, 'b')
    plt.grid()
    plt.subplot(224)
    plt.title('feature reduction using chi2')
    plt.plot(range(len(best_3)), best_3, 'b')
    plt.grid()
    plt.show()

    plt.figure(figsize=(8, 4))
    plt.title('Accuracy of 5-nn vs. # features')
    plt.plot(k_options, method_1, 'c')
    plt.plot(k_options, method_2, 'y')
    plt.plot(k_options, method_3, 'm')
    plt.plot(k_options, no_reduction, linestyle=':', color='g')
    plt.plot(max_k[0, 0], max_k[0, 1], 'cx')
    plt.plot(max_k[1, 0], max_k[1, 1], 'yx')
    plt.plot(max_k[2, 0], max_k[2, 1], 'mx')
    plt.ylim((0.94, 0.96))
    plt.legend([selection_method[0], selection_method[1], selection_method[2], 'No feature reduction'])
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()

