from estado_reproductor import EstadoReproductor

class EstadoReproduciendo(EstadoReproductor):
    def reproducir(self, reproductor):
        print("Reproduciendo")

    def pausar(self, reproductor):
        print("Pausando")

    def detener(self, reproductor):    
        print("Deteniendo")