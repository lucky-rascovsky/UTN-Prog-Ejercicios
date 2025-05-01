"""
Desarrollar una función que pida 10 nombres de manera secuencial, los
guarde en una lista y la retorne. El programa principal debe invocar a la función y
mostrar por pantalla el retorno.
"""
def pedir_nombre ()->list:
    """
    Funcion sin parametros que recibe una lista/array que solicita 10 nombres al usuario de manera secuencial, los guarda en una lista y retorna la misma.
    """
    mi_lista = [0] *10

    for i in range(len(mi_lista)):
        nombre = input("ingrese un nombre: ")
        mi_lista[i] = nombre
    
    return mi_lista


lista_retornada = []
lista_retornada = pedir_nombre()
print("Nombres:")
for i in range(len(lista_retornada)):
    print(lista_retornada[i])
