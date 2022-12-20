# TODO Finish member models


class PkMemberPrivacy:
    pass


class PkProxyTag:
    prefix: str | None
    suffix: str | None


class PkMember:
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
