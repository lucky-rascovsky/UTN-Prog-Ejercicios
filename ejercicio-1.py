"""
Dadas las siguientes listas:
Nombres =
["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Anto
nio", "Eugenia", "Soledad", "Mario", "Mariela"]

Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

Desarrollar una función que realice el ordenamiento de las listas por nombre de
manera ascendente.

Manera mas bonita de mostrar los datos:
print("{:<30} {:<20}".format("Apellidos", "Notas"))

"""
def ordenar_nombre_asc(nombres: list, edades: list):
    for i in range(len(nombres) - 1):
        for j in range(i + 1, len(nombres)):
            if nombres[i] > nombres[j]:
                temp_nombre = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = temp_nombre
                temp_edad = edades[i]
                edades[i] = edades[j]
                edades[j] = temp_edad


nombres = ["Ana", "Luis", "Juan", "Sol", "Roberto", "Sonia", "Ulises", "Sofía", "María", "Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]

edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

ordenar_nombre_asc(nombres, edades)
print("{:<30} {:<20}".format("Nombres", "Edades"))
print("-" * 45)
for i in range(len(nombres)):
    print("{:<30} {:<20}".format( nombres[i], edades[i]))
