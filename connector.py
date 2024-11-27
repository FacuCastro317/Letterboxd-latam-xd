import sqlite3

def crear_base_de_datos ():

    # Crear una conexión a SQLite (creará un archivo si no existe)
    conexion = sqlite3.connect("escuela.db")

    # Crear un cursor para ejecutar comandos SQL
    cursor = conexion.cursor()

    # Crear tabla alumnos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alumnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        dni TEXT NOT NULL,
        fecha_nac DATE NOT NULL,
        correo TEXT UNIQUE NOT NULL,
        telefono TEXT
    )
    """)

    # Crear tabla profesores
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profesores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        correo TEXT UNIQUE NOT NULL,
        telefono TEXT
    )
    """)

    # Crear tabla materias
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS materias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT
    )
    """)

    # Crear tabla clases
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_materia INTEGER NOT NULL,
        id_profesor INTEGER NOT NULL,
        horario TEXT,
        FOREIGN KEY (id_materia) REFERENCES materias(id),
        FOREIGN KEY (id_profesor) REFERENCES profesores(id)
    )
    """)

    # Crear tabla inscripciones
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cursado (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_alumno INTEGER NOT NULL,
        id_clase INTEGER NOT NULL,
        nota INTEGER NOT NULL,
        FOREIGN KEY (id_alumno) REFERENCES alumnos(id),
        FOREIGN KEY (id_clase) REFERENCES clases(id)
    )
    """)

    print("Base de datos y tablas creadas exitosamente.")

    # Cerrar la conexión
    conexion.commit()
    conexion.close()


crear_base_de_datos()