from fabrica_italiana import FabricaItaliana
from fabrica_mexicana import FabricaMexicana

def main():
    fabrica_italiana = FabricaItaliana()
    fabrica_mexicana = FabricaMexicana()

    print("Menu de Italia")
    comida = fabrica_italiana.crear_comida()
    comida.preparar()
    comida.servir()

    bebida = fabrica_italiana.crear_bebida()
    bebida.preparar()
    bebida.servir()

    print("Menu de México")
    comida = fabrica_mexicana.crear_comida()
    comida.preparar()
    comida.servir()

    bebida = fabrica_mexicana.crear_bebida()    
    bebida.preparar()
    bebida.servir()

if __name__ == "__main__":
    main()