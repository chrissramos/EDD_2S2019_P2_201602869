import hashlib
from datetime import datetime
import os
import csv
import socket
import select
import sys
import json
from Structures.DoubleLinkedList import node
from Structures.DoubleLinkedList import DoubleLinked

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
	print ("Correct usage: script, IP address, port number")
	exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))
#server.sendall('hola desde el cliente'.encode('utf-8'))
exit = False
opcion = 0
listaDoble = DoubleLinked()
nodoNuevo = node()
contador = 0
def encrypt_string(string):
        sha_encryption = hashlib.sha256(string.encode()).hexdigest()
        return sha_encryption

def crearJson(index, time, clas, data, prev, has):
    print("creando json")
    """jsonTotal = '{'
    jsonTotal+= "\"INDEX\": "+index
    jsonTotal+= "\"TIMESTAMP\": "+time + ","
    jsonTotal+= "\"CLASS\": "+clas+ ","
    jsonTotal+= "\"DATA\": "+data + ","
    jsonTotal+= "\"PREVIOUSHASH\": "+prev + ","
    jsonTotal+= "\"HASH\": "+has
    jsonTotal += '}'  
    
    print("Valores de variables:")
    print(index)
    print(time)
    print(clas)
    print(data)
    print(prev)
    print(has)
    """
    #print("Imprimiendo solo la dataB")
    #print(data)
    print("-------------------------------------")
    #datab = json.loads(data)
    #print(datab)
    #data = data.replace("\n", "")
    #data = data.replace("'\'", "")
    
    """objeto = {
        "INDEX": index,
        "TIMESTAMP": ''+time+'',
        "CLASS": ''+clas+'',
        "DATA": data,
        "PREVIOUSHASH": ''+prev+'',
        "HASH": ''+has+''
    }"""

    envio = "{\"INDEX\": " + str(index)+ ","+ "\"TIMESTAMP\": \""+ time+"\",\"CLASS\": \""+clas+"\",\"DATA\": "+data+",\"PREVIOUSHASH\": \""+prev+"\",\"HASH\": \""+has+"\"}"                                     
    #y = json.dumps(objeto)
    
    print("+++++++++++++++++++++++++")
    print(envio)
    print("+++++++++++++++++++++++++")
    #print(y)
    return envio


while True:
    read_sockets = select.select([server], [], [], 1)[0]
    import msvcrt
    if msvcrt.kbhit(): read_sockets.append(sys.stdin)

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            if message.decode('utf-8') != 'true' and message.decode('utf-8') != 'false' and message.decode('utf-8') != 'Welcome to [EDD]Blockchain Project!': 
                print("Recibiendo un Json")
                #print(message.decode('utf-8'))
                print("Su previous en respuesta es:")
                
                #nodoNuevo.HASH = encrypt_string(str(nodoNuevo.INDEX) + nodoNuevo.TIMESTAMP + nodoNuevo.CLASS + nodoNuevo.DATA +str(nodoNuevo.PREVIOUSHASH)  )
                x = json.loads(message.decode('utf-8'))
                ind = x["INDEX"]
                tim = x["TIMESTAMP"]
                clas = x["CLASS"]
                data = x["DATA"]
                prev = x["PREVIOUSHASH"]
                ha = x["HASH"]
                print("la data es:")
                print(data)
                print("ffffffffffffffffffffffffffffffffffffffff")
                databb = json.dumps(data)
                print("la data nueva es:")
                print(databb)
                print("333333333333333333333333333333333333")
                nuevoHash = encrypt_string(str(ind) + tim + clas + databb +prev)


                print("NUEVO HASH")
                print(nuevoHash)
                print("hash recibido:")
                print(ha)
                if nuevoHash == ha:
                    print("verdaderoo")
                    server.sendall("true".encode())
                else:
                    print("falsoo")
                    server.sendall('false'.encode())

                #print(prev)
                #print(dat)
            else:
                new_message = message.decode('utf-8')
                if new_message == 'false':
                    print("FALSO DE SERVIDOR")
                elif new_message == 'true':
                    print("verdadero de servidor")
                    print("true")
            #print ("recv:"+message.decode('utf-8'))
        else:
            print("1 insert bloque")
            print("2 select")
            print("3 reports")
            print("elige una opcion..")
            opcion = int(input("Ingrese numero deseado: "))
            if opcion == 1:
                print ("Ingrese Nombre de Archivo .csv")
                nombreA = input()+".csv"
                datos = []
                with open("bloques\\"+nombreA) as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    for row in readCSV:
                        dato = row[1]
                        datos.append(dato)
                    archi = datos[1]
                    
                    now = datetime.now()
                    nodoNuevo.INDEX = contador
                    if listaDoble.head is None:
                        nodoNuevo.PREVIOUSHASH = "0000"
                    else:
                        nodoNuevo.PREVIOUSHASH = "0001"
                    nodoNuevo.TIMESTAMP = now.strftime("%d-%m-%Y::%H:%M:&S")
                    nodoNuevo.CLASS = datos[0]
                    #nuevod = datos[1]
                    #nuevodd = nuevod.replace("\n", "")
                    nodoNuevo.DATA = datos[1]
                    #nodoNuevo.DATA = nuevodd
                    nodoNuevo.HASH = encrypt_string(str(nodoNuevo.INDEX) + nodoNuevo.TIMESTAMP + nodoNuevo.CLASS + nodoNuevo.DATA +nodoNuevo.PREVIOUSHASH)
                    #nodoNuevo.HASH = encrypt_string(str(nodoNuevo.INDEX) + nodoNuevo.TIMESTAMP + nodoNuevo.CLASS  +nodoNuevo.PREVIOUSHASH)
                    envioJsonString = crearJson(nodoNuevo.INDEX,nodoNuevo.TIMESTAMP,nodoNuevo.CLASS,nodoNuevo.DATA,nodoNuevo.PREVIOUSHASH,nodoNuevo.HASH)
                    #jsonString = json.dumps(envioJsonString)
                    
                    print("******************************")
                    print(envioJsonString)
                    #print("HASH ENVIADO es:")
                    #x = json.loads(envioJsonString)
                    #print(x["HASH"])
                    #print(nodoNuevo.DATA)
                    #print("")
                    server.sendall(envioJsonString.encode())


                #message = sys.stdin.readline()
                #server.sendall('JSON'.encode('utf-8'))
                #sys.stdout.write("YOU:")
                #sys.stdout.write(message)
                #sys.stdout.flush()
server.close()


    
        