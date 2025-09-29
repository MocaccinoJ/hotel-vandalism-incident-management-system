"""TODO: Cambiar la estructura de la importaciòn"""
from controlador.dto_user import UserDTO
from validations.validationsUsers import confirmarAccion, normalizarTexto, validarUsername, validarEmail, validateEncriptaPassword, validarExistenciaUsuarioPorUsername, validarExistenciaUsuarioPorEmail
from seguridad import encryptor

# from acciones.accionesCliente import listarClientes, agregarCliente, actualizarCliente, eliminarCliente


def listarUsuarios():
    usuariosEncontrados = UserDTO().listarUsuarios()
    if len(usuariosEncontrados) > 0:
        print("-- Lista de Usuarios --")
        for usuario in usuariosEncontrados:
            print(usuario)
            print(" ")
    else:
        print("¡No hay resultados!")

    print("\nPresione ENTER para volver al menú...")
    input()

def agregarUsuario():
    username = normalizarTexto(input("Ingrese username a incorporar: "))
    while not validarUsername(username) or validarExistenciaUsuarioPorUsername(username) is not None:
        print("Usuario inválido. Intente nuevamente") 
        username = normalizarTexto(input("Ingrese username a incorporar: "))

    email = normalizarTexto(input("Ingrese email a incorporar: "))
    while not validarEmail(email) or not validarExistenciaUsuarioPorEmail(email) is not None: 
        print("Email inválido. Intente nuevamente")
        email = normalizarTexto(input("Ingrese email de usuario a incorporar: "))

    password = input("Ingrese la contraseaña deseada: ")
    password = validateEncriptaPassword(password)
    
    usuarioCreado = UserDTO().agregarUsuario(username, email, password)

    if usuarioCreado:
        print(" ")
        print("¡Usuario creado correctamente!")
        print(" ")
    if not usuarioCreado:
        print("¡Usuario no pudo ser agregado!")

def buscarUsuario():
    username = normalizarTexto(input("Ingrese el username a buscar: "))
    if not validarUsername(username):
        print("username inválido.")
        return
    usuario = UserDTO().buscarUsuarioPorUsername(username)
    if usuario is not None:
        print("¡Usuario encontrado!:")
        print(usuario)
    else:
        print("¡Usuario no encontrado!.")

def editarUsuario():
    try:
        username = normalizarTexto(input("Ingrese username del usuario a modificar: "))
        while not validarUsername(username):
            print("Usename inválido. Intente nuevamente.")
            username = normalizarTexto(input("Ingrese el username del usuario a modificar: "))
        # usuario = UserDTO().buscarUsuarioPorUsername(username)

        usuario = validarExistenciaUsuarioPorUsername(username)

        if usuario is None:
            print("Usuario no encontrado")
            return #Salir si no existe
        
        # Datos actuales del usuario
        print(usuario)
        originalUsername =usuario.getUsername()
        username = usuario.getUsername()
        mensaje = "¿Desea modificar el username del usuario? (s/n): "
        if confirmarAccion(mensaje):
            nuevoUsername = normalizarTexto(input("Ingrese el nuevo username: "))
            while not validarUsername(nuevoUsername):
                print("Username inválido. Intente nuevamente.")
                nuevoUsername = normalizarTexto(input("Ingrese el nuevo username: "))
            username = nuevoUsername
        
        email = usuario.getEmail()
        mensaje = "¿Desea modificar el email del usuario? (s/n): "
        if confirmarAccion(mensaje):
            nuevoEmail = normalizarTexto(input("Ingrese el nuevo email: "))
            while not validarEmail(nuevoEmail) or validarExistenciaUsuarioPorEmail(nuevoEmail) is not None: 
                print("Email inválido. Intente nuevamente")
                nuevoEmail = normalizarTexto(input("Ingrese email de usuario a incorporar: "))
            email = nuevoEmail

        
        password = usuario.getPassword()
        mensaje = "¿Desea modificar la contraseña? (s/n): "
        if confirmarAccion(mensaje):
            nuevaPassword = input("Ingrese la nueva contraseña del usuario: ")
            password = validateEncriptaPassword(nuevaPassword)
        
        usuarioActualizado = UserDTO().actualizarUsuario(originalUsername, username, email, password)
        if usuarioActualizado is not None:
            print("Usuario actualizado correctamente.")

    except Exception as ex:
        print("¡Ha ocurrido un error!", ex)

def eliminarUsuario():
    try:
        username = normalizarTexto(input("¡Ingrese el username del usuario que desea eliminar!: "))
        while not validarUsername(username):
            print("¡Username inválido!")
            username = normalizarTexto(input("¡Ingrese el username del usuario que desea eliminar!: "))
        usuario = validarExistenciaUsuarioPorUsername(username)
        if usuario is None:
            return #Salir si no existe
        mensaje="¿Está seguro que desea eliminar este usuario? (s/n): "
        if confirmarAccion(mensaje):
            usuarioEliminado = UserDTO().eliminarUsuario(username)
    except Exception as ex:
        print("¡Ha ocurrido un error! ", ex)

def validarLogin():
    username = input("Ingrese nombre de usuario : ")
    clave = input("Ingrese contraseña : ")
    
    resultado = UserDTO().validarLogin(username, clave)
    if resultado is not None:
        print(f"¡Login exitoso! Bienvenido {resultado.getUsername()}")
    else:
        print("Usuario o contraseña incorrecta")
    return resultado