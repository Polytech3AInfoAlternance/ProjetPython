class Site:

    tempList = []
    consoList = []

    def __init__(self, name):
        self.name = name
        print('Site créé -> ' + name)

    def addTempList(self, ptemp):
        self.tempList.append(ptemp)

    def addConsoList(self, pconso):
        self.tempList.append(pconso)
