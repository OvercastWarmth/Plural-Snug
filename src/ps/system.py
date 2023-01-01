from datetime import datetime
from os.path import exists, join
from typing import Optional

from colour import Color

from globals import DB_PATH
from ps.globals import Metadata
from pluralkit.v2.models import (
    System as PluralKitSystem,
    Privacy as PluralKitPrivacy,
)


# System class and related functions
class PsSystem:
    """Represents a PluralSnug System

    Most of the values here are used in social models that can display system-wide information

    Class creation should be passed a supported system model from another api, PS will convert it
    (full list under 'Conversion Types')

    Attributes:
        name: The system's display name
        description: The system's description
        tag: The tag appended to the name in applicable proxy services
        pronouns: The system's pronouns
        avatar: The system's avatar image url
        banner: The system's banner image url
        color: The system's color as a hex code
        birthday: The system's birthday
        metadata: A list of metadata for specific services (non optional but can be empty)

    Conversion Types:
        PluralKitSystem from pluralkit.v2.models
    """

    name: Optional[str] = None
    description: Optional[str] = None
    tag: Optional[str] = None
    pronouns: Optional[str] = None
    avatar: Optional[str] = None
    banner: Optional[str] = None
    color: Optional[Color] = None
    birthday: Optional[datetime] = None
    metadata: dict[str, Metadata] = {}

    def __init__(self, system: PluralKitSystem):
        if system.__class__ == PluralKitSystem:
            from_pk(self, system)
        else:
            raise TypeError(
                f"{system}, instance of {system.__class__}, is not a supported conversion type"
            )

    def __str__(self):
        return f"PS System with name {self.name}"

    def saveable_dict(self):
        """Generates a dictionary capable of being converted to json directly and saved
        (all values are json acceptable)
        """

        # Handle metadata correctly
        metadata = {}
        for service, data in self.metadata.items():
            metadata[service] = data.dict()

        return {
            "name": self.name,
            "description": self.description,
            "tag": self.tag,
            "pronouns": self.pronouns,
            "avatar": self.avatar,
            "banner": self.banner,
            "color": self.color.hex if self.color is not None else None,
            "birthday": self.birthday.isoformat() + "Z"
            if self.birthday is not None
            else None,
            "metadata": metadata,
        }

    def convert_to(self, service: str) -> any:
        match service:
            case "pk":
                return to_pk(self)
            case _:
                raise ValueError(f"{service} is not a valid service type")


class PluralKitSystemMetadata(Metadata):
    """Represents PluralKit system metadata

    Attributes:
        id (str): PluralKit's 5 letter system ID
        uuid (str): PluralKit's unique UUID
        created (datetime): The system's creation timestamp
        privacy (dict[str, PluralKitPrivacy]): Dictionary of privacy keys : objects
    """

    id: str
    uuid: str
    created: Optional[datetime]
    privacy: Optional[dict[str, PluralKitPrivacy]]

    type = "PluralKit"

    def __init__(self, system: PluralKitSystem):
        self.id = system.id.id
        self.uuid = system.id.uuid
        self.created = system.created.datetime if system.created is not None else None
        self.privacy = {
            "description_privacy": system.description_privacy,
            "pronoun_privacy": system.pronoun_privacy,
            "member_list_privacy": system.member_list_privacy,
            "group_list_privacy": system.group_list_privacy,
            "front_privacy": system.front_privacy,
            "front_history_privacy": system.front_history_privacy,
        }

        # pluralkit.py complains unless we format null privacy api-consistent
        privacy_given = False
        for privacy in self.privacy.values():
            if privacy is not None:
                privacy_given = True
                break
        if not privacy_given:
            self.privacy = None

    def dict(self) -> dict:
        # Handle privacy separately
        if self.privacy is not None:
            privacy = {}
            for i, v in self.privacy.items():
                privacy[i] = v.value
        else:
            privacy = None

        return {
            "id": self.id,
            "uuid": self.uuid,
            "created": self.created.isoformat(timespec="seconds") + "Z",
            "privacy": privacy,
        }


def from_pk(self: PsSystem, system: PluralKitSystem) -> None:
    """Helper function for converting PK Systems to PS Systems

    Args:
        self: A PsSystem
        system: A PluralKitSystem to source the values from
    """

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
        self.metadata = {"PluralKit": PluralKitSystemMetadata(system)}


def to_pk(system: PsSystem) -> PluralKitSystem:
    metadata = system.metadata["PluralKit"]
    return PluralKitSystem(
        {
            "id": metadata.id,
            "uuid": metadata.uuid,
            "name": system.name,
            "description": system.description,
            "tag": system.tag,
            "pronouns": system.pronouns,
            "avatar_url": system.avatar,
            "banner": system.banner,
            "color": system.color,
            "created": metadata.created,
            "privacy": metadata.privacy,
        }
    )


def check_system_exists() -> bool:
    """Checks if the system file exists"""
    return exists(join(DB_PATH, "system.json"))
