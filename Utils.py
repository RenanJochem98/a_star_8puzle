import random
from Node import Node
class Utils(object):

    def __init__(self):
        self.upperLevel = 3

    def defineGoalMatrix(self):
        goalMatrix = []
        goalMatrix.append([Node(1,0),Node(2,0),Node(3,0)])
        goalMatrix.append([Node(4,1),Node(5,1),Node(6,1)])
        goalMatrix.append([Node(7,2),Node(8,2),Node(0,2)])
        return goalMatrix

    def defineScrambledMatrix(self):
        arr = []
        scrambledMatrix = []
        count = 1
        level = 0
        randomValues = random.sample(range(0,9), 9)
        for value in randomValues:
            arr.append(Node(value,level))
            if count % self.upperLevel == 0:
                scrambledMatrix.append(arr)
                arr = []
                level+=1
            count+=1
        return scrambledMatrix

    def showIntMatrix(self, matrix):
        for level in matrix:
            count = 1
            for value in level:
                endLine = " "
                if count % self.upperLevel == 0:
                    endLine = "\n"
                print(value, end=endLine)
                count+=1

    def showNodeMatrix(self, nodeMatrix):
        print ("Visao resumida:")
        for level in nodeMatrix:
            count = 1
            for node in level:
                endLine = " "
                if count % self.upperLevel == 0:
                    endLine = "\n"
                print(node.getValue(), end=endLine)
                count+=1

    def showNodeMatrixDetailed(self, nodeMatrix):
        print ("Visao Detalhada:")
        print ("N = Nodo")
        print ("L = Nivel (Level)")
        print ("H = Heuristica")
        print ("")
        print ("N L H   N L H   N L H")
        for level in nodeMatrix:
            count = 1
            for node in level:
                endLine = "   "
                if count % self.upperLevel == 0:
                    endLine = "\n"
                print(node.getValue(),node.getLevel(),node.getH(), end=endLine)
                count+=1
