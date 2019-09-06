from Node import Node
from Matrix import Matrix
from SearchEngine import SearchEngine

print("")
print("#"*30)
print(" "*7+"INICIANDO BUSCA")
print("#"*30)
print("\n")

goalMatrix = Matrix('goal')
scrambledMatrix = Matrix('scrambled')
searchEngine = SearchEngine(scrambledMatrix, goalMatrix)

print("Matriz objetivo:")
goalMatrix.showNodeMatrix()
print("\n")

print("Matriz Inicial:")
scrambledMatrix.showNodeMatrix()
print("\n")
scrambledMatrix.showNodeMatrixDetailed()
print("\n")

print("Valores Calculados:")
searchEngine.calculateHeuristic()
searchEngine.getScrambledMatrix().showNodeMatrixDetailed()
print("\n")

print("\n")
print("#"*30)
print(" "*4+"FINALIZANDO ALGORITMO")
print("#"*30)
