import json

with open("config.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()


def get_config():
    return jsonObject

def get_jwt():
    configObj = get_config()
    return configObj['jwt']


def get_security():
    configObj = get_config()
    return configObj['security']