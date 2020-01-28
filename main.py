from moduleChargementDonnees import ChargementManager

managerDonnees = ChargementManager()
managerDonnees.ReadJSON('data.json')

#Exemple d'utilisation afin de récupérer le nom d'un site
print(managerDonnees.GetSite("0100001797").name)

#Passez en parametre 'managerDonnees' afin de ne pas avoir à le créer


#-------------------VOS CODES-------------------#

#for site in managerDonnees.GetListNameSite():

    #print(managerDonnees.GetSite(site).tempList)
    #print(managerDonnees.GetSite(site).consoList)
