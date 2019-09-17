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
searchEngine = BuscaCega(scrambledMatrix, goalMatrix)
searchEngine2 = BuscaHeuristica(scrambledMatrix, goalMatrix)


print("Matriz objetivo:")
# goalMatrix.showNodeMatrix()
# print("\n")

print("Matriz Inicial:")
scrambledMatrix.showNodeMatrix()
print("\n")
# scrambledMatrix.showNodeMatrixDetailed()
# print("\n")

print("Valores Calculados:")
print("\n")
# print(searchEngine.isGoalMatrix(scrambledMatrix))
# searchEngine.calculateHeuristic()
# searchEngine.getScrambledMatrix().showNodeMatrixDetailed()
# print("\n")
# horiz = int(input("Posicao Horizontal: "))
# vert = int(input("Posicao Vertical: "))
# scrambledMatrix.move(horiz, vert)
# scrambledMatrix.showNodeMatrix()
print("####  INICIO BUSCA CEGA ####")
print("\n")
searchEngine.buscaCega()
print("####   FIM BUSCA CEGA ####")
print("####  INICIO BUSCA HEURISTICA ####")
print("\n")
searchEngine2.buscaHeuristica()
print("####   FIM BUSCA HEURISTICA ####")

print("\n")
print("#"*30)
print(" "*4+"FINALIZANDO ALGORITMO")
print("#"*30)
