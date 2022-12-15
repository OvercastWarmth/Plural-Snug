from json import load
from rich.console import Console
from rich.traceback import install

install()

with open("config.json") as f:
    config = load(f)

PLURALKIT_TOKEN = config["PluralKit"]["token"]
PLURALKIT_API = "https://api.pluralkit.me/v2"
DB_PATH = config["database"]

try:
    console = Console()
except:
    class FakeConsole():
        def log(self, value):
            print(value)

    console = FakeConsole()
    console.log("You don't have rich installed, so the console won't look as nice. You can fix that with `pip install rich` if you like.")