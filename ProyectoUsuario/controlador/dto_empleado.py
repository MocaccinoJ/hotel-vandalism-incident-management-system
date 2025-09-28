from modelo.empleado import Empleado
from dao.dao_empleado import daoEmpleado

class EmpleadoDTO:
    def listarEmpleados(self):
        dao = daoEmpleado()
        empleados = dao.listarEmpleados()
        lista = []
        if empleados:
            for e in empleados:
                empleado_objeto = Empleado(
                    nombre=e[0],
                    apellido=e[1],
                    direccion=e[2],
                    codigo=e[3],
                    sueldo=e[4]
                )
                lista.append(empleado_objeto)
        return lista
# TODO: Probar buscar empleados
    def buscarEmpleado(self, codigo):
        daoempleado = daoEmpleado()
        codigo = Empleado(codigo = codigo)
        empleado = daoempleado.buscarEmpleado(codigo)
        if empleado:
            return Empleado(
                nombre=empleado[0],
                apellido=empleado[1],
                direccion=empleado[2],
                codigo=empleado[3],
                sueldo=empleado[4]
            )
        return empleado

    def agregarEmpleado(self, nombre, apellido, direccion, codigo, sueldo):
        empleado = Empleado(
                    nombre=nombre,
                    apellido=apellido,
                    direccion=direccion,
                    codigo=codigo,
                    sueldo=sueldo
                )
        dao = daoEmpleado()
        return dao.agregarEmpleado(empleado)

   
    def actualizarEmpleado(self, nombre, apellido, direccion, codigo, sueldo):
        empleado = Empleado(nombre, apellido, direccion, codigo, sueldo)
        print("Empleado DTO: ", empleado)
        dao = daoEmpleado()
        return dao.actualizarEmpleado(empleado)


    def eliminarEmpleado(self, codigo):
        empleado = Empleado(codigo = codigo)
        daoEmpleado = daoEmpleado()
        return daoEmpleado.eliminarEmpleado(empleado)
