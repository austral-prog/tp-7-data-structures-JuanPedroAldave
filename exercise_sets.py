ALCOHOLS = {
    "whiskey", "whisky", "white rum", "dark rum", "bourbon", "rye", "scotch",
    "vodka", "tequila", "gin", "dry vermouth", "sweet vermouth", "prosecco",
    "aperol", "brandy", "mezcal", "triple sec", "coffee liqueur",
    "almond liqueur", "champagne", "orange curacao", "rum"
}


def clean_ingredients(nombre_plato, ingredientes):
    sin_duplicados = set(ingredientes)
    return nombre_plato, sin_duplicados

def check_drinks(nombre_bebida, ingredientes):
    for ingrediente in ingredientes:

        if ingrediente in ALCOHOLS:

            return f"{nombre_bebida} Cocktail"

    return f"{nombre_bebida} Mocktail"

print(check_drinks('Shirley Tonic',
             ['cinnamon stick', 'scotch', 'whole cloves', 'ginger']))
def unique_chars(texto):
    return set(texto)


def sum_set(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

def common_elements(set_a, set_b):
    return {elemento for elemento in set_a if elemento in set_b}