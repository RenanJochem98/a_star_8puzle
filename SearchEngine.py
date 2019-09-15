from State import State
class SearchEngine(object):

    def __init__(self, scrambledMatrix, goalMatrix):
        self.scrambledMatrix = scrambledMatrix
        self.goalMatrix = goalMatrix
        self.states = {}
        self.toVisitStates = []
        self.visitedStates = []

    def getScrambledMatrix(self):
        return self.scrambledMatrix

    def setScrambledMatrix(self, newMatrix):
        self.scrabledmatrix = newMatrix

    def getGoalMatrix(self):
        return self.goalMatrix

    # procura por algum valor diferente
    def isGoalMatrix(self, compareMatrix):
        finded = True
        horiz = 0
        for scrLevel in compareMatrix.getValues():
            vert = 0
            for scrNode in scrLevel:
                value = self.goalMatrix.getValues()[horiz][vert].getValue()
                if scrNode.getValue() != value:
                    finded = False
                    break
                vert += 1
            if not finded:
                break
            horiz += 1
        return finded

    def getValidMoves(self, state):
        emptyPosition = state.getEmptyPosition() #dict com posicao vertical e horizontal
        leftPosition = emptyPosition['Vert']-1
        rightPosition = emptyPosition['Vert']+1
        upPosition = emptyPosition['Horiz']-1
        downPosition = emptyPosition['Horiz']+1

        movePositions = {'left': leftPosition, 'right': rightPosition, 'up': upPosition, 'down': downPosition}

        validMoves = []
        for position in movePositions:
            if movePositions[position] >= 0 and movePositions[position] < state.getUpperLevel():
                validMoves.append(position)

        return validMoves
