from acciones.accionesUsuario import listarUsuarios, agregarUsuario, validaDelUser, validateUpdateUser, validateFindUser
from acciones.accionesCliente import listarClientes, agregarCliente, actualizarCliente, eliminarCliente
from acciones.accionesHabitacion import listarHabitaciones, agregarHabitacion, actualizarHabitacion, eliminarHabitacion
from acciones.accionesEmpleado import listarEmpleados, agregarEmpleado, actualizarEmpleado, eliminarEmpleado
# from menu.menu_reserva import menuReservas
# from acciones.accionesReserva import listarReservas, agregarReserva, modificarReserva, cancelarReserva



def inicial():
    while True:
        opc=menu()
        if opc == 1:
            listarUsuarios()
        elif opc == 2:
            agregarUsuario()
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

        elif opc == 301:
            listarEmpleados()
        elif opc == 302:
            agregarEmpleado()
        elif opc == 303:
            actualizarEmpleado()
        elif opc == 304:
            eliminarEmpleado()

        # elif opc == 401:
        #     listarReservas()
        # elif opc == 402:
        #     agregarReserva()
        # elif opc == 403:
        #     modificarReserva()
        # elif opc == 404:
        #     cancelarReserva()

        elif opc == 50:
            
            break


def menu():
    print("1. Listar Usuarios")
    print("2. Agregar Usuario")
    print("3. Eliminar Usuario")
    print("4. Actualizar Usuario")
    print("5. Buscar Usuario")
    
    print("6. Opciones de Clientes")
    print("7. Opciones de Habitación")
    print("8. Opciones de Reservas")
    print("9. Opciones de Empleados")

    print("50. Salir")
    opc = int( input("Ingrese una opción : "))

    if(opc == 6): opc = menuClientes()
    if(opc == 7): opc = menuHabitacion()
    # if(opc == 8): opc = menuReservas()
    if(opc == 9): opc = menuEmpleado()

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

def menuEmpleado():
    # TODO: Hacer validaciones de ingreso de datos

    print("   ")
    print("---- Bienvenido al Menú de Empleados ----")
    print("1. Listar Empleados")
    print("2. Agregar Empleado")
    print("3. Editar Empleado")
    print("4. Eliminar Empleado")

    totalOpciones = 4;
    opc = int(input("Ingrese una Opción: "))

    opc_usuario = validarOpcion(opc, totalOpciones)

    if opc_usuario == 1: opc=301
    if opc_usuario == 2: opc=302
    if opc_usuario == 3: opc=303
    if opc_usuario == 4: opc=304
    
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
