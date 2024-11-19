from creador_fromulario import CreadorFromulario

class FormularioReg(CreadorFromulario):
    def agregar_campos(self):
        print("Agregando campos al formulario")

    def validar_datos(self):
        print("Validando datos del formulario")
        return True

    def enviar_fromulario(self):
        print("Enviando formulario de registro")