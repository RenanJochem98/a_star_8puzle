from Node import Node
from Matrix import Matrix
# from SearchEngine import SearchEngine
from BuscaCega import BuscaCega
from BuscaHeuristica import BuscaHeuristica

print("")
print("#"*30)
print(" "*7+"INICIANDO BUSCA")
print("#"*30)
print("\n")

goalMatrix = Matrix('goal')
scrambledMatrix = Matrix('scrambled')
buscaCega = BuscaCega(scrambledMatrix, goalMatrix)
buscaHeuristica = BuscaHeuristica(scrambledMatrix, goalMatrix)


print("Matriz objetivo:")
goalMatrix.showNodeMatrix()
print("\n")

print("Matriz Inicial:")
scrambledMatrix.showNodeMatrix()
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
