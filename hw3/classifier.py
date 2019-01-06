from hw3_utils import abstract_classifier, abstract_classifier_factory
from hw3_utils import load_data
#FIXME: does those packages are allowed ?
import csv
import random


def euclidean_distance(x, y):
    d = [x_i - y_i for x_i, y_i in zip(x, y)]
    d_sqr = [d_i**2 for d_i in d]
    return sum(d_sqr)**0.5


class knn_classifier(abstract_classifier):

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
            # we still don't have K samples
            if len(k_dists) < self.K:
                k_dists.append(dist)
                k_tags.append(neighbor_tag)
            # we have already reached K samples so we replace the worst neighbore
            elif dist < max_k_dist:
                k_dists[max_k_idx] = dist
                k_tags[max_k_idx] = neighbor_tag
            #FIXME: what to return in case of a tie?
            # calc the majority call - 0 in case of tie
            max_k_dist = max(k_dists)
            max_k_idx = k_dists.index(max_k_dist)
        # when done all examples
        majority_call = bool(round(sum(k_tags) / len(k_tags)))
        #FIXME: return Boolean on Integer?
        return majority_call


class knn_factory(abstract_classifier_factory):

    # each instance of knn_factory should have its own K
    def __init__(self, k):
        self.K = k

    def train(self, data, labels):
        return knn_classifier(data, labels, self.K)


def split_crosscheck_groups(dataset, num_folds):
    true_exmp, false_exmp = [], []
    # split the data to True and False examples
    for example in dataset:
        if example[-1]:
            true_exmp.append(example)
        else:
            false_exmp.append(example)

    # divide into separate files
    true_sample_size = int(len(true_exmp)/num_folds)
    false_sample_size = int(len(false_exmp)/num_folds)
    for fold_i in range(num_folds):
        #FIXME: what happens if dataset % num_folds != 0, do we miss some at the last group ?
        true_i = random.sample(true_exmp, true_sample_size)
        false_i = random.sample(false_exmp, false_sample_size)
        with open('data/ecg_fold_'+str(fold_i+1)+'.data', 'w') as f:
            f.write(', '.join([str(feature) for feature in true_i]) + '\n')
            f.write(', '.join([str(feature) for feature in false_i]) + '\n')
        # remove all chosen from the picking list
        true_exmp = [exmp for exmp in true_exmp if exmp not in true_i]
        false_exmp = [exmp for exmp in false_exmp if exmp not in false_i]

#def evaluate(classifier_factory, k):
#
#    # create training and test sets
#    train_set = # all data files but data/ecg_fold_i.data
#    test_set = # data/ecg_fold_i.data
#    for i in range(1, k+1):
#        # update train_set and test set
#
#    classifier = classifier_factory.train(train_set.data, train_set.labels)
#
#    # compute accuracy and error
#    for features in test_set:
#
#        # get classification
#        tag = classifier.classify(features)
#
#        # get real tag
#
#        real_tag
#
#        if classification is correct (check original full file)
#          # if is positive
#              # true_positive += 1
#          # else
#              # true_negative += 1
#        elif classification is wrong
#          # if is positive
#              # false_positive += 1
#          # else
#              # false_negative += 1



train_set, train_tags, test_set = load_data()
F = knn_factory(9)
A = F.train(train_set, train_tags)

