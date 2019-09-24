class State(object):

    def __init__(self, parentId, matrix, level, direction="Inicio", h=0):
        self.matrix = matrix
        self.h = int(h)
        self.parentId = parentId
        self.direction = direction
        self.level = int(level)
        self.childs = []
        self.coust = self.calculateHeuristicCoust()
        self.id = self.createId()

    def createId(self):
        id = ""
        for level in self.matrix.getValues():
            for val in level:
                id += str(val)

        return int(id)

    def calculateHeuristicCoust(self):
        return self.level + self.h
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
    def getH(self):
        return self.h
    def setH(self, newH):
        self.h = newH
