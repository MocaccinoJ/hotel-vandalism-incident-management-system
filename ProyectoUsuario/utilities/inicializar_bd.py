from conex import conn
from datetime import datetime

def inicializar_bd():
    c = conn.Conex("localhost", "root", "", "superbase")

    try:
        cursor = c.getConex().cursor()

        # Crear tabla User si no existe
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            username VARCHAR(50) PRIMARY KEY,
            email VARCHAR(100),
            password VARCHAR(100),
            create_time DATETIME
        );
        """)

        # Crear tabla Empleado si no existe
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleado (
            codigo VARCHAR(20) PRIMARY KEY,
            nombre VARCHAR(50),
            apellido VARCHAR(50),
            direccion VARCHAR(100),
            sueldo DECIMAL(10,2)
        );
        """)

        # Crear tabla Cliente si no existe
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cliente (
            documento VARCHAR(20) PRIMARY KEY,
            nombre VARCHAR(50),
            apellido VARCHAR(50),
            direccion VARCHAR(100),
            tipoDocumento VARCHAR(20)
        );
        """)

        # Crear tabla Habitacion si no existe
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS habitacion (
            numero INT PRIMARY KEY,
            precio DECIMAL(10,2),
            disponible TINYINT(1)
        );
        """)

        # Crear tabla Reserva si no existe
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS reserva (
            numReserva INT PRIMARY KEY,
            fechaLlegada DATE,
            fechaSalida DATE,
            costoTotal DECIMAL(10,2),
            documentoCliente VARCHAR(20),
            codigoEmpleado VARCHAR(20),
            numeroHabitacion INT,
            FOREIGN KEY (documentoCliente) REFERENCES cliente(documento),
            FOREIGN KEY (codigoEmpleado) REFERENCES empleado(codigo),
            FOREIGN KEY (numeroHabitacion) REFERENCES habitacion(numero)
        );
        """)

        # Insertar usuarios iniciales si no existen
        cursor.execute("SELECT COUNT(*) FROM user")
        if cursor.fetchone()[0] == 0:
            cursor.executemany("""
                INSERT INTO user (username, email, password, create_time) VALUES (%s, %s, %s, %s)
            """, [
                ("admin", "admin@hotel.com", "admin123", datetime.now()),
                ("guest", "guest@hotel.com", "guest123", datetime.now())
            ])

        # Insertar empleados iniciales
        cursor.execute("SELECT COUNT(*) FROM empleado")
        if cursor.fetchone()[0] == 0:
            cursor.executemany("""
                INSERT INTO empleado (codigo,nombre,apellido,direccion,sueldo) VALUES (%s,%s,%s,%s,%s)
            """, [
                ("1","Juan","Perez","Calle Falsa 123",1200.50),
                ("2","Maria","Gomez","Avenida Siempre Viva 456",1500.00)
            ])

        # Insertar clientes iniciales
        cursor.execute("SELECT COUNT(*) FROM cliente")
        if cursor.fetchone()[0] == 0:
            cursor.executemany("""
                INSERT INTO cliente (documento,nombre,apellido,direccion,tipoDocumento) VALUES (%s,%s,%s,%s,%s)
            """, [
                ("1000001","Pepe","López","Calle Real 12","RUT"),
                ("1000002","Ana","Martínez","Avenida Central 45","Pasaporte")
            ])

        # Insertar habitaciones iniciales (ahora 5 habitaciones)
        cursor.execute("SELECT COUNT(*) FROM habitacion")
        if cursor.fetchone()[0] == 0:
            cursor.executemany("""
                INSERT INTO habitacion (numero,precio,disponible) VALUES (%s,%s,%s)
            """, [
                (101, 50000, 1),
                (102, 60000, 1),
                (103, 55000, 0),
                (104, 70000, 1),
                (105, 65000, 0)
            ])

        # Insertar reservas iniciales
        cursor.execute("SELECT COUNT(*) FROM reserva")
        if cursor.fetchone()[0] == 0:
            cursor.executemany("""
                INSERT INTO reserva (numReserva, fechaLlegada, fechaSalida, costoTotal, documentoCliente, codigoEmpleado, numeroHabitacion)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, [
                (1, "2025-10-01", "2025-10-05", 200000, "1001", "1", 101),
                (2, "2025-10-10", "2025-10-15", 300000, "1002", "2", 102)
            ])

        c.getConex().commit()
        print("Base de datos inicializada correctamente.")

    except Exception as e:
        print("¡Ha ocurrido un error al inicializar la base de datos!", e)
    finally:
        c.closeConex()