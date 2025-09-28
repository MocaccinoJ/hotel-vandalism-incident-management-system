import re
from controlador.dto_user import UserDTO
from seguridad.strategyEncryptor import encriptarPassword, verificarPassword

# TODO: Terminar las validaciones para terminar de estructurar métodos e impresiones de usuario
# VAMOS QUE FALTA NO TANTO, TIENE QUE QUEDAR WENO MI CHAN
def validarUsername (username):
    return username.strip() !=""

def validateEncriptaPassword (password):
    while True:
        password = password.strip()
        if password:
            return encriptarPassword(password)
        else:
            print("La contraseña no puede estar vacía. Intente nuevamente.")
# TODO:Implementar bien el modulo de validacion

# TODO: Cambiar la lógica
def validarEmail(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None

def validarExistenciaUsuarioPorUsername(username):
    usuario = UserDTO().buscarUsuarioPorUsername(username)
    if usuario is not None:
        print("!Usuario existe!")
        usuarioEncontrado = usuario
        return usuarioEncontrado
    else:
        return None

def validarExistenciaUsuarioPorEmail(email):
    usuario = UserDTO().buscarUsuarioPorEmail(email)
    if usuario is not None:
        print("!Email existe!")
        usuarioEncontrado = usuario
        return usuarioEncontrado
    else:
        print("¡Email no está siendo utilizado!")
        return None


def normalizarTexto(texto):
    return texto.strip().lower()

def confirmarAccion(mensaje="¿Desea continuar? (s/n): "):
    respuesta = input(mensaje).strip().lower()
    while respuesta not in ["s","n"]:
        print("Respuesta inválida. Ingrese 's' para sí o 'n' para no.")
        respuesta = input(mensaje).strip().lower()
    return respuesta == "s"