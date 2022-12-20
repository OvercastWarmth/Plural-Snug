from json import load
from rich.console import Console
from rich.traceback import install


with open("config.json") as f:
    config = load(f)

PLURALKIT_TOKEN = config["PluralKit"]["token"]
PLURALKIT_API = "https://api.pluralkit.me/v2"
DB_PATH = config["database"]

try:
    console = Console()
    install()
except NameError:

    class FakeConsole:
        def log(self, value) -> None:
            print(value)

    console = FakeConsole()
    console.log(
        "You don't have rich installed, so the console won't look as nice. You can fix that with `pip install rich` "
        "if you like. "
    )


def get_key(dictionary, value):
    """Get the key of a value in a dictionary

    Args:
        dictionary (dict): Dictionary to search
        value (any): Value to search for

    Returns:
        any: The key for the value found
    """
    return list(dictionary.keys())[list(dictionary.values()).index(value)]
