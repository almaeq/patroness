from controlador_impresoras import ControladorImpresoras

def main():
    controlador = ControladorImpresoras()

    # Agregar impresoras
    controlador.agregar_impresora("HP LaserJet 1010")
    controlador.agregar_impresora("Canon PIXMA MG2500")
    controlador.agregar_impresora("Epson EcoTank L3110")

    # Listar impresoras
    controlador.listar_impresoras()

    # Imprimir un documento
    controlador.imprimir("HP LaserJet 1010", "ReporteAnual.pdf")

    # Verificar estado de una impresora
    controlador.verificar_estado("HP LaserJet 1010")
    controlador.verificar_estado("Canon PIXMA MG2500")

    # Intentar imprimir en una impresora ocupada
    controlador.imprimir("HP LaserJet 1010", "DocumentoUrgente.docx")

    # Verificar estado de una impresora no registrada
    controlador.verificar_estado("Impresora No Existente")

if __name__ == "__main__":
    main()
