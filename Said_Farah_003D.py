planes = {
'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
'F003': ['Plan Estudiante', 'trimestral', 3, False, True,
'tarde'],
'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche']
}
inscripciones = {
'F001': [14990, 30],
'F002': [22990, 10],
'F003': [39990, 0],
'F004': [35990, 6],
'F005': [159990, 2],
'F006': [18990, 15]
}
def validacion_int(msg):
    while True:
        try:
            valor = int(input(msg))
            if valor <0:
                print("ERROR: ¡El valor ha de ser mayor o igual a 0!")
            else:
                return valor
        except ValueError:
            print("ERROR: ¡Debe ingresar valores enteros!")
def validacion_string(msg):
    while True:
        texto = (input(msg))
        texto = texto.strip()
        texto = texto.lower()
        if len(texto) <= 2:
            print("ERROR: ¡El texto no puede estár practicamente vacío!")
        else:
            return texto
def cupos_tipo(tipo):
    while True:
        existencia = False
        total_cupos = 0
        for codigo, datos in planes.items():
            if tipo == datos[1]:
                existencia = True
                total_cupos += inscripciones[codigo][1]
        if existencia == False:
            print("ERROR: ¡No se encontró ningun plan!")
            return
        elif existencia == True:
            print(f"El total de cupos disponibles es: {total_cupos}")
            return
def busqueda_precio(p_min, p_max):
    resultado = []
    existencia = False
    for codigo, datos in inscripciones.items():
        if datos[0] >= p_min and datos[0] <= p_max and datos[1] > 0:
            existencia = True
            resultado.append(f"{planes[codigo][0]}--{codigo}")
    if existencia == False:
        print("No hay planes en ese rango de precios")
    elif existencia == True:
        print(f"Los planes encontrados son: {resultado}")
def actualizar_precio(codigo, nuevo_precio):
    if codigo in inscripciones:
        inscripciones[codigo][0] = nuevo_precio
        return True
    else:
        return False

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
    opcion = validacion_int("Ingrese opción: ")
    if opcion < 1 or opcion > 6:
        print("ERROR: ¡Escoja una opción del 1 hasta al 6!")
    elif opcion == 1:
        tipo = validacion_string("Ingrese tipo de plan a consultar: ")
        cupos_tipo(tipo)
    elif opcion == 2:
        while True:
            p_min = validacion_int("Ingrese precio mínimo: ")
            p_max = validacion_int("Ingrese precio máximo: ")
            if p_min > p_max:
                print(f"ERROR: ¡El precio mínimo ({p_min}) ha de ser mayor que el precio máximo ({p_max})!")
            else:
                break
        busqueda_precio(p_min, p_max)
    elif opcion == 3:
        while True:
            codigo = validacion_string("Ingrese código del plan: ")
            codigo = codigo.upper()
            nuevo_precio = validacion_int("Ingrese nuevo precio: ")
            existencia = actualizar_precio(codigo, nuevo_precio)
            if existencia == True:
                print("Precio actualizado")
            elif existencia == False:
                print("El código no existe")
            while True:
                eleccion = input("¿Desea actualizar otro precio (s/n)?: ")
                eleccion = eleccion.strip()
                eleccion = eleccion.lower()
                if len(eleccion) > 1 or len(eleccion) < 1:
                    print("ERROR: ¡Ingrese o 's' para SÍ o 'n' para NO!")
                else:
                    break
            if eleccion == "s":
                continue
            elif eleccion == "n":
                break
    elif opcion == 4:
        print("DEBUG")
    elif opcion == 5:
        print("DEBUG")
    elif opcion == 6:
        print("DEBUG")
        break