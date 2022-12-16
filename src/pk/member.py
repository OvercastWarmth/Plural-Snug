"""Methods for managing PluralKit member data"""

from time import time
from uuid import uuid4

from requests import get as fetch

from globals import PLURALKIT_API, PLURALKIT_TOKEN, console
from ps.db import overwriteMemberEntry
from ps.index import convertPS2PK


def getMemberList() -> list:
    """Get the curent token's member list

    Returns:
        list: The api response
    """
    return fetch(
        f"{PLURALKIT_API}/systems/@me/members",
        headers={"Authorization": PLURALKIT_TOKEN},
    ).json()


def getMember(id: str) -> dict:
    """Get the specified member

    Args:
        id (str): The ID of the member to fetch

    Returns:
        dict: The api response
    """
    return fetch(
        f"{PLURALKIT_API}/members/{id}",
        headers={"Authorization": PLURALKIT_TOKEN},
    ).json()


convertWhitelist = [
    "name",
    "display_name",
    "color",
    "birthday",
    "pronouns",
    "avatar_url",
    "banner",
    "description",
    "keep_proxy",
    "proxy_tags",
]
convertMetaWhitelist = [
    "id",
    "uuid",
    "created",
    "privacy",
    "autoproxy_enabled",
    "message_count",
    "last_message_timestamp",
]
convertBlacklist = ["system"]  # This value has no reason to be saved


def convertPKToPS(memberDataPK: dict) -> dict:
    """Convert a PluralKit member model to a PluralSnug member model

    Args:
        memberDataPK (dict): The PluralKit member model

    Returns:
        dict: The PluralSnug member model
    """
    pkMemberID = memberDataPK["id"]

    try:
        convertPS2PK(pkMemberID)
        memberDataPS = {"meta": {"PluralKit": {}}, "id": pkMemberID}
    except:
        memberDataPS = {"meta": {"PluralKit": {}}, "id": str(uuid4())}

    for point, data in memberDataPK.items():
        if point in convertWhitelist:
            memberDataPS[point] = data
        elif point in convertMetaWhitelist:
            memberDataPS["meta"]["PluralKit"][point] = data
        elif not point in convertBlacklist:
            console.log(
                f"[red]Unknown value found in member data for {memberDataPK['name']} ({pkMemberID}):"
            )
            console.log({point: data})

    memberDataPS["updated"] = round(time())

    return memberDataPS


def massImport(memberList: list):
    for member in memberList:
        overwriteMemberEntry(convertPKToPS(member))
