"""TODO: Cambiar la estructura de la importaciòn"""
from controlador.dto_user import UserDTO
from validations.validationsUsers import confirmarAccion, normalizarTexto, validarUsername, validarEmail
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
    username = normalizarTexto(input("Ingrese nombre de usuario a incorporar: "))
    while not validarUsername: username = normalizarTexto(input("Usuario inválido. Intente nuevamente: "))

    email = normalizarTexto(input("Ingrese Email a incorporar: "))
    while not validarEmail: email = normalizarTexto(input("Error. Intente nuevamente: "))

    password = input("Ingrese su contraseña: ")


    #trae un objeto usuario
    resu = UserDTO().buscarUsuario(username)
    if resu is not None:
        """desplegamos el usuario, por medio de __str()__
        de la clase Usuario, que se encuentra en el 
        paquete modelo"""
        print("Datos existentes--> ", resu)
    else:
        #Ingresamos el nuevo usuario
        email = input("Ingrese email : ") #crear función para validar email
        clave = input("Ingrese clave : ") #crear funci+on para valida clave
        print(UserDTO().agregarUsuario(username, email,clave))

def validateFindUser():
    username = input("Ingrese el nombre de usuario a buscar : ")
    if username == "":
        """Se puede mejorar el mensaje"""
        print("Nombre de usuario incorrecto")
        return validateFindUser()
    else:
        resu = UserDTO().buscarUsuario(username)
        if resu is not None:
            print(f"Resultado : {resu}")
        else:
            print("Usuario No encontrado")
def validaDelUser():
    username = input("Ingrese el nombre de usuario a eliminar : ")
    if len(username) == 0:
        print("Debe ingresar un nombre de usuario")
        return validaDelUser()
    #trae devuelta un objeto User
    resu = UserDTO().buscarUsuario(username)
    if resu is not None:
        print("Datos --> ", resu)
        respuesta = input("Esta seguro de la eliminación [s/n]: ") #crear función para validar respuesta
        if respuesta == "s":
            print("Ay: ",UserDTO().eliminarUsuario(resu.getUsername()))

    else:
        print("Usuario No encontrado")
def validateUpdateUser():
    username = input("Ingrese el nombre de usuario a modificar : ")
    if len(username) == 0:
        print("Debe ingresar un nombre de usuario")
        return validateUpdateUser()
    #trae devuelta un objeto User
    resu = UserDTO().buscarUsuario(username)
    if resu is not None:
        print("Datos --> ", resu)
        email = input("Ingrese email : ") #crear función para validar email
        clave = input("Ingrese clave : ") #crear funci+on para valida clave
        #muestra el objeto string devuelto
        print(UserDTO().actualizarUsuario(username, email,clave))

    else:
        print("Usuario No encontrado")
        

def validarLogin():
    username = input("Ingrese nombre de usuario : ")
    clave = input("Ingrese contraseña : ")
    resultado = UserDTO().validarLogin(username, clave)
    print("RESULTADO: validarLogin() | ",resultado)
    return resultado