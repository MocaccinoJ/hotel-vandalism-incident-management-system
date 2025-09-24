"""TODO: Definir cuales serán los atributos obligatorios"""
class Habitacion():
    def __init__(
            self, 
            numero="", 
            precio="", 
            disponible=""
        ):
        self.__numero = numero
        self.__precio = precio
        self.__disponible = disponible

    def __str__(self):
        return f"Número: {self.getNumero()} \n Precio: {self.getPrecio()} \n Disponible: {self.getDisponible()}"

    def getNumero(self):
        return self.__numero
    
    def getPrecio(self):
        return self.__precio
    
    def getDisponible(self):
        return self.__disponible
    
'''TODO: Falta hacer los SETTERS de esta clase'''