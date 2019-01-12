from matplotlib import pyplot as plt


def plot_knn_accuracy(k_vals, acc_list):
    plt.figure()
    plt.stem(k_vals, acc_list)
    plt.title("Accuracy as a factor of K - KNN Classifier")
    plt.ylim((0.9, 1))
    plt.xticks(k_vals, k_vals)
    plt.grid()
    plt.show()
