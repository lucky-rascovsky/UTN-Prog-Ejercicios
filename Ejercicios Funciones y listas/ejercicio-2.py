"""
Desarrollar una función que inicialice una lista de 10 números en 0, pida
posición y número a guardar al usuario, lo guarde en una lista en la posición
solicitada aleatoriamente y la retorne. El programa principal debe invocar a la
función y mostrar por pantalla el retorno.
"""
mi_lista = [0] *10


def inicializar_lista ()->list:
        """
        Funcion sin parametros, que recibe una lista de 10 numeros incicializada en 0, solicita la posicion y el numero a guardar y guarda ambos en una lista dentro de la posicion seleccionada por el usuario aleatoriamente y retorna la lista.
        """
        respuesta = "s" 
        while respuesta =="s":
                posicion = int(input("Ingrese la posicion de la lista entre 0-9: "))
                numero = int(input(" ingrese un numero: "))
                mi_lista[posicion] = numero
                respuesta = input("ingresa otro? s/n: ")
        for i in range(len(mi_lista)):
            if mi_lista [i] > 0:
                print("Numero: ", mi_lista[i])
                print("Posicion: ", i)
        print("Fin del programa.")
        return mi_lista

inicializar_lista()