import hashlib
from datetime import datetime
import os
import csv
from Structures.DoubleLinkedList import node
from Structures.DoubleLinkedList import DoubleLinked

exit = False
opcion = 0
def encrypt_string(string):
        sha_encryption = hashlib.sha256(string.encode()).hexdigest()
        return sha_encryption
while not exit:
    listaDoble = DoubleLinked()
    contador = 0    
    print ("1. Insert Block")
    print ("2. Select Block")
    print ("3. Reports")
    print ("4. Salir")
    
    print ("Elige una opcion")
    
    opcion = int(input("Ingrese numero deseado: "))
    
    if opcion == 1:
        os.system('cls')
        print ("Ingrese Nombre de Archivo .csv")
        nombreA = input()+".csv"
        #os.system('pause')
        print("Archivo ingresado: " + nombreA)
        print("Leyendo archivo\n\n")
        datos = []
        #creando nodo bloque 
        
        
        
        #os.system("ls")
        with open("bloques\\"+nombreA) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                #print(row)
                #print(row[1])
                dato = row[1]
                datos.append(dato)
                #print("\n")
                #print(row[0],row[1],)
            #datos 0 = nombre de la clase
            #datos 1 = el json
            #print(datos[0])
            #print("\n")
            #print(datos[1])
            #agregando atributos al bloque a crear
            if listaDoble.head is None:
                nodoNuevo = node()
                now = datetime.now()
                nodoNuevo.INDEX = contador
                nodoNuevo.PREVIOUSHASH = "0000"
                nodoNuevo.TIMESTAMP = now.strftime("%d-%m-%Y::%H:%M:&S")
                nodoNuevo.CLASS = datos[0]
                nodoNuevo.DATA = datos[1]
                nodoNuevo.HASH = encrypt_string(str(nodoNuevo.INDEX) + nodoNuevo.TIMESTAMP + nodoNuevo.CLASS + nodoNuevo.DATA +str(nodoNuevo.PREVIOUSHASH)  )
                contador+=1
                print("Se creo el bloque Genesis:")
            else:
                nodoNuevoC = node()

                print("Ya tiene info")
        os.system('pause')
    
    elif opcion == 2:
        print ("Opcion 2")
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        exit = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")