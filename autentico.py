import os
import random
import calendar

def menu():
   os.system('cls')
   print ("Carta")
   print ("\t1 - Entradas")
   print ("\t2 - Platos de fondo")
   print ("\t3 - Bebidas")
   print ("\t4 - salir")
   print("Escoja una opción:")
   return(' ')

def menudia():
    cl = calendar.TextCalendar()
    c_abril = cl.formatmonth(2018,4)
    print(c_abril)
    os.system('cls')
    print("\t1 - Menú del día")
    print("\t2 - Elegir desde Carta:")
    return ('')

def carta():
    os.system('cls')
    print("\t1 - Menú del día")
    print("\t2 - Elegir desde Carta:")
    return ('')

print("Bienvenidos al restaurante Pytec:")
print("¿Ha reservado?:")
print("1 - He reservado")
print("2 - No he reservado")
print("Según sus preferenias escoja un número:")
y = int(input())

if y == 1:
    print("Gracias, su mesa es: ", (random.randrange(10)))
    print(carta())
    n = int(input())
    if n ==1:
        print (menudia())
    if n==2:
        print(menu())
    else:
        print("porfavor seleccione de los números dados")

if y == 2:
   print("Espere una mesa libre")
if y!= 1 and y != 2:
   print("No existe esa opción...")
x = int(input())
if x == 4:
   print("fin del programa, gracias por su preferencia :)")


#codigos para insertar parte del menu
for e in range(1,n+1):
  print("inserte fruta: ",end='')
  x = str(input())
  print()


"uso de diccionario para los precios"
postres = {
   'pasteles':['tres leches', 'mil hojas','torta de chocolate'],
       'helados':['chocolate','uva','vainilla','fresa','lúcuma','maracuyá']}
sopitas = {
    'cremas':['de espinaca','de lacayote','de maíz','de papa','de coliflor']}
Piqueos_Picanteros = {'especial','escribano de la casa','caliente','frío','torrejas a la Arequipeña','Mote de Habas'}

#caja
"suma de valores anteriores"

#promociones
"apilamiento de ambos datos"

import os

def menu():
    os.system('cls')
    print ("Carta")
    print ("\t1 - Entradas")
    print ("\t2 - Platos de fondo")
    print ("\t3 - Bebidas")
    print ("\t4 - salir")
    print("Escoja una opción:")
    return(' ')

print("Bienvenidos al restaurante Pytec:")
print("¿Ha reservado?:")
print("1 - He reservado")
print("2 - No he reservado")
print("Según sus preferenias escoja un número:")
y = int(input())
if y == 1:
    print(menu())
if y == 2:
    print("Espere una mesa libre")
    print("Después de 10 minutos...")
    print(menu())
if y!= 1 and y != 2:
    print("No existe esa opción...")
x = int(input())
if x == 4:
    print("fin del programa")

