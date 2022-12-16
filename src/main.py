from pk.member import getMemberList, massImport
from ps.index import refreshIndexFile

massImport(getMemberList())
refreshIndexFile()
