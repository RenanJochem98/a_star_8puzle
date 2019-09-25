from HeuristicSearch import HeuristicSearch
class OutOfPositionSearch(HeuristicSearch):

    def __init__(self, scrambledMatrix, goalMatrix):
        HeuristicSearch.__init__(self, scrambledMatrix, goalMatrix)

    # Heuristica: Numero de passos ate a posicao correta
    def calculateHeuristic(self, matrix=None):
        if matrix == None:
            matrix = self.scrambledMatrix
        estimateValue = 0
        scrPosHoriz = 0; #horizontal
        for scrLevel in matrix.getValues():
            scrPosVert = 0; #vertical
            for scrVal in scrLevel:
                estimateValue += self.outOfPositionSearch(scrVal, scrPosHoriz, scrPosVert)
                scrPosVert+=1
            scrPosHoriz+=1
        return estimateValue

    def outOfPositionSearch(self, value, positionHoriz, positionVert):
        result = 1
        if self.goalMatrix.getValues()[positionHoriz][positionVert] == value:
            result = 0
        return result
