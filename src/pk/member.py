from globals import PLURALKIT_API, PLURALKIT_TOKEN
from requests import get as fetch


def getMemberList() -> dict:
    """Get the curent token's member list

    Returns:
        dict: The api response
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


def convertPKToPS(memberDataPK: dict) -> dict:
    memberDataPS = {"meta": {"PluralKit": {}}}

    # Handle the metadata values separately
    memberDataPS["meta"]["PluralKit"]["id"] = memberDataPK.pop("id")
    memberDataPS["meta"]["PluralKit"]["uuid"] = memberDataPK.pop("uuid")
    memberDataPS["meta"]["PluralKit"]["created"] = memberDataPK.pop("created")
    memberDataPS["meta"]["PluralKit"]["privacy"] = memberDataPK.pop("privacy")

    # TODO more

    return memberDataPS
