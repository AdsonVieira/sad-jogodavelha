
class Game:
    
    def __init__(self):
        self.board = []
        self.rows = 3
        self.columns = 3

    def init_game(self):
        run_game=1
        
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

        for _ in range(self.rows):
            rows_temp = []
            for _ in range(self.columns):
                rows_temp.append(0)
            self.board.append(rows_temp)
        
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
            print("\nJogador ", move%2 + 1)

            self.show_board()

            row = int(input("\nlinha: "))
            column = int (input("\ncoluna: "))

            if self.board[row-1][column-1] == 0:
                if(move%2+1) == 1:
                    self.board[row-1][column-1] = 1
                else:
                    self.board[row-1][column-1] = -1
            else:
                print("Jogada inválida")
                move -=1

            if self.checks_winner():
                print("Jogador ",move%2 + 1," venceu ")

            move += 1

    def checks_winner(self):
        #verificando as linhas
        for i in range(3):
            sum = self.board[i][0]+self.board[i][1]+self.board[i][2]
            if sum == 3 or sum == -3:
                return 1

        #checando  colunas
        for i in range(3):
            sum = self.board[0][i]+self.board[1][i]+self.board[2][i]

            if sum == 3 or sum == -3:
                return 1

        #checando as diagonais
        dglx = self.board[0][0]+self.board[1][1]+self.board[2][2]
        dgly = self.board[2][2]+self.board[1][1]+self.board[2][0]

        if dglx == 3 or dglx ==-3 or dgly ==3 or dgly ==-3:
            return 1
        
        return 0
    

game = Game()
game.init_game()




