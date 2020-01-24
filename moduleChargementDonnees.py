import moduleChargementDonneesPackage.parseConfigJson as parse
from moduleChargementDonneesPackage.site import Site
import moduleChargementDonneesPackage.csvToDataFrame as csvDF

if __name__ == "__main__":
    print('ok moduleChargementDonnees.py')


class ChargementManager:
    sites_ = []

    def __init__(self):
        print('moduleChargementDonnees is ready')

    def GetSite(self, name):
        for site in self.sites_:
            if site.name == name:
                return site

    def GetListNameSite(self):
        listNameSite = []
        for site in self.sites_:
            listNameSite.append(site.name)
        return listNameSite

    def ReadCSV(self, CSVPAth, CSVColumn):
        df = csvDF.csv_to_df(CSVPAth, CSVColumn)
        print(df)

    def ReadJSON(self, JSONPath):
        data = parse.readJson(JSONPath)

        # for each site, read all temp and conso files
        for site in data['sites']:

            mySite = Site(site['nomSite'])
            self.sites_.append(mySite)

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
       