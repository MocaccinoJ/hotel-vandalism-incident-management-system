from modelo.persona import Persona

"""TODO: Definir cuales serán los atributos obligatorios"""
"""TODO: PREGUNTA 1) para el profe ¿Está bien que los atributos heredados vayan en el constructor"""
class Cliente(Persona):
    def __init__(
            self, 
            nombre="", 
            apellido="", 
            direccion="", 
            documento="", 
            tipoDocumento=""
        ):
        super().__init__(nombre, apellido, direccion)
        self.__documento=documento
        self.__tipoDocumento=tipoDocumento

    def getDocumento(self):
        return self.__documento
    
    def getTipoDocumento(self):
        return self.__tipoDocumento
    
    def __str__(self):
        return f"{super().__str__()} | Documento: {self.__documento} ({self.__tipoDocumento})"