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
    #print("creando json")
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
    #print("----------------creando json---------------------")
    #print(data)
    #print("----------------creo json---------------------")
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
    
    #print("+++++++++++++++++++++++++")
    #print(envio)
    #print("+++++++++++++++++++++++++")
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
                
                #print(message.decode('utf-8').rstrip())

                #nodoNuevo.HASH = encrypt_string(str(nodoNuevo.INDEX) + nodoNuevo.TIMESTAMP + nodoNuevo.CLASS + nodoNuevo.DATA +str(nodoNuevo.PREVIOUSHASH)  )
                x = json.loads(message.decode('utf-8').rstrip())
                ind = x["INDEX"]
                tim = x["TIMESTAMP"]
                clas = x["CLASS"]
                data = x["DATA"]
                prev = x["PREVIOUSHASH"]
                ha = x["HASH"]
                nuevo=json.dumps(data,separators=(',',':'))
                nuevoHash = encrypt_string(str(ind) + tim + clas + nuevo +prev)

                if nuevoHash == ha:
                    print("verdaderoo")
                    server.sendall("true".encode())
                    nodoNuevo = node()
                    nodoNuevo.INDEX = ind
                    nodoNuevo.TIMESTAMP = tim
                    nodoNuevo.CLASS = clas
                    nodoNuevo.DATA = nuevo
                    nodoNuevo.PREVIOUSHASH = prev
                    nodoNuevo.HASH = ha
                    #listaDoble.add(nodoNuevo)

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
                    print("A INSERTAR:")
                    listaDoble.add(nodoNuevo)
                    print("tama")
                    listaDoble.tam()
                    listaDoble.graph()
                    #print("tamanio: "+str(listaDoble.tam))
                    #print("graficando")
                    #listaDoble.print()
                    listaDoble.printa()
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
                    nodoNuevo = node()
                    now = datetime.now()
                    nodoNuevo.INDEX = contador
                    contador +=1
                    if listaDoble.head is None:
                        nodoNuevo.PREVIOUSHASH = "0000"
                    else:
                        nodoNuevo.PREVIOUSHASH = "0001"
                    nodoNuevo.TIMESTAMP = now.strftime("%d-%m-%Y::%H:%M:&S")
                    nodoNuevo.CLASS = datos[0]
                    nuevod = datos[1]
                    nodoNuevo.DATA = datos[1]
                    nodoNuevo.HASH = encrypt_string(str(nodoNuevo.INDEX) + nodoNuevo.TIMESTAMP + nodoNuevo.CLASS + nodoNuevo.DATA +nodoNuevo.PREVIOUSHASH)
                    #nodoNuevo.HASH = encrypt_string(str(nodoNuevo.INDEX) + nodoNuevo.TIMESTAMP + nodoNuevo.CLASS  +nodoNuevo.PREVIOUSHASH)
                    envioJsonString = crearJson(nodoNuevo.INDEX,nodoNuevo.TIMESTAMP,nodoNuevo.CLASS,nodoNuevo.DATA,nodoNuevo.PREVIOUSHASH,nodoNuevo.HASH)
                    #jsonString = json.dumps(envioJsonString)
                    
                    #print("***********json que envia*******************")
                    #print(envioJsonString)

                    #print("HASH ENVIADO es:")
                    #x = json.loads(envioJsonString)
                    #print(x["HASH"])
                    #print(nodoNuevo.DATA)
                    #print("")
                    server.sendall(envioJsonString.encode('utf-8'))


                #message = sys.stdin.readline()
                #server.sendall('JSON'.encode('utf-8'))
                #sys.stdout.write("YOU:")
                #sys.stdout.write(message)
                #sys.stdout.flush()
server.close()


    
        