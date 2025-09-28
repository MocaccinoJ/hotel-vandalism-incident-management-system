from conex import conn
import traceback

"""TODO: CREAR UN MODULO DE CONEXIÓN HACIA LA BASE DE DATOS PARA EVITARA TENER QUE REPLICARLO EN TODOS LOS DAO'S"""
class daoCliente:
    def __init__(self):
        try:
            self.__conn = conn.Conex("localhost", "root", "", "superbase")
        except Exception as ex:
            print("Error | dao_cliente: ", ex)
    
    def getConex(self):
        return self.__conn
    
    def listarClientes(self):
        c = self.getConex()
        result=None
        try:
            cursor = c.getConex().cursor()
            cursor.execute("SELECT nombre, apellido, direccion, documento, tipoDocumento FROM cliente")
            result = cursor.fetchall()
        except Exception as ex:
            print("¡Ha ocurrido un error!: ", ex)
        finally:
            c.closeConex()
        return result
    
    def agregarCliente (self, cliente):
        sql="INSERT INTO CLIENTE (nombre, apellido, direccion, documento, tipoDocumento) values (%s,%s,%s,%s,%s)"
        c = self.getConex()
        mensaje = ""
        try:
            nombre = cliente.getNombre()
            apellido = cliente.getApellido()
            direccion = cliente.getDireccion()
            documento = cliente.getDocumento()
            tipoDocumento = cliente.getTipoDocumento()

            cursor = c.getConex().cursor()
            cursor.execute(sql, (nombre, apellido, direccion, documento, tipoDocumento))
            c.getConex().commit()

            filas = cursor.rowcount

            if filas > 0:
                mensaje="¡Datos agregados satisfactoriamente!"
            else:
                mensaje="¡No se realizaron cambios!"
        except Exception as ex:
            print(traceback.print_exc())
            print("¡Ha ocurrido un error! ", ex)
            return None
        finally:
            c.closeConex()
        return mensaje
    
    def buscarCliente(self, cliente):
        sql = "SELECT nombre, apellido, direccion, documento, tipoDocumento FROM cliente WHERE documento =%s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql,(cliente.getDocumento()))
            cliente = cursor.fetchone()

            return cliente
        except Exception as ex:
            print("¡Ha ocurrido un error! ", ex)
            return None
        finally:
            c.closeConex()

    def actualizarCliente(self, cliente):
        sql="""
            UPDATE cliente
            SET nombre = %s, apellido = %s, direccion = %s, tipoDocumento = %s
            WHERE documento = %s
        """
        c = self.getConex()
        mensaje=""
        try:
            nombre = cliente.getNombre()
            apellido = cliente.getApellido()
            direccion = cliente.getDireccion()
            tipoDocumento = cliente.getTipoDocumento()
            documento = cliente.getDocumento()
            
            cursor = c.getConex().cursor()
            cursor.execute(sql, (nombre, apellido, direccion, tipoDocumento, documento))
            c.getConex().commit()

            filas = cursor.rowcount
            
            if filas > 0:
                mensaje = "¡Cliente actualizado correctamente!"
            else:
                mensaje = "No se realizaron cambios. Verifique el documento."
            
        except Exception as ex:
            print("¡Ha ocurrido un error! ", ex)
            traceback.print_exc()
            return None
        finally:
            c.closeConex()
        return mensaje
    
    def eliminarCliente(self, cliente):
        sql = "DELETE FROM cliente WHERE documento = %s"
        c = self.getConex()
        mensaje = ""
        try:
            documento = cliente.getDocumento()

            cursor = c.getConex().cursor()
            cursor.execute(sql,(documento))
            c.getConex().commit()
            
            filas = cursor.rowcount
            
            if filas > 0:
                mensaje = "¡Cliente eliminado correcamente!"
            else:
                mensaje = "¡Ha ocurrido un error inesperado!"
        except Exception as ex:
            print("¡Ha ocurrido un error: ", ex)
            traceback.print_exc()
            return None
        finally:c.closeConex()
        return mensaje