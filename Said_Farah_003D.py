planes = {
'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
'F003': ['Plan Estudiante', 'trimestral', 3, False, True,
'tarde'],
'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],
}
inscripciones = {
'F001': [14990, 30],
'F002': [22990, 10],
'F003': [39990, 0],
'F004': [35990, 6],
'F005': [159990, 2],
'F006': [18990, 15],
}
def validacion_int(msg):
    while True:
        try:
            valor = int(input(msg))
            if valor <=0:
                print("ERROR: ¡El valor ha de ser mayor a 0!")
            else:
                return valor
        except ValueError:
            print("ERROR: ¡El valor ha de ser entero númerico!")
while True:
    print("""
========== MENÚ PRINCIPAL ==========
1. Cupos por tipo de plan
2. Búsqueda de planes por rango de precio
3. Actualizar precio de plan
4. Agregar plan
5. Eliminar plan
6. Salir
=====================================""")
    opcion = validacion_int("Ingrese opción:")
    if opcion < 1 or opcion > 6:
        print("ERROR: ¡Escoja una opción del 1 hasta al 6!")
    elif opcion == 1:
        print("DEBUG")
    elif opcion == 2:
        print("DEBUG")
    elif opcion == 3:
        print("DEBUG")
    elif opcion == 4:
        print("DEBUG")
    elif opcion == 5:
        print("DEBUG")
    elif opcion == 6:
        print("DEBUG")
        break