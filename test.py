import numpy as np 


boardx = np.array([
    [1, 1, 1], 
    [0, 1, 0], 
    [1, 0, 1]
])

# print(board)

# print("Soma das linhas", board.sum(axis=1))
# print("Soma das colunas", board.sum(axis=0))
# print("Soma das diagonais", board.trace())


rows = int(input("Informe o número de linhas: "))
columns = int(input("Informe o número de colunas: "))

board = np.zeros((rows,columns), dtype=int)

print(board)
# print(boardx)