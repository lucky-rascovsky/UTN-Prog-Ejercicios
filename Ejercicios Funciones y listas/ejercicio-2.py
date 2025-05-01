"""
Desarrollar una función que inicialice una lista de 10 números en 0, pida
posición y número a guardar al usuario, lo guarde en una lista en la posición
solicitada aleatoriamente y la retorne. El programa principal debe invocar a la
función y mostrar por pantalla el retorno.
"""
def inicializar_lista ()->list:
        """
        Funcion sin parametros, que recibe una lista de 10 numeros incicializada en 0, solicita la posicion y el numero a guardar y guarda ambos en una lista dentro de la posicion seleccionada por el usuario aleatoriamente y retorna la lista.
        """
        mi_lista = [0] *10
        respuesta = "s" 
        while respuesta =="s":
                posicion = int(input("Ingrese la posicion de la lista entre 0-9: "))
                numero = int(input(" ingrese un numero: "))
                mi_lista[posicion] = numero
                respuesta = input("ingresa otro? s/n: ")
        return mi_lista

lista_retornada = []
lista_retornada = inicializar_lista()
print("Numero y Posicion:")
for i in range(len(lista_retornada)):
            if lista_retornada [i] > 0:
                print("Numero: ", lista_retornada[i])
                print("Posicion: ", i)
