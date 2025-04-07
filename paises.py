#Coleccion de paises:
paises = [
    {  "nombre": "Colombia",
       "capital": "Bogota",
       "moneda": "Peso colombiano",
       "ciudades":
        [   
            {
                "nombre": "Bogota",
                "poblacion": 8.2,
                "fundacion": 1538,
            },
            {
                "nombre": "Medellin",
                "poblacion": 2.5,
                "fundacion": 1675,
            },
            {
                "nombre": "Cali",
                "poblacion": 2.3,
                "fundacion": 1536,
            },
           
           
        ]
    },
    { "nombre": "Peru",
       "capital": "Lima",
       "moneda": "Sol peruano",
       "ciudades":
       [   
            {
                "nombre": "Lima",
                "poblacion": 3.6,
                "fundacion": 1538,
            },
            {
                "nombre": "Arequipa",
                "poblacion": 6.5,
                "fundacion": 1556,
            },
            {
                "nombre": "Cusco",
                "poblacion": 1.3,
                "fundacion": 1678,
            },
           
           
        ]
    },
    { "nombre": "Mexico",
       "capital": "Ciudad de Mexico",
       "moneda": "Peso Mexicano",
       "ciudades":
       [   
            {
                "nombre": "Ciudad de Mexico",
                "poblacion": 10.2,
                "fundacion": 1567,
            },
            {
                "nombre": "Guadalajara",
                "poblacion": 6.5,
                "fundacion": 1635,
            },
            {
                "nombre": "Monterrey",
                "poblacion": 4.3,
                "fundacion": 1598,
            },
           
           
        ]
    },
    { "nombre": "Argentina",
       "capital": "Buenos Aires",
       "moneda": "Peso Argentino",
       "ciudades":
       [   
            {
                "nombre": "Buenos Aires",
                "poblacion": 11.2,
                "fundacion": 1538,
            },
            {
                "nombre": "La plata",
                "poblacion": 2.5,
                "fundacion": 1675,
            },
            {
                "nombre": "Rosario",
                "poblacion": 3.8,
                "fundacion": 1667,
            },
           
           
        ]
    },
]

#Iterar cada pais 
print( "-------------------" )
print( "Recorrido de Paises" )
print( "-------------------" )   
for pais in paises:
    print("Nombre:", pais["nombre"])
    print("Capital:", pais["capital"])
    print("Moneda", pais["moneda"])
    print( "-------------------" )   
    print("Ciudades principales de ", pais["nombre"])
    for ciudad in pais["ciudades"]:
        print("--ciudad", ciudad["nombre"])
        print(" poblacion", ciudad["poblacion"])
        print(" fundacion", ciudad["fundacion"])
    print( "-------------------" )