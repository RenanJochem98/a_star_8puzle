from HeuristicSearch import HeuristicSearch

class TwoStepsSearch(HeuristicSearch):

    def __init__(self, scrambledMatrix, goalMatrix):
        HeuristicSearch.__init__(self, scrambledMatrix, goalMatrix)

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
