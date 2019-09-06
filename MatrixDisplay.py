class MatrixDisplay(object):

    def showNodeMatrix(matrix, breakLineMatrix):
        print ("Visao resumida:")
        for level in matrix:
            count = 1
            for node in level:
                endLine = " "
                if count % breakLineMatrix == 0:
                    endLine = "\n"
                print(node.getValue(), end=endLine)
                count+=1

    def showNodeMatrixDetailed(matrix, breakLineMatrix):
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
                if count % breakLineMatrix == 0:
                    endLine = "\n"
                print(node.getValue(),node.getLevel(),node.getH(), end=endLine)
                count+=1
