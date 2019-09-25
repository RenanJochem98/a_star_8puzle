import copy
from State import State
from SearchEngine import SearchEngine
from Board import Board

class HeuristicSearch(SearchEngine):

    def __init__(self, scrambledMatrix, goalMatrix):
        SearchEngine.__init__(self, scrambledMatrix, goalMatrix)

    def buscaHeuristica(self):
        self.buscaResumida(None, True)

    def visitNode(self, currentState, matrix):
        validMoves = self.getValidMoves(matrix)
        newLevel = currentState.getLevel() + 1
        for move in validMoves:
            tempMatrix = copy.deepcopy(matrix)
            node = tempMatrix.moveTo(move)
            h = self.calculateHeuristic(tempMatrix)
            newState = State( currentState.getId(), tempMatrix, newLevel, move, h)
            exist = True
            count = 0
            for x in self.toVisitStates:
                if x.getId() == newState.getId():
                    exist = False
                    if newState.getCoust() < currentState.getCoust():
                        self.toVisitStates[count] = newState
                    break
                count+=1

            if newState.getId() not in self.visitedStates and exist:
                self.states[newState.getId()] = newState
                self.toVisitStates.append(newState)

        self.visitedStates.append(currentState.getId())
