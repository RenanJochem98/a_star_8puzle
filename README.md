# a_star_8puzzle
Algoritmo para resolver o jogo 8 puzzle.

A Heuristica usada é o **número de passos** até a posição correta.
É necesário Python 3

Comando inicial:
> python main.py
Comando inicial no Linux:
> python3 main.py

Explicação do Algoritmo:

Classe Board:
Responsável pela organização do tabuleiro. Guarda a matriz com os valores em  cada posição e é responsável por realizar os movimentos.

Classe BoardDisplay:
Responsável pela exibição da matriz na linha de comando.

Classe State:
Para o problema apresentado, o estado e nodo são representados da mesma maneira. A classe State é responsável pela abstração de um possível estado do tabuleiro,
guardando a os valores em cada posição do tabuleiro, a classe pai, o movimento que levou a aquele estado, seu nível e sua Heuristica, caso seja necessário
ppara calculo da posição

Classe SearchEngine:
Classe abstrata, responsável pela generalização dos algoritimos de busca. Verificamos no trabalho que a principal diferença entre a busca cega e busca com heuristica
é forma como fica organizado a fronteira. Então, abstraímos a parte de comparação e vericação de estados para essa classe, e deixamos a criação de filhos e organização
de fronteira para os filhos.

Classe BuscaCega:
Responsavel pela criação dos nodos e organização da fronteira como busca cega. É implementada uma busca cega horizontal.
