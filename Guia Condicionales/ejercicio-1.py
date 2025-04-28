"""
A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot

"""
altura = float(input("Ingrese la altura del jugador en centimetros: "))

if altura <= 0:
    print("Altura Invalida.")

elif altura < 160:
    print("La posicion del jugador es: Base")
else:
    if altura <= 179:
        print("La posicion del jugador es: Escolta")
    else:
        if altura <= 199:
            print("La posicion del jugador es: Alero")
        else:
            print("La posicion del jugador es: Ala-Pívot o Pívot")

print("Fin del Programa")