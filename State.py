class State(object):

    def __init__(self, parentId, matrix, level, direction=""):
        self.matrix = matrix
        self.id = self.createId()
        self.parentId = parentId
        self.direction = direction
        self.level = level
        self.childs = []

    def createId(self):
        id = ""
        for level in self.matrix.getValues():
            for node in level:
                id += str(node.getValue())
        return int(id)
    def getDirection(self):
        return self.direction
    def getId(self):
        return self.id
    def getParentId(self):
        return self.parentId
    def getMatrix(self):
        return self.matrix
    def getLevel(self):
        return self.level
    def addChild(self, childId):
        self.childs.append(childId)
