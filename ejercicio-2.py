"""
Dadas las siguientes listas:
Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias
Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos",
"Base de Datos", "Ergonomia", "Naturaleza"]

Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

Desarrollar una función que realice el ordenamiento de las listas por nombre de
manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera
descendente.
"""
def ordenar_nombre_asc_y_puntos_desc(nombres: list, puntos: list):
    for i in range(len(nombres) - 1):
        for j in range(i + 1, len(nombres)):
            if nombres[i] > nombres[j]:
                temp_nombre = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = temp_nombre

                temp_puntos = puntos[i]
                puntos[i] = puntos[j]
                puntos[j] = temp_puntos

            elif nombres[i] == nombres[j]:
                if puntos[i] < puntos[j]:
                    temp_puntos = puntos[i]
                    puntos[i] = puntos[j]
                    puntos[j] = temp_puntos



nombres = ["Matemática", "Investigación Operativa", "Inglés", "Literatura", "Ciencias Sociales", 
"Computación", "Inglés", "Álgebra"]

puntos = [100, 95, 87, 38, 64, 42, 28, 91]


ordenar_nombre_asc_y_puntos_desc(nombres, puntos)


print(f"{'Asignatura':<25} {'Puntos':>6}")
print("-" * 35)
for i in range(len(nombres)):
    print(f"{nombres[i]:<25} {puntos[i]:>6}")
