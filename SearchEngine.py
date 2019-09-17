import time
from itertools import filterfalse
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
        self.stateId = 0
        self.currentLevel = 0

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

    def busca(self, state, needOrder = False):
        inicio = datetime.now()
        currentLevelControl = 1 #comeca com 1 para nao contar o primeiro nivel
        previousState = None
        print("Inicio:", end="")
        print(inicio)
        finded = False
        if state == None:
            state =State( -1, self.scrambledMatrix, 0)
            self.states[state.getId()] = state
            self.toVisitStates.append(state.getId())
        count = 0
        currentStateId = state.getId()
        while not finded:
            currentState = self.states[currentStateId]

            print("Loop: ", end="")
            print(count)
            print("Visitando estado: ", end="")
            print(currentState.getId())
            print("Estado Pai: ", end="")
            print(currentState.getParentId())
            print("Nivel atual: ", end="")
            print(currentState.getLevel())
            currentMatrix = currentState.getMatrix()
            # if count > 4:
            #     break
            if self.isGoalMatrix(currentMatrix):
                self.goalState = currentState
                print("Estado "+str(currentState.getId())+ " é final!")
                finded = True
                break
            else:
                self.visitNode(currentState, currentMatrix)
                del self.toVisitStates[0]
                currentStateId = self.toVisitStates[0] # novo posicao 0 era posicao 1 antes da delecao
                if self.currentLevel != currentLevelControl: #current level pode ser alterado no visitNode()
                    self.addCoustInVisitedStates()
                if needOrder:
                    self.toVisitStates.sort(key=lambda x: self.states[x].getOrdered())
                    for i in self.visitedStates:
                        self.states[i].setH(0)

            currentLevelControl = self.currentLevel
            currentMatrix.showNodeMatrix()
            count += 1
            tempoExec = datetime.now()
            print("Tempo de Execução: ", end="")
            print(tempoExec - inicio)
            print("\n")
        print("\n")
        print("Fim da Busca")
        print("\n")
        if finded:
            self.showFindedResult(inicio, datetime.now())
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

    def buscaResumida(self, state, needOrder = False):
        inicio = datetime.now()
        currentLevelControl = 1 #comeca com 1 para nao contar o primeiro nivel
        previousState = None
        finded = False
        if state == None:
            state =State( -1, self.scrambledMatrix, 0)
            self.states[state.getId()] = state
            self.toVisitStates.append(state.getId())
        count = 0
        currentStateId = state.getId()
        while not finded:
            currentState = self.states[currentStateId];
            count += 1
            currentMatrix = currentState.getMatrix()
            # if count > 2:
            #     break
            if self.isGoalMatrix(currentMatrix):
                self.goalState = currentState
                finded = True
                break
            else:
                self.visitNode(currentState, currentMatrix) #deve ser implementa em classe filha
                currentState.setVisited(True)
                del self.toVisitStates[0]
                currentStateId = self.toVisitStates[0] # novo posicao 0 era posicao 1 antes da delecao
                if self.currentLevel != currentLevelControl: #current level pode ser alterado no visitNode()
                    self.addCoustInVisitedStates()
                if needOrder:
                    self.toVisitStates.sort(key=lambda x: self.states[x].getOrdered())
                    for i in self.visitedStates:
                        if self.states[i].getVisited():
                            self.states[i].setH(0)
            currentLevelControl = self.currentLevel

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
        # print("Estados a visitar: ", end="")
        # print(len(self.toVisitStates))
        # print("Inicio:", end="")
        # print(inicio)
        # print("Fim:", end="")
        # print(fim)
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
        print("Caminho (Da posicao vazia): ", end="")
        for id in reverse_way:
            print(self.states[id].getDirection(), end=" -> ")

    def addCoustInVisitedStates(self):
        for state in self.visitedStates:
            self.states[state].addCoust()
