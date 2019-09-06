import random
from Node import Node
class Matrix(object):

    def __init__(self, type):
        self.upperLevel = 3 # precisa ficar antes de defineMatrix() para caso de matriz embaralhada
        self.emptyPosition = {'Horiz': None, 'Vert': None}
        self.defineMatrix(type)

    def defineMatrix(self, type):
        if type == 'scrambled':
            self.matrix = self.mountScrambledMatrix()
        else:
            self.matrix = self.mountGoalMatrix()

    def getMatrix(self):
        return self.matrix

    def getEmptyPosition(self):
        return self.emptyPosition

    def setEmptyPosition(self, horiz, vert):
        if horiz is not None:
            self.emptyPosition['Horiz'] = horiz
        if vert is not None:
            self.emptyPosition['Vert'] = vert

    def mountGoalMatrix(self):
        goalMatrix = []
        goalMatrix.append([Node(1,0),Node(2,0),Node(3,0)])
        goalMatrix.append([Node(4,1),Node(5,1),Node(6,1)])
        goalMatrix.append([Node(7,2),Node(8,2),Node(0,2)])

        self.emptyPosition['Horiz'] = 2
        self.emptyPosition['Vert'] = 2

        return goalMatrix

    def mountScrambledMatrix(self):
        arr = []
        scrambledMatrix = []
        count = 1
        level = 0
        randomValues = random.sample(range(0,9), 9)
        for value in randomValues:
            arr.append(Node(value,level))
            if value == 0:
                self.emptyPosition['Horiz'] = (count-1) % self.upperLevel
                self.emptyPosition['Vert'] = level
            if count % self.upperLevel == 0:
                scrambledMatrix.append(arr)
                arr = []
                level+=1
            count+=1
        return scrambledMatrix

    def showNodeMatrix(self):
        print ("Visao resumida:")
        for level in self.matrix:
            count = 1
            for node in level:
                endLine = " "
                if count % self.upperLevel == 0:
                    endLine = "\n"
                print(node.getValue(), end=endLine)
                count+=1

    def showNodeMatrixDetailed(self):
        print ("Visao Detalhada:")
        print ("N = Nodo")
        print ("L = Nivel (Level)")
        print ("H = Heuristica")
        print ("")
        print ("N L H   N L H   N L H")
        for level in self.matrix:
            count = 1
            for node in level:
                endLine = "   "
                if count % self.upperLevel == 0:
                    endLine = "\n"
                print(node.getValue(),node.getLevel(),node.getH(), end=endLine)
                count+=1
