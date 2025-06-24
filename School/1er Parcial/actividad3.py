import re  # Nuestra librería para expresiones regulares

documentos_act1 = [
    "La programación en Python es una habilidad fundamental para cualquier desarrollador de software que desee mejorar sus conocimientos en estructuras de datos, inteligencia artificial y desarrollo web. Aprender a implementar algoritmos eficientes permite optimizar el rendimiento de cualquier aplicación y facilita la solución de problemas en diversos campos tecnológicos.",
    "El fútbol es un deporte apasionante que une a millones de personas alrededor del mundo. Desde las ligas locales hasta los torneos internacionales, los aficionados disfrutan de cada partido con entusiasmo. Equipos históricos como el Barcelona y el Real Madrid han marcado épocas con jugadores legendarios y momentos inolvidables.",
    "La inteligencia artificial ha transformado diversas industrias, desde la medicina hasta la automoción. Algoritmos de aprendizaje profundo permiten diagnósticos más precisos, mientras que los coches autónomos prometen cambiar la movilidad urbana. A medida que la tecnología avanza, surgen debates sobre la ética y el impacto en el mercado laboral."
]


# Construcción de un índice invertido con frecuencia de palabras en cada documento
def construir_indice_invertido_con_frecuencia(documentos):
    indice_invertido = {}  # Diccionario para guardar el índice con "frecuencia"

    for document_id, texto in enumerate(documentos, start=1):
        palabras = re.findall(r'\b\w+\b', texto.lower())

        for palabra in palabras:
            if palabra not in indice_invertido:
                indice_invertido[palabra] = {}

            # Incrementamos la cuenta para este documento
            if document_id not in indice_invertido[palabra]:
                indice_invertido[palabra][document_id] = 0

            indice_invertido[palabra][document_id] += 1

    return indice_invertido

def buscar_palabra(indice_invertido, palabra):
    palabra = palabra.lower()
    return indice_invertido.get(palabra, {})


# Función para buscar varias palabras en una misma consulta
def buscar_varias_palabras(indice_invertido, consulta):
    palabras = consulta.lower().split()
    resultados = {}
    for palabra in palabras:
        resultados[palabra] = indice_invertido.get(palabra, {})
    return resultados


# Ejemplo de uso:
if __name__ == "__main__":
    # Construimos el índice invertido con frecuencias
    indice_con_frecuencia = construir_indice_invertido_con_frecuencia(documentos_act1)

    # Ejemplo de consulta para varias palabras:
    consulta = "inteligencia artificial caporal"   #Aqui metemos todas de golpe para que se haga la búsqueda en los docs de act1_2
    resultados_consulta = buscar_varias_palabras(indice_con_frecuencia, consulta)
    print("\nResultados de búsqueda para la consulta:", consulta)
    for palabra, info in resultados_consulta.items():
        print(f"La palabra '{palabra}' se encuentra en: {info}")



# Comentario sobre rendimiento (parte final):
#
# La implementación anterior mejora la eficiencia en búsquedas, ya que, una vez construido el índice,
# cada consulta (incluso de múltiples palabras) se realiza en tiempo constante por palabra (O(1)).
# Perooo, se incrementa el uso de memoria debido al almacenamiento de las frecuencias de cada palabra.
# Este trade-off entre tiempo y espacio es común en optimizaciones de índices invertidos.
