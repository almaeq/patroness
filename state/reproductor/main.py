from reproductor import Reproductor

def main():
    reproductor = Reproductor()
    reproductor.reproducir()
    reproductor.pausar()
    reproductor.detener()
    reproductor.avanzar_cancion()
    reproductor.retroceder_cancion()

if __name__ == "__main__":
    main()