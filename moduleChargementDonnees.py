import moduleChargementDonneesPackage.parseConfigJson as parse
import moduleChargementDonneesPackage.csvToDataFrame as csvDF

if __name__ == "__main__":
    print('ok moduleChargementDonnees.py')


class ChargementManager:
    def GetCSV(self, CSVPath):
        print(CSVPath)

    def ReadCSV(self, CSVPAth, CSVColumn):
        df = csvDF.csv_to_df(CSVPAth, CSVColumn)
        print(df)

    def ReadJSON(self, JSONPath):
        data = parse.readJson(JSONPath)

        # for each site, read all temp and conso files
        for site in data['sites']:
            # for each temp file, call the csv to data frame function
            for tempFiles in site['temp']:
                self.ReadCSV('../jeu_de_donnees/' + site['nomSite'] + '/' + tempFiles, data['fieldTemp'])

            # for each conso file, call the csv to data frame function
            for consoFiles in site['conso']:
                self.ReadCSV('../jeu_de_donnees/' + site['nomSite'] + '/' + consoFiles, data['fieldConso'])


def main():
    dataRepPath = 'entrer le chemin des données ici'
    print('\nmoduleChargementDonnees is ready')
    instance = ChargementManager()
    instance.ReadJSON('data.json')
    # instance.GetCSV("hello")
