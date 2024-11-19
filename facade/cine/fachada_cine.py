from television import Television
from reproductorDVD import ReproductorDVD
from sistema_sonido import SistemaSonido

class FachadaCine:
    def __init__(self):
        self.television = Television()
        self.reproductorDVD = ReproductorDVD()
        self.sistemaSonido = SistemaSonido()

    def iniciar_pelicula(self):
        print("Preparando la película...")
        self.television.encender()
        self.reproductorDVD.encender()
        self.sistemaSonido.encender()
        self. sistemaSonido.volumen(10)
        print("Iniciando la película...")
        self.reproductorDVD.reproducir()
        print("Pelicula iniciada.")

    def finalizar_pelicula(self):
        print("Apagando sistema de cine...")
        self.reproductorDVD.detener()
        self.reproductorDVD.apagar()
        self.sistemaSonido.apagar()
        self.television.apagar()
        print("Cine finalizado.")