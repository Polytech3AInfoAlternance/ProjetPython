class Site:

    tempList = []
    consoList = []

    def __init__(self, name):
        self.name = name

    def setTempList(self,ptemp):
        for temp in ptemp :
            self.tempList.append(temp)

    def setConsoList(self,pconso):
        for conso in pconso :
            self.tempList.append(conso)
