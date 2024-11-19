from abc import ABC, abstractmethod

class Bebida(ABC):
    @abstractmethod
    def preparar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Tequia(Bebida):
    def preparar(self):
        print("Preparando la tequila")

    def servir(self):
        print("Serviendo la tequila")

class Cerveza(Bebida):
    def preparar(self):
        print("Preparando la cerveza")

    def servir(self):
        print("Serviendo la cerveza")