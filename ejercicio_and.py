"""
EJERICICIO 11 AND
"""

entrada = [10, 20, 30, 40]

valor = 24

def calcular_promedio(entrada:list, valor: int): #parametros formales
    contador = 0 
    valor = 24
    for i in range(len(entrada)):
        contador += entrada[i]
        contador % 4 
        if contador > valor:
            print("es mayor")
            return True
        else:
            print("es menor")
            return False

calcular_promedio(entrada, valor) # parametros actuales
