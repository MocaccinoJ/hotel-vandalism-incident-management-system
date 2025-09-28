from controlador.dto_habitacion import HabitacionDTO
from validations.validationsHabitacion import validarNumero, validarPrecio, validarDisponible, validarExistenciaHabitacion, normalizarTexto, confirmarAccion

def listarHabitaciones():
    habitacionesEncontradas = HabitacionDTO().listarHabitaciones()
    if len(habitacionesEncontradas) > 0:
        for habitacion in habitacionesEncontradas:
            numero = habitacion.getNumero()
            disponible = "Sí" if habitacion.getDisponible() else "No"
            precio = habitacion.getPrecio()
            print(
                f"Número: {numero}\n",
                f"Precio: {precio}\n",
                f"Disponible: {disponible}"
            )

            
def agregarHabitacion():
    try:
        numero = input("Ingrese el número de la habitación: ")
        while not validarNumero(numero) or validarExistenciaHabitacion(numero) is not None:
            print("Número inválido. Intente nuevamente")
            numero = input("Ingrese el nombre de la habitación: ")

        #todo: crear conexión con API para que se pueda ingresar en dólares el recio
        precio = input("Ingrese el precio en USD de la habitación: ")
        while not validarPrecio(precio):
            print("Apellido inválido. Intente nuevamente")
            precio = input("Ingrese el precio de la habitación: ")

        disponible = normalizarTexto(input("Indique si la habitación está ocupada (s/n): "))
        while not validarDisponible(disponible):
            print("¡Ingrese valor válido!")
            disponible = normalizarTexto(input("Indique si la habitación está ocupada (s/n): "))
        # Convertir valor ingresado a booleanoa para la base de datos
        disponible_bool = True if disponible == 's' else False
            
        # TODO: Mostrar mensaje de confirmación de agregado a la base de datos
        habitacionCreada = HabitacionDTO().agregarHabitacion(numero, precio, disponible_bool)
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

        habitacion = validarExistenciaHabitacion(numero)
        if habitacion is None:
            return  # Salir si no existe
        
        # Datos actuales de la habitación
        print(habitacion)
        
        precio = habitacion.getPrecio()
        if confirmarAccion("¿Desea modificar el Precio? (s/n): "):
            nuevoPrecio = input("Ingrese el nuevo Precio: ")
            while not validarPrecio(nuevoPrecio):
                print("Precio inválido. Intente nuevamente.")
                nuevoPrecio = input("Ingrese el nuevo apellido: ")
            precio = nuevoPrecio
    
        disponible = habitacion.getDisponible()
        disponible_bool = disponible
        if confirmarAccion("¿Desea modificar si está disponible? (s/n): "):
            nuevoDisponible = normalizarTexto(input("Ingrese el nuevo estado de disponibilidad: "))
            while not validarDisponible(nuevoDisponible):
                print("Precio inválido. Intente nuevamente.")
                nuevoDisponible = normalizarTexto(input("Ingrese el nuevo estado de disponibilidad: "))
            disponible = nuevoDisponible
            # Convertir valor ingresado a booleano para la base de datos
            disponible_bool = True if disponible == 's' else False
            
        habitacionActualizada = HabitacionDTO().actualizarHabitacion(numero, precio, disponible_bool)
        if habitacionActualizada:
            print("Habitación actualizada correctamente.")

    except Exception as ex:
        print("!Ha ocurrido un error! ", ex)
    
    #Eliminar Habitación
def eliminarHabitacion():
    try:
        numero = input("Ingrese el número de habitación que desea eliminar: ")
        while not validarNumero(numero):
            print("Número inválido. Intente nuevamente.")
            numero = input("Ingrese el número de habitación que desea eliminar: ")
        habitacion = HabitacionDTO().buscarHabitacion(numero)

        habitacion = validarExistenciaHabitacion(numero)
        if habitacion is None:
            return # Salir si no existe (TODO:Cuestionable)
        
        mensaje="¿Está seguro que desea eliminar este Habitación? (s/n): "
        if confirmarAccion(mensaje):
            habitacionEliminada = HabitacionDTO().eliminarHabitacion(numero)

    except Exception as ex:
        print("¡Ha ocurrido un error! ", ex)