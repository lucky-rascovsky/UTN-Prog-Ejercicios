"""
Dadas las siguientes listas:

Estudiantes =
["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Anto
nio", "Eugenia", "Soledad", "Mario", "María"]

Apellidos =
[“Sosa”,”Gutierrez”,”Alsina”,”Martinez”,”Sosa”,”Ramirez”,”Perez”,”Lopez”,”Arregui”
,”Mitre”,”Andrade”,”Loza”,”Antares”,”Roca”,”Perez”]

Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

Desarrollar una función que realice el ordenamiento de las listas por apellido de
manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera
ascendente, si el nombre también es el mismo, debe ordenar por nota de manera
descendente.
"""
def ordenar_apell_estud_nota(estudiantes: list, apellidos: list, nota: list)->list:
    for i in range(len(estudiantes) - 1):
        for j in range(i + 1, len(estudiantes)):
            if apellidos[i] > apellidos[j]:
                temp_apellidos = apellidos[i]
                apellidos[i] = apellidos[j]
                apellidos[j] = temp_apellidos

            elif apellidos[i] == apellidos[j]:
                if estudiantes[i] > estudiantes[j]:
                    temp_estudiantes = estudiantes[i]
                    estudiantes[i] = estudiantes[j]
                    estudiantes[j] = temp_estudiantes

                    if estudiantes[i] == estudiantes[j]:
                        if nota[i] < nota[j]:
                            temp_nota = nota[i]
                            nota[i] = nota[j]
                            nota[j] = temp_nota


estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]

apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]

nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

ordenar_apell_estud_nota(estudiantes, apellidos, nota)

print(f"{'Estudiantes':<25} {'Apellidos':>25} {'Nota':>25}")
print("-" * 90)
for i in range(len(estudiantes)):
    print(f"{estudiantes[i]:<25} {apellidos[i]:>25} {nota[i]:>25}")

