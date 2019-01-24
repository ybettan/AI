import numpy as np
from hw3_utils import load_data
from matplotlib import pyplot as plt


def main():
    # Load the data
    train_set, train_tags, test_set = load_data('data/Data.pickle')

    # Range of the data
    print("max(train_set) = " + '{:.4f}'.format(np.max(train_set)))
    print("min(train_set) = " + '{:.4f}'.format(np.min(train_set)))
    print("mean(train_set) = " + '{:.4f}'.format(np.mean(train_set)))
    print("var(train_set) = " + '{:.4f}'.format(np.var(train_set)))
    print("")
    print("max(test_set) = " + '{:.4f}'.format(np.max(test_set)))
    print("min(test_set) = " + '{:.4f}'.format(np.min(test_set)))
    print("mean(test_set) = " + '{:.4f}'.format(np.mean(test_set)))
    print("var(test_set) = " + '{:.4f}'.format(np.var(test_set)))

    plt.figure(figsize=(10, 6))
    plt.subplot(211)
    plt.title('Dynamic range vs feature (Train set)')
    plt.plot(range(train_set.shape[1]), np.min(train_set, axis=0), 'r')
    plt.plot(range(train_set.shape[1]), np.max(train_set, axis=0), 'g')
    plt.plot(range(train_set.shape[1]), np.mean(train_set, axis=0), 'b')
    plt.plot(range(train_set.shape[1]), np.mean(train_set, axis=0) + 2*np.var(train_set, axis=0), linestyle=':', color='k')
    plt.plot(range(train_set.shape[1]), np.mean(train_set, axis=0) - 2*np.var(train_set, axis=0), linestyle=':', color='k')
    plt.legend(['max', 'min', 'avg', '+2 Sigma', '-2 Sigma'])
    plt.grid()
    plt.subplot(212)
    plt.title('Dynamic range vs feature (Test set)')
    plt.plot(range(test_set.shape[1]), np.min(test_set, axis=0), 'r')
    plt.plot(range(test_set.shape[1]), np.max(test_set, axis=0), 'g')
    plt.plot(range(test_set.shape[1]), np.mean(test_set, axis=0), 'b')
    plt.plot(range(test_set.shape[1]), np.mean(test_set, axis=0) + 2*np.var(test_set, axis=0), linestyle=':', color='k')
    plt.plot(range(test_set.shape[1]), np.mean(test_set, axis=0) - 2*np.var(test_set, axis=0), linestyle=':', color='k')
    plt.legend(['max', 'min', 'avg', '+2 Sigma', '-2 Sigma'])
    plt.grid()
    plt.show()

    # Divide the examples to true/false
    good = train_set[train_tags]
    bad = np.asarray([exmp for exmp in train_set if exmp not in train_set[train_tags]])

    plt.figure(figsize=(10, 6))
    plt.subplot(211)
    plt.title('Dynamic range vs feature (True examples)')
    plt.plot(range(good.shape[1]), np.min(good, axis=0), 'r')
    plt.plot(range(good.shape[1]), np.max(good, axis=0), 'g')
    plt.plot(range(good.shape[1]), np.mean(good, axis=0), 'b')
    plt.plot(range(good.shape[1]), np.mean(good, axis=0) + 2*np.var(good, axis=0), linestyle=':', color='k')
    plt.plot(range(good.shape[1]), np.mean(good, axis=0) - 2*np.var(good, axis=0), linestyle=':', color='k')
    plt.legend(['max', 'min', 'avg', '+2 Sigma', '-2 Sigma'])
    plt.grid()
    plt.subplot(212)
    plt.title('Dynamic range vs feature (False examples)')
    plt.plot(range(bad.shape[1]), np.min(bad, axis=0), 'r')
    plt.plot(range(bad.shape[1]), np.max(bad, axis=0), 'g')
    plt.plot(range(bad.shape[1]), np.mean(bad, axis=0), 'b')
    plt.plot(range(bad.shape[1]), np.mean(bad, axis=0) + 2*np.var(bad, axis=0), linestyle=':', color='k')
    plt.plot(range(bad.shape[1]), np.mean(bad, axis=0) - 2*np.var(bad, axis=0), linestyle=':', color='k')
    plt.legend(['max', 'min', 'avg', '+2 Sigma', '-2 Sigma'])
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()

