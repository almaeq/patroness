class Computadora:
    def __init__(self):
        self.cpu = 0
        self.memoria = 0
        self.discos = 0
        self.teclado = False
        self.marca = "Unknown"

    def mostrar_configuracion(self):
        configuracion = (
            f"- CPU: {self.cpu}\n"
            f"- Memoria: {self.memoria}\n"
            f"- Discos: {self.discos}\n"
            f"- Teclado: {'Sí' if self.teclado else 'No'}\n"
            f"- Marca: {self.marca}\n"
        )
        print(configuracion)