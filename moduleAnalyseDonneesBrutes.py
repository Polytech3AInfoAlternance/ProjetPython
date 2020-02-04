import pandas
import matplotlib.pyplot as plt
import seaborn as sns

class Analyse:
    def __init__(self, site, name):
        self.name = name
        self.site = site
        self.pas = 0
        self.borneInf = -1
        self.borneSup = -1

    def init(self):
        print("\n\n==> INIT OF SITE: " + self.name + " <===")
        run = True
        while run:
            self.pas = input("Selection du pas pour la simulation:\n [1] Une semaine (7 jours)\n [2] Une journée\n [3] 12h\n [4] 6h\n [5] 1h\n Votre choix: ")
            if self.pas == "1":
                self.pas = 1008
                run = False
            elif self.pas == "2":
                self.pas = 144
                run = False
            elif self.pas == "3":
                self.pas = 72
                run = False
            elif self.pas == "4":
                self.pas = 36
                run = False
            elif self.pas == "5":
                self.pas = 6
                run = False
            else:
                print("WRONG RESPONSE !!!")

        self.borneInf = int(input("Entrez la borne inférieur: "))
        self.borneSup = int(input("Entrez la borne supérieur: "))


    def TracePlot(self):
        dfList = self.site.tempList  # Return one dataframe per temperature
        i = self.borneInf
        while i < self.borneSup:
            ax = plt.gca()
            cpt = 1
            legend = []
            for df in dfList:
                legend.append("Temp " + str(cpt))
                df = df.iloc[i * self.pas:i * self.pas + self.pas, :]
                df.plot(kind='line', x='Date', y='CV', ax=ax)
                cpt = cpt + 1
            ax.legend(legend)
            plt.title("Temperature evolution")
            plt.ylabel("Temperature (°C)")
            plt.xlabel("Date")
            plt.show()
            i = i + 1

    def TraceTempPowerConsumption(self):
        i = self.borneInf

        temp = self.getMoyenne(self.site.tempList, 'CV')
        consoList = self.site.consoList
        tot_a = self.getMoyenne(consoList, 'TOT_A')
        puissance_a = self.getMoyenne(consoList, 'PUISSANCE_A')

        while i < self.borneSup:
            ax = plt.gca()
            legend = []
            legend.append("Temperature")
            loopTemp = temp.iloc[i * self.pas:i * self.pas + self.pas]
            loopTemp.plot(kind='line', x='Date', y='CV', ax=ax)

            legend.append("All consumption")
            loopTot_a = tot_a.iloc[i * self.pas:i * self.pas + self.pas]
            loopTot_a.plot(kind='line', x='Date', y='TOT_A', ax=ax)

            legend.append("Active power")
            loopPuissance_a = puissance_a.iloc[i * self.pas:i * self.pas + self.pas]
            loopPuissance_a.plot(kind='line', x='Date', y='PUISSANCE_A', ax=ax)

            ax.legend(legend)
            plt.title("Comparison between power, consumption and temperature")
            plt.ylabel("")
            plt.xlabel("Date")
            plt.show()
            i = i + 1

    def getCorr(self):
        temp = self.getMoyenne(self.site.tempList, 'CV')
        tot_a = self.getMoyenne(self.site.consoList, 'TOT_A')
        puissance_a = self.getMoyenne(self.site.consoList, 'PUISSANCE_A')
        d = {'CV': temp, 'TOT_A': tot_a, 'PUISSANCE_A': puissance_a}

        df = pandas.DataFrame(data=d)
        plt.subplot(221)
        ax = sns.heatmap(df.corr(), annot=True)
        bottom, top = ax.get_ylim()
        ax.set_ylim(bottom + 0.5, top - 0.5)
        plt.show()

    def getCorrInterval(self):
        temp = self.getMoyenne(self.site.tempList, 'CV')
        tot_a = self.getMoyenne(self.site.consoList, 'TOT_A')
        puissance_a = self.getMoyenne(self.site.consoList, 'PUISSANCE_A')
        d = {'CV': temp, 'TOT_A': tot_a, 'PUISSANCE_A': puissance_a}

        df = pandas.DataFrame(data=d)
        plt.subplot(221)
        i = self.borneInf
        while i < self.borneSup:
            ax = sns.heatmap(df.iloc[i * self.pas:i * self.pas + self.pas, :].corr(), annot=True)
            bottom, top = ax.get_ylim()
            ax.set_ylim(bottom + 0.5, top - 0.5)
            plt.show()
            i = i + 1

    # Récupérer la moyenne d'un attribut d'une liste de dataframe
    # listData: la liste de dataframe
    # attribute: l'attribut auquel on va calculer la moyenne
    def getMoyenne(self, listData, attribute):
        df = pandas.DataFrame()
        for temp in listData:
            df = pandas.concat([df, temp[attribute]], axis=1)
        return df.mean(axis=1)