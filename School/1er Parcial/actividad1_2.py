import re  #Nuestra librería para expresiones regulares

documentos_act1 = [
    "La programación en Python es una habilidad fundamental para cualquier desarrollador de software que desee mejorar sus conocimientos en estructuras de datos, inteligencia artificial y desarrollo web. Aprender a implementar algoritmos eficientes permite optimizar el rendimiento de cualquier aplicación y facilita la solución de problemas en diversos campos tecnológicos.",
    "El fútbol es un deporte apasionante que une a millones de personas alrededor del mundo. Desde las ligas locales hasta los torneos internacionales, los aficionados disfrutan de cada partido con entusiasmo. Equipos históricos como el Barcelona y el Real Madrid han marcado épocas con jugadores legendarios y momentos inolvidables.",
    "La inteligencia artificial ha transformado diversas industrias, desde la medicina hasta la automoción. Algoritmos de aprendizaje profundo permiten diagnósticos más precisos, mientras que los coches autónomos prometen cambiar la movilidad urbana. A medida que la tecnología avanza, surgen debates sobre la ética y el impacto en el mercado laboral."
]


def construir_indice_invertido(documents):
    indice_invertido = {}  #Diccionario para guardar el índice

    for document_id, texto in enumerate(documents, start=1):
        palabras = re.findall(r'\b\w+\b', texto.lower())  # Extraemos las palabrichis, quitamos su puntiacion (si tienen) y las hacemo minisculas con lower

        for palabra in set(palabras):  # Usamos `set` para evitar palabras duplicadas en el mismo documento
            if palabra not in indice_invertido:
                indice_invertido[palabra] = []
            indice_invertido[palabra].append(document_id)

    return indice_invertido


def buscar_palabra(indice_invertido):
    while True:
        palabra = input("Ingresa la palabra que deseas buscar o ingresa salir para terminar proceso: ").lower() #Pedimos la palabra a buscar al usuario y la hacemos miniscula con lower

        if palabra in indice_invertido:
            print(f"La palabra '{palabra}' se encuentra en los documentos: {indice_invertido[palabra]}") #Se busca la palabra, las llaves es para ingresar la palabra (sintaxis vista en lo de las listas solopython)
        else:
            print(f"La palabra '{palabra}' no se encuentra en ningún documento.") #No se encontro la palabrichi

        if palabra == "salir":
            print("Saliendo...")
            break

# Construimos el índice invertido
indice = construir_indice_invertido(documentos_act1)

# Permitimos al usuario buscar palabras
buscar_palabra(indice)
