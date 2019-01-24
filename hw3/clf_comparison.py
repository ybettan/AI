import numpy as np
from hw3_utils import load_data
from sklearn.model_selection import cross_val_score
from sklearn import svm, tree, neighbors, linear_model, naive_bayes
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.feature_selection import SelectKBest, f_classif, mutual_info_classif, chi2
import csv


def main():
    train_set_full, train_tags, _ = load_data('data/Data.pickle')
    clf_type = ['SVM', 'Tree', 'KNN', 'Perceptron', 'Bayes', 'RF', 'Voting']
    kernel_type = ['Linear', 'Polynomial', 'Gaussian', 'Sigmoid']
    selectors = ['f_classif', 'mutual_info_classif', 'chi2']
    path = 'Classifiers_comparison.csv'

    with open(path, 'w', newline='') as csv_f:
        writer = csv.writer(csv_f)
        writer.writerow(['Selection', 'Features', 'Classifier', 'Param1', 'Param2', 'Param3', 'Param4', 'Param5',
                         'Accuracy', 'Var'])

        for num_of_features in [50, 70, 85, 98, 115, 140, 187]:
            best_svm_score = 0
            for selection_method in selectors:
                if selection_method is selectors[0]:
                    train_set = SelectKBest(f_classif, k=num_of_features).fit_transform(train_set_full, train_tags)
                elif selection_method is selectors[1]:
                    train_set = SelectKBest(mutual_info_classif, k=num_of_features).fit_transform(train_set_full, train_tags)
                else:
                    train_set = SelectKBest(chi2, k=num_of_features).fit_transform(abs(train_set_full), train_tags)

                # Testing SVM classifier
                C_param = np.linspace(0.78, 0.9, 12)
                kernel_param = ['linear', 'poly', 'rbf', 'sigmoid']
                degree_param = np.linspace(7, 11, 5, dtype=int)
                coef0_param = np.linspace(-3, 3, 10)

                # Testing linear kernel
                for penal in C_param:
                    clf = svm.SVC(kernel=kernel_param[0], C=penal, gamma='auto')
                    scores = cross_val_score(clf, train_set, train_tags, cv=3)
                    avg_score = np.mean(scores)
                    var = np.var(scores)
                    writer.writerow([selection_method, num_of_features, clf_type[0], kernel_type[0], str(penal), '', '', '',
                                     avg_score, var])
                    if avg_score > best_svm_score:
                        best_svm_score = avg_score
                        svm_clf = svm.SVC(kernel=kernel_param[0], C=penal, gamma='auto')

                # Testing Polynomial kernel
                for penal in C_param:
                    for deg in degree_param:
                        for C0 in coef0_param:
                            clf = svm.SVC(kernel=kernel_param[1], C=penal, degree=deg, coef0=C0, gamma='auto')
                            scores = cross_val_score(clf, train_set, train_tags, cv=3)
                            avg_score = np.mean(scores)
                            var = np.var(scores)
                            writer.writerow([selection_method, num_of_features, clf_type[0], kernel_type[1], str(penal),
                                             str(deg), str(C0), '', avg_score, var])
                            if avg_score > best_svm_score:
                                best_svm_score = avg_score
                                svm_clf = svm.SVC(kernel=kernel_param[1], C=penal, degree=deg, coef0=C0, gamma='auto')

                # Testing Gaussian kernel
                for penal in C_param:
                    clf = svm.SVC(kernel=kernel_param[2], C=penal, gamma='auto')
                    scores = cross_val_score(clf, train_set, train_tags, cv=3)
                    avg_score = np.mean(scores)
                    var = np.var(scores)
                    writer.writerow([selection_method, num_of_features, clf_type[0], kernel_type[2], str(penal), '', '', '',
                                     avg_score, var])
                    if avg_score > best_svm_score:
                        best_svm_score = avg_score
                        svm_clf = svm.SVC(kernel=kernel_param[2], C=penal, gamma='auto')

                # Testing Sigmoidial kernel
                for penal in C_param:
                    for C0 in coef0_param:
                        clf = svm.SVC(kernel=kernel_param[3], C=penal, coef0=C0, gamma='auto')
                        scores = cross_val_score(clf, train_set, train_tags, cv=3)
                        avg_score = np.mean(scores)
                        var = np.var(scores)
                        writer.writerow([selection_method, num_of_features, clf_type[0], kernel_type[3], str(penal), '',
                                         str(C0), '', avg_score, var])
                        if avg_score > best_svm_score:
                            best_svm_score = avg_score
                            svm_clf = svm.SVC(kernel=kernel_param[3], C=penal, coef0=C0, gamma='auto')

                print("SVM Done")

                # Testing Decision-tree classifier
                critirion_param = ['gini', 'entropy']
                splitter_param = ['best', 'random']
                weight_param = [None, 'balanced']

                best_tree_score = 0
                for crit in critirion_param:
                    for split in splitter_param:
                        for weight in weight_param:
                            clf = tree.DecisionTreeClassifier(criterion=crit, splitter=split, class_weight=weight)
                            scores = cross_val_score(clf, train_set, train_tags, cv=3)
                            avg_score = np.mean(scores)
                            var = np.var(scores)
                            writer.writerow([selection_method, num_of_features, clf_type[1], crit, split, str(weight), '',
                                             '', avg_score, var])
                            if avg_score > best_tree_score:
                                best_tree_score = avg_score
                                tree_clf = tree.DecisionTreeClassifier(criterion=crit, splitter=split, class_weight=weight)

                print("Decision Tree Done")

                # Testing KNN classifier
                neighbors_param = [1, 3, 5, 9]
                weight_param = ['uniform', 'distance']
                dist_metric_param = [1, 2, 3]
                dst = ['manhattan', 'euclidean', 'minkowski']

                best_knn1_score, best_knn3_score = 0, 0
                for n in neighbors_param:
                    for weight in weight_param:
                        for dm in dist_metric_param:
                            clf = neighbors.KNeighborsClassifier(n_neighbors=n, weights=weight, p=dm)
                            scores = cross_val_score(clf, train_set, train_tags, cv=3)
                            avg_score = np.mean(scores)
                            var = np.var(scores)
                            writer.writerow([selection_method, num_of_features, clf_type[2], str(n), weight, '', '',
                                             dst[dm-1], avg_score, var])
                            if n == 1:
                                if avg_score > best_knn1_score:
                                    best_knn1_score = avg_score
                                    knn1_clf = neighbors.KNeighborsClassifier(n_neighbors=n, weights=weight, p=dm)
                            elif n == 3:
                                if avg_score > best_knn3_score:
                                    best_knn3_score = avg_score
                                    knn3_clf = neighbors.KNeighborsClassifier(n_neighbors=n, weights=weight, p=dm)
                print("KNN Done")

                # Testing Perceptron classifier
                penalty_param = [None, 'l1', 'l2']
                alpha_param = np.logspace(-7, -2, 6, dtype=float)
                intercept_param = [True, False]
                tol_param = np.logspace(-7, -2, 6, dtype=float)
                weight_param = [None, 'balanced']

                for penal in penalty_param:
                    for a in alpha_param:
                        for fip in intercept_param:
                            for tl in tol_param:
                                for weight in weight_param:
                                    clf = linear_model.Perceptron(penalty=penal, alpha=a, fit_intercept=fip, tol=tl,
                                                                  class_weight=weight)
                                    scores = cross_val_score(clf, train_set, train_tags, cv=3)
                                    avg_score = np.mean(scores)
                                    var = np.var(scores)
                                    writer.writerow([selection_method, num_of_features, clf_type[3], str(penal), str(a),
                                                     str(fip), str(tl), weight, avg_score, var])
                print("Perceptron Done")

                # Testing Naive Bayes classifier
                NB_type = ['Gaussian', 'Multinomial', 'Bernoulli']
                alpha_param = np.linspace(1e-5, 1, 6, dtype=float)
                prio_param = [True, False]

                clf = naive_bayes.GaussianNB()
                scores = cross_val_score(clf, train_set, train_tags, cv=3)
                avg_score = np.mean(scores)
                var = np.var(scores)
                writer.writerow([selection_method, num_of_features, clf_type[4], NB_type[0], '', '', '', '', avg_score,
                                 var])
                for a in alpha_param:
                    for prio in prio_param:
                        clf = naive_bayes.MultinomialNB(alpha=a, fit_prior=prio)
                        scores = cross_val_score(clf, abs(train_set), train_tags, cv=3)
                        avg_score = np.mean(scores)
                        var = np.var(scores)
                        writer.writerow([selection_method, num_of_features, clf_type[4], NB_type[1], str(a), str(prio), '',
                                         '', avg_score, var])

                for a in alpha_param:
                    for prio in prio_param:
                        clf = naive_bayes.BernoulliNB(alpha=a, fit_prior=prio)
                        scores = cross_val_score(clf, abs(train_set), train_tags, cv=3)
                        avg_score = np.mean(scores)
                        var = np.var(scores)
                        writer.writerow([selection_method, num_of_features, clf_type[4], NB_type[2], str(a), str(prio), '',
                                         '', avg_score, var])
                print("Naive Bayes Done")

                # Testing Random Forest classifier
                n_param = [100, 200, 300]
                critirion_param = ['gini', 'entropy']
                depth_param = [5, 50, None]

                best_rf_score = 0
                for n in n_param:
                    for crit in critirion_param:
                        for d in depth_param:
                            clf = RandomForestClassifier(n_estimators=n, criterion=crit, max_depth=d)
                            scores = cross_val_score(clf, train_set, train_tags, cv=3)
                            avg_score = np.mean(scores)
                            var = np.var(scores)
                            writer.writerow([selection_method, num_of_features, clf_type[5], n, crit, str(d), '', '',
                                             avg_score, var])
                            if avg_score > best_rf_score:
                                best_rf_score = avg_score
                                rf_clf = RandomForestClassifier(n_estimators=n, criterion=crit, max_depth=d)
                print("Random forest Done")

                # Testing Voting classifier
                vote_clf = VotingClassifier(estimators=[('svm', svm_clf), ('tree', tree_clf), ('knn1', knn1_clf),
                                                        ('knn3', knn3_clf), ('rf', rf_clf)], voting='hard')
                scores = cross_val_score(vote_clf, train_set, train_tags, cv=3)
                avg_score = np.mean(scores)
                var = np.var(scores)
                writer.writerow([selection_method, num_of_features, clf_type[6], 'Hard', '', '', '', '', avg_score, var])
                print("Voting Done")

    print("\n ***** ALL Done *****")


if __name__ == "__main__":
    main()

