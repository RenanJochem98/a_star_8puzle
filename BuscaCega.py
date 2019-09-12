from State import State
from SearchEngine import SearchEngine
class BuscaCega(SearchEngine):

    def __init__(self, scrambledMatrix, goalMatrix):
        SearchEngine.__init__(self, scrambledMatrix, goalMatrix)

    def buscaCega(self, state):
        finded = False
        if state == None:
            state =State(0, -1, self.scrambledMatrix)
            self.states[state.getId()] = state
            self.toVisitStates.append(state)
        count = 0
        for visitedState in self.toVisitStates:
            if count > 1000:
                break
            visitedState.getMatrix().showNodeMatrix()
            print("\n")
            if self.isGoalMatrix(visitedState.getMatrix()):
                finded = True
                break
            print("Visitando estado: " + str(visitedState.getId()) )
            self.visitState(visitedState)
            count+=1
        #     del self.toVisitStates[0]
        # if finded:
        #     print("Achou!!!!!")
        #     visitedState.getMatrix().showNodeMatrix()
        # else:
        #     print("Nao achou")

        print("\n")
        print("\n")
        for x in self.visitedStates:
            print(x)

    def visitState(self, state):
        currentMatrix = state.getMatrix()
        validDirections = self.getValidMoves(currentMatrix)
        for direction in validDirections:
            currentMatrix.moveTo(direction)
            newState = State(state.getId()+1, state.getId(), currentMatrix)
            if newState.getId() not in self.visitedStates:
                self.states[newState.getId()] = newState
                self.toVisitStates.append(newState)

        self.visitedStates.append(state.getId())
