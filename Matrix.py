import random
from Node import Node
from MatrixDisplay import MatrixDisplay
class Matrix(object):

    def __init__(self, type, matrix=None):
        self.upperLevel = 3 # precisa ficar antes de defineMatrix() para caso de matriz embaralhada
        self.emptyPosition = {'Horiz': None, 'Vert': None}
        self.emptyValue = 0
        self.display = MatrixDisplay()
        self.defineMatrix(type, matrix)

    def defineMatrix(self, type, matrix):
        if type == 'scrambled':
            self.matrix = self.mountScrambledMatrix()
        elif type == 'goal':
            self.matrix = self.mountGoalMatrix()
        else:
            self.matrix = matrix
            self.searchEmptyPosition()

    def getValues(self):
        return self.matrix

    def setValues(self, newMatrix):
        self.matrix = newMatrix;

    def getUpperLevel(self):
        return self.upperLevel

    def getEmptyPosition(self):
        return self.emptyPosition

    def setEmptyPosition(self, horiz, vert):
        if horiz is not None:
            self.emptyPosition['Horiz'] = horiz
        if vert is not None:
            self.emptyPosition['Vert'] = vert

    def searchEmptyPosition(self):
        horizCount = 0
        for level in self.matrix:
            vertCount = 0
            for node in level:
                if node.getValue() == self.emptyValue:
                    self.setEmptyPosition(horizCount, vertCount)
                    break
                vertCount +=1
            horizCount +=1

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
            newHoriz = self.emptyPosition['Horiz']
            newVert = self.emptyPosition['Vert'] - 1
            self.move(newHoriz, newVert)
        if direction == 'right':
            newHoriz = self.emptyPosition['Horiz']
            newVert = self.emptyPosition['Vert'] + 1
            self.move(newHoriz, newVert)
        if direction == 'up':
            newVert = self.emptyPosition['Vert']
            newHoriz = self.emptyPosition['Horiz'] - 1
            self.move(newHoriz, newVert)
        if direction == 'down':
            newHoriz = self.emptyPosition['Horiz'] + 1
            newVert = self.emptyPosition['Vert']
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
        # para testes
        scrambledMatrix = []
        scrambledMatrix.append([Node(5,1),Node(4,1),Node(2,0)])
        scrambledMatrix.append([Node(self.emptyValue,2),Node(1,0),Node(3,0)])
        scrambledMatrix.append([Node(7,2),Node(8,2),Node(6,1)])

        self.emptyPosition['Horiz'] = 1
        self.emptyPosition['Vert'] = 0

        # arr = []
        # scrambledMatrix = []
        # count = 1
        # level = 0
        # randomValues = random.sample(range(0,9), 9)
        # for value in randomValues:
        #     arr.append(Node(value,level))
        #     if value == self.emptyValue:
        #         self.emptyPosition['Horiz'] = level
        #         self.emptyPosition['Vert'] = (count-1) % self.upperLevel
        #     if count % self.upperLevel == 0:
        #         scrambledMatrix.append(arr)
        #         arr = []
        #         level+=1
        #     count+=1
        return scrambledMatrix

    def showNodeMatrix(self):
        self.display.showMatrix(self.matrix, self.upperLevel)

    def showNodeMatrixDetailed(self):
        self.display.showMatrixDetailed(self.matrix, self.upperLevel)
