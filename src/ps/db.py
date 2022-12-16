"""Methods for managing the PluralSnug database"""

from json import dump as dumpJson
from json import load as loadJson

from globals import DB_PATH


def loadSystemEntry() -> dict:
    """Load the PluralSnug system entry to a python dictionary

    Returns:
        dict: The system entry
    """
    with open(f"{DB_PATH}/system.json") as f:
        return loadJson(f)


def overwriteSystemEntry(systemModel: dict) -> None:
    """Overwrite the system entry's data

    Args:
        systemModel (dict): The model to overwrite the entry with
    """
    with open(f"{DB_PATH}/system.json", "w") as f:
        dumpJson(systemModel, f, indent=4)


def loadMemberEntry(memberID: int) -> dict:
    """Load a PluralSnug member entry to a python dictionary

    Returns:
        dict: The member entry
    """
    with open(f"{DB_PATH}/members/{memberID}.json") as f:
        return loadJson(f)


def overwriteMemberEntry(memberModel: dict) -> None:
    """Overwrite the system entry's data

    Args:
        systemModel (dict): The model to overwrite the entry with
    """
    with open(f"{DB_PATH}/members/{memberModel['id']}.json", "w") as f:
        dumpJson(memberModel, f, indent=4)
