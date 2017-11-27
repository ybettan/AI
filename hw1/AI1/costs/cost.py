import abc

class Cost(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def compute(self, source, target):
        raise NotImplementedError

