"""
Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
4 y 5                ---> Aprobado, la nota es ...
1, 2 y 3            ---> Desaprobado, la nota es ...
"""

nota = int(input("Ingrese una nota (entre 1/10): "))

if nota <= 0:
    print("Nota Invalida.")
else:
    if nota <= 3:
        print("Desaprobado, la nota es: ", nota)
    else: 
        if nota <= 5:
            print("Aprobado, la nota es: ", nota)
        else: 
            if nota <= 10:
                print("Promocion directa, la nota es: ", nota)
            else:
                print("Nota Invalida.")

print("Fin del Programa")