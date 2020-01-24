import moduleChargementDonneesPackage.parseConfigJson as parse
import moduleChargementDonneesPackage.csvToDataFrame as csvDF

if __name__ == "__main__":
    print('ok moduleChargementDonnees.py')


class ChargementManager:
    def GetCSV(self, CSVPath):
        print(CSVPath)

    def ReadCSV(self, CSVPAth):
        print("CSV")

    def ReadJSON(self, JSONPath):
        parse.readJson(JSONPath)
        print("JSON")


def main():

    instance = ChargementManager()
    instance.ReadJSON('data.json')
    instance.GetCSV("hello")
