def create_inventory(items):
    diccionario = dict()
    for item in items:
        if item in diccionario:
            diccionario[item] += 1
        else:
            diccionario[item] = 1
    return diccionario

def add_items(inventario, items):
    for item in items:
        if item in inventario:
            inventario[item] += 1
        else:
            inventario[item] = 1
    return inventario

def decrement_items(inventario, items):

    for item in items:
        if item in inventario:  # Solo restamos si existe
            inventario[item] -= 1
            if inventario[item] < 0:
                inventario[item] = 0
    return inventario

def remove_item(inventario, item):
    if item in inventario.keys():
            del inventario[item]
    return inventario

def list_inventory(inventario):
    lista = []
    for item in inventario:
        if inventario[item] > 0:
            lista.append((item, inventario[item]))
    return lista

def find_max_value(diccionario):
    if not diccionario:
        return ""
    nombre_max = ""
    puntaje_max = float('-inf')
    for nombre, puntaje in diccionario.items():
        if puntaje > puntaje_max:
            puntaje_max = puntaje
            nombre_max = nombre
    return nombre_max

def reverse_dict(diccionario):
    nuevo = dict()
    for clave, valor in diccionario.items():
        if valor in nuevo:
            nuevo[valor] += clave
        else:
            nuevo[valor]=clave
    return nuevo

def word_frequency(palabras):

    if palabras == "":
        return {}
    res = {}
    for palabra in palabras:
        res[palabra] = res.get(palabra, 0) + 1
    return res

def find_biggest_expense(gastos):
    if not gastos:
        return ""
    else:
        categoria_max = ""
        promedio_max = -1

        for categoria, lista_gastos in gastos.items():

            promedio_actual = sum(lista_gastos) / len(lista_gastos)

            if promedio_actual > promedio_max:
                promedio_max = promedio_actual
                categoria_max = categoria

        return categoria_max

def sum_expenses(gastos):
    if not gastos:
        return {}
    resultado = {}
    for categoria, lista in gastos.items():
        resultado[categoria] = sum(lista)
    return resultado

def sum_expenses_by_type(gastos):
    nuevo = {}
    for categoria, lista_gastos in gastos.items():
        for tipo, gastos in lista_gastos:
            nuevo[tipo] = nuevo.get(tipo, 0) + gastos
    return nuevo