def sfs(x, y, k, clf, score):
    """
    :param x: feature set to be trained using clf. list of lists.
    :param y: labels corresponding to x. list.
    :param k: number of features to select. int
    :param clf: classifier to be trained on the feature subset.
    :param score: utility function for the algorithm, that receives clf, feature subset and labeles, returns a score. 
    :return: list of chosen feature indexes
    """

    v_k = []
    b = 0

    while b <= k:
        score_rate = -1
        v = -1
        # check all features
        for v_i in range(len(x[0])):
            # check feature was not selected
            if v_i not in v_k:
                # add feature to list
                v_k.append(v_i)
                # remove unselected features from data
                x_i = [[row[i] for i in v_k] for row in x]
                # get selection score
                score_i = score(clf, x_i, y)
                # update best score
                if score_rate < score_i:
                    score_rate = score_i
                    v = v_i
                # remove feature from list
                v_k.pop()
        # add best feature
        v_k.append(v)
        b += 1
    return v_k
