from abc import ABC, abstractmethod
from auto import Auto

class AutoBuilder(ABC):
    def __init__(self):
        self.auto = Auto()

    @abstractmethod
    def buid_marca(self):
        pass

    @abstractmethod
    def buid_modelo(self):
        pass
    
    @abstractmethod
    def buid_motor(self):
        pass

    @abstractmethod
    def build_puertas(self):    
        pass

    def get_auto(self):        
        auto_final = self.auto
        self.auto = Auto()  # Reiniciar el builder para nuevas construcciones
        return auto_final