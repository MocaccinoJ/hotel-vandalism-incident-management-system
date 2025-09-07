def menu():
    print("1. Listar Usuarios")
    print("2. Agregar Usuario")
    print("3. Eliminar Usuario")
    print("4. Actualizar Usuario")
    print("5. Buscar Usuario")
    
    """MENU PARA CLIENTES"""
    print("6. Opciones de Clientes")
    
    print("50. Salir")
    opc = int( input("Ingrese una opción : "))
    
    if(opc==6): opc=menuClientes() 

    print("Valor de la opc sistema clientes: ", opc)
    return opc

"""Las opciones del menú de clientes serán con valores 100"""
def menuClientes():
    print("   ")
    print("---- Bienvenido al Menú de Clientes ----")
    print("1. Listar Clientes")
    print("2. Agregar Cliente")
    totalOpciones = 2;
    opc = int(input("Ingrese una Opción: "))
    
    opc_usuario = validarOpcion(opc, totalOpciones)
    if opc_usuario == 1: opc=101
    if opc_usuario == 2: opc=102

    return opc

"""Se podría hacer un módulo de validaciones por módulo"""
def validarOpcion(opc, totalOpciones):
    if (opc > totalOpciones or opc < 0):
        print(" ")
        print("¡Debe ingresar una opción válida!")
        menuClientes()
    
    if (opc > 0 and opc < totalOpciones):
        print(" ")
        print("Usted ha ingresado: ", opc)
        return opc
