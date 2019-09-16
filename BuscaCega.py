
import copy
from State import State
from SearchEngine import SearchEngine
class BuscaCega(SearchEngine):

    def __init__(self, scrambledMatrix, goalMatrix):
        SearchEngine.__init__(self, scrambledMatrix, goalMatrix)
        self.stateId = 0
        self.goalState = None
        self.caminho = []

    def buscaCega(self):
        self.busca(None)

    def visitNode(self, currentState, matrix):
        validMoves = self.getValidMoves(matrix)
        for move in validMoves:
            self.stateId += 1
            tempMatrix = copy.deepcopy(matrix)
            tempMatrix.moveTo(move)
            newState = State( currentState.getId(), tempMatrix)
            if newState.getId() not in self.visitedStates:
                self.states[newState.getId()] = newState
                self.toVisitStates.append(newState)
        self.visitedStates.append(newState.getId())
