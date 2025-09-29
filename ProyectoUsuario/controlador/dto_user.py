from modelo.user import User
from dao.dao_user import daoUser
from datetime import datetime
from seguridad.strategyEncryptor import verificarPassword
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

    def buscarUsuarioPorUsername(self, username):
        daouser = daoUser()
        username = User(username=username)
        usuario = daouser.buscarUsuarioPorUsername(username)
        if usuario is not None:
            usuario = User(
                username = usuario[0],
                email = usuario[1],
                password= usuario[2]
            )
        return usuario
    
    def buscarUsuarioPorEmail(self, email):
        daouser = daoUser()
        email = User(email=email)
        usuario = daouser.buscarUsuarioPorEmail(email)
        if usuario is not None:
            usuario = User(
                username = usuario[0],
                email = usuario[1],
                create_time= usuario[2]
            )
        return usuario

    def validarLogin(self, username, clave):
        try:
            daouser = daoUser()
            resultado = daouser.validarLogin(User(username=username))
            if resultado is None:
                return None

            username_db, password_hash = resultado
            if verificarPassword(clave, password_hash):
                return User(username=username_db, password=password_hash)
            else:
                return None
        except Exception as ex:
            print('¡Ha ocurrido un error!: ', ex)
            return None
        
    def actualizarUsuario(self, originalUsername, username, email, password):
        daouser = daoUser()

        user = User()                 # creas el objeto vacío
        user.setUsername(username)    # usas setters
        user.setEmail(email)
        user.setPassword(password)

        usuarioActualizado = daouser.actualizarUsuario(user, originalUsername)
        return usuarioActualizado

    def eliminarUsuario(self, username):
        daouser = daoUser()
        usuarioEliminado = daouser.eliminarUsuario(User(username=username))
        return usuarioEliminado
    
    def agregarUsuario(self, username, email, password):
        daouser = daoUser()
        nuevoUsuario = daouser.agregarUsuario(User(username=username, email=email, create_time= datetime.now(), password=password))
        return nuevoUsuario