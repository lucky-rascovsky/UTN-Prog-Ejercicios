"""
: Crear una función que permita determinar si un número es par o no. La
función retorna “True” en caso afirmativo y “False en caso contrario. Probar en el
programa principal realizando la invocación o llamada.
"""

from funciones import determinar_par



numero = int(input("Ingrese un numero: "))
if determinar_par(numero):
    print(f"{numero} es Par")
else: 
    print(f"{numero} es Impar")