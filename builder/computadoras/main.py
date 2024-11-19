from computadora_builder import ComputadoraBuilder

def main():
    builder = ComputadoraBuilder()
    builder.set_cpu(4)
    builder.set_memoria(8)
    builder.set_discos(2)
    builder.set_teclado(True)
    builder.set_marca("Dell")

    computadora = builder.build()
    computadora.mostrar_configuracion()

if __name__ == "__main__":    
    main()