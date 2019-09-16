import time
from datetime import datetime
from State import State
class SearchEngine(object):

    def __init__(self, scrambledMatrix, goalMatrix):
        self.scrambledMatrix = scrambledMatrix
        self.goalMatrix = goalMatrix
        self.states = {}
        self.toVisitStates = []
        self.visitedStates = []
        self.stateId = 0
        self.goalState = None
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
            for scrNode in scrLevel:
                value = self.goalMatrix.getValues()[horiz][vert].getValue()
                if scrNode.getValue() != value:
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

    def busca(self, state):
        inicio = datetime.now()
        print("Inicio:", end="")
        print(inicio)
        finded = False
        if state == None:
            state =State( -1, self.scrambledMatrix, 0)
            self.states[state.getId()] = state
            self.toVisitStates.append(state)
        count = 0
        for currentState in self.toVisitStates:
            count += 1
            print("Loop: ", end="")
            print(count)
            print("Visitando estado: ", end="")
            print(currentState.getId())
            print("Estado Pai: ", end="")
            print(currentState.getParentId())
            currentMatrix = currentState.getMatrix()
            # if count > 10:
            #     break
            if self.isGoalMatrix(currentMatrix):
                self.goalState = currentState
                print("Estado "+str(currentState.getId())+ " é final!")
                finded = True
                break
            else:
                # print("Estado "+str(currentState.getId())+ " não é final!")
                self.visitNode(currentState, currentMatrix)
            tempoExec = datetime.now()
            print("Tempo de Execução: ", end="")
            print(tempoExec - inicio)
            currentMatrix.showNodeMatrix()
            print("\n")
        print("\n")
        print("Fim da Busca")
        print("\n")
        if finded:
            print("Achou")
            print("Numero de estados totais: ", end="")
            print("Id estado Final: ", end="")
            print(self.goalState.getId())
            print("Nivel estado Final: ", end="")
            print(self.goalState.getLevel())
            print("Estado Final: ")
            self.goalState.getMatrix().showNodeMatrix()
        else:
            print("Não achou")
        print("States: ")
        print(len(self.states))
        print("\n")
        print("Visited States: ")
        print(len(self.visitedStates))
        print("\n")
        print("To Visit States: ")
        print(len(self.toVisitStates))

        print("\n")
        fim = datetime.now()
        print(fim - inicio)
        print("Acabou")

    def buscaResumida(self, state):
        finded = False
        if state == None:
            state =State( -1, self.scrambledMatrix, 0)
            self.states[state.getId()] = state
            self.toVisitStates.append(state)
        count = 0
        for currentState in self.toVisitStates:
            count += 1
            currentMatrix = currentState.getMatrix()
            # if count > 10:
            #     break
            if self.isGoalMatrix(currentMatrix):
                self.goalState = currentState
                finded = True
                break
            else:
                self.visitNode(currentState, currentMatrix) #deve ser implementa em classe filha

        if finded:
            self.showFindedResult()
        else:
            print("Não achou")

        print("Acabou")

    def showFindedResult(self):
        print("Achou")
        print("Numero de estados visitados: ", end="")
        print(len(self.visitedStates))
        print("Total de estados: ", end="")
        print(len(self.states))
        print("Estados a visitar: ", end="")
        print(len(self.toVisitStates))
        print("Id estado Final: ", end="")
        print(self.goalState.getId())
        print("Nivel estado Final: ", end="")
        print(self.goalState.getLevel())
        # print("Estado Final: ")
        # self.goalState.getMatrix().showNodeMatrix()

        findedId = self.goalState.getParentId()
        while findedId != -1:
            self.caminho.append(findedId)
            findedId = self.states[findedId].getParentId()
        reverse_way = self.caminho[::-1] #sei la, funciona. Nao me pergunte como
        for id in reverse_way:
            print(self.states[id].getDirection())
