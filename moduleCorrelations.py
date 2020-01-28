import numpy as np
import pandas
from pandas import DataFrame
import seaborn as sn
import matplotlib.pyplot as plt


if __name__ == "__main__":
    print('ok moduleCorrelations')

def main(managerDonnees):
    Data = {}
    DataP = {}
    DataT = {}
    siteName = [];
    plt.subplots(figsize=[10, 8])

    j=0;

    for site in managerDonnees.GetListNameSite():

        # TOT_A
        consoList = managerDonnees.GetSite(site).consoList
        Data['' + site] = [float(i) for i in consoList[0]['TOT_A'][:].tolist()]

        #PUISSANCE
        consoListP = managerDonnees.GetSite(site).consoList
        DataP['' + site] = [float(i) for i in consoListP[0]['PUISSANCE_A'][:].tolist()]

        # TEMPERATURE
        tempList = managerDonnees.GetSite(site).tempList
        DataT['' + site] = [float(i) for i in tempList[1]['CV'][:40000].tolist()]

        j += 1
        siteName.append(managerDonnees.GetSite(site).name)



    df = DataFrame(Data, columns=siteName)
    dfP = DataFrame(DataP, columns=siteName)
    dfT=DataFrame(DataT, columns=siteName)
    corrMatrix = df.corr()
    corrMatrixP = dfP.corr()
    corrMatrixT =dfT.corr()



    plt.subplot(221)
    plt.title('TOT_A')
    ax = sn.heatmap(corrMatrix, annot=True)
    bottom, top = ax.get_ylim()
    ax.set_ylim(bottom + 0.5, top - 0.5)

    plt.subplot(222)
    plt.title('Puissance A')
    axp = sn.heatmap(corrMatrixP, annot=True)
    bottom, top = axp.get_ylim()
    axp.set_ylim(bottom + 0.5, top - 0.5)

    plt.subplot(223)
    plt.title('Température')
    axT = sn.heatmap(corrMatrixT, annot=True)
    bottom, top = axT.get_ylim()
    axT.set_ylim(bottom + 0.5, top - 0.5)
    plt.show()
