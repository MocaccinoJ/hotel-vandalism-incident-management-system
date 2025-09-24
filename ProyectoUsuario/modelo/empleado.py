class Empleado:
    def __init__(
            self, 
            nombre="", 
            apellido="", 
            direccion="", 
            codigo="", 
            sueldo=0.0
        ):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__codigo = codigo
        self.__sueldo = sueldo

    def __str__(self):
        return f"Nombre: {self.getNombre()}\nApellido: {self.getApellido()}\nDirección: {self.getDireccion()}\nCódigo: {self.getCodigo()}\nSueldo: {self.getSueldo()}"

    # Getters
    def getNombre(self): return self.__nombre
    def getApellido(self): return self.__apellido
    def getDireccion(self): return self.__direccion
    def getCodigo(self): return self.__codigo
    def getSueldo(self): return self.__sueldo

    # Setters
    def setNombre(self, nombre): self.__nombre = nombre
    def setApellido(self, apellido): self.__apellido = apellido
    def setDireccion(self, direccion): self.__direccion = direccion
    def setCodigo(self, codigo): self.__codigo = codigo
    def setSueldo(self, sueldo): self.__sueldo = sueldo
