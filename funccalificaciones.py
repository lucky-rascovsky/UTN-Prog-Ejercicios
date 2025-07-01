#-----------------------------FUNCIONES GESTION DE CALIFICACIONES-------------------------
#------------------------------1-----------------------------------------------------
def mostrar_estudiantes_calificaciones(estudiantes:list, calificaciones:list):
    '''Muestra la lista de estudiantes y la matriz de calificaciones'''
    print("\nEstado actual de la lista de estudiantes y matriz de calificaciones:")
    print("Lista de Estudiantes: ")
    for i in range(len(estudiantes)):
        print(f"Estudiante: {estudiantes[i]}")
    for j in range(len(calificaciones)):
        for k in range(len(calificaciones[j])):
            celda = calificaciones[j][k]
            print(f"Posicion en Matriz fila/columna: [{j},{k}] Nombre: {estudiantes[j]} Calificacion: {celda}")



#-------------------------2-----------------------------------------------
def ordenar_estudiantes_mayor_menor_promedio(estudiantes:list, calificaciones:list):
    '''Ordena de mayor a menor segun el promedio del estudiante'''
    promedios = []
    for i in range(len(calificaciones)):
        total = 0
        for j in range(len(calificaciones[i])):
            total += calificaciones[i][j] / 3
        promedios.append(total)

    for i in range(len(estudiantes) - 1):
        for j in range(i + 1, len(estudiantes)):
            if promedios[i] < promedios[j]:
                aux_total = promedios[i]
                promedios[i] = promedios[j]
                promedios[j] = aux_total

                aux_calif = estudiantes[i]
                estudiantes[i] = estudiantes[j]
                estudiantes[j] = aux_calif

    print("Estudiantes ordenados de mayor a menor según sus promedios:")
    for i in range(len(estudiantes)):
        print("Estudiante:", estudiantes[i])
        print("Promedio:", promedios[i])


#--------------------------------3-----------------------------------------
def buscar_estudiante_mostrar_calificaciones(estudiantes:list, calificaciones:list):
    """Busca estudiante por nombre y muestra sus calificaciones."""
    while True:
        nombre = input("Ingrese el nombre del estudiante: ")
        
        
        resultado = None
        for i in range(len(estudiantes)):
            if estudiantes[i].lower() == nombre.lower():  
                resultado = calificaciones[i]
                break
        
        if resultado != None:  
            print(f"Calificaciones de {estudiantes[i]}: Matemática = {resultado[0]}, Historia = {resultado[1]}, Biología = {resultado[2]}")
            break
        else:
            print(f"¡Error! El nombre '{nombre}' no está en la lista. Intente nuevamente.")
    


#-----------------------------------4------------------------------------
def buscar_calificacion(estudiantes:list, calificaciones:list, materias:list):
    '''Busca una calificacion y muestra su respectivo estudiante y materia correspondiente'''
    while True:
        entrada = input("Ingrese la calificación a buscar (entre 5 y 10): ")
        es_numero = True
        for c in entrada:
            if not (c >= '0' and c <= '9'):
                es_numero = False
                break
        
        if es_numero and entrada:
            calificacion = int(entrada)
            if 5 <= calificacion <= 10:
                break
            else:
                print("La calificación debe estar entre 5 y 10.")
        else:
            print("Ingrese solo números enteros.")
    
    
    encontrados = False
    for i in range(len(estudiantes)):
        for j in range(len(materias)):
            if calificaciones[i][j] == calificacion:
                print(f"Estudiante: {estudiantes[i]} | Materia: {materias[j]}")
                encontrados = True
    
    if not encontrados:
        print("No se encontraron estudiantes con esa calificación.")