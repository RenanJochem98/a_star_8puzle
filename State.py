class State(object):

    def __init__(self, parentId, matrix, level, direction=""):
        self.matrix = matrix
        self.coust = 0
        self.id = self.createId()
        self.parentId = parentId
        self.direction = direction
        self.level = level
        self.childs = []
        self.h = 0

    def createId(self):
        id = ""
        for level in self.matrix.getValues():
            for val in level:
                id += str(val)
        if self.coust > 0:
            id += str(self.coust)

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
    def getH(self):
        return self.h
    def setH(self, newH):
        self.h = newH
    def getOrdered(self):
        value = self.h + self.coust
        return value
