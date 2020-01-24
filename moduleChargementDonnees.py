import json

if __name__ == "__main__":
    print('ok moduleChargementDonnees.py')

def main():
    dataRepPath = 'entrer le chemin des données ici'
    print('\nmoduleChargementDonnees is ready')
    readJson()

def readJson():

    with open('data.json') as jsonfile:
        data = json.load(jsonfile)

    for site in data['sites']:
        print(site['nomSite'])
        for tempFiles in site['temp']:
            print(tempFiles)
        for consoFiles in site['conso']:
            print(consoFiles)
