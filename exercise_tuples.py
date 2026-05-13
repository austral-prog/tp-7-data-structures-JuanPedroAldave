def get_coordinate(registro):
    return registro[1]

def convert_coordinate(coordenada):
    return (coordenada[0] , coordenada[1])

def create_record(registro_azara, registro_rui):
    cord_azara = convert_coordinate(registro_azara[1])
    if cord_azara == registro_rui[1]:
        return (registro_azara + registro_rui)
    else:
        return "not a match"

def sum_tuple(numeros):
    numeros_suma = 0
    for num in numeros:
        numeros_suma += num
    return numeros_suma

def count_occurrences(tupla, elemento):
    count = 0
    for i in tupla:
        if elemento == i:
            count += 1
    return count

def find_index(tupla, elemento):
    pos=-1
    i = 0
    while i < len(tupla) and pos == -1:
        if tupla[i] == elemento:
            pos= i
        i += 1
    return pos
print(find_index(('a', 'b', 'c', 'b'), 'b'))
def filter_positives(numeros):
    tupla = ()
    for n in numeros:
        if n > 0:
            tupla = tupla + (n,)
    return tupla