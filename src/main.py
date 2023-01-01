# Notes for future us:
#   We finally finished it oh my god
#   Next step is either saving the system or member things,
#   your choice

from pluralkit.v2.client import Client
from pluralkit.v2.models import SystemId
from globals import config, console
from ps.system import PsSystem

client = Client(config["PluralKit"]["token"], async_mode=False)

pk_system = client.get_system(SystemId("exmpl"))
ps_system = PsSystem(pk_system)
ps_system_jpegged = PsSystem(ps_system.convert_to("pk"))

console.log(pk_system.description)
