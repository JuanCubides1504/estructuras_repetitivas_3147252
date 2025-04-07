#Diccionarios:

##Son colecciones de datos
##Cada elemento en un diccionario 
##se puede dividir en 2 partes:
# ##    1. clave: el nombre del elemento 
# ##    2. valor: el valor del elemento
## Ejemplo de un diccionario:
## Para caracterizar un pais:

pais = {
    "nombre": "Colombia",
    "capital": "Bogota",
    "idioma": "Español",
    "poblacion": 51,
    "superficie": 1141748,
    "moneda": "Peso colombiano",
    "ciudades":[ 
        "Bogota",
        "Medellin",
        "Cali",
        "Barranquilla",
        "Cartagena",
    ]
}

#acceder a propiedades
print("Capital de Colombia:", pais["capital"])
print("Y se habla:", pais["idioma"])
print("Habitantes:", pais["poblacion"])
print ("y sus ciudades son:")
for ciudad in pais["ciudades"]:
    print(ciudad)
