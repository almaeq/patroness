from estado_reproductor import EstadoReproductor

class EstadoPausado(EstadoReproductor):
    def reproducir(self, reproductor):
        print("Reanudando reproducción")
        reproductor.cambiar_estado(reproductor.estado_reproductor)

    def pausar(self, reproductor):
        print("Ya esta pausado")

    def detener(self, reproductor):
        print("Deteniendo reproducción")
        reproductor.cambiar_estado(reproductor.estado_detenido)