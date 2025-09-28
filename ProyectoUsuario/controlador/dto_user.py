from modelo.user import User
from dao.dao_user import daoUser
from datetime import datetime
from modelo import user 

class UserDTO:

    def listarUsuarios(self):
        daouser = daoUser()
        usuarios = daouser.listarUsuarios()
        lista = []
        if usuarios is not None:
            for usuario_encontrado in usuarios:
                usuario = User(
                    username=usuario_encontrado[0], 
                    email=usuario_encontrado[1], 
                    password=usuario_encontrado[2], 
                    create_time=usuario_encontrado[3]
                )
                lista.append(usuario)
        return lista

    def buscarUsuario(self, username):
        daouser = daoUser()
        # username = User(username=username)
        usuario = daouser.buscarUsuario(User(username=username))
        # print('2) Estructura resultado!', resultado)
        if usuario is not None:
            usuario = User(
                username = usuario[0],
                email = usuario[1],
                password = usuario[2],
                create_time= usuario[3]
            )
            return usuario
        return None

    def validarLogin(self, username, clave):
        try:
            daouser = daoUser()
            user=User(username=username, password=clave)
            resultado = daouser.validarLogin(User(username=username, password=clave))

            return User(resultado[0]) if resultado is not None else None
        except Exception as ex:
            print('!Ha ocurrido un error!: ', ex)
            return None

    def actualizarUsuario(self, username, email, password):
        daouser = daoUser()
        usuarioActualizado = daouser.actualizarUsuario(User(username=username, email=email, password=password))
        return usuarioActualizado
    
    def eliminarUsuario(self, username):
        daouser = daoUser()
        print("DTO USERNAME: ",username)
        usuarioEliminado = daouser.eliminarUsuario(User(username=username))
        return usuarioEliminado
    
    def agregarUsuario(self, username, email, password):
        daouser = daoUser()
        nuevoUsuario = daouser.agregarUsuario(User(username=username, email=email, create_time= datetime.now(), password=password))
        return nuevoUsuario