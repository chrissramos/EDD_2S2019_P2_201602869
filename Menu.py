import os
import csv
exit = False
opcion = 0
while not exit:
 
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
            print(datos[0])
            print("\n")
            print(datos[1])
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