from ps.globals import Metadata


class PsSystem:
    id: str
    name: str | None
    description: str | None
    tag: str | None
    pronouns: str | None
    avatar_url: str | None
    banner: str | None
    color: str | None
    birthday: str | None
    metadata: list[Metadata]
