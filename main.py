from utilidades import (
    cargar_preguntas, mostrar_pregunta, guardar_puntaje,
    verificar_respuesta, calcular_nueva_posicion, juego_terminado,
    input_validado, POSICION_INICIAL, POSICION_GANADOR
)
import random

def iniciar_juego():
    """Función principal que ejecuta el juego."""
    preguntas = cargar_preguntas()
    nombre = input("¡Bienvenido! Ingresa tu nombre: ").strip()
    
    while True:
        jugar = input_validado(
            f"{nombre}, ¿deseas jugar? (s/n): ",
            ["s", "n"]
        )
        if jugar != 's':
            print("¡Hasta luego!")
            return
        
        posicion_actual = POSICION_INICIAL
        
        while True:
            pregunta_actual = random.choice(preguntas)
            mostrar_pregunta(pregunta_actual)
            
            respuesta = input_validado(
                "Elija una opción (a/b/c): ",
                ["a", "b", "c"]
            )
            
            correcta = verificar_respuesta(pregunta_actual, respuesta)
            posicion_actual = calcular_nueva_posicion(posicion_actual, correcta)
            
            if juego_terminado(posicion_actual):
                if posicion_actual >= POSICION_GANADOR:
                    print("¡Felicidades! Ganaste el juego.")
                else:
                    print("¡Ups! Caíste en el casillero perdedor.")
                guardar_puntaje(nombre, posicion_actual)
                break
            
            continuar = input_validado(
                "¿Quieres seguir jugando? (s/n): ",
                ["s", "n"]
            )
            if continuar != 's':
                guardar_puntaje(nombre, posicion_actual)
                print(f"Fin del juego. Tu posición final es: {posicion_actual}")
                break
        break

if __name__ == "__main__":
    iniciar_juego()