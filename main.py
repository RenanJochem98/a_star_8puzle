from Board import Board
# from SearchEngine import SearchEngine
from BuscaCega import BuscaCega
from BuscaHeuristica import BuscaHeuristica

print("")
print("#"*30)
print(" "*7+"INICIANDO BUSCA")
print("#"*30)
print("\n")

goalBoard = Board('goal')
scrambledBoard = Board('scrambled')
buscaCega = BuscaCega(scrambledBoard, goalBoard)
buscaHeuristica = BuscaHeuristica(scrambledBoard, goalBoard)


print("Matriz objetivo:")
goalBoard.showNodeMatrix()
print("\n")

print("Matriz Inicial:")
scrambledBoard.showNodeMatrix()
print("\n")

print("####  INICIO BUSCA CEGA ####")
print("\n")
buscaCega.buscaCega()
print("####   FIM BUSCA CEGA ####")
print("####  INICIO BUSCA HEURISTICA ####")
print("\n")
buscaHeuristica.buscaHeuristica()
print("####   FIM BUSCA HEURISTICA ####")

print("\n")
print("#"*30)
print(" "*4+"FINALIZANDO ALGORITMO")
print("#"*30)
