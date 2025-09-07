class Persona:

    """TODO: Definir cuales serán los atributos obligatorios"""
    def __init__(
            self, 
            nombre="", 
            apellido="", 
            direccion=""
        ):
        self.__nombre =    nombre
        self.__apellido =  apellido
        self.__direccion = direccion 
    
    def __str__(self):
        return "{0} {1} {2}".format(self)
    
    '''GETTERS TODO: Revisar si es que hay una forma de hacer que sean opcionales, esto es solo como punto extra'''
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getDireccion(self):
        return self.__direccion
    
    '''TODO: Falta hacer los SETTERS de esta clase'''