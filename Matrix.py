import random
from Node import Node
from MatrixDisplay import MatrixDisplay
class Matrix(object):

    def __init__(self, type):
        self.upperLevel = 3 # precisa ficar antes de defineMatrix() para caso de matriz embaralhada
        self.emptyPosition = {'Horiz': None, 'Vert': None}
        self.emptyValue = 0
        self.display = MatrixDisplay()
        self.defineMatrix(type)

    def defineMatrix(self, type):
        if type == 'scrambled':
            self.matrix = self.mountScrambledMatrix()
        else:
            self.matrix = self.mountGoalMatrix()

    def getMatrix(self):
        return self.matrix

    def getUpperLevel(self):
        return self.upperLevel

    def getEmptyPosition(self):
        return self.emptyPosition

    def setEmptyPosition(self, horiz, vert):
        if horiz is not None:
            self.emptyPosition['Horiz'] = horiz
        if vert is not None:
            self.emptyPosition['Vert'] = vert

    def move(self, positonHoriz, positionVert):
        #verifica se movimento eh valido
        node = self.matrix[positonHoriz][positionVert]
        val = node.getValue()
        lev = node.getValue()
        self.matrix[self.emptyPosition['Horiz']][self.emptyPosition['Vert']] = node
        self.matrix[positonHoriz][positionVert] = Node(self.emptyValue, lev)
        self.emptyPosition['Horiz'] = positonHoriz
        self.emptyPosition['Vert'] =positionVert

    def moveTo(self, direction):
        if direction == 'left':
            newHoriz = self.emptyPosition['Vert'] - 1
            newVert = self.emptyPosition['Horiz']
            self.move(newHoriz, newVert)
        if direction == 'right':
            newHoriz = self.emptyPosition['Vert'] + 1
            newVert = self.emptyPosition['Horiz']
            self.move(newHoriz, newVert)
        if direction == 'up':
            newHoriz = self.emptyPosition['Vert']
            newVert = self.emptyPosition['Horiz'] - 1
            self.move(newHoriz, newVert)
        if direction == 'down':
            newHoriz = self.emptyPosition['Vert']
            newVert = self.emptyPosition['Horiz'] + 1
            self.move(newHoriz, newVert)


    def mountGoalMatrix(self):
        goalMatrix = []
        goalMatrix.append([Node(1,0),Node(2,0),Node(3,0)])
        goalMatrix.append([Node(4,1),Node(5,1),Node(6,1)])
        goalMatrix.append([Node(7,2),Node(8,2),Node(self.emptyValue,2)])

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
            if value == self.emptyValue:
                self.emptyPosition['Horiz'] = level
                self.emptyPosition['Vert'] = (count-1) % self.upperLevel
            if count % self.upperLevel == 0:
                scrambledMatrix.append(arr)
                arr = []
                level+=1
            count+=1
        return scrambledMatrix

    def showNodeMatrix(self):
        self.display.showMatrix(self.matrix, self.upperLevel)

    def showNodeMatrixDetailed(self):
        self.display.showMatrixDetailed(self.matrix, self.upperLevel)
