import threading
import time

class ControladorImpresoras:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(ControladorImpresoras, cls).__new__(cls, *args, **kwargs)
                    cls._instance.impresoras = {}
                    cls._instance.impresora_actual = None
        return cls._instance

    def agregar_impresora(self, nombre):
        if nombre not in self.impresoras:
            self.impresoras[nombre] = 'Disponible'
            print(f"Impresora '{nombre}' agregada exitosamente.")
        else:
            print(f"La impresora '{nombre}' ya existe.")

    def listar_impresoras(self):
        print("Lista de impresoras:")
        for nombre, estado in self.impresoras.items():
            print(f"- {nombre}: {estado}")

    def imprimir(self, impresora, documento):
        if impresora not in self.impresoras:
            print(f"Error: La impresora '{impresora}' no está registrada.")
            return

        if self.impresoras[impresora] == 'Imprimiendo':
            print(f"Error: La impresora '{impresora}' está ocupada.")
            return

        # Simular el proceso de impresión
        with self._lock:
            print(f"Iniciando la impresión en la impresora '{impresora}'...")
            self.impresoras[impresora] = 'Imprimiendo'
            self.impresora_actual = impresora
            time.sleep(2)  # Simula el tiempo de impresión
            print(f"Documento '{documento}' impreso en la impresora '{impresora}'.")
            self.impresoras[impresora] = 'Disponible'
            self.impresora_actual = None

    def verificar_estado(self, impresora):
        if impresora in self.impresoras:
            print(f"Estado de la impresora '{impresora}': {self.impresoras[impresora]}")
        else:
            print(f"Error: La impresora '{impresora}' no está registrada.")
