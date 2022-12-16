"""Methods for managing PluralKit system data"""

from requests import get as fetch

from globals import PLURALKIT_API, PLURALKIT_TOKEN, console


def getSystem() -> dict:
    """Get the curent token's system

    Returns:
        dict: The api response
    """
    return fetch(
        f"{PLURALKIT_API}/systems/@me",
        headers={"Authorization": PLURALKIT_TOKEN},
    ).json()


convertWhitelist = [
    "name",
    "description",
    "tag",
    "pronouns",
    "avatar_url",
    "banner",
    "color",
]
convertMetaWhitelist = ["id", "uuid", "created", "privacy", "webhook_url"]
convertBlacklist = [""]


def convertPKToPS(systemDataPK: dict) -> dict:
    """Convert a PluralKit system model to a PluralSnug system model

    Args:
        systemDataPK (dict): The PluralKit system model

    Returns:
        dict: The PluralSnug system model
    """

    systemDataPS = {"meta": {"PluralKit": {}}}

    for point, data in systemDataPK.items():
        if point in convertWhitelist:
            systemDataPS[point] = data
        elif point in convertMetaWhitelist:
            systemDataPS["meta"]["PluralKit"][point] = data
        elif not point in convertBlacklist:
            console.log(
                f"[red]Unknown value found in system data for {systemDataPK['name']} ({systemDataPK['id']}):"
            )
            console.log({point: data})

    return systemDataPS


PLURALKIT_SYSTEM_ID = getSystem()["id"]
