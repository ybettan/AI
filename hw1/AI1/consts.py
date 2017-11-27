import numpy as np

class Consts:
    STOCH_INITIAL_TEMPERATURE = 1
    STOCH_TEMPERATURE_DECAY_FUNCTION = 0.95
    STOCH_TOP_SCORES_TO_CONSIDER = 5

    DATA_PATH = "../db/"

    @staticmethod
    def getDataFilePath(fileName):
        return Consts.DATA_PATH + ("/" if Consts.DATA_PATH[-1] != "/" else "") + fileName

    @staticmethod
    def setSeed():
        np.random.seed(236501)

Consts.setSeed()