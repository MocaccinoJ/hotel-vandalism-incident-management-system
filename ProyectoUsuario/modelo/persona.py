class Persona:

    """Clase base para personas con atributos comunes"""
    def init(
            self, 
            nombre="", 
            apellido="", 
            direccion=""
        ):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion 

    def str(self):
        return f"{self.nombre} {self.apellido} {self.direccion}"

# Getters
    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getDireccion(self):
        return self.direccion

# Setters
    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setDireccion(self, direccion):
        self.direccion = direccion