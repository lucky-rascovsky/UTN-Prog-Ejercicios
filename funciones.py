# FUNCIONES REUTILIZABLES

# FUNCIONES-3-1
def mostrar_num(num)->int:
    """
    Funcion que muestra por pantalla el numero ingresado por el usuario.
    """
    print("El numero ingresado es: ", num)

# FUNCIONES-3-2
def num_ingresado() -> int:
    """
    Funcion que solicita un numero al usuario, lo muestra por pantalla y lo retorna.
    """
    num = int(input("Ingrese un numero: "))
    print(num)
    return num

# FUNCIONES-3-3
def determinar_par(num1:int)-> bool:
    """
    Funcion que determina si un numero es es par o no, retorna True en caso afirmatvo, caso contrario retorna False, se realiza invocacion por llamada en el programa principal.
    """
    resultado = False
    if num1 % 2 == 0:
        resultado = True
        print(f"El {num1} es un numero par (No es primo)")
    else:
        print(f"El {num1} es un numero primo")
    return resultado