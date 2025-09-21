from modelo.persona import Persona

"""TODO: Definir cuales serán los atributos obligatorios"""
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

    def __str__(self):
        return f"Nombre: {self.getNombre()} \n Apellido: {self.getApellido()} \n Dirección: {self.getDireccion()} \n Documento: {self.getDocumento()} \n Tipo Documento: {self.getTipoDocumento()}"

    def getDocumento(self):
        return self.__documento
    
    def getTipoDocumento(self):
        return self.__tipoDocumento
    
