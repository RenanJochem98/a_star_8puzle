import random
class Utils(object):

    def defineGoalMatrix():
        goalMatrix = []
        goalMatrix.append([1,2,3])
        goalMatrix.append([4,5,6])
        goalMatrix.append([7,8,0])
        return goalMatrix

    def defineScrambledMatrix():
        arr = []
        scrambledMatrix = []
        count = 1
        randomValues = random.sample(range(10), 10) # comeca no zero...
        for value in randomValues:
            arr.append(value)
            if count % 3 == 0:
                scrambledMatrix.append(arr)
                arr = []
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
