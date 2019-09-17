class State(object):

    def __init__(self, parentId, matrix, level, direction=""):
        self.matrix = matrix
        self.id = self.createId()
        self.parentId = parentId
        self.direction = direction
        self.level = level
        self.childs = []
        self.coust = 0
        self.h = 0
        self.visited = False

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
    def getCoust(self):
        return self.coust
    def setCoust(self, newCoust):
        self.coust = newCoust
    def addCoust(self):
        self.coust +=1
    def setH(self, newH):
        self.h = newH
    def getVisited(self):
        return self.visited
    def setVisited(self, newVisited):
        self.visited = newVisited
    def getOrdered(self):
        value = self.h + self.coust
        return value
