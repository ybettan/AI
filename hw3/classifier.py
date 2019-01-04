from hw3_utils import abstract_classifier, abstract_classifier_factory
from hw3_utils import load_data
import csv
import random


def euclidean_distance(x, y):
    d = [x_i - y_i for x_i, y_i in zip(x, y)]
    d_sqr = [d_i**2 for d_i in d]
    return sum(d_sqr)**0.5


class knn_classifier(abstract_classifier):

    #train_set, train_tags, _ = load_data()
    # train_set, train_tags = [[-2, 1], [2, 1], [-3, 0], [3, 0], [-2, -1], [2, -1]], [1, 0, 0, 1, 1, 0]

    def __init__(self, data, tags, k):
        self.data = data
        self.tags = tags
        self.K = k

    def classify(self, features):
        k_dists, k_tags = [], []
        max_k_dist, max_k_idx = 0, 0
        majority_call = True
        # Iterate through tagged data to find the K closest
        for neighbor_features, neighbor_tag in zip(self.data, self.tags):
            dist = euclidean_distance(features, neighbor_features)
            if len(k_dists) < self.K:
                k_dists.append(dist)
                k_tags.append(neighbor_tag)
                # calc the majority call - 0 in case of tie
                majority_call = bool(round(sum(k_tags) / len(k_tags)))
                max_k_dist = max(k_dists)
                max_k_idx = k_dists.index(max_k_dist)
            elif dist < max_k_dist:
                k_dists[max_k_idx] = dist
                k_tags[max_k_idx] = neighbor_tag
                majority_call = bool(round(sum(k_tags) / self.K))
                max_k_dist = max(k_dists)
                max_k_idx = k_dists.index(max_k_dist)
        # when done all examples
        return majority_call


class knn_factory(abstract_classifier_factory):

    def train(self, data, labels):
        k = 9
        return knn_classifier(data, labels, k)


def split_crosscheck_groups(dataset, num_folds=10):
    true_exmp, false_exmp = [], []
    # split the data to True and False examples
    for example in dataset:
        if example[-1]:
            true_exmp.append(example)
        else:
            false_exmp.append(example)

    true_sample_size = int(len(true_exmp)/num_folds)
    false_sample_size = int(len(false_exmp)/num_folds)
    for fold_i in range(num_folds):
        true_i = random.sample(true_exmp, true_sample_size)
        false_i = random.sample(false_exmp, false_sample_size)
        with open('data/ecg_fold_'+str(fold_i+1)+'.data', 'w') as f:
            f.write(', '.join([str(feature) for feature in true_i]) + '\n')
            f.write(', '.join([str(feature) for feature in false_i]) + '\n')
        true_exmp = [exmp for exmp in true_exmp if exmp not in true_i]
        false_exmp = [exmp for exmp in false_exmp if exmp not in false_i]


train_set, train_tags, test_set = load_data()
F = knn_factory()
A = F.train(train_set, train_tags)

