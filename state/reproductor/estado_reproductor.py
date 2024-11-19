from abc import ABC, abstractmethod

class EstadoReproductor(ABC):
    @abstractmethod
    def reproducir(self,reproductor):
        pass
    
    @abstractmethod
    def pausar(self, reproductor):
        pass

    @abstractmethod
    def detener(self,reproductor):
        pass    
