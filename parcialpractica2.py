"""
Parcial de practica 2 !

Realizar el juego "Radar del Tesoro"
Dado el siguiente mapa de 5x5 donde se encuentra oculto un único tesoro, marcado con un 1:
mapa = [
[0, 0, 0, 0, 0],
[0, 0, 0, 1, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0] ]

Pedir al usuario una coordenada fila (x) entre 0 y 4 (inclusive).

Pedir al usuario una coordenada columna (y) entre 0 y 4 (inclusive).

Desarrollar una función con el siguiente prototipo:
verificar_tesoro(mapa: list, x: int, y: int) -> int

La función debe retornar:
- 0 si el usuario encontró el tesoro.
- En caso contrario, retornar la distancia Manhattan entre la coordenada ingresada y la ubicación real del
tesoro.

**Distancia Manhattan**:
distancia = |x_usuario - x_tesoro| + |y_usuario - y_tesoro|
Según el valor retornado, mostrar al usuario:
- "¡Encontraste el tesoro!" si retorna 0.
- "Fallaste. El tesoro está a X casilleros de distancia." si retorna otro número.
El juego continúa hasta que el usuario encuentre el tesoro o hasta que el usuario lo desee.

Nota: No se pueden utilizar funciones propias.

"""


coordenada_x = int(input("Ingrese una coordenada para la fila (x) entre (0-4) "))
coordenada_y = int(input("Ingrese una coordenada para la columna (y) entre (0-4) ")) 

while coordenada_x < 0 or coordenada_x > 4:
    coordenada_x = int(input("Error. Ingrese una coordenada para la fila Valida: "))
print("¡Coordenada valida!")
while coordenada_y < 0 or coordenada_y > 4:
    coordenada_y = int(input("Error. Ingrese una coordenada para la columna Valida: "))
print("¡Coordenada valida!")

mapa = [
[0, 0, 0, 0, 0],
[0, 0, 0, 1, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0] ]

def verificar_tesoro(mapa: list, coordenada_x: int, coordenada_y: int) -> int:
    seguir = "s"
    while seguir == "s":
        for i in mapa:
            if coordenada_x == 1 and coordenada_y == 3:
                encontro_tesoro = i
                print("¡Encontraste el tesoro!")
                return encontro_tesoro
        else:
            distancia = coordenada_x - 1 + coordenada_y - 3
            print(f"Fallaste. El tesoro está a {distancia} casilleros de distancia.")
            seguir = input("Desea seguir jugando? (s/n)")  
    return distancia


verificar_tesoro(mapa, coordenada_x, coordenada_y)

