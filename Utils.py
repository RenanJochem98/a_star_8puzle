import random
from Node import Node
class Utils(object):

    def defineGoalMatrix():
        goalMatrix = []
        goalMatrix.append([Node(1,1),Node(2,1),Node(3,1)])
        goalMatrix.append([Node(1,4),Node(5,2),Node(6,2)])
        goalMatrix.append([Node(7,3),Node(8,3),Node(0,3)])
        return goalMatrix

    def defineScrambledMatrix():
        arr = []
        scrambledMatrix = []
        count = 1
        level = 1
        randomValues = random.sample(range(0,9), 9)
        for value in randomValues:
            arr.append(Node(value,level))
            if count % 3 == 0:
                scrambledMatrix.append(arr)
                arr = []
                level+=1
            count+=1
        return scrambledMatrix

    def showIntMatrix(matrix):
        for level in matrix:
            count = 1
            for value in level:
                endLine = " "
                if count % 3 == 0:
                    endLine = "\n"
                print(value, end=endLine)
                count+=1

    def showNodeMatrix(nodeMatrix):
        print ("N = Nodo")
        print ("L = Nivel (Level)")
        print ("\n")
        print ("N L   N L   N L")
        for level in nodeMatrix:
            count = 1
            for node in level:
                endLine = "   "
                if count % 3 == 0:
                    endLine = "\n"
                print(node.getValue(),node.getLevel(), end=endLine)
                count+=1
