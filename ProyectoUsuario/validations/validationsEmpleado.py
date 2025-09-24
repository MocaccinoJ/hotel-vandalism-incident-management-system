from controlador.dto_empleado import EmpleadoDTO

def validarNombre(nombre): return nombre.strip() != ""
def validarApellido(apellido): return apellido.strip() != ""
def validarCodigo(codigo): return codigo.strip() != "" and codigo.isdigit()
def validarTipoDocumento(tipoDocumento): return tipoDocumento.isdigit() and len(tipoDocumento) == 1
def validarSueldo(sueldo): return float(sueldo) >= 0 and sueldo.isdigit()

def normalizarTexto(texto): return texto.strip().title()

def validarExistenciaEmpleado(codigo):
    emp = EmpleadoDTO().buscarEmpleado(codigo)
    if emp:
        print("¡Empleado encontrado!")
        print(emp)
        return emp
    else:
        print("¡Empleado no encontrado!")
        return None

def confirmarAccion(mensaje="¿Desea continuar? (s/n): "):
    respuesta = input(mensaje).strip().lower()
    while respuesta not in ["s","n"]:
        print("Respuesta inválida. Ingrese 's' para sí o 'n' para no.")
        respuesta = input(mensaje).strip().lower()
    return respuesta == "s"