from controlador.dto_user import UserDTO
# TODO: Terminar las validaciones para terminar de estructurar métodos e impresiones de usuario
# VAMOS QUE FALTA NO TANTO, TIENE QUE QUEDAR WENO MI CHAN
def validarUsername (username):
    return username.strip() !=""

def validarPassword (password):
    return password.strip() !=""
# TODO: Cambiar la lógica
def validarEmail(email):
    return email.isdigit()
# TODO: Crear lógica para buscar la existencia de un usuario
def validarExistenciaUsuario(username):
    print("Hay que construir la lógica de existencia de usuarios")

def normalizarTexto(texto):
    return texto.strip().lower()

def confirmarAccion(mensaje="¿Desea continuar? (s/n): "):
    respuesta = input(mensaje).strip().lower()
    while respuesta not in ["s","n"]:
        print("Respuesta inválida. Ingrese 's' para sí o 'n' para no.")
        respuesta = input(mensaje).strip().lower()
    return respuesta == "s"