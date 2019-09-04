from Node import Node
from Utils import Utils

print("#"*30)
print(" "*7+"INICIANDO BUSCA")
print("#"*30)
print("\n")

goalMatrix = Utils.defineGoalMatrix()
scrambledMatrix = Utils.defineScrambledMatrix()

print("Matriz objetivo:")
Utils.showNodeMatrix(goalMatrix)
print("\n")
print("Matriz Inicial:")
Utils.showNodeMatrix(scrambledMatrix)


print("\n")
print("#"*30)
print(" "*4+"FINALIZANDO ALGORITMO")
print("#"*30)
