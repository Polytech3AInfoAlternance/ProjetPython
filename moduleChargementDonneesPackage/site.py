class Site:



    def __init__(self, name):
        self.name = name
        self.consoList = []
        self.tempList = []

        print('Site créé -> ' + name)

    def addTempList(self, ptemp):
        self.tempList.append(ptemp)

    def addConsoList(self, pconso):
        self.consoList.append(pconso)
