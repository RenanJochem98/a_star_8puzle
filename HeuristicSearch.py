import copy
from abc import abstractmethod
from operator import attrgetter
from State import State
from SearchEngine import SearchEngine
from Board import Board

class HeuristicSearch(SearchEngine):

    def __init__(self, scrambledMatrix, goalMatrix):
        SearchEngine.__init__(self, scrambledMatrix, goalMatrix)

    @abstractmethod
    def calculateHeuristic(self, matrix=None):
        pass

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
            # for x in self.frontier:
            #     if x.getId() == newState.getId():
            #         exist = False
            #         if newState.getCoust() < x.getCoust():
            #             self.frontier[count] = newState
            #         break
            #     count+=1

            if newState.getId() not in self.visitedStates and exist:
                self.states[newState.getId()] = newState
                self.frontier.append(newState)

        self.frontier.sort(key=attrgetter("coust"))
