
class Result(object):
    """docstring for Result."""
    name = ''
    size = ''
    time = ''
    magenatic = ''

    def __init__(self, arg):
        super(Result, self).__init__()
        self.arg = arg

    def addName(self,name):
        self.name = name

    def addSize(self,size):
        self.size = size

    def addTime(self,Time):
        self.time = time

    def addMage(self,add):
        self.magenatic = add
