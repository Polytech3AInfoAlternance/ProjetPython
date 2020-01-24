import moduleChargementDonneesPackage.parseConfigJson as parse
import moduleChargementDonneesPackage.csvToDataFrame as csvDF

if __name__ == "__main__":
    print('ok moduleChargementDonnees.py')


class ChargementManager:
    def GetCSV(self, CSVPath):
        print(CSVPath)

    def ReadCSV(self, CSVPAth, CSVColumn, CSVType):
        print(CSVPAth + ' -> ' + CSVColumn + ' -> ' + CSVType)

    def ReadJSON(self, JSONPath):
        data = parse.readJson(JSONPath)

        # for each site, read all temp and conso files
        for site in data['sites']:
            # for each temp file, call the csv to data frame function
            for tempFiles in site['temp']:
                self.ReadCSV('jeu_de_donnees/' + site['nomSite'] + tempFiles, str(data['fieldTemp']), 'temp')

            # for each conso file, call the csv to data frame function
            for consoFiles in site['conso']:
                self.ReadCSV('jeu_de_donnees/' + site['nomSite'] + consoFiles, str(data['fieldConso']), 'conso')

<<<<<<< HEAD

def main():
=======
def main():
    dataRepPath = 'entrer le chemin des données ici'
    print('\nmoduleChargementDonnees is ready')
>>>>>>> ffb342eefcdb74f7af9ea493b3e3cf28d513f385

    instance = ChargementManager()
    instance.ReadJSON('data.json')
    instance.GetCSV("hello")
