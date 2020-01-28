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
        return df

    def ReadJSON(self, JSONPath):
        data = parse.readJson(JSONPath)
        # for each site, read all temp and conso files
        for site in data['sites']:

            mySite = Site(site['nomSite'])

            # for each temp file, call the csv to data frame function
            for tempFiles in site['temp']:
                dataFrameTemp = self.ReadCSV('jeu_de_donnees/' + site['nomSite'] + '/' + tempFiles, data['fieldTemp'])
                for it in dataFrameTemp['CV']:
                    try:
                        it = float(it)
                    except:
                        continue

                mySite.addTempList(dataFrameTemp)

            # for each conso file, call the csv to data frame function
            for consoFiles in site['conso']:
                dataFrameConso = self.ReadCSV('jeu_de_donnees/' + site['nomSite'] + '/'  + consoFiles, data['fieldConso'])
                for it in dataFrameConso['TOT_A']:
                    try:
                        it = float(it)
                    except:
                        continue

                for it in dataFrameConso['PUISSANCE_A']:
                    try:
                        it = float(it)
                    except:
                        continue

                mySite.addConsoList(dataFrameConso)

            self.sites_.append(mySite)
       
