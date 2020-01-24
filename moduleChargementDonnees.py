import moduleChargementDonneesPackage.parseConfigJson as parse

if __name__ == "__main__":
    print('ok moduleChargementDonnees.py')

class ChargementManager:
    def GetCSV(self, CSVPath):
        print(CSVPath)

    def ReadCSV(self, CSVPAth):
        print("CSV")

    def ReadJSON(self, JSONPath):
        parse.readJson('data.json')
        print("JSON")

def main():
    dataRepPath = 'entrer le chemin des données ici'
    print('\nmoduleChargementDonnees is ready')



    instance = ChargementManager()
    instance.GetCSV("hello");
