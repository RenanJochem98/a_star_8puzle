class BoardDisplay(object):

    def showBoard(self, matrix, breakLineBoard):
        print ("Visao resumida:")
        for level in matrix:
            count = 1
            for val in level:
                endLine = " "
                if count % breakLineBoard == 0:
                    endLine = "\n"
                print(val, end=endLine)
                count+=1

    def showBoardDetailed(self, matrix, breakLineBoard):
        print ("Visao Detalhada:")
        print ("N = Nodo")
        print ("L = Nivel (Level)")
        print ("H = Heuristica")
        print ("")
        print ("N L H   N L H   N L H")
        for level in matrix:
            count = 1
            for node in level:
                endLine = "   "
                if count % breakLineBoard == 0:
                    endLine = "\n"
                print(node.getValue(),node.getLevel(),node.getH(), end=endLine)
                count+=1
