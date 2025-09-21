from modelo.user import User
from dao.dao_user import daoUser
from datetime import datetime
from modelo import user 

class UserDTO:

    def listarUsuarios(self):
        daouser = daoUser()
        resultado = daouser.listarUsuarios()
        lista = []
        if resultado is not None:
            for u in resultado:
                usuario = User(
                    username=u[0], 
                    email=u[1], 
                    password=u[2], 
                    create_time=u[3]
                )
                lista.append(usuario)
        return lista

    def buscarUsuario(self, username):
        daouser = daoUser()
        resultado = daouser.buscarUsuario(User(username=username))
        """ENVIAR EN VARIABLES QUE IDENTIFIQUEN CON SOLO LECTURA QUË ATRIBUTO SE ESTÁ ENVIANDO"""
        print('2) Estructura resultado!', resultado)
        return User(resultado[0], resultado[1], resultado[2]) if resultado is not None else None

    def validarLogin(self, username, clave):
        print("!HOLADTO_USER!")
        try:
            daouser = daoUser()
            user=User(username=username, password=clave)
            print("DTO_USER.validarLogin() | ", user)
            resultado = daouser.validarLogin(User(username=username, password=clave))
            print('resultado DTO.validarLogin: ', resultado)

            return User(resultado[0]) if resultado is not None else None
        except Exception as ex:
            """TODO: No dar demasiada información sobre el error para practicas de seguridad"""
            print('!Ha ocurrido un error!: ', ex)
            return None

    def actualizarUsuario(self, username, email, password):
        daouser = daoUser()
        resultado = daouser.actualizarUsuario(User(username=username, email=email, password=password))
        return resultado
    def eliminarUsuario(self, username):
        daouser = daoUser()
        resultado = daouser.eliminarUsuario(User(username=username))
        return resultado
    def agregarUsuario(self, username, email, password):
        daouser = daoUser()
        resultado = daouser.agregarUsuario(User(username=username, email=email, create_time= datetime.now(), password=password))
        return resultado
    
