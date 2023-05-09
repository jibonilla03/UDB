class Usuario:
    # Metodo constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.session_iniciada = False

# Funcion decoradora
def verificar_sesion(funcion):
    def funcion_interna(*args):
        # print(args[0].nombre)
        # print(args[0].session_iniciada)
        # if args[0].session_iniciada == True:
        if args[0].sesion_iniciada:
            funcion(args[0])

    return funcion_interna

@verificar_sesion
def ver_sitio(usuario):
    print(f"Bienvenido al sistema: {usuario.nombre}")

salvador = Usuario("Salvador") # En esta linea el usuario tiene session_iniciada = False
salvador.session_iniciada = True
ver_sitio(salvador)