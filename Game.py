import numpy as np


class Game:

    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.rows = 3
        self.columns = 3
        self.points = []

    def init_game(self):
        run_game = 1

        while run_game:
            run_game = input("Jogar novamente? (y, n) ")

            if run_game == 'y':
                self.init_board()
                self.run_match()
            else:
                print('Fim de jogo...')
                run_game = 0

    def init_board(self):

        self.rows = int(input("Informe o número de linhas: "))
        self.columns = int(input("Informe o número de colunas: "))

        self.board = np.zeros((self.rows, self.columns), dtype=int)

        return self.board

    def show_board(self):

        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] == 0:
                    print(" _ ", end=' ')
                elif self.board[i][j] == 1:
                    print(" X ", end=' ')
                elif self.board[i][j] == -1:
                    print(" O ", end=' ')
            print()

    def run_match(self):
        move = 0

        while self.checks_winner() == 0:
            print("\nJogador ", move % 2 + 1)

            self.show_board()
            # print("melhor jogaga ", [
            #     np.amax(self.board, axis=1),
            #     np.amax(self.board, axis=0),
            #     np.amax(self.board)
            # ])
            row = int(input("\nlinha: "))
            column = int(input("\ncoluna: "))

            if self.board[row - 1][column - 1] == 0:
                if (move % 2 + 1) == 1:
                    self.board[row - 1][column - 1] = 1
                else:
                    self.board[row - 1][column - 1] = -1
            else:
                print("Jogada inválida")
                move -= 1

            if self.checks_winner():
                print("Jogador ", move % 2 + 1, " venceu ")

            move += 1

    def checks_winner(self):
        # verificando as linhas
        rows = self.board.sum(axis=1)
        if 3 in rows:
            return 1

        # verificando as colunas
        columns = self.board.sum(axis=0)
        if 3 in columns:
            return 1

        if self.board.trace() == 3 or self.board.trace() == -3:
            return 1
        return 0


game = Game()
game.init_game()
