from abc import *

class AbstractTrace(metaclass=ABCMeta):
    @abstractmethod
    def testTrace(self):
        pass
