
import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="DB_reseniando"
    )
    cursor = connection.cursor()
    print("Conexión exitosa a la base de datos")
except mysql.connector.Error as err:
    print(f"Error: no se pudo conectar a la BD. Detalles: {err}")
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión cerrada correctamente")