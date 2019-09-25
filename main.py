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
# matrix =  newInput.pedeMatrizInicial()
goalBoard = Board('goal')
scrambledBoard = Board('scrambled')

# blindSearch = BlindSearch(scrambledBoard, goalBoard)
# outOfPosition = OutOfPositionSearch(scrambledBoard, goalBoard)
# twoSteps = TwoStepsSearch(scrambledBoard, goalBoard)

opt = None
while opt != 0:
    try:
        print("Escolha o algoritimo de busca:")
        print("1 - Busca Cega:")
        print("2 - Busca Heuristica(Numero de passos até a posicao correta)(Busca Boa):")
        print("3 - Busca Heuristica(Valores fora de posição)(Não tão boa):")
        print("4 - Trocar tabuleiro")
        print("0 - Finalizar")
        opt = int(input())
    except ValueError:
        print("Você digitou um valor que não é um número!!!")
    print("\n")
    if opt == 1:
        searchEngine = BlindSearch(scrambledBoard, goalBoard)
    elif  opt == 2:
        searchEngine = TwoStepsSearch(scrambledBoard, goalBoard)
    elif  opt == 3:
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
        print("####  INICIO DA BUSCA HEURISTICA ####")
        print("\n")
        searchEngine.busca()
        print("####   FIM BUSCA HEURISTICA ####")
        time.sleep(2)
    print("\n")
print("#"*30)
print(" "*4+"FINALIZANDO ALGORITMO")
print("#"*30)
