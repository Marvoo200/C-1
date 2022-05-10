#Funciones: Tareas a ejecutar
def Sumar(a, b): #Obtiene o recibe parámetros o argumentos
    suma = a+b   #contenido de la funcion
    return suma #return es devolver o retornar o regresar un valor.

def Restar (x, y):
    return x - y

def Multiplicar (num1, num2):
    multi = num1 * num2
    return multi

def Dividir(f, g):
    div = f/g
    return div

num1 = int(input("Ingresa el 1er número: "))
num2 = int(input("Ingresa el 2do número: "))

#Mandar a llamar o invocar las funciones
s = Sumar(num1,num2) #son parametros que se le envían o pasan
r = Restar(num1,num2)
d = Dividir(num1, num2)


print("La suma es = ", s)
print("La resta es = ", r)
print("La multiplicacion es = ", Multiplicar(num1, num2))
print("La multiplicacion es = ", d)
