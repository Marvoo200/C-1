#Arreglos o listas
'''
Conjunto de elementos o valores de uno o más tipos de datos

'''
#sintaxis:
#nombre_arreglo = [elementos]

#Entradas de datos

nombres = ["Marvin", "Uriel", "Eduardo"]
edades = [20, 24, 30]

arreglo_lista = [10, 5.7, "Hola", True]

#OPERACIONES CON ARREGLOS

'''Modificar un elemento del arreglo'''
nombres [0] = "Marvin Toribio"
nombres [1] = "Uriel David"
'''Agregar un elemento de un Arreglo'''
edades.append(10)
'''Ordenar los elementos del arreglo'''
edades.sort() #ordena numeros de manera ascendente
edades.reverse()#ordena numeros de manera descendente
#Salida de Datos

print(nombres)
print(edades)
print(arreglo_lista)