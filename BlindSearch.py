
import copy
from State import State
from SearchEngine import SearchEngine
class BlindSearch(SearchEngine):

    def __init__(self, scrambledMatrix, goalMatrix):
        SearchEngine.__init__(self, scrambledMatrix, goalMatrix)

    def buscaCega(self):
        self.buscaResumida(None)

    def visitNode(self, currentState, matrix):
        validMoves = self.getValidMoves(matrix)
        newLevel = currentState.getLevel() + 1
        self.currentLevel = newLevel
        for move in validMoves:
            self.stateId += 1
            tempMatrix = copy.deepcopy(matrix)
            tempMatrix.moveTo(move)
            newState = State( currentState.getId(), tempMatrix, newLevel, move)
            if newState.getId() not in self.visitedStates:
                self.states[newState.getId()] = newState
                self.toVisitStates.append(newState)
        self.visitedStates.append(currentState.getId())
