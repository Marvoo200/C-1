
a = 0
numero = 0
promedio = 0
'''while(numero >=0):
    
    numero = float(input("Ingresa un numero: "))
    if (numero>0):
        promedio += numero
        a+=1
    else:
        print("Numero negativo invalido, obteniendo promedio")
'''
while(numero >=0):
    promedio += numero
    a+=1
    numero = float(input("Ingresa un numero: "))

    
promedio = promedio/a
print("El promedio es: ", promedio)



        