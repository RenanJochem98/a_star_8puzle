from Node import Node
from Utils import Utils
from SearchEngine import SearchEngine

print("")
print("#"*30)
print(" "*7+"INICIANDO BUSCA")
print("#"*30)
print("\n")

utils = Utils()
goalMatrix = utils.defineGoalMatrix()
scrambledMatrix = utils.defineScrambledMatrix()
searchEngine = SearchEngine(scrambledMatrix, goalMatrix)
#
print("Matriz objetivo:")
utils.showNodeMatrix(goalMatrix)
print("\n")
# utils.showNodeMatrixDetailed(goalMatrix)
# print("\n")

print("Matriz Inicial:")
utils.showNodeMatrix(scrambledMatrix)
print("\n")
utils.showNodeMatrixDetailed(scrambledMatrix)
print("\n")

print("Valores Calculados:")
searchEngine.calculateHeuristic()
utils.showNodeMatrixDetailed(searchEngine.getScrambledMatrix())
print("\n")

print("\n")
print("#"*30)
print(" "*4+"FINALIZANDO ALGORITMO")
print("#"*30)
