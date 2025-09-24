from controlador.dto_habitacion import HabitacionDTO

def validarNumero(numero):
    if numero is None:
        return "El número de habitación no puede estar vacío."
    if not isinstance(numero, int):
        return "El número de habitación debe ser un número entero."
    if numero <= 0:
        return "El número de habitación debe ser mayor que cero."
    return None


def validarPrecio(precio):
    if precio is None:
        return "El precio no puede estar vacío."
    if not isinstance(precio, (int, float)):
        return "El precio debe ser un número."
    if precio <= 0:
        return "El precio debe ser mayor que cero."
    return None


def validarDisponible(disponible):
    if not isinstance(disponible, bool):
        return "El campo 'disponible' debe ser verdadero o falso."
    return None

def normalizarTexto(texto):
    return texto.strip().lower()
# TODO: PROBAR
def validarExistenciaHabitacion(numero):
    habitacion = HabitacionDTO().buscarHabitacion(numero)
    if habitacion is not None:
        print("¡Habitación ya existe!")
        return False
    else:
        print("¡Habitación no encontrado!")
        return True

def confirmarAccion(mensaje="¿Desea continuar? (s/n): "):
    respuesta = input(mensaje).strip().lower()
    while respuesta not in ["s","n"]:
        print("Respuesta inválida. Ingrese 's' para sí o 'n' para no.")
        respuesta = input(mensaje).strip().lower()
    return respuesta == "s"