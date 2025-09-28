import bcrypt

def encriptarPassword(password):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')  # Para guardar como string en la base de datos

def verificarPassword(password_plana, password_encriptada):
    return bcrypt.checkpw(password_plana.encode('utf-8'), password_encriptada.encode('utf-8'))
