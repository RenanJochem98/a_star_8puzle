from Board import Board
from BlindSearch import BlindSearch
from TwoStepsSearch import TwoStepsSearch
from OutOfPositionSearch import OutOfPositionSearch
from Input import Input
import time

print("")
print("#"*30)
print(" "*7+"INICIANDO BUSCA")
print("#"*30)
print("\n")

newInput = Input()
goalBoard = Board('goal')
scrambledBoard = Board('scrambled')

print("Tabuleiro Objetivo:")
goalBoard.showNodeMatrix()
print("")
print("Tabuleiro Inicial:")
scrambledBoard.showNodeMatrix()
print("")

opt = None
while opt != 0:
    opt = newInput.showSearchOption()

    if opt == 1:
        searchTitle = "BUSCA CEGA"
        searchEngine = BlindSearch(scrambledBoard, goalBoard)
    elif  opt == 2:
        searchTitle = "BUSCA HEURISTICA BOA"
        searchEngine = TwoStepsSearch(scrambledBoard, goalBoard)
    elif  opt == 3:
        searchTitle = "BUSCA HEURISTICA MEDIA"
        searchEngine = OutOfPositionSearch(scrambledBoard, goalBoard)

    elif  opt == 4:
        matrix =  newInput.pedeMatrizInicial()
        scrambledBoard = Board('matrix', matrix)
        print("Matriz Inicial Alterado:")
        scrambledBoard.showNodeMatrix()
        time.sleep(2)

    elif  opt == 0:
        print("Fim")
    else:
        print("Você digitou uma opção fora dos limites!!")

    if opt != 0 and opt != 4:
        print("####  INICIO DA "+searchTitle+" ####")
        print("\n")
        searchEngine.busca()
        print("####   FIM DA "+searchTitle+" ####")
        time.sleep(2)
    print("\n")

print("#"*30)
print(" "*4+"FINALIZANDO ALGORITMO")
print("#"*30)
