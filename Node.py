class Node(object):

    def __init__(self, value, level):
        self.value = value
        self.level = level
        self.h = 0 # heuristic

    def getValue(self):
        return self.value
    def setValue(self, newValue):
        self.value = newValue

    def getLevel(self):
        return self.level
    def setLevel(self, newLevel):
        self.level = newLevel

    def getH(self):
        return self.h
    def setH(self, newH):
        self.h = newH
