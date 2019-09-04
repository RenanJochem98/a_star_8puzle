class Node(object):

    def __init__(self, value, level):
        self.value = value
        self.level = level

    def getValue(self):
        return self.value
    def getLevel(self):
        return self.level
    def setValue(self, newValue):
        self.value = newValue
    def setLevel(self, newLevel):
        self.level = newLevel
