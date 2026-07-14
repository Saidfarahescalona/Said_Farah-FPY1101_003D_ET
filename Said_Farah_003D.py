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
        if len(texto) == 0:
            print("ERROR: ¡El texto no puede estár vacío!")
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
def validador_código(codigo):
    if codigo in planes:
        return False
    elif len(codigo) == 0:
        return False
    else:
        return True
def validador_nombre(nombre):
    if len(nombre) == 0:
        return False
    else:
        return True
def validador_tipo(tipo):
    if tipo == "mensual":
        return True
    elif tipo == "trimestral":
        return True
    elif tipo == "anual":
        return True
    else:
        return False
def validador_duración(duracion):
    if duracion <= 0:
        return False
    else:
        return True
def validador_acceso_piscina(piscina):
    if piscina == "s":
        return True
    elif piscina == "n":
        return False
def validador_incluye_clases(clases):
    if clases == "s":
        return True
    elif clases == "n":
        return False
def validador_horario(horario):
    if len(horario) == 0:
        return False
    else:
        return True
def validador_precio(precio):
    if precio <= 0:
        return False
    else:
        return True
def validador_cupos(cupos):
    if duracion < 0:
        return False
    else:
        return True
def agregar_plan(codigo, nombre, tipo, duracion, piscina, clases, horario, precio, cupos):
    lista_planes = [nombre, tipo, duracion, piscina, clases, horario]
    lista_inscripciones = [precio, cupos]
    #planes.append(codigo:lista_planes)
    #inscripciones.append(codigo:lista_inscripciones)
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
        while True:
            codigo = input("Ingrese código del plan: ")
            codigo = codigo.strip()
            codigo = codigo.upper()
            validador = validador_código(codigo)
            if validador == False:
                print("ERROR: ¡El código no puede estar en blanco ni tampoco estár ya existente!")
                continue
            elif validador == True:
                nombre = input("Ingrese nombre del plan: ")
                nombre = nombre.strip()
                nombre = nombre.capitalize()
                validador = validador_nombre(nombre)
                if validador == False:
                    print("ERROR: ¡El nombre no puede estár vacío!")
                    continue
                elif validador == True:
                    tipo = input("Ingrese tipo (mensual/trimestral/anual): ")
                    tipo = tipo.strip()
                    tipo = tipo.lower()
                    validador = validador_tipo(tipo)
                    if validador == False:
                        print("ERROR: ¡Debe ser exactamente 'mensual', 'trimestral' o 'anual'!")
                        continue
                    elif validador == True:
                        try:
                            duracion = int(input("Ingrese duración (meses): "))
                            validador = validador_duración(duracion)
                            if validador == False:
                                print("ERROR: ¡La duración ha de ser mayor que 0!")
                            elif validador == True:
                                piscina = input("¿Incluye acceso a piscina? (s/n): ")
                                picina = piscina.strip()
                                piscina = piscina.lower()
                                validador = validador_acceso_piscina(piscina)
                                if validador == False:
                                    piscina = validador
                                elif validador == True:
                                    piscina = validador
                                    clases = input("¿Incluye clases grupales? (s/n): ")
                                    clases = clases.strip()
                                    clases = clases.lower()
                                    validador = validador_incluye_clases(clases)
                                    if validador == False:
                                        clases = validador
                                    elif validador == True:
                                        clases = validador
                                        horario = input("Ingrese horario: ")
                                        horario = horario.strip()
                                        horario = horario.lower()
                                        validador = validador_horario(horario)
                                        if validador == False:
                                            print("ERROR: ¡El horario no puede estar vacío!")
                                            continue
                                        elif validador == True:
                                            try:
                                                precio = int(input("Ingrese precio: "))
                                                validador = validador_precio(precio)
                                                if validador == False:
                                                    print("ERROR: ¡El precio tiene que ser mayor a 0!")
                                                    continue
                                                elif validador == True:
                                                    try:
                                                        cupos = int(input("Ingrese cupos: "))
                                                        validador = validador_cupos(cupos)
                                                        if validador == False:
                                                            print("ERROR: ¡Los cupos tienen que ser mayores o igual a 0!")
                                                            continue
                                                        elif validador == True:
                                                            agregar_plan(codigo, nombre, tipo, duracion, piscina, clases, horario, precio, cupos)
                                                            break
                                                    except ValueError:
                                                        print("ERROR: ¡El valor ha de ser un numero entero!")
                                                        continue
                                            except ValueError:
                                                print("ERROR: ¡El valor ha de ser un numero entero!")
                                                continue
                        except ValueError:
                            print("ERROR: ¡El valor ha de ser un numero entero!")
                            continue        
        if validador == True:
            print("Plan agregado")
        elif validador == False:
            print("Codigo ya existente")
    elif opcion == 5:
        print("DEBUG")
    elif opcion == 6:
        print("DEBUG")
        break