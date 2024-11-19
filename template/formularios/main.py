from formulario_contacto import FormularioContacto
from formulario_reg import FormularioReg

def main():
    formulario_contacto = FormularioContacto()
    formulario_reg = FormularioReg()

    print("Creando formulario de contacto:")
    formulario_contacto.crear_formulario()
    print("Creando formulario de registro:")
    formulario_reg.crear_formulario()

if __name__ == "__main__":
    main()