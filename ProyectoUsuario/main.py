from validations1 import validarLogin
from menu.menu import inicial


##### login
intentos = 1
print("Sistema POO")
while intentos <= 3:
    try:
        print("MENU: ")
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



"""
TODO: -Modificar la contraseña y/o el nombre de usuario


from validations import inicial, validarLogin


##### login
intentos = 1
print("Sistema POO")
while intentos <= 3:
    try:
        resu = validarLogin()
        if resu is not None:
            print(f"Bienvenido(a) Sr(a). : {resu.getUsername()}")
            print(f"Bienvenido(a) Sr(a). : {resu.getUsername()}")
            inicial()
            break
        else:
            print("usuario o contraseña incorrecta")
            intentos += 1
    except:
        print("intentar nuevamente")
if intentos == 4:
    print("contraseña bloqueada")

"""