from abc import ABC, abstractmethod

class TransporteFactory(ABC):
    @abstractmethod
    def crear(self):
        pass