import time
from datetime import datetime
import copy
from Matrix import Matrix
from State import State
from SearchEngine import SearchEngine
class BuscaCega(SearchEngine):

    def __init__(self, scrambledMatrix, goalMatrix):
        SearchEngine.__init__(self, scrambledMatrix, goalMatrix)
        self.stateId = 0
        self.goalState = None
        self.caminho = []

    def buscaCega(self, state):
        inicio = datetime.now()
        print("Inicio:", end="")
        print(inicio)
        finded = False
        if state == None:
            state =State( -1, self.scrambledMatrix)
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
            if count > 10:
                break
            if self.isGoalMatrix(currentMatrix):
                self.goalState = currentState
                print("Estado "+str(currentState.getId())+ " é final!")
                finded = True
                break
            else:
                # print("Estado "+str(currentState.getId())+ " não é final!")
                validMoves = self.getValidMoves(currentMatrix)
                for move in validMoves:
                    self.stateId += 1
                    tempMatrix = copy.deepcopy(currentMatrix)
                    tempMatrix.moveTo(move)
                    newState = State( currentState.getId(), tempMatrix)
                    if newState.getId() not in self.visitedStates:
                        self.states[newState.getId()] = newState
                        self.toVisitStates.append(newState)
                self.visitedStates.append(newState.getId())
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
            print("Estado Final: ")
            self.goalState.getMatrix().showNodeMatrix()
        else:
            print("Não achou")
        print("States: ")
        print(len(self.states))
        # for s in self.states:
        #     print(str(self.states[s].getId()), end=" -> ")
        print("\n")
        print("Visited States: ")
        print(len(self.visitedStates))
        # for s in self.states:
        #     print(str(s), end=" -> ")
        print("\n")
        print("To Visit States: ")
        print(len(self.toVisitStates))

        print("\n")
        fim = datetime.now()
        print(fim - inicio)
        print("Acabou")
