board = [[0,0,0], [0,0,0], [0,0,0]]

def menu():
    run_game=1
    
    while run_game:
        run_game = input("Jogar novamente? (y, n) ")

        if run_game == 'y':
            game()
        else:
            print('Fim de jogo...')
            run_game = 0



def game():
    move = 0
    
    while checks_winner() == 0:
        print("\nJogador ", move%2 + 1)

        show_board()

        row = int(input("\nlinha: "))
        column = int (input("\ncoluna: "))

        if board[row-1][column-1] == 0:
            if(move%2+1) == 1:
                board[row-1][column-1] = 1
            else:
                board[row-1][column-1] = -1
        else:
            print("Jogada inválida")
            move -=1


        if checks_winner():
            print("Jogador ",move%2 + 1," venceu ")

        move += 1

def checks_winner():
    
    #verificando as linhas
    for i in range(3):
        sum = board[i][0]+board[i][1]+board[i][2]

        if sum == 3 or sum == -3:
            return 1

    #checando  colunas
    for i in range(3):
        sum = board[0][i]+board[1][i]+board[2][i]

        if sum == 3 or sum == -3:
            return 1

    #checando as diagonais
    dglx = board[0][0]+board[1][1]+board[2][2]
    dgly = board[2][2]+board[1][1]+board[2][0]

    if dglx == 3 or dglx ==-3 or dgly ==3 or dgly ==-3:
        return 1
    
    return 0


def show_board():

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                print(" _ ", end=' ')
            elif board[i][j] == 1:
                print(" X ", end=' ')
            elif board[i][j] == -1:
                print(" O ", end=' ')
        print()

menu()