import random
from BoardDisplay import BoardDisplay
class Board(object):

    def __init__(self, type, matrix=None):
        self.upperLevel = 3 # precisa ficar antes de defineMatrix() para caso de matriz embaralhada
        self.emptyPosition = {'Horiz': None, 'Vert': None}
        self.emptyValue = 0
        self.display = BoardDisplay()
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
            for val in level:
                if val == self.emptyValue:
                    self.setEmptyPosition(horizCount, vertCount)
                    break
                vertCount +=1
            horizCount +=1

    def move(self, positonHoriz, positionVert):
        #verifica se movimento eh valido
        val = self.matrix[positonHoriz][positionVert]

        result = self.matrix[self.emptyPosition['Horiz']][self.emptyPosition['Vert']]
        self.matrix[self.emptyPosition['Horiz']][self.emptyPosition['Vert']] = val

        self.matrix[positonHoriz][positionVert] = self.emptyValue
        self.emptyPosition['Horiz'] = positonHoriz
        self.emptyPosition['Vert'] =positionVert
        return result

    def moveTo(self, direction):
        node = ""
        if direction == 'left':
            newHoriz = self.emptyPosition['Horiz']
            newVert = self.emptyPosition['Vert'] - 1
            node= self.move(newHoriz, newVert)
        if direction == 'right':
            newHoriz = self.emptyPosition['Horiz']
            newVert = self.emptyPosition['Vert'] + 1
            node= self.move(newHoriz, newVert)
        if direction == 'up':
            newVert = self.emptyPosition['Vert']
            newHoriz = self.emptyPosition['Horiz'] - 1
            node= self.move(newHoriz, newVert)
        if direction == 'down':
            newHoriz = self.emptyPosition['Horiz'] + 1
            newVert = self.emptyPosition['Vert']
            node= self.move(newHoriz, newVert)
        return node

    def mountGoalMatrix(self):
        goalMatrix = []
        goalMatrix.append([1,2,3])
        goalMatrix.append([4,5,6])
        goalMatrix.append([7,8,self.emptyValue])
        # goalMatrix.append([Node(1,0),Node(2,0),Node(3,0)])
        # goalMatrix.append([Node(4,1),Node(5,1),Node(6,1)])
        # goalMatrix.append([Node(7,2),Node(8,2),Node(self.emptyValue,2)])

        return goalMatrix

    def mountScrambledMatrix(self):
        # para testes
        scrambledMatrix = []
        ## Facil
        # scrambledMatrix.append([self.emptyValue,1,2])
        # scrambledMatrix.append([4,5,3])
        # scrambledMatrix.append([7,8,6])

        ## Dificil
        # scrambledMatrix.append([4,7,5])
        # scrambledMatrix.append([self.emptyValue,2,1])
        # scrambledMatrix.append([3,6,8])

        ## Menos facil
        scrambledMatrix.append([5,4,2])
        scrambledMatrix.append([7,1,3])
        scrambledMatrix.append([self.emptyValue,8,6])

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
        self.display.showBoard(self.matrix, self.upperLevel)

    def showNodeMatrixDetailed(self):
        self.display.showBoardDetailed(self.matrix, self.upperLevel)
