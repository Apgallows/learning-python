#this is tic tac toe.


board_dict = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

win_X = False

def win_state_X():
    '''
    checks for win X
    '''
    global win_X
    if board_dict[1] == 'X' and board_dict[2] == 'X' and board_dict[3] == 'X':
        win_X = True
    elif board_dict[4] == 'X' and board_dict[5] == 'X' and board_dict[6] == 'X':
        win_X = True
    elif board_dict[7] == 'X' and board_dict[8] == 'X' and board_dict[9] == 'X':
        win_X = True
    elif board_dict[1] == 'X' and board_dict[4] == 'X' and board_dict[7] == 'X':
        win_X = True
    elif board_dict[2] == 'X' and board_dict[5] == 'X' and board_dict[8] == 'X':
        win_X = True
    elif board_dict[3] == 'X' and board_dict[6] == 'X' and board_dict[9] == 'X':
        win_X = True
    elif board_dict[1] == 'X' and board_dict[5] == 'X' and board_dict[9] == 'X':
        win_X = True
    elif board_dict[3] == 'X' and board_dict[5] == 'X' and board_dict[7] == 'X':
        win_X = True
    else:
        pass

win_O = False

def win_state_O():
    '''
    checks for win O
    '''
    global win_O
    if board_dict[1]  == 'O' and board_dict[2]  == 'O' and board_dict[3] == 'O':
        win_O = True
    elif board_dict[4]  == 'O' and board_dict[5]  == 'O' and board_dict[6] == 'O':
        win_O = True
    elif board_dict[7]  == 'O' and board_dict[8]  == 'O' and board_dict[9] == 'O':
        win_O = True
    elif board_dict[1]  == 'O' and board_dict[4]  == 'O' and board_dict[7] == 'O':
        win_O = True
    elif board_dict[2]  == 'O' and board_dict[5]  == 'O' and board_dict[8] == 'O':
        win_O = True
    elif board_dict[3]  == 'O' and board_dict[6]  == 'O' and board_dict[9] == 'O':
        win_O = True
    elif board_dict[1]  == 'O' and board_dict[5]  == 'O' and board_dict[9] == 'O':
        win_O = True
    elif board_dict[3]  == 'O' and board_dict[5]  == 'O' and board_dict[7] == 'O':
        win_O = True
    else:
        pass


'''
1x2x3x4 5 6 7 8 9
1 2 3 4x5x6x7 8 9
1 2 3 4 5 6 7x8x9x
1x2 3 4x5 6 7x8 9 
1 2x3 4 5x6 7 8x9
1 2 3x4 5 6x7 8 9x
1x2 3 4 5x6 7 8 9x
1 2 3x4 5x6 7x8 9
'''

def print_board():
    '''
    prints tic tac toe board\n
        takes no args
    '''
    print (f' {board_dict[1]}|{board_dict[2]}|{board_dict[3]}\n-------')
    print (f' {board_dict[4]}|{board_dict[5]}|{board_dict[6]}\n-------')
    print (f' {board_dict[7]}|{board_dict[8]}|{board_dict[9]}')



def X_input():
    '''
    asks for player X input (1-9)\n
        takes no args
    '''
    player_X = int(input('please enter a number 1-9:'))
    if player_X in board_dict and board_dict[player_X] == ' ':
        board_dict[player_X] = 'X'
    else:
        print('nope')



def O_input():
    '''
    asks for player O input (1-9)\n
        takes no args
    '''
    player_O = int(input('please enter a number 1-9:'))
    if player_O in board_dict and board_dict[player_O] == ' ':
        board_dict[player_O] = 'O'
    else:
        print('nope')


'''
need to:
check board state
iterate until win state or draw state
'''


def tic_tac_toe():
    while ' ' in board_dict.values():
        global win_X
        global win_O
        X_input()
        print_board()
        win_state_X()
        if win_X == True:
            print('win X')
            break
        if ' ' not in board_dict.values():
            continue
        O_input()
        print_board()
        win_state_O()
        if win_O == True:
            print('win O')
            break
    else:
        print('DRAW')

tic_tac_toe()

