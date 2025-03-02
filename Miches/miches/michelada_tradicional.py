from abc import ABC, abstractmethod

class MicheladaTradicional(ABC):
    def __init__(self, miche):
        self.miche= miche

    @abstractmethod
    def costoExtra(self):
        pass

    @abstractmethod
    def preparar(self):
        pass
