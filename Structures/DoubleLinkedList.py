from graphviz import Digraph
class node:
    def __init__(self):
        self.INDEX = None
        self.TIMESTAMP = None
        self.CLASS = None
        self.DATA = None
        self.PREVIOUSHASH = None
        self.HASH = None
        self.next = None
        self.previous = None

class DoubleLinked:
    def __init__(self):
        self.head = None
        self.end = None

    def returnHead(self):
        return self.head

    def add(self,bloque):
        print("entro: ", bloque.CLASS)
        if self.head is None:
            print("insertando cabeza: ", bloque.CLASS)
            self.head = bloque
            self.end = bloque
            self.head.next = None
            self.head.previous = None
        else:
            print("insertando nodos, ya hay cabeza y es:" , self.head.CLASS)
            print("nodo entrante: ",bloque.CLASS)
            self.end.next = bloque
            bloque.previous = self.end
            self.end = bloque
            self.end.next = None
            
    
    def getUltimo(self):
            temp = self.head
            while temp.NEXT is not None:
                temp = temp.NEXT
            return temp

    def tam(self):
        temp = self.head
        contador = 0
        if self.head.next is None:
            contador = 1
        else:
            while temp is not None:
                contador = contador+1
                temp = temp.next

        print(str(contador))

    def graph(self):
        g = Digraph('G', filename='lista', format='png')
        temp = self.head
        while temp.next is not None:
            #primer = 'Class= '+ temp.CLASS + '\n'+'Timestamp = ' + temp.TIMESTAMP + '\n' + 'PHASH = ' + temp.PREVIOUSHASH + '\n' + 'HASH = '+temp.HASH
            g.edge(temp.CLASS, temp.next.CLASS)
            g.edge(temp.next.CLASS, temp.CLASS)
            temp = temp.next
        primero = 'Class= '+ temp.CLASS  + ' PHASH = ' + temp.PREVIOUSHASH + ' HASH = '+temp.HASH
        print(temp.TIMESTAMP)
        g.edge(primero, "Null")
        g.view()

    def print(self):
        if self.head is None:
            print("lista vacia")
        else:
            temp = self.head
            while temp is not None:
                print("entro a while")
                print("[",temp.CLASS,"]")
                print("->")
                temp = temp.next
            
    def printa(self):
        print("cabeza:", self.head.CLASS)
        print("")
        if self.head.next is None:
            print("no hay sig")
        else:
            print("sig: ", self.head.next.CLASS)
        


