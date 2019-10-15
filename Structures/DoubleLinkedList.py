class node:
    def __init__(self):
        self.INDEX = None
        self.TIMESTAMP = None
        self.CLASS = None
        self.DATA = None
        self.PREVIOUSHASH = None
        self.HASH = None
        self.NEXT = None
        self.PREVIOUS = None

class DoubleLinked:
    def __init__(self):
        self.head = None

    def returnHead(self):
        return self.head

    def add(self,bloque):
        if self.head is None:
            self.head = bloque
        else:
            temp = self.head
            while temp.NEXT is not None:
                temp = temp.NEXT
            temp.NEXT = bloque
            bloque.PREVIOUS = temp
    
    def getUltimo(self):
            temp = self.head
            while temp.NEXT is not None:
                temp = temp.NEXT
            return temp
           

