import json

def readJson(path):

    with open(path) as jsonfile:
        data = json.load(jsonfile)

    return data