from estado_reproduciendo import EstadoReproduciendo
from estado_pausado import EstadoPausado
from estado_detenido import EstadoDetenido

class Reproductor:
    def __init__(self):
        self.estado_reproductor = EstadoReproduciendo()
        self.estado_detenido = EstadoDetenido()
        self.estado_pausado = EstadoPausado()

    def cambiar_estado(self, nuevo_estado):
        self.estado_reproductor = nuevo_estado

    def reproducir(self):
        self.estado_reproductor.reproducir(self)

    def pausar(self):
        self.estado_reproductor.pausar(self)

    def detener(self):
        self.estado_reproductor.detener(self)

    def avanzar_cancion(self):
        print("Avanzando canción")
        if isinstance(self.estado_reproductor, EstadoReproduciendo):
            print("Reproduciendo siguiente canción")

    def retroceder_cancion(self):
        print("Retrocediendo canción")
        if isinstance(self.estado_reproductor, EstadoReproduciendo):
            print("Reproduciendo canción anterior")