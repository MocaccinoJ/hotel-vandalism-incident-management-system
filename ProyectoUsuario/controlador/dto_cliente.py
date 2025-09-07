from modelo.cliente import Cliente
from dao.dao_cliente import daoCliente

class ClienteDTO:
    def listarClientes(self):
        print("CLIENTE DTO FUNCIONANDO")
        """TODO: CAMBIAR ESTRUCTURA DE TRASPASO DE INFORMACIÓN PARA MEJOR LECTURA"""
        daocliente = daoCliente();
        clientes = daoCliente.listarClientes()
        lista = []

        if clientes is not None:
            for cliente in clientes:
                cliente = Cliente(
                    nombre=cliente[0], 
                    apellido=cliente[1], 
                    direccion=cliente[2],
                    documento=cliente[3],
                    tipoDocumento=cliente[4]
                )
                lista.append(cliente)
        return lista;