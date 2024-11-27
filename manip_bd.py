import sqlite3

def insertar_datos(tabla, columnas, valores):
    """
    Inserta datos en la tabla indicada.

    Args:
        El argumento de la tabla debe ser string.
        El de las columnas una lista.
        El de los valores una tupla.

    Ejemplo:
        insertar_datos("alumnos", ["nombre", "apellido", "fecha_nac", "correo", "telefono"], 
                       ("Juan", "Pérez", "2000-05-15", "juan.perez@example.com", "123456789"))
    """
    # Conexión a la base de datos
    conexion = sqlite3.connect("escuela.db")
    cursor = conexion.cursor()
    
    # Crear una consulta dinámica
    columnas_str = ", ".join(columnas)
    placeholders = ", ".join(["?" for _ in valores])
    query = f"INSERT INTO {tabla} ({columnas_str}) VALUES ({placeholders})"
    
    try:
        cursor.execute(query, valores)
        conexion.commit()
        print(f"Datos insertados exitosamente en la tabla {tabla}.")
    except sqlite3.Error as e:
        print(f"Error al insertar datos: {e}")
    finally:
        conexion.close()