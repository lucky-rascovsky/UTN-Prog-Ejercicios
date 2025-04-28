"""
Ejercicio 2:
Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
adolescente (entre 13 y 17 años) o niño (menor a 13 años).
"""

edad = int(input("Ingrese su Edad: "))

if edad < 13:
    print("Usted es Niño")
elif edad < 17:
    print("Usted es Adolescente")
elif edad >= 18:
    print("Usted es Mayor de edad")

print("Fin del programa")