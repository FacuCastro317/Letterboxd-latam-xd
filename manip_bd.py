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

def mostrar_tabla(tabla):
    """
    Imprime todos los resultados de la tabla especificada.

    Args:
        tabla (str): Nombre de la tabla a consultar.

    Returns:
        None
    """
    # Conexión a la base de datos
    conexion = sqlite3.connect("escuela.db")
    cursor = conexion.cursor()
    
    try:
        # Consulta para obtener todos los datos de la tabla
        query = f"SELECT * FROM {tabla}"
        cursor.execute(query)
        
        # Recuperar resultados
        resultados = cursor.fetchall()
        
        # Obtener nombres de columnas
        columnas = [descripcion[0] for descripcion in cursor.description]
        
        # Imprimir resultados
        if resultados:
            print(f"Resultados de la tabla '{tabla}':")
            print(f"{' | '.join(columnas)}")  # Encabezados de columnas
            for fila in resultados:
                print(f"{' | '.join(map(str, fila))}")
        else:
            print(f"La tabla '{tabla}' no tiene datos.")
    except sqlite3.Error as e:
        print(f"Error al consultar la tabla '{tabla}': {e}")
    finally:
        conexion.close()

mostrar_tabla("cursado")