from globals import *
from requests import get as fetch


def getSystem():
    return fetch(
        f"{PLURALKIT_API}/systems/@me",
        headers={"Authorization": PLURALKIT_TOKEN},
    ).json()


def convertPKToPS(systemDataPK):
    console.log(systemDataPK)

    systemDataPS = {"meta": {"PluralKit": {}}}

    # Handle the metadata values separately
    systemDataPS["meta"]["PluralKit"]["id"] = systemDataPK.pop("id")
    systemDataPS["meta"]["PluralKit"]["uuid"] = systemDataPK.pop("uuid")
    systemDataPS["meta"]["PluralKit"]["created"] = systemDataPK.pop("created")

    # TODO parse the rest of the data

    console.log(systemDataPS)


PLURALKIT_SYSTEM_ID = getSystem()["id"]
