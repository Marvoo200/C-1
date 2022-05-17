preguntas =[
    "1. Herramienta de programación, parecido al lenguaje español utilizado para crear código.",
    "2. Conjunto de símbolos, letras, números, imágenes, audio y video organizadas y que son relevantes en un tiempo y forma determinados",
    "3. Instituciones encargadas de estandarizar reglas y simbología de los Diagramas de Flujo.",
    "4. Serie de pasos consecutivos, ordenados y finitos que se siguen para resolver un problema.",
    "5. Conjunto de elementos que se relacionan para cumplir una función determinada.",
    "6. Componente de un IDE que se encarga de traducir el código fuente a código máquina.",
    "7. Elemento que se usa para almacenar una cantidad donde cambia su valor.",
    "8. Conjunto de símbolos, letras, números que no tienen un significado.",
    "9. Disciplina que argumenta conclusiones a partir de premisas mediante un razonamiento.",
    "10. Medida, patrón, modelo o norma universal para realizar una actividad o producir un objeto.",
    "11. Conjunto de elementos ordenados que componen y son la base de algo físico o no físico.",
    "12. Conjunto de instrucciones (código) que indican a la computadora tareas a realizar."
    ]

respuestas =["     a) IDE     b) Pseudocódigo     c) Compilador     d) ANSI / ISO",
             "     a) Información     b) Datos     c) Programa     d) Código",
             "     a) IEEE     b) IDE     c) ANSI/ISO     d) VSCode",
             "     a) Proceso     b) Solución     c) Función     d) Algoritmo",
             "     a) Estructura     b) Datos     c) Operación     d) Sistema",
             "     a) Depurador     b) Editor de Texto     c) Terminal de Salida     d) Compilador/Intérprete",
             "     a) Constante     b) Variable     c) Librería     d) Tipo de Dato",
             "     a) Datos     b) Estructura     c) Información     d) Sistema",
             "     a) Filosofía     b) Sociología     c)Lógica     d)Argumentación",
             "     a) Evento     b) Estándar     c) Calidad     d) Productividad",
             "     a) Estructura     b) Sistema     c) Objeto     d) Virtual",
             "     a) Operaciones/Cálculos     b) Sintaxis     c) Programa de Computadora     d) Comando"
            ]
correctas = ["B", "A", "C", "D", "D", "D", "B", "A", "C", "B", "A", "C"]
score = 0
print("\n\nLea las preguntas e ingrese la letra de la respuesta\n\n")

for i in range(0, 12, 1):
    print("\n", preguntas[i], "\n",respuestas[i], "\n")
    respuesta = input("Ingresa la letra de la respuesta: ")

    if(respuesta.upper() == correctas[i]):
        print("\nRespuesta correcta ^_^\n")
        score +=1
    else:
        print("\nLa respuesta correcta era: ", correctas[i])

calificacion = score * 10 / 12

print("Tu calificación final es: ", round(calificacion, 2), " tuviste ", score, " preguntas correctas")