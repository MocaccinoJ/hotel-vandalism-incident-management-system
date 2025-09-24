from controlador.dto_cliente import ClienteDTO
from validations.validationsCliente import validarNombre, validarDocumento, validarApellido, validarTipoDocumento, normalizarTexto, validarExistenciaCliente, confirmarAccion
# from modelo.cliente import Cliente

def listarClientes():
    clientesEncontrados = ClienteDTO().listarClientes()
    if len(clientesEncontrados) > 0:
        for cliente in clientesEncontrados:
            print(cliente)
        else:
            print("¡No hay resultados!")
def agregarCliente():
    #TODO: Agregar la validación de ingreso de datos y existencia de cliente
    try:
        nombre = normalizarTexto(input("Ingrese el nombre del cliente: "))
        while not validarNombre(nombre):
            print("Nombre inválido. Intente nuevamente")
            nombre = normalizarTexto(input("Ingrese el nombre del cliente: "))

        apellido = normalizarTexto(input("Ingrese el apellido del cliente: "))
        while not validarApellido(apellido):
            print("Apellido inválido. Intente nuevamente")
            apellido = normalizarTexto(input("Ingrese el apellido del cliente: "))

        direccion = normalizarTexto(input("Ingrese la dirección del cliente: "))
        
        #todo: crear validación para documento del cliente API PKG
        documento = normalizarTexto(input("Ingrese el número de documento del cliente: "))
        while not validarDocumento(documento): 
            print("Ingrese un documento válido de 7 caracteres")
            documento = normalizarTexto(input("Ingrese el número de documento del cliente: "))

        tipoDocumento = normalizarTexto(input("Ingrese el tipo de documento del cliente: "))#todo: Función para validar la existencia API PKG
        while not validarTipoDocumento(tipoDocumento):
            print("¡Ingrese un tipo de documento válido de 1 dígito!")
            tipoDocumento = normalizarTexto(input("Ingrese el tipo de documento del cliente: "))

        clienteCreado = ClienteDTO().agregarCliente(nombre, apellido, direccion, documento, tipoDocumento)
        if clienteCreado:
            print(" ")
            print("!Cliente creado correctamente!")
            print(" ")
        if not clienteCreado:
            print("¡No se pudo agregar el cliente!")
        # TODO: Mostrar mensaje de confirmación de agregado a la base de datos
    except Exception as ex:
        print("¡Ha ocurrido un error!", ex)

def actualizarCliente():
    try:
        documento = normalizarTexto(input("Ingrese el número de documento del cliente a modificar: "))
        while not validarDocumento(documento):
            print("Documento inválido. Intente nuevamente.")
            documento = normalizarTexto(input("Ingrese el número de documento del cliente a modificar: ")) 
        cliente = ClienteDTO().buscarCliente(documento)

        cliente = validarExistenciaCliente(documento)
        if cliente is None:
            return  # Salir si no existe
        
        # Datos actuales del cliente
        print(cliente)

        # Actualización condicional de cada campo
        nombre = cliente.getNombre()
        mensaje = "¿Desea modificar el nombre el nombre? (s/n): "
        if confirmarAccion(mensaje):
            nuevoNombre = normalizarTexto(input("Ingrese el nuevo nombre: "))
            while not validarNombre(nuevoNombre):
                print("Nombre inválido. Intente nuevamente.")
                nuevoNombre = normalizarTexto(input("Ingrese el nuevo nombre: "))
            nombre = nuevoNombre
        
        apellido = cliente.getApellido()
        if confirmarAccion("¿Desea modificar el apellido? (s/n): "):
            nuevoApellido = normalizarTexto(input("Ingrese el nuevo apellido: "))
            while not validarApellido(nuevoApellido):
                print("Apellido inválido. Intente nuevamente.")
                nuevoApellido = normalizarTexto(input("Ingrese el nuevo apellido: "))
            apellido = nuevoApellido
        
        direccion = cliente.getDireccion()
        if confirmarAccion("¿Desea modificar la dirección? (s/n): "):
            direccion = normalizarTexto(input("Ingrese la nueva dirección: "))
        
        tipoDocumento = cliente.getTipoDocumento()
        if confirmarAccion("¿Desea modificar el tipo de documento? (s/n): "):
            nuevoTipoDocumento = normalizarTexto(input("Ingrese el nuevo tipo de documento: "))
            while not validarTipoDocumento(nuevoTipoDocumento):
                print("Tipo de documento inválido. Intente nuevamente.")
                nuevoTipoDocumento = normalizarTexto(input("Ingrese el nuevo tipo de documento: "))
            tipoDocumento = nuevoTipoDocumento
        
        #Enviar información al DTO
        print("HOLA SI ENVIAR INFORMACION AL DTO")
        clienteActualizado = ClienteDTO().actualizarCliente(nombre, apellido, direccion, documento, tipoDocumento)
        if clienteActualizado:
            print("Cliente actualizado correctamente.")

    except Exception as ex:
        print("!Ha ocurrido un error! ", ex)
    
    #Eliminar Cliente
def eliminarCliente():
    try:
        documento = normalizarTexto(input("Ingrese el número de documento del cliente que desea eliminar: "))
        while not validarDocumento(documento):
            # TODO: Podría implementar un módulo de alertas automáticas.
            print("Documento inválido. Intente nuevamente.")
            documento = normalizarTexto(input("Ingrese el número de documento del cliente que desea eliminar: "))
        cliente = ClienteDTO().buscarCliente(documento)

        cliente = validarExistenciaCliente(documento)
        if cliente is None:
            return # Salir si no existe (TODO:Cuestionable)
        
        mensaje="¿Está seguro que desea eliminar este cliente? (s/n): "
        if confirmarAccion(mensaje):
            clienteEliminado = ClienteDTO().eliminarCliente(documento)

    except Exception as ex:
        print("¡Ha ocurrido un error! ", ex)
    # TODO: Buscar un cliente