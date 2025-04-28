"""
Ejercicio 1:
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
sueldo para esa persona.
"""
nombre = input("Ingrese su nombre: ")
sueldo = int(input("Ingrese su sueldo: "))

incremento = sueldo * 0.10

print(f"El aumento de sueldo para {nombre} es de {incremento}")
print("Fin del programa")