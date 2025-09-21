from controlador.dto_habitacion import HabitacionDTO
from validations.validationsHabitacion import validarNumero, validarPrecio, validarDisponible, validarExistenciaHabitacion, normalizarTexto, confirmarAccion

def listarHabitaciones():
    habitacionesEncontradas = HabitacionDTO().listarHabitaciones()
    if len(habitacionesEncontradas) > 0:
        for habitacion in habitacionesEncontradas:
            print(habitacion)
        else:
            print("¡No hay resultados!")
def agregarHabitacion():
    #TODO: Agregar la validación de ingreso de datos y existencia de habitación
    try:
        numero = input("Ingrese el número de la habitación: ")
        while not validarNumero(numero):
            print("Número inválido. Intente nuevamente")
            numero = input("Ingrese el nombre de la habitación: ")

        #todo: crear conexión con API para que se pueda ingresar en dólares el recio
        precio = input("Ingrese el precio en USD de la habitación: ")
        while not validarPrecio(precio):
            print("Apellido inválido. Intente nuevamente")
            precio = input("Ingrese el precio de la habitación: ")

        disponible = input("Indique si la habitación está ocupada (s/n): ")
        while not validarDisponible(disponible):
            print("¡Ingrese valor válido!")
            disponible = input("Indique si la habitación está ocupada (s/n): ")
            
        # TODO: Mostrar mensaje de confirmación de agregado a la base de datos
        habitacionCreada = HabitacionDTO().agregarHabitacion(numero, precio, disponible)
        if habitacionCreada:
            print(" ")
            print("!Habitación creada correctamente!")
            print(" ")
        if not habitacionCreada:
            print("¡No se pudo agregar la habitación!")

    except Exception as ex:
        print("¡Ha ocurrido un error!", ex)

def actualizarHabitacion():
    try:
        numero = input("Ingrese el número de habitación a modificar: ")
        while not validarNumero(numero):
            print("Número inválido. Intente nuevamente.")
            numero = normalizarTexto(input("Ingrese el número de habitacion a modificar: ")) 
        habitacion = HabitacionDTO().buscarHabitacion(numero)

        habitacion = validarExistenciaHabitacion(numero)
        if habitacion is None:
            return  # Salir si no existe
        
        # Datos actuales de la ´habitación
        print(habitacion)

        # Actualización condicional de cada campo
        # Validar si el número de habitación ya existe
        numero = habitacion.getNumero()
        mensaje = "¿Desea modificar el número de habitación? (s/n): "
        if confirmarAccion(mensaje):
            nuevoNumero = input("Ingrese el nuevo Número: ")
            while not validarNumero(nuevoNumero):
                print("Nombre inválido. Intente nuevamente.")
                nuevoNumero = normalizarTexto(input("Ingrese el nuevo nombre: "))
            numero = nuevoNumero
        
        precio = habitacion.getPrecio()
        if confirmarAccion("¿Desea modificar el Precio? (s/n): "):
            nuevoPrecio = input("Ingrese el nuevo Precio: ")
            while not validarPrecio(nuevoPrecio):
                print("Precio inválido. Intente nuevamente.")
                nuevoPrecio = input("Ingrese el nuevo apellido: ")
            precio = nuevoPrecio
        # TODO: que el usuario ingrese s/n y se envíe un verdadero si es s y un falso si es n
        disponible = habitacion.getDisponible()
        if confirmarAccion("¿Desea modificar si está disponible? (s/n): "):
            nuevoDisponible = input("Ingrese el nuevo estado de disponibilidad: ")
            while not validarDisponible(nuevoDisponible):
                print("Precio inválido. Intente nuevamente.")
                nuevoDisponible = input("Ingrese el nuevo estado de disponibilidad: ")
            disponible = nuevoDisponible
            
        #Enviar información al DTO
        # TODO: Eliminar print
        print("HOLA SI ENVIAR INFORMACION AL DTO")
        habitacionActualizada = HabitacionDTO().actualizarHabitacion(numero, precio, disponible)
        if habitacionActualizada:
            print("Habitación actualizada correctamente.")

    except Exception as ex:
        print("!Ha ocurrido un error! ", ex)
    
    #Eliminar Habitación
def eliminarHabitacion():
    try:
        numero = input("Ingrese el número de habitación que desea eliminar: ")
        while not validarNumero(numero):
            # TODO: Podría implementar un módulo de alertas automáticas.
            print("Número inválido. Intente nuevamente.")
            numero = input("Ingrese el número de habitación que desea eliminar: ")
        habitacion = HabitacionDTO().buscarHabitacion(numero)

        habitacion = validarExistenciaHabitacion(numero)
        if habitacion is None:
            return # Salir si no existe (TODO:Cuestionable)
        
        mensaje="¿Está seguro que desea eliminar este cliente? (s/n): "
        if confirmarAccion(mensaje):
            habitacionEliminada = HabitacionDTO().eliminarHabitacion(numero)

    except Exception as ex:
        print("¡Ha ocurrido un error! ", ex)