from globals import *
from json import load as loadJson

def loadSystemEntry():
    with open(f"{DB_PATH}/system.json") as f:
        return loadJson(f)
