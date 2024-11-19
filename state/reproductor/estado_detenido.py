from estado_reproductor import EstadoReproductor

class EstadoDetenido(EstadoReproductor):
    def reproducir(self, reproductor):
        print("Iniciando reproducción")
        reproductor.cambiar_estado(reproductor.estado_reproduciendo)

    def pausar(self, reproductor):
        print("No se puede pausar un reproductor en estado DETENIDO")

    def detener(self, reproductor):
        print("La reproducción ya ha sido detenida")