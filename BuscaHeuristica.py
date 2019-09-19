import copy
from State import State
from SearchEngine import SearchEngine
class BuscaHeuristica(SearchEngine):

    def __init__(self, scrambledMatrix, goalMatrix):
        SearchEngine.__init__(self, scrambledMatrix, goalMatrix)

    def buscaHeuristica(self):
        self.buscaResumida(None, True)

    def visitNode(self, currentState, matrix):
        validMoves = self.getValidMoves(matrix)
        newLevel = currentState.getLevel() + 1
        self.currentLevel = newLevel
        for move in validMoves:
            self.stateId += 1
            tempMatrix = copy.deepcopy(matrix)
            node = tempMatrix.moveTo(move)
            newState = State( currentState.getId(), tempMatrix, newLevel, move)
            h = self.calculateHeuristic(tempMatrix)
            newState.setH(h)
            if newState.getId() not in self.visitedStates:
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
            for scrNode in scrLevel:
                value =scrNode.getValue()
                estimateValue += self.numberSteps(value, scrPosHoriz, scrPosVert)
                # scrNode.setH(numberSteps)
                scrPosVert+=1
            scrPosHoriz+=1
        return estimateValue

    def numberSteps(self, value, positionHoriz, positionVert):
        searched = False
        searchedHoriz = -1
        for level in self.goalMatrix.getValues():
            searchedVert = -1
            searchedHoriz+=1
            for node in level:
                searchedVert+=1
                if node.getValue() == value:
                    searched = True
                    break
            if searched:
                break

        numberStepsHoriz = abs(searchedHoriz - positionHoriz)
        numberStepsVert = abs(searchedVert - positionVert)
        numberSteps = numberStepsHoriz + numberStepsVert
        return numberSteps
