from controlador.dto_cliente import ClienteDTO

def validarNombre (nombre):
    return nombre.strip() !=""

def validarApellido (apellido):
    return apellido.strip() !=""

def validarDocumento(documento):
    return documento.isdigit() and len(documento) >= 7

def validarTipoDocumento(tipoDocumento):
    return tipoDocumento.isdigit() and len(tipoDocumento) == 1

def normalizarTexto(texto):
    return texto.strip().lower()

def validarExistenciaCliente(documento):
    cliente = ClienteDTO().buscarCliente(documento)
    if cliente is not None:
        print("¡Cliente encontrado!")
        print(cliente)
        return cliente
    else:
        print("¡Cliente no encontrado!")
        return None

def confirmarAccion(mensaje="¿Desea continuar? (s/n): "):
    respuesta = input(mensaje).strip().lower()
    while respuesta not in ["s","n"]:
        print("Respuesta inválida. Ingrese 's' para sí o 'n' para no.")
        respuesta = input(mensaje).strip().lower()
    return respuesta == "s"