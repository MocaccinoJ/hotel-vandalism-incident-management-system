from controlador.dto_empleado import EmpleadoDTO
from validations.validationsEmpleado import *

def listarEmpleados():
    empleadosEncontrados = EmpleadoDTO().listarEmpleados()
    if len(empleadosEncontrados) > 0:
        for empleado in empleadosEncontrados:
            print(empleado)
    
        # print("\n========== LISTADO DE EMPLEADOS ==========")
        # for i, e in enumerate(empleados, start=1):
        #     print(f"\nEmpleado {i}")
        #     print(f"  Nombre: {e.getNombre()}")
        #     print(f"  Apellido: {e.getApellido()}")
        #     print(f"  Dirección: {e.getDireccion()}")
        #     print(f"  Código: {e.getCodigo()}")
        #     print(f"  Sueldo: {e.getSueldo():.2f}")
        # print("==========================================")
    else:
        print("¡No hay resultados!")
    
    print("\nPresione ENTER para volver al menú...")
    input()

def agregarEmpleado():
    nombre = normalizarTexto(input("Ingrese nombre: "))
    while not validarNombre(nombre): nombre = normalizarTexto(input("Nombre inválido. Reintente: "))

    apellido = normalizarTexto(input("Ingrese apellido: "))
    while not validarApellido(apellido): apellido = normalizarTexto(input("Apellido inválido. Reintente: "))

    direccion = normalizarTexto(input("Ingrese dirección: "))

    codigo = input("Ingrese código: ")
    while not validarCodigo(codigo): codigo = input("Código inválido. Reintente: ")

    sueldo = input("Ingrese sueldo: ")
    while not validarSueldo(sueldo): sueldo = input("Sueldo inválido. Reintente: ")
    sueldo = float(sueldo)

    empleadoCreado = EmpleadoDTO().agregarEmpleado(nombre, apellido, direccion, codigo, sueldo)
    print(empleadoCreado)

def actualizarEmpleado():
    try:
        codigo = normalizarTexto(input("Ingrese código del empleado a modificar: "))
        while not validarCodigo(codigo):
            print("¡Código inválido!")
            codigo = normalizarTexto().input("Ingrese código del empleado a modificar: ")
        # empleado = EmpleadoDTO().buscarEmpleado(codigo)
        empleadoEncontrado = validarExistenciaEmpleado(codigo)

        if empleadoEncontrado is None:
            return

        print("\nDatos actuales del empleado:")
        print(empleadoEncontrado)

        # Solicitar nuevos valores, permitiendo mantener los actuales
        mensaje="¿Desea modificar el nombre? (s/n)"
        if confirmarAccion(mensaje):
            nuevoNombre = normalizarTexto(input("Ingrese el nuevo nombre: "))
            while not validarNombre(nuevoNombre):
                print("Nombre inválido. Intente nuevamente.")
                nuevoNombre = normalizarTexto(input("Ingrese el nuevo nombre: "))
            nombre = nuevoNombre

        apellido = empleadoEncontrado.getApellido()
        if confirmarAccion("¿Desea modificar el apellido? (s/n): "):
            nuevoApellido = normalizarTexto(input("Ingrese el nuevo apellido: "))
            while not validarApellido(nuevoApellido):
                print("Apellido inválido. Intente nuevamente.")
                nuevoApellido = normalizarTexto(input("Ingrese el nuevo apellido: "))
            apellido = nuevoApellido
        
        direccion = empleadoEncontrado.getDireccion()
        if confirmarAccion("¿Desea modificar la dirección? (s/n): "):
            direccion = normalizarTexto(input("Ingrese la nueva dirección: "))

        sueldo = empleadoEncontrado.getSueldo()
        if confirmarAccion("¿Desea modificar el sueldo? (s/n): "):
            nuevoSueldo = input("Ingrese el nuevo sueldo: ")
            while not validarSueldo(nuevoSueldo):
                print("Sueldo inválido. Intente nuevamente.")
                nuevoSueldo = input("Ingrese el nuevo sueldo: ")
            sueldo = nuevoSueldo

        # Actualizar usando DTO
        empleadoActualizado = EmpleadoDTO().actualizarEmpleado(
            nombre = nombre,
            apellido = apellido,
            direccion = direccion,
            sueldo = sueldo,
            codigo = codigo
        )

        if empleadoActualizado: print("¡Empleado Actualizado de forma satisfactoria!")
    except Exception as ex:
        print("¡Ha ocurrido un error:", ex)

def eliminarEmpleado():
    try:
        codigo = normalizarTexto(input("Ingrese el código de empleado que desea eliminar: "))
        while not validarCodigo(codigo):
            # TODO: Podría implementar un módulo de alertas automáticas.
            print("Código inválido. Intente nuevamente.")
            codigo = normalizarTexto(input("Ingrese el código de empleado que desea eliminar: "))
        empleado = EmpleadoDTO().buscarEmpleado(codigo)

        empleado = validarExistenciaEmpleado(codigo)
        if empleado is None:
            return # Salir si no existe (TODO:Cuestionable)
        
        mensaje="¿Está seguro que desea eliminar este empleado? (s/n): "
        if confirmarAccion(mensaje):
            empleadoEliminado = EmpleadoDTO().eliminarEmpleado(codigo)

    except Exception as ex:
        print("¡Ha ocurrido un error! ", ex)
