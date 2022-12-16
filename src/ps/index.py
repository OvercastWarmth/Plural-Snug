"""Methods for managing the PluralSnug member index"""

from json import dump as dumpJson
from json import load as loadJson
from os import listdir
from os.path import join as joinPaths
from time import time

from globals import DB_PATH, getKey

indexLocation = f"{DB_PATH}/index.json"


def checkIndexExists() -> bool:
    """Check if the index file exists

    Returns:
        bool: Whether or not the index file exists
    """
    try:
        with open(indexLocation) as f:
            loadJson(f)
        return True
    except:
        return False


def createIndexFile() -> None:
    """Creates the index file"""
    if checkIndexExists():
        return

    with open(indexLocation, "w") as f:
        dumpJson({"updated": round(time()), "members": {"ps": {}, "pk": {}}}, f)


def refreshIndexFile() -> None:
    """Refresh the index file and collect all the IDs"""
    if checkIndexExists():
        with open(indexLocation) as index:
            indexData = loadJson(index)
    else:
        createIndexFile()
        return refreshIndexFile()

    indexMembers = indexData["members"]

    for filename in listdir(f"{DB_PATH}/members"):
        p = joinPaths(f"{DB_PATH}/members", filename)

        with open(p) as f:
            member = loadJson(f)

            PSID = filename.strip(".json")

            indexMembers["ps"][PSID] = member["name"]
            indexMembers["pk"][member["meta"]["PluralKit"]["id"]] = PSID

    indexData["updated"] = round(time())

    with open(indexLocation, "w") as index:
        dumpJson(indexData, index, indent=4)


def convertPS2Name(PSId: int) -> str:
    with open(indexLocation) as f:
        return loadJson(f)["members"]["ps"].get(PSId)


def convertName2PS(name: str) -> int:
    with open(indexLocation) as f:
        return getKey(loadJson(f)["members"]["ps"], name)


def convertPK2PS(PKId: str) -> int:
    with open(indexLocation) as f:
        return loadJson(f)["members"]["pk"].get(PKId)


def convertPS2PK(PSId: int) -> str:
    with open(indexLocation) as f:
        return getKey(loadJson(f)["members"]["pk"], PSId)
