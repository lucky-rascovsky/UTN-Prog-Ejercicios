"""
Desarrollar una función que pida 10 números dentro de un rango
especificado, validar los números solicitados dentro de ese rango, guardar en una
lista y retornarla. El programa principal debe invocar a la función y mostrar por
pantalla el retorno.
"""
mi_lista = [0] *10

def pedir_numeros ()->list:
    """
    Funcion sin parametros que recibe una lista, solicita al usuario 10 numeros dentro del rango (1-10), valida los numeros dentro del rango y los guarda en una lista y la retorna.
    """
    for i in range(len(mi_lista)):
        numero = int(input("ingrese un numero entre (1-10): "))
        mi_lista[i] = numero
        print(mi_lista[i])
        while numero < 1 or numero > 10:
            numero = int(input("Ingrese un numero dentro del rango: "))
    return mi_lista


pedir_numeros()