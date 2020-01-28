if __name__ == "__main__":
    print('ok moduleAnalyseDonneesBrutes')

import pandas
import matplotlib.pyplot as plt

# pandas.options.display.max_rows = 10

print(pandas.__version__)

datas = pandas.read_csv("jeu_donnees.txt", sep="\t", header=0, usecols=["date", "temp_1", "temp_2"])

run = True

while (run):
    pas = input(
        "Selection du pas:\n [1] Une semaine (7 jours)\n [2] Une journée\n [3] 12h\n [4] 6h\n [5] 1h\n Votre choix: ")
    if (pas == "1"):
        pas = 1008
        run = False
    elif (pas == "2"):
        pas = 144
        run = False
    elif (pas == "3"):
        pas = 72
        run = False
    elif (pas == "4"):
        pas = 36
        run = False
    elif (pas == "5"):
        pas = 6
        run = False
    else:
        print("WRONG RESPONSE !!!")

borneInf = int(input("Entrez la borne inférieur: "))
borneSup = int(input("Entrez la borne supérieur: "))

i = borneInf
while i < borneSup:
    ax = plt.gca()
    df = datas.iloc[i * pas:i * pas + pas, :]
    df.plot(kind='line', x='date', y='temp_1', ax=ax)
    df.plot(kind='line', x='date', y='temp_2', ax=ax, color='red')
    plt.show()
    i = i + 1

# series = df['date']
# print(type(series))
# series.dt.strftime('%Y-%m-%d')