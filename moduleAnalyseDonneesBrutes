if __name__ == "__main__":
    print('ok moduleAnalyseDonneesBrutes')

import pandas
import numpy as np
import matplotlib.pyplot as plt

pandas.options.display.max_rows = 10

print(pandas.__version__)

df = pandas.read_csv("jeu_donnees.txt", sep ="\t", header = 0, usecols = ["date","temp_1","temp_2","tot_a","puissance_a"])

print(type(df))
df.head()
print(df.shape)
print(df.dtypes)

print(df[['date','temp_1','temp_2','tot_a']])

print(df.temp_1.describe())

#df.hist(column='temp_1')
#df.hist(column='temp_2')
#df.hist(column='tot_a')

#plt.figure()

#df['temp_1'].plot()
#df['temp_2'].plot()