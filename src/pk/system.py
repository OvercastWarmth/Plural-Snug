from requests import get as fetch

from globals import PLURALKIT_API, PLURALKIT_TOKEN


class PkSystemPrivacy:
    description: bool | None
    pronoun: bool | None
    member_list: bool | None
    group_list: bool | None
    front: bool | None
    front_history: bool | None

    def __init__(self, privacy_data: dict) -> None:
        self.description = privacy_data["description_privacy"]
        self.pronoun = privacy_data["pronoun_privacy"]
        self.member_list = privacy_data["member_list_privacy"]
        self.group_list = privacy_data["group_list_privacy"]
        self.front = privacy_data["front_privacy"]
        self.front_history = privacy_data["front_history_privacy"]

    def __str__(self) -> str:
        return f"""im not bothered so {self.description} heres one to check it works"""
        # TODO: better privacy display


# TODO: document
class PkSystem:
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
    privacy: PkSystemPrivacy | None

    def __init__(self, system_data: dict) -> None:
        self.id = system_data["id"]
        self.uuid = system_data["uuid"]
        self.name = system_data["name"]
        self.description = system_data["description"]
        self.tag = system_data["tag"]
        self.pronouns = system_data["pronouns"]
        self.avatar_url = system_data["avatar_url"]
        self.banner = system_data["banner"]
        self.color = system_data["color"]
        self.created = system_data["created"]

        if system_data["privacy"] is not None:
            self.privacy = PkSystemPrivacy(system_data["privacy"])
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


def get_system() -> dict:
    """Get the curent token's system

    Returns:
        dict: The api response
    """
    return fetch(
        f"{PLURALKIT_API}/systems/@me",
        headers={"Authorization": PLURALKIT_TOKEN},
    ).json()


PLURALKIT_SYSTEM_ID = get_system()["id"]
