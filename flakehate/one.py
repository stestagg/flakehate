from flake8.checker import FileChecker


class PluginOne(FileChecker):

    name = "flakehate"
    version = "666"
    def __init__(self, tree, filename):
        self.filename = filename

    def run(self):
        lengths = set()
        with open(self.filename) as myfile:
            for i, line in enumerate(myfile.readlines()):
                if len(line) in lengths:
                    yield i, 0, "Already have line of length {}".format(len(line)), type(self)
                else:
                    lengths.add(len(line))

