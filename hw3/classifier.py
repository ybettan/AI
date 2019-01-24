from hw3_utils import abstract_classifier, abstract_classifier_factory, load_data
from sklearn import tree, linear_model
import random


def euclidean_distance(x, y):
    d = [x_i - y_i for x_i, y_i in zip(x, y)]
    d_sqr = [d_i**2 for d_i in d]
    return sum(d_sqr)**0.5


class knn_classifier(abstract_classifier):

    def __init__(self, examples, k):
        self.data = examples[0]
        self.tags = examples[1]
        self.K = k

    def classify(self, features):
        k_dists, k_tags = [], []
        max_k_dist, max_k_idx = 0, 0
        # Iterate through tagged data to find the K closest
        for neighbor_features, neighbor_tag in zip(self.data, self.tags):
            dist = euclidean_distance(features, neighbor_features)
            # we still don't have K samples
            if len(k_dists) < self.K:
                k_dists.append(dist)
                k_tags.append(neighbor_tag)
                max_k_dist = max(k_dists)
                max_k_idx = k_dists.index(max_k_dist)
            # we have already reached K samples so we replace the worst neighbore
            elif dist < max_k_dist:
                k_dists[max_k_idx] = dist
                k_tags[max_k_idx] = neighbor_tag
                # calc the majority call - 0 in case of tie
                max_k_dist = max(k_dists)
                max_k_idx = k_dists.index(max_k_dist)
        # when done all examples
        if len(k_tags) == 0:
            return True
        else:
            return bool(round(sum(k_tags) / len(k_tags)))

    def score(self, features, tags):
        true_pos, true_neg, idx = 0, 0, 0
        for smpl in features:
            # get classification
            tag = self.classify(smpl)
            # get real value
            real_tag = tags[idx]
            if tag:
                if real_tag:
                    true_pos += 1
                # else: false_pos += 1
            else:
                if not real_tag:
                    true_neg += 1
                # else: false_neg += 1
            idx += 1

        accuracy = (true_pos + true_neg) / len(features)
        return accuracy


class knn_factory(abstract_classifier_factory):

    # each instance of knn_factory should have its own K
    def __init__(self, k):
        self.K = k

    def train(self, data, labels):
        return knn_classifier((data, labels), self.K)


class tree_factory(abstract_classifier_factory):

    def train(self, data, labels):
        tree_classifier = tree.DecisionTreeClassifier(criterion='entropy')
        tree_classifier.fit(data, labels)
        return tree_classifier


class perceptron_factory(abstract_classifier_factory):

    def train(self, data, labels):
        linear_classifier = linear_model.Perceptron(penalty=None, tol=1e-4, fit_intercept=True)
        linear_classifier.fit(data, labels)
        return linear_classifier


def split_crosscheck_groups(dataset, num_folds):
    true_exmp = dataset[0][dataset[1]]
    false_exmp = [exmp for exmp in dataset[0] if exmp not in true_exmp]
    random.shuffle(true_exmp)
    random.shuffle(false_exmp)
    # divide into separate files
    true_sample_size = int(len(true_exmp)/num_folds)
    false_sample_size = int(len(false_exmp)/num_folds)
    for fold_i in range(num_folds):
        with open('ecg_fold_'+str(fold_i+1)+'.data', 'w') as f:
            for i in range(true_sample_size * fold_i, true_sample_size*(fold_i + 1)):
                f.write(', '.join(map(str, true_exmp[i, :])) + ', 1\n')
            for i in range(false_sample_size*fold_i, false_sample_size*(fold_i+1)):
                f.write(', '.join(map(str, false_exmp[i][:])) + ', 0\n')
            if fold_i == (num_folds - 1):
                true_mod = len(true_exmp) - num_folds * true_sample_size
                false_mod = len(false_exmp) - num_folds * false_sample_size
                f.write(', '.join(map(str, true_exmp[-true_mod, :])) + ', 1\n')
                f.write(', '.join(map(str, false_exmp[-false_mod][:])) + ', 0\n')


def load_k_fold_data(fold_idx):
    lines = [line.strip() for line in open('ecg_fold_' + str(fold_idx) + '.data', 'r')]
    train_i, labels_i = [], []
    for line in lines:
        b = [float(v) for v in line.split(', ')]
        train_i.append(b[:len(b)-1])
        labels_i.append(bool(b[-1]))
    return train_i, labels_i


def evaluate(classifier_factory, k):
    accuracy = 0
    # create training and test sets for the i'th fold
    full_train_data, full_train_tags, _ = load_data()
    full_train_set = [list(l) for l in full_train_data]
    for fold in range(k):
        fold_test_set = load_k_fold_data(fold+1)
        fold_train_set = [smpl for smpl in full_train_set if smpl not in fold_test_set[0]]
        fold_train_tags = [full_train_tags[full_train_set.index(smpl)] for smpl in fold_train_set]
        classifier = classifier_factory.train(fold_train_set, fold_train_tags)

        # compute accuracy and error
        accuracy += classifier.score(fold_test_set[0], fold_test_set[1])

    accuracy /= k
    error = 1 - accuracy
    return accuracy, error


def main():
    train_set, train_tags, test_set = load_data()
    split_crosscheck_groups((train_set, train_tags), 2)

    with open('experiment6.csv', 'w') as f:
        k_vals, acc_list, err_list = [1, 3, 5, 7, 13], [], []
        for k in k_vals:
            knn = knn_factory(k)
            acc, err = evaluate(knn, 2)
            f.write(', '.join([str(k), str(acc), str(err)]) + '\n')
            acc_list.append(acc)
            err_list.append(err_list)

    tf = tree_factory()
    tree_acc, tree_err = evaluate(tf, 2)

    pf = perceptron_factory()
    percp_acc, percp_err = evaluate(pf, 2)

    with open('experiment12.csv', 'w') as f:
        f.write(', '.join([str(1), str(tree_acc), str(tree_err)]) + '\n')
        f.write(', '.join([str(2), str(percp_acc), str(percp_err)]) + '\n')


if __name__ == "__main__":
    main()

