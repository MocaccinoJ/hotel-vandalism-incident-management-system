from modelo.habitacion import Habitacion
from dao.dao_habitacion import daoHabitacion

class HabitacionDTO:
    def listarHabitaciones(self):
        """TODO: CAMBIAR ESTRUCTURA DE TRASPASO DE INFORMACIÓN PARA MEJOR LECTURA"""
        daohabitacion = daoHabitacion();
        habitaciones = daohabitacion.listarHabitaciones()
        print("Habitaciones: ",habitaciones)
        
        lista_habitaciones = []
        if habitaciones is not None:
            for habitacion in habitaciones:
                #TODO: Eliminar print
                print("Habitación: ",habitacion)
                habitacion = Habitacion(
                    numero=habitacion[0], 
                    precio=habitacion[1], 
                    disponible=habitacion[2]
                )
                lista_habitaciones.append(habitacion)
        #TODO: Eliminar print 
        print("LISTA: ",lista_habitaciones)
        return lista_habitaciones;
    
    def buscarHabitacion(self, numero):
        daohabitacion = daoHabitacion()
        numero = Habitacion(numero=numero)
        habitacion = daohabitacion.buscarHabitacion(numero)
        if habitacion is not None:
            habitacion = Habitacion(
                    numero=habitacion[0], 
                    precio=habitacion[1], 
                    disponible=habitacion[2]
            )
            return habitacion
        return None


    def agregarHabitacion(self, numero, precio, disponible):
        habitacion = Habitacion(numero = numero, precio = precio, disponible = disponible)
        return daoHabitacion().agregarHabitacion(habitacion)
    
    def actualizarHabitacion(self, numero, precio, disponible):
        habitacion = Habitacion(numero = numero, precio = precio, disponible = disponible)
        daohabitacion = daoHabitacion()
        habitacionActualizada=daohabitacion.actualizarHabitacion(habitacion)

    def eliminarHabitacion(self, numero):
        habitacion = Habitacion(numero = numero)
        print("CLIENTE: ",habitacion)
        daohabitacion = daoHabitacion()
        
        habitacionEliminada = daohabitacion.eliminarHabitacion(habitacion)
        
        return habitacionEliminada