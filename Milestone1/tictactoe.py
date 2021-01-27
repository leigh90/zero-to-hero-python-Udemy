
def display_board(board):
    print(board[7]+ '|' + board[8]+ '|' + board[9])
    print(board[4]+ '|' + board[5]+ '|' + board[6])
    print(board[1]+ '|' + board[2]+ '|' + board[3])

test_board = ['#','X','0','X','0','X','0','X','0','X']
display_board(test_board)

def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    marker = ''
    while marker != 'X' and marker != '0':
        marker = input('Player1: Choose x  or O:').upper()

    if marker == 'x':
        return ('X', 'O')
    else:
        return('O','X')

        
    

