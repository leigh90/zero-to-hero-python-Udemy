# display the board

def display_board(board):
    print(board[7]+ '|' + board[8]+ '|' + board[9])
    print(board[4]+ '|' + board[5]+ '|' + board[6])
    print(board[1]+ '|' + board[2]+ '|' + board[3])

test_board = ['#','X','0','X','0','X','0','X','0','X']
display_board(test_board)
# assign each player a symbol
def choose_symbol():
    player_1_symbol = input('Choose a symbol either X or O:' ).upper()
    if player_1_symbol == 'X':
        player_2_symbol = 'O'
        print('Player 1 is X Player 2 is O')

    else:
        player_2_symbol ='X'
        print('Player 1 is  O Player 2 is X')

choose_symbol()

# player chooses a position to place their symbole
def play_game():
    play_position = int(input('Choose a number between 1 and 9'))

    # player one turn
    'X'.append(board[play_position])
    # player two turn
    

play_game()
# check for winner by checking if any row or columns are similar
# return the winner
# return a tie