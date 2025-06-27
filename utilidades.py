import csv


TABLERO = [
    0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 1, 0, 0, 0, 2,  
    1, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0   
]
POSICION_INICIAL = 15
POSICION_GANADOR = len(TABLERO) - 1
POSICION_PERDEDOR = 0

def cargar_preguntas():
    """Importa las preguntas desde preguntas.py."""
    from preguntas import preguntas
    return preguntas

def mostrar_pregunta(pregunta):
    """Muestra una pregunta y sus opciones."""
    print("\n" + pregunta["pregunta"])
    print(f"a) {pregunta['respuesta_a']}")
    print(f"b) {pregunta['respuesta_b']}")
    print(f"c) {pregunta['respuesta_c']}")

def guardar_puntaje(nombre:str, posicion:int):
    """Guarda el puntaje en Score.csv."""
    with open("Score.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nombre, posicion])

def verificar_respuesta(pregunta, respuesta:str):
    """Retorna True si la respuesta es correcta."""
    return respuesta == pregunta["respuesta_correcta"]

def calcular_nueva_posicion(posicion_actual:int, respuesta_correcta):
    """Aplica el movimiento básico (+1/-1) y despues el efecto del casillero destino."""
    
    if respuesta_correcta:
        nueva_posicion = posicion_actual + 1
        print(f"\n¡Correcto! Avanzas al casillero {nueva_posicion}.")
    else:
        nueva_posicion = posicion_actual - 1
        print(f"\n¡Incorrecto! Retrocedes al casillero {nueva_posicion}.")
    
    
    if nueva_posicion < 0:
        nueva_posicion = 0
    elif nueva_posicion >= len(TABLERO):
        nueva_posicion = len(TABLERO) - 1

    
    if 0 <= nueva_posicion < len(TABLERO):
        efecto = TABLERO[nueva_posicion]
        if efecto != 0:
            if respuesta_correcta:  
                posicion_final = nueva_posicion + efecto
                print(f"¡Escalera en {nueva_posicion}! Avanzas {efecto} casilleros más (-> {posicion_final}).")
            else:  
                posicion_final = nueva_posicion - abs(efecto)  
                print(f"¡Serpiente en {nueva_posicion}! Retrocedes {abs(efecto)} casilleros (<- {posicion_final}).")
            
            if posicion_final < 0:
                posicion_final = 0
            elif posicion_final >= len(TABLERO):
                posicion_final = len(TABLERO) - 1
            
            nueva_posicion = posicion_final

    print(f"Posición final: {nueva_posicion}")
    return nueva_posicion


def juego_terminado(posicion:int):
    """Retorna True si el juego debe terminar."""
    return posicion >= POSICION_GANADOR or posicion <= POSICION_PERDEDOR

def input_validado(mensaje, opciones_validas):
    """
    Valida que el input del usuario esté en las opciones válidas.
    """
    while True:
        respuesta = input(mensaje).lower()
        if respuesta in opciones_validas:
            return respuesta
        print(f"Error: Ingresa una de estas opciones: {', '.join(opciones_validas)}")