from conex import conn
import traceback

class daoUser:
    def __init__(self):
        try:
            self.__conn = conn.Conex("localhost", "root", "", "superbase")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.__conn

    def listarUsuarios(self):
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute("SELECT username, email, password, create_time FROM user")
            result = cursor.fetchall()
        except Exception as ex:
            print("¡Ha ocurrido un error! ",ex)
        finally:
            c.closeConex()
        return result

    def buscarUsuarioPorUsername(self, user):
        sql = "SELECT username, email, password, create_time FROM user WHERE username = %s"
        usuario = None
        c = self.getConex()
        try:
            print(user.getUsername())
            cursor = c.getConex().cursor()
            cursor.execute(sql, (user.getUsername(),))
            usuario = cursor.fetchone()
            return usuario
        except Exception as ex:
            print("¡Ha ocurrido un error! ",ex)
            print(traceback.print_exc())
            return None
        finally:
            c.closeConex()
    
    def buscarUsuarioPorEmail(self, user):
        sql = "SELECT username, email, password, create_time FROM user WHERE email = %s"
        usuario = None
        c = self.getConex()

        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (user.getEmail(),))
            usuario = cursor.fetchone()
        except Exception as ex:
            print("¡Ha ocurrido un error! ",ex)
            print(traceback.print_exc())
        finally:
            c.closeConex()
        return usuario


    def validarLogin(self,user):
        sql = "SELECT username FROM user WHERE username = %s AND password = %s"
        resultado = None
        conn = self.getConex()
        try:
            # TODO: Mètodo para encriptar y comparar contraseña encriptada
            cursor = conn.getConex().cursor()
            cursor.execute(sql, (user.getUsername(), user.getPassword()))
            resultado = cursor.fetchone()

        except Exception as ex:
            print("¡Ha ocurrido un error! ",ex)
            print(traceback.print_exc())
        finally:
            conn.closeConex()
        return resultado
    
    def actualizarUsuario(self, user, orginalUsername):
        sql = "UPDATE user SET username=%s, email=%s, password=%s WHERE username = %s"
        c = self.getConex()
        mensaje = ""
        try:

            cursor = c.getConex().cursor()
            cursor.execute(sql, (
                user.getUsername(), 
                user.getEmail(),
                user.getPassword(), 
                orginalUsername
            ))
            c.getConex().commit()
            filas = cursor.rowcount

            if filas > 0:
                mensaje ="Datos modificados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print("¡Ha ocurrido un error! ",ex)
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            c.closeConex()
        return mensaje
    
    def eliminarUsuario(self, user):

        sql = "DELETE FROM user WHERE username = %s"
        c = self.getConex()
        mensaje = ""
            
        try:
            username = user.getUsername()

            cursor = c.getConex().cursor()
            cursor.execute(sql, (username,))
            c.getConex().commit()

            filas = cursor.rowcount
            if filas > 0:
                mensaje = "Usuario eliminado satisfactoriamente"
            else:
                mensaje = "No se realizaron cambios"
        except Exception as ex:
            print("¡Ha ocurrido un error! ", ex)
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos. Vuelva a intentarlo"
        finally:
            c.closeConex()
        return mensaje

    
    def agregarUsuario(self,user):
        sql = "INSERT INTO user (username, email, password, create_time) VALUES (%s,%s,%s,%s)"
        c = self.getConex()
        mensaje = ""
        try:
            username = user.getUsername()
            email = user.getEmail()
            password = user.getPassword()
            create_time = user.getCreateTime()

            cursor = c.getConex().cursor()
            cursor.execute(sql, (username, email, password, create_time))
            c.getConex().commit()
            filas = cursor.rowcount

            if filas > 0:
                mensaje ="Datos agregados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            c.closeConex()
        return mensaje