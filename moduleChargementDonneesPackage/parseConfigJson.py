import json

def readJson(path):

    with open(path) as jsonfile:
        data = json.load(jsonfile)

    return data

    # for each site, read all temp and conso files
    for site in data['sites']:
        print('site: ' + site['nomSite'])

        # for each temp file, call the csv to data frame function
        for tempFiles in site['temp']:
            print('  temp file path: ' + tempFiles + ' ; field: ' + str(data['fieldTemp']))

        # for each conso file, call the csv to data frame function
        for consoFiles in site['conso']:
            print('  conso file path: ' + consoFiles + ' ; field: ' + str(data['fieldConso']))