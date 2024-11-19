from abc import ABC, abstractmethod

class Comida(ABC):
    @abstractmethod
    def preparar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Pasta(Comida):
    def preparar(self):
        print("Preparando la pasta")

    def servir(self):
        print("Serviendo la pasta")

class Taco(Comida):
    def preparar(self):
        print("Preparando el taco")

    def servir(self):    
        print("Serviendo el taco")