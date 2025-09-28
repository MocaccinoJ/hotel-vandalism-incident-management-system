from modelo.persona import Persona


class Cliente(Persona):
    def __init__(
            self, 
            nombre="", 
            apellido="", 
            direccion="", 
            documento="", 
            tipoDocumento=""
        ):
        super().init(nombre, apellido, direccion)
        self.__documento = documento
        self.__tipoDocumento = tipoDocumento

    def __str__(self):
        return f"Nombre: {self.getNombre()} \nApellido: {self.getApellido()} \nDirección: {self.getDireccion()} \nDocumento: {self.getDocumento()} \nTipo Documento: {self.getTipoDocumento()}"

    # Getters
    def getDocumento(self):
        return self.__documento

    def getTipoDocumento(self):
        return self.__tipoDocumento

    # Setters
    def setDocumento(self, documento):
        self.__documento = documento

    def setTipoDocumento(self, tipoDocumento):
        self.__tipoDocumento = tipoDocumento
