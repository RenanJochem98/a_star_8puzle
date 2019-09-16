from Node import Node
from Matrix import Matrix
# from SearchEngine import SearchEngine
from BuscaCega import BuscaCega

print("")
print("#"*30)
print(" "*7+"INICIANDO BUSCA")
print("#"*30)
print("\n")

goalMatrix = Matrix('goal')
scrambledMatrix = Matrix('scrambled')
searchEngine = BuscaCega(scrambledMatrix, goalMatrix)


print("Matriz objetivo:")
# goalMatrix.showNodeMatrix()
# print("\n")

print("Matriz Inicial:")
scrambledMatrix.showNodeMatrix()
print("\n")
# scrambledMatrix.showNodeMatrixDetailed()
# print("\n")

print("Valores Calculados:")
# print(searchEngine.isGoalMatrix(scrambledMatrix))
# searchEngine.calculateHeuristic()
# searchEngine.getScrambledMatrix().showNodeMatrixDetailed()
# print("\n")
# horiz = int(input("Posicao Horizontal: "))
# vert = int(input("Posicao Vertical: "))
# scrambledMatrix.move(horiz, vert)
# scrambledMatrix.showNodeMatrix()
# print("\n")
searchEngine.buscaCega(None)

print("\n")
print("#"*30)
print(" "*4+"FINALIZANDO ALGORITMO")
print("#"*30)
