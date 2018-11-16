import numpy as np
import os


class Consts:
    STOCH_INITIAL_TEMPERATURE = 1
    STOCH_TEMPERATURE_DECAY_FUNCTION = 0.95
    STOCH_TOP_SCORES_TO_CONSIDER = 5

    PROJECT_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')
    FRAMEWORK_PATH = os.path.join(PROJECT_PATH, 'framework/')
    DATA_PATH = os.path.join(FRAMEWORK_PATH, 'db/')

    @staticmethod
    def get_data_file_path(file_name: str):
        return os.path.join(Consts.DATA_PATH, file_name)

    @staticmethod
    def set_seed():
        np.random.seed(236501)


Consts.set_seed()
