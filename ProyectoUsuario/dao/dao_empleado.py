from conex import conn
import traceback


"""TODO: CREAR UN MODULO DE CONEXIÓN HACIA LA BASE DE DATOS PARA EVITARA TENER QUE REPLICARLO EN TODOS LOS DAO'S"""
class daoEmpleado:
    def __init__(self):
        try:
            self.__conn = conn.Conex("localhost", "root", "", "superbase")
        except Exception as ex:
            print("Error | dao_empleado: ", ex)

    def getConex(self):
        return self.__conn

    def listarEmpleados(self):
        c = self.getConex()
        result = None
        try:
            cursor= c.getConex().cursor()
            cursor.execute("SELECT nombre, apellido, direccion, codigo, sueldo FROM empleado")
            result = cursor.fetchall()
        except Exception as ex:
            print("¡Ha ocurrido un error! ", ex)
            traceback.print_exc()
        finally:
            c.closeConex()
        return result
    
    def agregarEmpleado (self, empleado):
        sql="INSERT INTO EMPLEADO (nombre, apellido, direccion, codigo, sueldo) values (%s,%s,%s,%s,%s)"
        c = self.getConex()
        mensaje = ""
        try:
            nombre = empleado.getNombre()
            apellido = empleado.getApellido()
            direccion = empleado.getDireccion()
            codigo = empleado.getCodigo()
            sueldo = empleado.getSueldo()

            cursor = c.getConex().cursor()
            cursor.execute(sql, (nombre, apellido, direccion, codigo, sueldo))
            c.getConex().commit()

            filas = cursor.rowcount

            if filas > 0:
                mensaje="¡Datos agregados satisfactoriamente!"
            else:
                mensaje="¡No se realizaron cambios!"
        except Exception as ex:
            print("¡Ha ocurrido un error! ", ex)
            traceback.print_exc()
            return None
        finally:
            c.closeConex()
        return mensaje
    

    def buscarEmpleado(self, empleado):
        sql ="SELECT nombre, apellido, direccion, codigo, sueldo FROM empleado WHERE codigo=%s"
        c = self.getConex()
        
        try:
            codigo = empleado.getCodigo()
            cursor = c.getConex().cursor()
            cursor.execute(sql, (codigo))
            empleado = cursor.fetchone()
        except Exception as ex:
            print("¡Ha ocurrido un error! ", ex)
            traceback.print_exc()
        finally:
            self.getConex().closeConex()
        return empleado

    def actualizarEmpleado(self, empleado):
        sql = "UPDATE empleado SET nombre = %s, apellido = %s, direccion = %s, sueldo = %s WHERE codigo = %s"
        c = self.getConex()
        mensaje=""

        try:
            cursor = c.getConex().cursor()

            nombre = empleado.getNombre()
            apellido = empleado.getApellido()
            direccion = empleado.getDireccion()
            sueldo = empleado.getSueldo()
            codigo = empleado.getCodigo()
            
            print("SQL:        ",sql)

            cursor.execute(sql, (nombre, apellido, direccion, sueldo, codigo))
            c.getConex().commit()

            filas = cursor.rowcount
            print(filas)
            
            if filas > 0:
                mensaje = "¡Cliente actualizado correctamente!"
            else:
                mensaje = "No se realizaron cambios. Verifique el documento."

        except Exception as ex:
            print("¡Ha ocurrido un error al actualizar! ", ex)
            traceback.print_exc()

        finally:
            c.closeConex()
        return mensaje 

    def eliminarEmpleado(self, empleado):
        sql = "DELETE FROM empleado WHERE codigo = %s"
        c = self.getConex()
        mensaje = ""
        try:
            codigo = empleado.getCodigo()

            cursor = c.getConex().cursor()
            cursor.execute(sql,(codigo))
            c.getConex().commit()
            
            filas = cursor.rowcount
            
            if filas > 0:
                mensaje = "EMpleado eliminado correcamente!"
            else:
                mensaje = "¡Ha ocurrido un error inesperado!"
        except Exception as ex:
            print("¡Ha ocurrido un error: ", ex)
            traceback.print_exc()
            return None
        finally:c.closeConex()
        return mensaje
