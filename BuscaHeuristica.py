import copy
from State import State
from SearchEngine import SearchEngine
from Board import Board

class BuscaHeuristica(SearchEngine):

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


    # Heuristica: Numero de passos ate a posicao correta
    def calculateHeuristic(self, matrix=None):
        if matrix == None:
            matrix = self.scrambledMatrix
        estimateValue = 0
        scrPosHoriz = 0; #horizontal
        for scrLevel in matrix.getValues():
            scrPosVert = 0; #vertical
            for scrVal in scrLevel:
                estimateValue += self.numberSteps(scrVal, scrPosHoriz, scrPosVert)
                scrPosVert+=1
            scrPosHoriz+=1
        return estimateValue

    def numberSteps(self, value, positionHoriz, positionVert):
        searched = False
        searchedHoriz = -1
        for level in self.goalMatrix.getValues():
            searchedVert = -1
            searchedHoriz+=1
            for val in level:
                searchedVert+=1
                if val == value:
                    searched = True
                    break
            if searched:
                break

        numberStepsHoriz = abs(searchedHoriz - positionHoriz)
        numberStepsVert = abs(searchedVert - positionVert)
        numberSteps = numberStepsHoriz + numberStepsVert
        return numberSteps
