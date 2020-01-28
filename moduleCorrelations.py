import numpy as np
import pandas
from pandas import DataFrame
import seaborn as sn
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print('ok moduleCorrelations')

def main():

    Data = {'Site D': [],
            'Site E': []
            }

    df1 = pandas.DataFrame({'Date': ['01/01/2020', '01/02/2020', '01/03/2020', '01/04/2020', '01/05/2020'], 'TOT_A': [10, 40, 35, 30, 20], 'PUISSANCE_A': [78, 90, 80, 80, 70]});
    df2 = pandas.DataFrame({'Date': ['01/01/2020', '01/02/2020', '01/03/2020', '01/04/2020', '01/05/2020'], 'TOT_A': [20, 40, 15, 25, 10], 'PUISSANCE_A': [78, 90, 80, 80, 80]});
    #df2 = pandas.DataFrame({'Date': ['01/01/2020', '01/02/2020'], 'CV': [34, 20]});
    Data['Site D'] = df1['TOT_A']
    Data['Site E'] = df2['TOT_A']

    df = DataFrame(Data, columns=['Site D', 'Site E'])

    corrMatrix = df.corr()
    plt.subplots(figsize=(10, 8))
    ax = sn.heatmap(corrMatrix, annot=True)
    bottom, top = ax.get_ylim()
    ax.set_ylim(bottom + 0.5, top - 0.5)
    plt.show()