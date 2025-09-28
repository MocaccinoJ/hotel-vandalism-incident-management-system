from acciones.accionesUsuario import validarLogin
from menu.menu import inicial
from utilities.inicializar_bd import inicializar_bd

##### login
intentos = 1
print("Sistema POO")
while intentos <= 3:
    try:
        
        inicializar_bd()

        print("-- MENU --")
        resu = validarLogin()
        if resu is not None:
            """TODO: ¡¡Saludar personalmente!!"""
            print(f"Bienvenido(a) Sr(a). : ")
            inicial()
            break
        else:
            print("usuario o contraseña incorrecta")
            intentos += 1
    except Exception as ex:
        print("¡Ha ocurrido un error: ", ex)
        print("intentar nuevamente")
if intentos == 4:
    print("contraseña bloqueada")

# TODO: -Modificar la contraseña y/o el nombre de usuario
# TODO: Cancelar App si la conexión a BB.DD no funciona
# TODO: Implementar los Setters
