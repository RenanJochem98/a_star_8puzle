class SearchEngine(object):

    def __init__(self, scrambledMatrix, goalMatrix):
        self.scrambledMatrix = scrambledMatrix
        self.goalMatrix = goalMatrix

    # Heuristica: Numero de passos ate a posicao correta
    def calculateHeuristic(self):
        scrPosY = 0; #vertical
        for scrLevel in self.scrambledMatrix:
            scrPosX = 0; #horizontal
            for scrNode in scrLevel:
                value = scrNode.getValue()


    def numberSteps(self, value, positionX, positionY):
        searchedY = -1
        for level in self.goalMatrix:
            searchedX = -1
            searchedY+=1
            for node in level:
                searchedX+=1
                if node.getValue() == value:
                    break
            searchedX = -1

        value = (positionX - searchedX)+(positionY - searchedY)
