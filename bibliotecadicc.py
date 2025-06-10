'''
BIBLIOTECA DE FUNCIONES EJERCICIOS DICCIONARIOS (ESTUDIANTES)
'''
from estudiantes import *

def menu_de_opciones():
    seguir = "s"
    while seguir == "s":
        print("*** Menu de opciones ***")
        print("1. para Listar los alumnos por orden ascendente de apellido")
        print("2. para Obtener el promedio de notas para cada estudiante")
        print("3. para Listar legajo, nombre, apellido y edad de los estudiantes que cursan el programa de (Ingenieria en Informatica)")
        print("4. para Obtener un promedio de edad de los estudiantes.")
        print("5. para Informar el alumno con mayor promedio de notas.")
        print("6. para Listar nombre y apellido de los alumnos que forman el grupo (Club de Informática) con sus respectivos promedios")
        print("7. para Listar legajo, nombre, apellido y programas que cursan los alumnosmás jóvenes")
        print("8. para Salir")
        opcion = int(input("Ingrese una opcion del Menu: "))
        while opcion < 1 or opcion > 8:
            opcion = int(input("Ingrese una opcion valida. 1-8: "))
        if opcion == 1:
            print("\n", listar_apellido_nombre_asc(estudiantes))
        elif opcion == 2:
            print("\n", obtener_promedio_notas_estudiante(estudiantes))
        elif opcion == 3:
            print("\n", listar_estudiantes_ing_informatica(estudiantes))
        elif opcion == 4:
            print("\n", obtener_promedio_edad_estudiante(estudiantes))
        elif opcion == 5:
            print("\n", informar_alumno_mayor_promedio_nota(estudiantes))
        elif opcion == 6:
            print("\n", listar_nombre_apellido_club_informatica(estudiantes))
        elif opcion == 7:
            print("\n", listar_alumnos_mas_jovenes(estudiantes))
        elif opcion == 8:
            seguir = "n"
            print("Gracias por usar el Programa. ¡Adios!")
    

# -------------------OPCION 1 DEL MENU DE OPCIONES--------------------
def listar_apellido_nombre_asc (estudiantes:list):
    '''
    Funcion que recibe como parametro la lista de diccionarios estudiantes, realiza el ordenamiento e imprime la lista ordenada, retorna un string vacio.
    '''
    for i in range(len(estudiantes) - 1):
        for j in range(i + 1, len(estudiantes)):
            if estudiantes[i]["apellido"] > estudiantes[j]["apellido"]:
                aux = estudiantes[i]
                estudiantes[i] = estudiantes[j]
                estudiantes[j] = aux
        
            elif estudiantes[i]["apellido"] == estudiantes[j]["apellido"]:
                if estudiantes[i]["nombre"] > estudiantes[j]["nombre"]:
                    temp_nombres = estudiantes[i]
                    estudiantes[i] = estudiantes[j]
                    estudiantes[j] = temp_nombres
    print("Listado Ordenado: \n")

    print(f"{'Legajo':<25} {'Nombre':>25} {'Apellido':>25} {'Edad':>25}")
    print("-" * 118)
    for k in range(len(estudiantes)):
        print(f"{estudiantes[k]['legajo']:<25} {estudiantes[k]['nombre']:>25} {estudiantes[k]['apellido']:>25} {estudiantes[k]['edad']:>25}")

    
    return ""


# -------------------OPCION 2 DEL MENU DE OPCIONES--------------------
def obtener_promedio_notas_estudiante (estudiantes:list):
    '''
    Funcion que recibe como parametro la lista de diccionarios estudiantes, obtiene el promedio de las notas e imprime nombre, apellido y nota promedio de cada estudiante, retorna un string vacio.
    '''
    lista_promedio_notas = []
    suma = 0
    lista_notas = []
    for estudiante in estudiantes:
        lista_notas = estudiante['notas']
        for elemento in range(len(lista_notas)):
            suma += lista_notas[elemento]
            promedio = suma / len(estudiantes)
            lista_promedio_notas.append(promedio)
    
    print(f"{'Nombre':>25} {'Apellido':>25} {'Nota Promedio':>25}")
    print("-" * 118)


    for i in range(len(estudiantes)):
        nombre = estudiantes[i]['nombre']
        apellido = estudiantes[i]['apellido']
        promedio = lista_promedio_notas[i]
        print(f"{nombre:>25} {apellido:>25} {promedio:>25.2f}")

    return ""



# -------------------OPCION 3 DEL MENU DE OPCIONES--------------------
def listar_estudiantes_ing_informatica(estudiantes:list):
    '''
    Funcion que recibe como parametro la lista de diccionarios estudiantes, realiza una lista que contiene el respectivo legajo, nombre, apellido y edad de los estudiantes que que cursan el programa (Ingenieria en Informatica) e imprime la lista con sus valores, retorna un string vacio.
    '''
    print(f"{'Legajo':>15} {'Nombre':>15} {'Apellido':>15} {'Edad':>15}")
    print("-" * 80)
    for estudiante in estudiantes:
        if estudiante['programa']['nombre'] == "Ingenieria en Informatica":
            print(f"{estudiante['legajo']:>15} {estudiante['nombre']:>15} {estudiante['apellido']:>15} {estudiante['edad']:>15}")
    return ""




# -------------------OPCION 4 DEL MENU DE OPCIONES-------------------- 
def obtener_promedio_edad_estudiante(estudiantes:list):
    '''
    Funcion que recibe como parametro la lista de diccionarios estudiantes, obtiene el promedio de las edades de los estudiantes e imprime nombre, apellido y edad promedio de cada estudiante, retorna un string vacio.
    '''
    lista_promedio_edades = []
    suma = 0
    promedio = 0
    for estudiante in estudiantes:
        suma += estudiante['edad']
        promedio = suma / len(estudiantes)
        lista_promedio_edades.append(promedio)
    
    print(f"{'Nombre':>25} {'Apellido':>25} {'Edad Promedio':>25}")
    print("-" * 118)


    for j in range(len(estudiantes)):
        nombre = estudiantes[j]['nombre']
        apellido = estudiantes[j]['apellido']
        promedio = lista_promedio_edades[j]
        print(f"{nombre:>25} {apellido:>25} {promedio:>25.2f}")
    return ""



# -------------------OPCION 5 DEL MENU DE OPCIONES-------------------- 
def informar_alumno_mayor_promedio_nota(estudiantes:list):
    '''
    Funcion que recibe como parametro la lista de diccionarios estudiantes, informa el alumno con mayor promedio de notas e imprime respectivo nombre y apellido, retorna un string vacio.
    '''
    lista_notas = []
    mayor_promedio = 0
    suma_notas = 0
    mejor_estudiante = None
    for estudiante in estudiantes:
        lista_notas = estudiante['notas']
    
        if lista_notas:  
            suma_notas = 0
            for nota in lista_notas:
                suma_notas += nota
            promedio = suma_notas / len(lista_notas)

            if promedio > mayor_promedio:
                mayor_promedio = promedio
                mejor_estudiante = estudiante

    if mejor_estudiante:
        print(f"El estudiante con mayor promedio es: {mejor_estudiante['nombre']} {mejor_estudiante['apellido']}")
        print(f"Promedio: {mayor_promedio:.2f}")
    else:
        print("No hay estudiantes con notas.")
    return ""


# -------------------OPCION 6 DEL MENU DE OPCIONES-------------------- 
def listar_nombre_apellido_club_informatica(estudiantes:list):
    '''
    Funcion que recibe como parametro la lista de diccionarios estudiantes, realiza una lista que contiene el respectivo nombre, apellido y promedio de los estudiantes que que cursan el programa (Club de Informatica) e imprime nombre, apellido y promedio de cada estudiante, retorna un string vacio.
    '''
    print(f"{'Nombre':>15} {'Apellido':>15} {'Promedio':>15}")
    print("-" * 50)

    for estudiante in estudiantes:
        if "grupos" in estudiante:
            for grupo in estudiante["grupos"]:
                if "nombre" in grupo and grupo["nombre"] == "Club de Informatica":
                    notas = estudiante["notas"]
                    suma = 0
                    for nota in notas:
                        suma += nota
                        if len(notas) > 0:
                            promedio = suma / len(notas)
                        else:
                            promedio = 0
                    print(f"{estudiante['nombre']:>15} {estudiante['apellido']:>15} {promedio:>15.2f}")
    return ""



# -------------------OPCION 7 DEL MENU DE OPCIONES-------------------- 
def listar_alumnos_mas_jovenes(estudiantes:list):
    '''
    Funcion que recibe como parametro la lista de diccionarios estudiantes, realiza una lista que contiene el respectivo legajo, nombre, apellido y programa de los estudiantes mas jovenes e imprime nombre, apellido y programa de cada estudiante, retorna un string vacio.
    '''
    for i in range(len(estudiantes)):
        if estudiantes[i]["edad"] <= 24:
            print(f"legajo: {estudiantes[i]['legajo']}-estudiante: {estudiantes[i]['nombre']} {estudiantes[i]['apellido']}--- programa: {estudiantes[i]['programa']['nombre']}")
    return ""