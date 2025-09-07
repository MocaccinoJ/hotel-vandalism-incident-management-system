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
            print("¡Ha ocurrido un error! ", ex)
        finally:
            c.closeConex()
        
        return result