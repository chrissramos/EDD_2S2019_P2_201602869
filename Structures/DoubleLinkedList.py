class node:
    def __init__(self):
        self.INDEX = None
        self.TIMESTAMP = None
        self.CLASS = None
        self.DATA = None
        self.PREVIOUSHASH = None
        self.HASH = None

class DoubleLinked:
    def __init__(self):
        self.head = None

    def returnHead(self):
        return self.head