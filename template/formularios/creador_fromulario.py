from abc import ABC, abstractmethod

class CreadorFromulario(ABC):
    def crear_formulario(self):
        self.agregar_campos()
        if self.validar_datos():
            self.enviar_fromulario()
        else:
            print("Error: los datos no son válidos")
    @abstractmethod
    def agregar_campos(self):
        pass

    @abstractmethod
    def validar_datos(self):
        pass

    @abstractmethod
    def enviar_fromulario(self):
        pass