from globals import PLURALKIT_API, PLURALKIT_TOKEN
from requests import get as fetch


def getSystem() -> dict:
    """Get the curent token's system

    Returns:
        dict: The api response
    """
    return fetch(
        f"{PLURALKIT_API}/systems/@me",
        headers={"Authorization": PLURALKIT_TOKEN},
    ).json()


def convertPKToPS(systemDataPK: dict) -> dict:
    """Convert a PluralKit system model to a PluralSnug system model

    Args:
        systemDataPK (dict): The PluralKit system model

    Returns:
        dict: The PluralSnug system model
    """

    systemDataPS = {"meta": {"PluralKit": {}}}

    # Handle the metadata values separately
    systemDataPS["meta"]["PluralKit"]["id"] = systemDataPK.pop("id")
    systemDataPS["meta"]["PluralKit"]["uuid"] = systemDataPK.pop("uuid")
    systemDataPS["meta"]["PluralKit"]["created"] = systemDataPK.pop("created")
    systemDataPS["meta"]["PluralKit"]["privacy"] = systemDataPK.pop("privacy")

    for point, data in systemDataPK.items():
        systemDataPS[point] = data

    return systemDataPS


PLURALKIT_SYSTEM_ID = getSystem()["id"]
