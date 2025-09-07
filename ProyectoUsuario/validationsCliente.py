from controlador.dto_cliente import ClienteDTO

def listarClientes():
    print("validationsClientes: ¡LISTAR TODOS LOS CLIENTES!")
    clientesEncontrados = ClienteDTO.listarClientes()
    if len(clientesEncontrados) > 0:
        for cliente in clientesEncontrados:
            print(cliente)
        else:
            print("¡No hay resultados!")
