from conex import conn
import traceback

"""TODO: CREAR UN MODULO DE CONEXIÓN HACIA LA BASE DE DATOS PARA EVITARA TENER QUE REPLICARLO EN TODOS LOS DAO'S"""
class daoHabitacion:
    def __init__(self):
        try:
            self.__conn = conn.Conex("localhost", "root", "", "superbase")
        except Exception as ex:
            print("Error | dao_habitacion: ", ex)
    
    def getConex(self):
        return self.__conn
    
    def listarHabitaciones(self):
        c = self.getConex()
        result=None
        try:
            cursor = c.getConex().cursor()
            cursor.execute("SELECT numero, precio, disponible FROM habitacion")
            result = cursor.fetchall()
        except Exception as ex:
            print("¡Ha ocurrido un error!: ", ex)
        finally:
            c.closeConex()
        return result
    
    def agregarHabitacion (self, habitacion):
        sql="INSERT INTO HABITACION (numero, precio, disponible) values (%s,%s,%s)"
        c = self.getConex()
        mensaje = ""
        try:
            numero = habitacion.getNumero()
            precio = habitacion.getPrecio()
            disponible = habitacion.getDisponible()

            cursor = c.getConex().cursor()
            cursor.execute(sql, (numero, precio, disponible))
            c.getConex().commit()

            filas = cursor.rowcount

            if filas > 0:
                mensaje="¡Datos de habitación agregados satisfactoriamente!"
            else:
                mensaje="¡No se realizaron cambios!"
        except Exception as ex:
            print(traceback.print_exc())
            print("¡Ha ocurrido un error! ", ex)
            return None
        finally:
            c.closeConex()
        return mensaje
    
    def buscarHabitacion(self, habitacion):
        sql = "SELECT numero, precio, disponible FROM habitacion WHERE numero =%s"
        c = self.getConex()
        try:
            numero = habitacion.getNumero()

            cursor = c.getConex().cursor()
            cursor.execute(sql,(numero))
            habitacion = cursor.fetchone()

            return habitacion
        except Exception as ex:
            print("¡Ha ocurrido un error! ", ex)
            return None
        finally:
            c.closeConex()

    def actualizarHabitacion(self, habitacion):
        sql="""
            UPDATE habitacion
            SET numero = %s, precio = %s, disponible = %s
            WHERE numero = %s
        """
        c = self.getConex()
        mensaje=""
        try:
            numero = habitacion.getNumero()
            precio = habitacion.getPrecio()
            disponible = habitacion.getDisponible()
            
            cursor = c.getConex().cursor()
            cursor.execute(sql, (numero, precio, disponible))
            c.getConex().commit()

            filas = cursor.rowcount
            
            if filas > 0:
                mensaje = "¡Habitación actualizada correctamente!"
            else:
                mensaje = "No se realizaron cambios. Verifique el numero."
            
        except Exception as ex:
            print("¡Ha ocurrido un error! ", ex)
            traceback.print_exc()
            return None
        finally:
            c.closeConex()
        return mensaje
    
    def eliminarHabitacion(self, habitacion):
        sql = "DELETE FROM habitacion WHERE numero = %s"
        c = self.getConex()
        mensaje = ""
        try:
            numero = habitacion.getNumero()

            cursor = c.getConex().cursor()
            cursor.execute(sql,(numero))
            c.getConex().commit()
            
            filas = cursor.rowcount
            
            if filas > 0:
                mensaje = "¡Habitación eliminada correcamente!"
            else:
                mensaje = "¡Ha ocurrido un error inesperado!"
        except Exception as ex:
            print("¡Ha ocurrido un error: ", ex)
            traceback.print_exc()
            return None
        finally:c.closeConex()
        return mensaje
