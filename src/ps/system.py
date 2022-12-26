from datetime import datetime
from os.path import exists, join
from typing import Optional

from globals import DB_PATH
from ps.globals import Metadata
from pluralkit.v2.models import (
    System as PluralKitSystem,
    Privacy as PluralKitPrivacy,
)


# System class and related functions
class PsSystem:
    name: Optional[str]
    description: Optional[str]
    tag: Optional[str]
    pronouns: Optional[str]
    avatar: Optional[str]
    banner: Optional[str]
    color: Optional[str]
    birthday: Optional[datetime]
    metadata: list[Metadata]

    def __init__(self, system: PluralKitSystem):
        if system.__class__ == PluralKitSystem:
            from_pk(self, system)


class PluralKitSystemMetadata(Metadata):
    id: str
    uuid: str
    created: datetime
    privacy: dict[str, PluralKitPrivacy]

    type = "PluralKit"

    def __init__(self, system: PluralKitSystem):
        self.id = system.id.id
        self.uuid = system.id.uuid
        self.created = system.created.datetime
        self.privacy = {
            "description_privacy": system.description_privacy,
            "pronoun_privacy": system.pronoun_privacy,
            "member_list_privacy": system.member_list_privacy,
            "group_list_privacy": system.group_list_privacy,
            "front_privacy": system.front_privacy,
            "front_history_privacy": system.front_history_privacy,
        }


def from_pk(self: PsSystem, system: PluralKitSystem):
    self.name = system.name
    self.description = system.description
    self.tag = system.tag
    self.pronouns = system.pronouns
    self.avatar = system.avatar_url
    self.banner = system.banner
    self.color = system.color

    if check_system_exists():
        pass
    else:
        self.metadata = [PluralKitSystemMetadata(system)]


def check_system_exists() -> bool:
    """Checks if the system file exists"""
    return exists(join(DB_PATH, "system.json"))
