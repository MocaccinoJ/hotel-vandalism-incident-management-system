from validations1 import listAll, validateAddUser, validaDelUser, validateUpdateUser, validateFindUser
from acciones.accionesCliente import listarClientes, agregarCliente, actualizarCliente, eliminarCliente
from acciones.accionesHabitacion import listarHabitaciones, agregarHabitacion, actualizarHabitacion, eliminarHabitacion

def inicial():
    while True:
        opc=menu()
        if opc == 1:
            listAll()
        elif opc == 2:
            validateAddUser()
        elif opc == 3:
            validaDelUser()
        elif opc == 4:
            validateUpdateUser()
        elif opc == 5:
            validateFindUser()
        elif opc == 101:
            listarClientes()
        elif opc == 102:
            agregarCliente()
        elif opc == 103:
            actualizarCliente()
        elif opc == 104:
            eliminarCliente()
        elif opc == 201:
            listarHabitaciones()
        elif opc == 202:
            agregarHabitacion()
        elif opc == 203:
            actualizarHabitacion()
        elif opc == 204:
            eliminarHabitacion()
        elif opc == 50:
            break


def menu():
    print("1. Listar Usuarios")
    print("2. Agregar Usuario")
    print("3. Eliminar Usuario")
    print("4. Actualizar Usuario")
    print("5. Buscar Usuario")
    
    # Menú para clientes
    print("6. Opciones de Clientes")
    # TODO: Menú para empleados
    # Menú para Habitaciones
    # PREGUNTA: ¿Es a través de empleados que se debería hacer la modificación?
    print("7. Opciones de Habitación")

    print("50. Salir")
    opc = int( input("Ingrese una opción : "))
    
    if(opc==6): opc=menuClientes()
    if(opc==7): opc=menuHabitacion()

    print("Valor de la opc sistema clientes: ", opc)
    return opc

# Las opciones del menú de clientes serán con valores 100
def menuClientes():
    # TODO: Hacer validaciones de ingreso de datos

    print("   ")
    print("---- Bienvenido al Menú de Clientes ----")
    print("1. Listar Clientes")
    print("2. Agregar Cliente")
    print("3. Editar Cliente")
    print("4. Eliminar Cliente")

    totalOpciones = 4;
    opc = int(input("Ingrese una Opción: "))
    print("menu.menuClientes() opc:", opc)
    opc_usuario = validarOpcion(opc, totalOpciones)

    if opc_usuario == 1: opc=101
    if opc_usuario == 2: opc=102
    if opc_usuario == 3: opc=103
    if opc_usuario == 4: opc=104
    
    return opc

def menuHabitacion():
    print("   ")
    print("---- Bienvenido al Menú de Habitación ----")
    print("1. Listar Habitaciones")
    print("2. Agregar Habitación")
    print("3. Editar Habitación")
    print("4. Eliminar Habitación")

    totalOpciones = 4;
    opc = int(input("Ingrese una Opción: "))
    opc_usuario = validarOpcion(opc, totalOpciones)

    if opc_usuario == 1: opc=201
    if opc_usuario == 2: opc=202
    if opc_usuario == 3: opc=203
    if opc_usuario == 4: opc=204
    
    return opc


"""TODO: Mover a módulo de validaciones"""
def validarOpcion(opc, totalOpciones):
    print("validacion de opciones de menu: ", opc)
    if (opc > totalOpciones or opc < 0):
        print(" ")
        print("¡Debe ingresar una opción válida!")
        menuClientes()
    
    if (opc > 0 and opc <= totalOpciones):
        print(" ")
        print("Usted ha ingresado: ", opc)
        return opc
