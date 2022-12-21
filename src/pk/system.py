from requests import get as fetch
from pk.globals import API, TOKEN, PRIVACY_MAP
from ps.globals import Metadata


class PkSystemPrivacy:
    """Pluralkit system privacy model"""

    description: bool
    pronoun: bool
    member_list: bool
    group_list: bool
    front: bool
    front_history: bool

    def __init__(self, privacy_data: dict) -> None:
        self.description = PRIVACY_MAP[privacy_data["description_privacy"]]
        self.pronoun = PRIVACY_MAP[privacy_data["pronoun_privacy"]]
        self.member_list = PRIVACY_MAP[privacy_data["member_list_privacy"]]
        self.group_list = PRIVACY_MAP[privacy_data["group_list_privacy"]]
        self.front = PRIVACY_MAP[privacy_data["front_privacy"]]
        self.front_history = PRIVACY_MAP[privacy_data["front_history_privacy"]]

    def __str__(self) -> str:
        return f"""im not bothered so {self.description} heres one to check it works"""
        # TODO: finish implementing string conversions


# TODO: document
class PkSystem:
    """Pluralkit system model"""

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


class PkSystemMetadata(Metadata):
    id: str
    uuid: str
    created: str | None
    privacy: PkSystemPrivacy | None

    def __init__(self, system: PkSystem):
        self.type = "pk"
        self.id = system.id
        self.uuid = system.uuid
        self.created = system.created
        self.privacy = system.privacy


def get_system() -> dict:
    """Get the current token's system

    Returns:
        dict: The api response
    """
    return fetch(
        f"{API}/systems/@me",
        headers={"Authorization": TOKEN},
    ).json()


PLURALKIT_SYSTEM_ID = get_system()["id"]
