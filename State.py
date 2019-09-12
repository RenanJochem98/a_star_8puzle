class State(object):

    def __init__(self, newId, parentId, matrix):
        self.id = newId
        self.parentId = parentId
        self.matrix = matrix
        self.childs = []

    def getId(self):
        return self.id
    def getMatrix(self):
        return self.matrix
    def addChild(self, childId):
        self.childs.append(childId)
