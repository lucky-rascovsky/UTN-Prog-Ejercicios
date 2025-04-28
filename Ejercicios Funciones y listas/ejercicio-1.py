"""
Desarrollar una función que pida 10 nombres de manera secuencial, los
guarde en una lista y la retorne. El programa principal debe invocar a la función y
mostrar por pantalla el retorno.
"""
mi_lista = [0] *10

def pedir_nombre ()->list:
    """
    Funcion sin parametros que recibe una lista/array que solicita 10 nombres al usuario de manera secuencial, los guarda en una lista y retorna la misma.
    """
    for i in range(len(mi_lista)):
        nombre = input("ingrese un nombre: ")
        mi_lista[i] = nombre
        print("En la posicion", i, "se encuentra ", nombre)
    for i in range(len(mi_lista)):
        print(mi_lista[i])
    print("Fin del programa.")
    return mi_lista

pedir_nombre()