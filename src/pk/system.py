from requests import get as fetch

from globals import PLURALKIT_API, PLURALKIT_TOKEN


class pkSystemPrivacy:
    description: bool | None
    pronoun: bool | None
    member_list: bool | None
    group_list: bool | None
    front: bool | None
    front_history: bool | None

    def __init__(self, privacyData: dict) -> None:
        self.description = privacyData["description_privacy"]
        self.pronoun = privacyData["pronoun_privacy"]
        self.member_list = privacyData["member_list_privacy"]
        self.group_list = privacyData["group_list_privacy"]
        self.front = privacyData["front_privacy"]
        self.front_history = privacyData["front_history_privacy"]

    def __str__(self) -> str:
        return f"""im not bothered so {self.description} heres one to check it works"""
        # TODO: better privacy display


# TODO: document
class pkSystem:
    id: str
    uuid: str
    name: str | None
    description: str | None
    tag: str | None
    pronouns: str | None
    avatar_url: str | None
    banner: str | None
    color: str | None
    created: str | None  # TODO: convert to python datetime format
    privacy: pkSystemPrivacy | None

    def __init__(self, systemData: dict) -> None:
        self.id = systemData["id"]
        self.uuid = systemData["uuid"]
        self.name = systemData["name"]
        self.description = systemData["description"]
        self.tag = systemData["tag"]
        self.pronouns = systemData["pronouns"]
        self.avatar_url = systemData["avatar_url"]
        self.banner = systemData["banner"]
        self.color = systemData["color"]
        self.created = systemData["created"]

        if systemData["privacy"] != None:
            self.privacy = pkSystemPrivacy(systemData["privacy"])
        else:
            self.privacy = None

    def __str__(self) -> str:
        return f"""PK System {self.name} ({self.id})
    {self.description}
    tag: {self.tag}
    pronouns: {self.pronouns}
    avatar url: {self.avatar_url}
    banner: {self.banner}
    color: {self.color}
    created: {self.created}
    privacy: {self.privacy}"""

    # TODO: prettier formatting?


def getSystem() -> dict:
    """Get the curent token's system

    Returns:
        dict: The api response
    """
    return fetch(
        f"{PLURALKIT_API}/systems/@me",
        headers={"Authorization": PLURALKIT_TOKEN},
    ).json()


PLURALKIT_SYSTEM_ID = getSystem()["id"]
