from fabrica_menu import FabricaMenu
from comida import Taco
from bebida import Tequia

class FabricaMexicana(FabricaMenu):
    def crear_comida(self):
        return Taco()

    def crear_bebida(self):    
        return Tequia()