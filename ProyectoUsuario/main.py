from validations import inicial, validarLogin


##### login
intentos = 1
print("Sistema POO")
while intentos <= 3:
    try:
        print("MENU: ")
        resu = validarLogin()
        if resu is not None:
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