from camion_factory import CamionFactory
from avion_factory import AvionFactory
from barco_factory import BarcoFactory

def simular_entrega(factory):
    transporte = factory.crear()
    transporte.entregar()

if __name__ == "__main__":
    camion = CamionFactory(tipo=" de pasajeros")
    avion = AvionFactory()
    barco = BarcoFactory()

    simular_entrega(camion)
    simular_entrega(avion)    
    simular_entrega(barco)