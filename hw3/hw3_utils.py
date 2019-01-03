data_path = r'data/Data.pickle'
import pickle
import numpy as np




def load_data(path=r'data/Data.pickle'):
    '''
    return the dataset that will be used in HW 3
    prameters:
    :param path: the path of the csv data file (default value is data/ecg_examples.data)

    :returns: a tuple train_features, train_labels ,test_features
    features - a numpy matrix where  the ith raw is the feature vector of patient i.
    '''
    with open(path,'rb') as f:
        train_features, train_labels, test_features = pickle.load(f)
    return train_features, train_labels ,test_features



def write_prediction(pred, path='results.data'):
    '''
    write the prediction of the test set into a file for submission
    prameters:
    :param pred: - a list of result the ith entry represent the ith subject (as integers of 1 or 0, where 1 is a healthy patient and 0 otherwise)
    :param path: - the path of the csv data file will be saved to(default value is res.data)
    :return: None
    '''
    output = []
    for l in pred:
        output.append(l)
    with open(path, 'w') as f:
        f.write(', '.join([str(x) for x in output]) + '\n')


class abstract_classifier_factory:
    '''
    an abstruct class for classifier factory
    '''
    def train(self, data, labels):
        '''
        train a classifier
        :param data: a list of lists that represents the features that the classifier will be trained with
        :param labels: a list that represents  the labels that the classifier will be trained with
        :return: abstruct_classifier object
        '''
        raise Exception('Not implemented')


class abstract_classifier:
    '''
        an abstruct class for classifier
    '''

    def classify(self, features):
        '''
        classify a new set of features
        :param features: the list of feature to classify
        :return: a tagging of the given features (1 or 0)
        '''
        raise Exception('Not implemented')


