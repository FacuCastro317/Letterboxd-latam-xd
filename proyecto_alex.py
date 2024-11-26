import datetime

def agregar_persona(personas):
    id_usuario = int(input("Ingrese ID de usuario: "))
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    nro_documento = input("Ingrese número de documento: ")
    fecha_nacimiento = input("Ingrese fecha de nacimiento (YYYY-MM-DD): ")
    telefono = input("Ingrese teléfono: ")
    domicilio = input("Ingrese domicilio: ")
    
    persona = {
        "ID": id_usuario,
        "Nombre": nombre,
        "Apellido": apellido,
        "Nro Documento": nro_documento,
        "Fecha de Nacimiento": datetime.datetime.strptime(fecha_nacimiento, "%Y-%m-%d"),
        "Teléfono": telefono,
        "Domicilio": domicilio
    }
    
    personas.append(persona)

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
    personas = []
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
            agregar_persona(personas)
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
