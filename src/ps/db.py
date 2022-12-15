from globals import DB_PATH
from json import load as loadJson, dump as dumpJson


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
        dumpJson(systemModel, f)
