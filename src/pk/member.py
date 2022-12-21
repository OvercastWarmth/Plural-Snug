from pk.globals import PRIVACY_MAP


class PkMemberPrivacy:
    """
    Pluralkit member privacy model
    """

    visibility: bool
    name: bool
    description: bool
    birthday: bool
    pronoun: bool
    avatar: bool
    metadata: bool

    def __init__(self, privacy: dict):
        self.visibility = PRIVACY_MAP[privacy["visibility"]]
        self.name = PRIVACY_MAP[privacy["name_privacy"]]
        self.description = PRIVACY_MAP[privacy["description_privacy"]]
        self.birthday = PRIVACY_MAP[privacy["birthday_privacy"]]
        self.pronoun = PRIVACY_MAP[privacy["pronoun_privacy"]]
        self.avatar = PRIVACY_MAP[privacy["avatar_privacy"]]
        self.metadata = PRIVACY_MAP[privacy["metadata_privacy"]]


class PkProxyTag:
    """Pluralkit proxy tag model"""

    prefix: str | None
    suffix: str | None

    def __init__(self, tag: dict):
        self.prefix = tag["prefix"]
        self.suffix = tag["suffix"]


def generate_proxy_tag_list(tags: list) -> list:
    out = []
    for tag in tags:
        out.append(PkProxyTag(tag))

    return out


class PkMember:
    """Pluralkit member model"""

    id: str
    uuid: str
    name: str
    display_name: str | None
    color: str | None
    birthday: str | None
    pronouns: str | None
    avatar_url: str | None
    banner: str | None
    description: str | None
    created: str | None  # TODO datetime parse
    proxy_tags: list[PkProxyTag]
    keep_proxy: bool
    autoproxy_enabled: bool | None
    message_count: int | None
    last_message_timestamp: str | None  # TODO datetime parse
    privacy: PkMemberPrivacy | None

    def __init__(self, member_data: dict):
        self.id = member_data["id"]
        self.uuid = member_data["uuid"]
        self.name = member_data["name"]
        self.display_name = member_data["display_name"]
        self.color = member_data["color"]
        self.birthday = member_data["birthday"]
        self.pronouns = member_data["pronouns"]
        self.avatar_url = member_data["avatar_url"]
        self.banner = member_data["banner"]
        self.description = member_data["description"]
        self.created = member_data["created"]
        self.proxy_tags = generate_proxy_tag_list(member_data["proxy_tags"])
        self.keep_proxy = member_data["keep_proxy"]
        self.autoproxy_enabled = member_data["autoproxy_enabled"]
        self.message_count = member_data["message_count"]
        self.last_message_timestamp = member_data["last_message_timestamp"]

        if member_data["privacy"] is not None:
            self.privacy = PkMemberPrivacy(member_data["privacy"])
        else:
            self.privacy = None
