class Input(object):

    def pedeMatrizInicial(self):
        mat = ""

        while len(mat) != 9:
            print("Digite o Jogo como deseja resolver:(No formato: 0,2,1,5,6...[separados por virgula e sem espaços em branco])(Zero representa a posicao vazia)")
            mat = input()
            mat.strip() #para retirar espacoes em brando na volta
            mat = mat.split(",")
            if len(mat) > 9:
                print("Você digitou numeros a mais!!")
            elif len(mat) < 9:
                print("Você digitou números a menos!!!")

        matrix = []
        temp = []
        for i in mat:
            temp.append(int(i))
            if len(temp) == 3:
                matrix.append(temp)
                temp = []
        return matrix

    def showSearchOption(self):
        opt = 0
        try:
            print("Escolha o algoritimo de busca:")
            print("1 - Busca Cega:")
            print("2 - Busca Heuristica(Numero de passos até a posicao correta)(Busca Boa):")
            print("3 - Busca Heuristica(Valores fora de posição)(Não tão boa):")
            print("4 - Trocar tabuleiro")
            print("0 - Finalizar")
            opt = int(input())
        except ValueError:
            print("Você digitou um valor que não é um número!!!")
        print("\n")
        return opt
