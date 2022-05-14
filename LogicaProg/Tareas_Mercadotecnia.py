#Funciones de mercadotecnia


'''
1.- Publicidad
2.- Estudio de mercado
3.- Precios del producto
4.- Logística
5.- Ventas

'''

def Publicidad(cantidad_banner, costos_banner):
    total_costos_banner = cantidad_banner * costos_banner
    print("\n\nEl precio de los banners es de: ", total_costos_banner)


def Logistica(transporteA, transporteB):
    total_distancia_transportar = transporteA + transporteB 
    print("\n\nLa distancia total es de: ", total_distancia_transportar)

def Ventas(cantidad_productos, costo_producto):
    total_ventas = cantidad_productos * costo_producto * IVA  
    print("\n\nEl total de ventas es de: ", total_ventas)

def Estudio_Mercado (personas_gusto, personas_no_gusto):
    promedio = (personas_gusto - personas_no_gusto)/100
    print("\n\nEl promedio de las personas que les gusto es de: ", promedio)

def Precios(costos, porcentaje_ganancia):
    precio = costos * (porcentaje_ganancia/100 + 1)
    print("\n\nEl precio en que nos sale es de: ", precio)

def Menu():
    print("\n\nBienvenido")
    print("1.-Publicidad")
    print("2.-Estudio de Mercado")
    print("3.-Precios del producto")
    print("4.-Logistica")
    print("5.-Ventas")
    print("6.-Salir")





#Entrada de datos

costos_banner = 100 #De publicidad / imagenes publicitarias
transporteA = 10 #Km
IVA = 0.16
cantidad_banner = 1000
transporteB = 20 #Km
cantidad_productos = 10000
costo_producto = 50
costos = 5
porcentaje = 10
personas_gusto = 40
personas_no_gusto = 10
#Procesos


#con switch no se puede hacer llamado de funciones, solo sirve como si fuera una lista ):

op = 0
while(op != 6):

    Menu()
    op = int(input("Ingresa la opción deseada: "))
    if(op == 1):
        Publicidad(cantidad_banner, costos_banner)
    elif(op == 2): 
        Estudio_Mercado(personas_gusto, personas_no_gusto)
    elif(op == 3): 
        Precios(costos, porcentaje)
    elif(op == 4): 
        Logistica(transporteA, transporteB)
    elif(op == 5): 
        Ventas(cantidad_productos, costo_producto)
    elif(op == 6): 
        print("De acuerdo, hasta luego ^_^")
    else:
        print("\n\nOpción invalida ):")

   

#Salidas



