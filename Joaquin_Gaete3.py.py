import json

archivo_datos = "datos_estudiantes.json"

def cargar_datos():

    try:
        with open("datos.json", "r") as file:
            estudiantes = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        estudiantes = {}
    return estudiantes

def guardar_datos(estudiantes):

    with open("datos.json", "w") as file:
        json.dump(estudiantes, file, indent=4)

def registrar_estudiante(estudiantes):

    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese los apellidos del estudiante: ")
    matematicas = float(input("Ingrese nota de matemáticas: "))
    ciencias = float(input("Ingrese nota de ciencias: "))
    historia = float(input("Ingrese nota de historia: "))
    
    promedio = (matematicas + ciencias + historia) / 3
    
    estudiantes[nombre] = {
        "apellido": apellido,
        "notas": {
            "matematicas": matematicas,
            "ciencias": ciencias,
            "historia": historia},
        "promedio": promedio
    }
    
    guardar_datos(estudiantes)
    print("Estudiante registrado exitosamente.")

def buscar_estudiante(estudiantes):

    nombre = input("Ingrese nombre del estudiante a buscar: ")
    if nombre in estudiantes:
        print(f"Información del estudiante {nombre}:")
        print(f"Apellido: {estudiantes[nombre]['apellido']}")
        print(f"Notas: {estudiantes[nombre]['notas']}")
        print(f"Promedio: {estudiantes[nombre]['promedio']}")
    else:
        print("Estudiante no encontrado.")

def mostrar_lista_estudiantes(estudiantes):

    print("Lista de estudiantes registrados:")
    for nombre, datos in estudiantes.items():
        print(f"Nombre: {nombre}")
        print(f"Apellido: {datos['apellido']}")
        print(f"Notas: {datos['notas']}")
        print(f"Promedio: {datos['promedio']}")
        print("")

def eliminar_estudiante(estudiantes):

    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    if nombre in estudiantes:
        del estudiantes[nombre]
        guardar_datos(estudiantes)
        print("Estudiante eliminado exitosamente.")
    else:
        print("Estudiante no encontrado.")

def main():
    estudiantes = cargar_datos()
    
    while True:
        print("\nMenu de Registro/Busqueda de estudiantes y Promedios:")
        print("1. Registrar estudiante")
        print("2. Buscar estudiante por nombre")
        print("3. Mostrar la lista de estudiantes")
        print("4. Eliminar estudiante")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            registrar_estudiante(estudiantes)
        elif opcion == "2":
            buscar_estudiante(estudiantes)
        elif opcion == "3":
            mostrar_lista_estudiantes(estudiantes)
        elif opcion == "4":
            eliminar_estudiante(estudiantes)
        elif opcion == "5":
            guardar_datos(estudiantes)
            print("¡Hasta Pronto!")
            break
        else:
            print("Opcion incorrecta. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()