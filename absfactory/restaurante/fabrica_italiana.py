from fabrica_menu import FabricaMenu
from comida import Pasta
from bebida import Cerveza

class FabricaItaliana(FabricaMenu):
    def crear_comida(self):
        return Pasta()

    def crear_bebida(self):
        return Cerveza()