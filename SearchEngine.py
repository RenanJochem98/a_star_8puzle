class SearchEngine(object):

    def __init__(self, scrambledMatrix, goalMatrix):
        self.scrambledMatrix = scrambledMatrix
        self.goalMatrix = goalMatrix

    def getScrambledMatrix(self):
        return self.scrambledMatrix

    def setScrambledMatrix(self, newMatrix):
        self.scrabledmatrix = newMatrix

    def getGoalMatrix(self):
        return self.goalMatrix

    # Heuristica: Numero de passos ate a posicao correta
    def calculateHeuristic(self):
        scrPosHoriz = 0; #horizontal
        for scrLevel in self.scrambledMatrix.getMatrix():
            scrPosVert = 0; #vertical
            for scrNode in scrLevel:
                value =scrNode.getValue()
                numberSteps = self.numberSteps(value, scrPosHoriz, scrPosVert)
                scrNode.setH(numberSteps)
                # print(scrPosHoriz, end=" ")
                # print(scrPosVert, end=" ")
                # print(value, end=" ")
                # print(numberSteps)
                scrPosVert+=1
            scrPosHoriz+=1

    def numberSteps(self, value, positionHoriz, positionVert):
        searched = False
        searchedHoriz = -1
        for level in self.goalMatrix.getMatrix():
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
