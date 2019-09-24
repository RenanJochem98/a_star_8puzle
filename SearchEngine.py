import time
from operator import attrgetter
from datetime import datetime
from State import State
class SearchEngine(object):

    def __init__(self, scrambledMatrix, goalMatrix):
        self.scrambledMatrix = scrambledMatrix
        self.goalMatrix = goalMatrix
        self.goalState = None
        self.states = {}
        self.toVisitStates = []
        self.visitedStates = []
        self.caminho = []

    def getScrambledMatrix(self):
        return self.scrambledMatrix

    def setScrambledMatrix(self, newMatrix):
        self.scrabledmatrix = newMatrix

    def getGoalMatrix(self):
        return self.goalMatrix

    # procura por algum valor diferente
    def isGoalMatrix(self, compareMatrix):
        finded = True
        horiz = 0
        for scrLevel in compareMatrix.getValues():
            vert = 0
            for scrVal in scrLevel:
                value = self.goalMatrix.getValues()[horiz][vert]
                if scrVal != value:
                    finded = False
                    break
                vert += 1
            if not finded:
                break
            horiz += 1
        return finded

    def getValidMoves(self, state):
        emptyPosition = state.getEmptyPosition() #dict com posicao vertical e horizontal
        leftPosition = emptyPosition['Vert']-1
        rightPosition = emptyPosition['Vert']+1
        upPosition = emptyPosition['Horiz']-1
        downPosition = emptyPosition['Horiz']+1

        movePositions = {'left': leftPosition, 'right': rightPosition, 'up': upPosition, 'down': downPosition}

        validMoves = []
        for position in movePositions:
            if movePositions[position] >= 0 and movePositions[position] < state.getUpperLevel():
                validMoves.append(position)

        return validMoves

    def buscaResumida(self, state, needOrder = False):
        inicio = datetime.now()
        finded = False
        if state == None:
            currentState =State( -1, self.scrambledMatrix, 0)
            self.states[currentState.getId()] = currentState
            self.toVisitStates.append(currentState)
        count = 0
        while not finded:
            count += 1
            currentMatrix = currentState.getMatrix()
            if self.isGoalMatrix(currentMatrix):
                self.goalState = currentState
                finded = True
                break
            else:
                del self.toVisitStates[0]
                self.visitNode(currentState, currentMatrix) #deve ser implementa em classe filha
                self.toVisitStates.sort(key=attrgetter("coust"))
                currentState = self.toVisitStates[0] # novo posicao 0 era posicao 1 antes da delecao

        fim = datetime.now()
        if finded:
            self.showFindedResult(inicio,fim)
        else:
            print("Não achou")

        print("Acabou")

    def showFindedResult(self, inicio,fim):
        print("Achou")
        print("Numero de estados visitados: ", end="")
        print(len(self.visitedStates))
        print("Total de estados: ", end="")
        print(len(self.states))
        print("Estados a visitar: ", end="")
        print(len(self.toVisitStates))
        print("Inicio:", end="")
        print(inicio)
        print("Fim:", end="")
        print(fim)
        print("Tempo de Execução:", end="")
        print(fim - inicio)
        print("Id estado Final: ", end="")
        print(self.goalState.getId())
        print("Nivel estado Final: ", end="")
        print(self.goalState.getLevel())
        print("Custo do estado final: ", end="")
        print(self.goalState.getCoust())
        print("Custo do estado inicial: ", end="")
        print(self.states[self.visitedStates[0]].getCoust())
        # print("Estado Final: ")
        # self.goalState.getMatrix().showNodeMatrix()

        self.caminho.append(self.goalState.getId())
        findedId = self.goalState.getParentId()
        while findedId != -1:
            self.caminho.append(findedId)
            findedId = self.states[findedId].getParentId()
        reverse_way = self.caminho[::-1] #sei la, funciona. Nao me pergunte como
        print("Caminho : ", end="")
        print(len(self.caminho))
        print("Caminho (Da posicao vazia): ", end="")
        count = 0
        for id in reverse_way:
            endLine = " -> "
            if count%5 == 0:
                endLine = "\n"
            print(self.states[id].getDirection(), end=endLine)
            count+=1
