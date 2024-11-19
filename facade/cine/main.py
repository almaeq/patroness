from fachada_cine import FachadaCine

def main():
    fachada = FachadaCine()
    fachada.iniciar_pelicula()
    fachada.finalizar_pelicula()

if __name__ == "__main__":
    main()