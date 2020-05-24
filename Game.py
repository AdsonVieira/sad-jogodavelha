import numpy as np
import random



class Game:

    def __init__(self):
        self.board_one = np.zeros((3, 3), dtype=int)
        self.board_two = np.zeros((3, 3), dtype=int)
        self.block = np.zeros((3, 3), dtype=int)
        self.rows = 3
        self.columns = 3
        self.player_round = 0
        self.points = [0, 0]
        self.player_sugestion = 0

    def init_game(self):
        run_game = 1

        while run_game:
         

            self.init_board()
            self.run_match()
            # if run_game == 'y':
                
            # else:
            #     print('Fim de jogo...')
            #     run_game = 0

    def init_board(self):

        rows_columns = input("Informe o número de linhas ex: (4x6) ")
        rows_columns = rows_columns.split('x')

        self.rows = int(rows_columns[0])
        self.columns =  int(rows_columns[1])

        self.board_one = np.zeros((self.rows, self.columns), dtype=int)
        self.board_two = np.zeros((self.rows, self.columns), dtype=int)
        self.block     = np.zeros((self.rows, self.columns), dtype=int)

        block_one  = input("Informe o primeiro bloqueio ex: (1x1) ")
        block_one  = block_one.split('x')
        self.block[int(block_one[0])  -1 ][int(block_one[1]) -1 ] = 1 

        
        block_two  = input("Informe o segundo bloqueio  ex: (1x2) ")
        block_two  = block_two.split('x')
        self.block[int(block_two[0])  -1 ][int(block_two[1]) - 1] = 1 

        self.player_sugestion = int(input("Quem é você novo jogo - jogador 1 ou 2 (1, 2) ? "))

        return True

    def show_board(self):

        data_board_merge = self.board_merge()

        for i in range(self.rows):
            for j in range(self.columns):

                if self.block[i][j] == 1:
                    print(" B ", end=' ')
                elif data_board_merge[i][j] == 0:
                    print(" _ ", end=' ')
                elif data_board_merge[i][j] == 1:
                    print(" X ", end=' ')
                elif data_board_merge[i][j] == -1:
                    print(" O ", end=' ')
            print()

    

    def run_match(self):
        move = 0

        while self.checks_winner() == 0:
            print("\nJogador ", move % 2 + 1, "\n")

            self.show_board()

            self.player_round = move % 2 + 1

            if self.player_sugestion == (move % 2 + 1):
                print('Sugestão ', self.plays_suggestion())

            rows_columns = input("Informe a jogada ex: (4x6) ")
            rc = rows_columns.split('x')

            rc[0] = int(rc[0])
            rc[1] = int(rc[1])

        
            data_board_merge = self.board_merge()
        
            # checando se jogada pode ser feita
            if data_board_merge[rc[0] - 1][rc[1] - 1] == 0 and self.block[rc[0] - 1][rc[1] - 1] == 0:
                if (move % 2 + 1) == 1:
                    self.board_one[rc[0] - 1][rc[1] - 1] = 1
                else:
                    self.board_two[rc[0] - 1][rc[1] - 1] = -1
            else:
                print("Jogada inválida")
                move -= 1

            if self.checks_winner():
                print("Jogador ",move%2 + 1," venceu ")
                exit()

            if self.tie():
                print("O jogo empatou")
                exit()

            move += 1

    def checks_winner(self):

        board = []
        #print(self.player_round)#
        if self.player_round == 1:
            board = self.board_one
        elif self.player_round == 2:
            board = self.board_two

        if len(board) == 0:
            return 0

        winner = 0
        # verificando as linhas
        rows = board.sum(axis=1)
        if 3 in rows: 
            winner  += np.count_nonzero(rows == 3)
           # print("Ponto ", winner, "player", self.player_round)
            
    
        # verificando as colunas
        columns = board.sum(axis=0)
        if 3 in columns:
            winner  += np.count_nonzero(columns == 3)
            #print("Ponto ", winner, "player", self.player_round)
            
        # verificando as diagonais
        dlx = board.trace()
        if dlx == 3 or dlx == -3:
            winner  += np.count_nonzero(dlx == 3)
            #print("Ponto ", winner, "player", self.player_round)


        # print("matriz de pontos", winner)
        # verificando se existem mais de 2 pontos
        if winner >= 2:
            return 1

        return 0

    def tie(self):

        data_board_merge = self.board_merge()
        
        for i in range(self.rows):
            for j in range(self.columns):
                if self.block[i][j] == 1:
                    data_board_merge[i][j] = self.block[i][j]

        if 0 not in data_board_merge:
            return 1

        return 0
       
    
    def board_merge(self):

        board_merge = np.zeros((self.rows, self.columns), dtype=int)
        for i in range(self.rows):
            for j in range(self.columns):
                if self.board_two[i][j] != -1:
                    board_merge[i][j] = self.board_one[i][j]

        for i in range(self.rows):
            for j in range(self.columns):
                if self.board_one[i][j] != 1:
                    board_merge[i][j] = self.board_two[i][j]

        return board_merge

    def plays_suggestion(self):
      
        data_board_merge = self.board_merge()

        for i in range(self.rows):
            for j in range(self.columns):

                if data_board_merge[i][j] == 0 and self.block[i][j] != 1:
                    return [i+1, j+1]

        # board_temp.random.randint(0, high=3, size=2)

        # Verificar se o oponente pode marcar um ponto, se sim impedir a jogada
        # Caso não pesquisar em minha matriz onde eu posso marcar um ponto
        # Caso nenhuma das alternativas acima seja contemplada verificar se é possível fazer uma jogada nas extremidades do tabuleiro
        

    
game = Game()
game.init_game()
