import abc

class Heuristic(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def estimate(self, problem, state):
        raise NotImplementedError
