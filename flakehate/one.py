from flake8.checker import FileChecker


class PluginOne(FileChecker):

	name = "flakehate"
	version = "666"

	def __init__(self, *a, **kw):
		print(a, kw)

