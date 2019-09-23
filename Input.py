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
