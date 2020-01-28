
import numpy as np
import pandas as pd
# from moduleChargementDonnees import ChargementManager



#  Définitions des classes

#  Définitions des fonctions

def lancer_nettoyage(df, column_name):
    df[column_name].fillna(0, inplace=True)
    moyenneGlobale = get_moyenne_propre(df, column_name)
    df_temp = df.copy()
    nettoyage(df, column_name, moyenneGlobale)
    while not df.equals(df_temp):
        df_temp = df.copy()
        nettoyage(df, column_name, moyenneGlobale)


def lancer_nettoyage_index(df, index):
    column_name = df.columns[index]
    df[column_name].fillna(0, inplace=True)
    moyenneGlobale = get_moyenne_propre(df, column_name)
    df_temp = df.copy()
    nettoyage(df, column_name, moyenneGlobale)
    while not df.equals(df_temp):
        df_temp = df.copy
        nettoyage(df, column_name, moyenneGlobale)

def nettoyage(df, column_name, moyenne):
    ecart_moyen = 0
    for i, row in df.iterrows():
        ifor_val = df.at[i, column_name]
        ecart = 0
        if ifor_val >= moyenne:
            ecart = ifor_val - moyenne
        else:
            ecart = moyenne - ifor_val
        ecart_moyen = ecart_moyen + ecart
    ecart_moyen = ecart_moyen/i
    for i, row in df.iterrows():
        val = df.at[i, column_name]
        if val > 1.5*ecart_moyen:
            df.at[i, column_name] = val%ecart_moyen
        elif val < -1.5*ecart_moyen:
            df.at[i, column_name] = -(val%ecart_moyen)

def get_moyenne_propre(df, column_name):
    moyenne = df[column_name].mean()
    ecart_moyen = 0
    for i, row in df.iterrows():
        ifor_val = df.at[i, column_name]
        ecart = 0
        if ifor_val >= moyenne:
            ecart = ifor_val - moyenne
        else:
            ecart = moyenne - ifor_val
        ecart_moyen = ecart_moyen + ecart
    ecart_moyen = ecart_moyen / i
    compteurMoyenne = 0
    cpt = 0
    for i, row in df.iterrows():
        val = df.at[i, column_name]
        if val > -2 * ecart_moyen and val < 2 * ecart_moyen:
            cpt = cpt + 1
            compteurMoyenne = compteurMoyenne + df.at[i, column_name]
    moyenne = compteurMoyenne / cpt
    return moyenne

#  Main
if __name__ == "__main__":
    d = {'col1': [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
         'col2': [93, -34, 55, 36, -75, 89, None, 21, 49, -38, 12, 14, -11112, 1393]}
    df = pd.DataFrame(data=d)
    lancer_nettoyage(df, 'col2')
    print(df)
    print('ok moduleNettoyage')

def main(managerDonnees):
    for site in managerDonnees.GetListNameSite():
        df = managerDonnees.GetSite(site).consoList
        dg = managerDonnees.GetSite(site).tempList
        print(df)
        lancer_nettoyage(df, 'TOT_A')
        lancer_nettoyage(df, df[1])
        print(df)


