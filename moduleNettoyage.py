
import numpy as np
import pandas as pd
# from moduleChargementDonnees import ChargementManager



#  Définitions des classes

#  Définitions des fonctions

def lancer_nettoyage(df, column_name, nb_iter):
    moyenneGlobale = df[column_name].mean()
    tab = nettoyage(df, column_name, moyenneGlobale)
    moyenneGlobale = tab[1]
    df = tab[0]
    for k in range(1, nb_iter):
        tab = nettoyage(df, column_name, moyenneGlobale)
    return tab[0]

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
    compteurMoyenne = 0
    for i, row in df.iterrows():
        val = df.at[i, column_name]
        if val > 2*ecart_moyen:
            df.at[i, column_name] = 2*ecart_moyen
        else:
            if val < -2*ecart_moyen:
                df.at[i, column_name] = -2 * ecart_moyen
            else:
                compteurMoyenne = compteurMoyenne+df.at[i, column_name]
    moyenne = compteurMoyenne/i
    return [df, moyenne]

# def remove_outlier(df_in, col_name):
#     q1 = df_in[col_name].quantile(0.25)
#     q3 = df_in[col_name].quantile(0.75)
#     iqr = q3 - q1  # ecart interquartile
#     fence_low = q1 - 1.5 * iqr
#     fence_high = q3 + 1.5 * iqr
#     df_out = df_in.loc[(df_in[col_name] > fence_low) & (df_in[col_name] < fence_high)]
#     df_ab = df_in.loc[(df_in[col_name] < fence_low) & (df_in[col_name] > fence_high)]
#
#     return df_out

# Possiblement utile pour valeur abberante
# print(df[ np.abs(df.Data - df.Data.mean()) > 1.5*df.Data.std() ])

#  Main
if __name__ == "__main__":
    print('ok moduleNettoyage')

def main(managerDonnees):
    print(managerDonnees.GetSite('010000179B').consoList)
    #for site in managerDonnees.GetListNameSite():
     #   df = pd.DataFrame(data=managerDonnees.GetSite(site).consoList)
      #  print(df)
        # dg = pd.DataFrame(data=managerDonnees.Get
        # print(managerDonnees.GetSite(site).tempList)
        #d = {'col1': [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'col2': [3, -4, 5, 6, -5, 9, 7, 1, 9, -8, 1, 4, -1, 139]}
        #df = pd.DataFrame(data=d)
        #lancer_nettoyage(df, 'col2', 6)
        #print(df)


