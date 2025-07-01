from funccalificaciones import *

# Lista de estudiantes (índice i)
estudiantes = ["Ana", "Bruno", "Carla", "Diego"]

materias = ["Matemática", "Historia", "Biología"]

# Matriz de calificaciones por estudiante [matemática, historia, biología]
calificaciones = [
    [9, 8, 10],    # Ana
    [6, 7, 8],     # Bruno
    [10, 10, 9],   # Carla
    [7, 6, 5]      # Diego
]

while True:
    print("*** Menu de opciones ***")
    print("1. para Mostrar la lista de estudiantes y la matriz de calificaciones")
    print("2. para Ordenar a los estudiantes de mayor a menor según su promedio general")
    print("3. para Buscar un estudiante por nombre y mostrar sus calificaciones")
    print("4. para Buscar una calificación en la matriz y mostrar a qué estudiante y materia pertenece")
    print("5. para Salir")
    opcion = int(input("Ingrese una opcion del Menu: "))
    if opcion == 1:
        mostrar_estudiantes_calificaciones(estudiantes, calificaciones)
    elif opcion == 2:
        ordenar_estudiantes_mayor_menor_promedio(estudiantes, calificaciones)
    elif opcion == 3:
        buscar_estudiante_mostrar_calificaciones(estudiantes, calificaciones)
    elif opcion == 4:
        buscar_calificacion(estudiantes, calificaciones, materias)
    elif opcion == 5:
        print("Gracias por usar el Programa. ¡Adios!")
        break
    else:
        print("Opción inválida. Por favor ingrese un número del 1 al 5.")