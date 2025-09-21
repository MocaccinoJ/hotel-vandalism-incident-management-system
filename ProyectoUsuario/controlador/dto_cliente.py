from modelo.cliente import Cliente
from dao.dao_cliente import daoCliente

class ClienteDTO:
    def listarClientes(self):
        """TODO: CAMBIAR ESTRUCTURA DE TRASPASO DE INFORMACIÓN PARA MEJOR LECTURA"""
        daocliente = daoCliente();
        clientes = daocliente.listarClientes()
        print("CLIENTES: ",clientes)
        lista = []
        if clientes is not None:
            for cliente in clientes:
                print("CLIENTE: ",cliente)
                cliente = Cliente(
                    nombre=cliente[0], 
                    apellido=cliente[1], 
                    direccion=cliente[2],
                    documento=cliente[3],
                    tipoDocumento=cliente[4]
                )
                lista.append(cliente)
        print("LISTA: ",lista)
        return lista;
    
    def buscarCliente(self, documento):
        daocliente = daoCliente()
        documento = Cliente(documento=documento)
        cliente = daocliente.buscarCliente(documento)
        if cliente is not None:
            cliente = Cliente(
                    nombre = cliente[0], 
                    apellido = cliente[1], 
                    direccion = cliente[2],
                    documento = cliente[3],
                    tipoDocumento = cliente[4]
            )
            return cliente
        return None


    def agregarCliente(self, nombre, apellido, direccion, documento, tipoDocumento):
        cliente = Cliente(nombre = nombre, apellido = apellido, direccion = direccion, documento=documento, tipoDocumento=tipoDocumento)
        
        print("HOLA!")
        print(cliente)
        return daoCliente().agregarCliente(cliente)
    
    def actualizarCliente(self, nombre, apellido, direccion, documento, tipoDocumento):
        cliente = Cliente(nombre = nombre, apellido = apellido, direccion = direccion, documento = documento, tipoDocumento = tipoDocumento)
        daocliente = daoCliente()
        clienteActualizado=daocliente.actualizarCliente(cliente)

        print("CLIENTE ACTUALIZADO: ",clienteActualizado)

    def eliminarCliente(self, documento):
        cliente = Cliente(documento=documento)
        print("CLIENTE: ",cliente)
        daocliente = daoCliente()
        
        clienteEliminado = daocliente.eliminarCliente(cliente)
        
        return clienteEliminado