import datetime, connector 
from manip_bd import insertar_datos

connector.crear_base_de_datos()

def ingresar_datos():

    opcion = input("""Indique qué datos desea ingresar:
          1- Ingresar alumnos.
          2- Ingresar profesor.
          3- Ingresar materia.
          4- Ingresar clase.
          5- Ingresar notas.
          6- Volver.
          """)

    if opcion == "1":
        agregar_alumno()
    elif opcion == "2":
        agregar_profesor()
    elif opcion == "3":
        agregar_materia()
    elif opcion == "4":
        agregar_clase()
    elif opcion == "5":
        agregar_notas()
    elif opcion == "6":
        menu()
    else:
        print("Opcion inválida. Por favor intente de nuevo.")
        ingresar_datos()

def agregar_alumno():
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    nro_documento = input("Ingrese número de documento: ")
    fecha_nacimiento = input("Ingrese fecha de nacimiento (YYYY-MM-DD): ")
    correo = input("Ingrese correo: ")
    telefono = input("Ingrese teléfono: ")
    
    alumno = (nombre, apellido, nro_documento, fecha_nacimiento, correo, telefono)

    insertar_datos("alumnos", ["nombre", "apellido", "dni", "fecha_nac", "correo", "telefono"],
                      alumno)
    print("Alumno ingresado con éxito.")
    menu()
    

def agregar_profesor():
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    correo = input ("Ingrese el correo electronico.")
    telefono = input ("Ingrese el numero de telefono.")

    profesor = (nombre, apellido, correo, telefono)

    insertar_datos("profesores", ["nombre", "apellido", "correo", "telefono"], profesor)

    print("Los datos han sido ingresados.")
    menu()

def agregar_materia():
    nombre = input("Ingrese nombre de la materia: ")
    descripcion = input("Realice una descripcion:")

    materia = (nombre, descripcion)

    insertar_datos("materias", ["nombre", "descripcion"], materia)

    print("Materia registrada con exito.")
    menu()


def agregar_clase():
    id_materia = int(input("Ingrese el ID de la materia:"))
    id_profesor = int(input("Ingrese el ID del profesor"))
    horario = input("Ingrese el horario de cursada")

    clase = (id_materia, id_profesor, horario)

    insertar_datos("clases", ["id_materia", "id_profesor", "horario"], clase)

    print("Clase registrada con éxito.")
    menu()


def agregar_notas():
    id_alumno = int(input("Ingrese el ID de alumno: "))
    id_clase = int(input("Ingrese el ID de la clase: "))
    nota = int(input("Ingrese la nota del alumno (1-10): "))

    cursado = (id_alumno, id_clase, nota)

    insertar_datos("cursado", ["id_alumno", "id_clase", "nota"], cursado)

    print("Nota cargada con exito.")
    menu()


def consultar_personas(personas):
    for persona in personas:
        print(persona)

def eliminar_persona(personas):
    id_usuario = int(input("Ingrese ID de usuario a eliminar: "))
    personas[:] = [persona for persona in personas if persona["ID"] != id_usuario]

def ordenar_personas(personas, criterio):
    if criterio == "alfabetico":
        personas.sort(key=lambda x: (x["Apellido"], x["Nombre"]))
    elif criterio == "id":
        personas.sort(key=lambda x: x["ID"])
    elif criterio == "edad":
        personas.sort(key=lambda x: x["Fecha de Nacimiento"])

def listar_personas(personas):
    for persona in personas:
        print(persona)

def menu():
    while True:
        print("\nMenu:")
        print("1. Ingreso de datos")
        print("2. Consulta de datos")
        print("3. Eliminación de datos")
        print("4. Ordenamiento por cualquier criterio")
        print("5. Listado de datos ordenados por pantalla")
        print("6. Salida")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ingresar_datos()
        elif opcion == "2":
            consultar_personas(personas)
        elif opcion == "3":
            eliminar_persona(personas)
        elif opcion == "4":
            print("Criterios de ordenamiento:")
            print("1. Alfabético")
            print("2. Numérico por ID de usuario")
            print("3. Por edad")
            criterio = input("Seleccione un criterio: ")
            if criterio == "1":
                ordenar_personas(personas, "alfabetico")
            elif criterio == "2":
                ordenar_personas(personas, "id")
            elif criterio == "3":
                ordenar_personas(personas, "edad")
        elif opcion == "5":
            listar_personas(personas)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu()
