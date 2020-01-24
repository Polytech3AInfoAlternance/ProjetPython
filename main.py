from moduleChargementDonnees import ChargementManager

managerDonnees = ChargementManager()
managerDonnees.ReadJSON('data.json')
print(managerDonnees.GetSite("0100001797").name)

#Passez en parametre 'managerDonnees' afin de ne pas avoir à le créer


#-------------------VOS CODES-------------------#
