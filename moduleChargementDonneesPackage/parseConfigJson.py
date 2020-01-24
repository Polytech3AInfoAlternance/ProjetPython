import json

def readJson():

    with open('data.json') as jsonfile:
        data = json.load(jsonfile)

    for site in data['sites']:
        print(site['nomSite'])
        for tempFiles in site['temp']:
            print(tempFiles)
        for consoFiles in site['conso']:
            print(consoFiles)