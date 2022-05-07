#entradas
agua = int(input("Ingresa el nivel del  agua: "))

#Proceso
if(agua > 6):
    print("Hay un desbordamiento en la cisterna")
elif(agua == 6):
    print("La cisterna está llena, apaga la bomba")
elif(agua >= 4 and agua < 6):
    print("Desacelera la bomba de agua")
elif(agua >= 2 and agua < 4): 
    print("Bomba trabajando")
elif(agua > 0 and agua < 2):
    print("Acelera la bomba de agua")
elif(agua == 0):
    print("No hay agua, encendiendo bomba de agua")
else: 
    print("Hay una fuga en la cisterna")