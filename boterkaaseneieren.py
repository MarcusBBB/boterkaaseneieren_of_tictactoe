from random import randint
from copy import deepcopy

def start():
    print("hi, tictactoe wil start.")
    input("Do you want to play as Tic (t), Tac (t) or Toe (t)? ")
    beginner = randint(0,1) #1 or True is the player, 0 or False is the computer.
    print("Great, you will be Toc, you will play with {} and {} will begin, great choice!".format("X", ["the computer (thinking long and hard :D)", "you"][beginner]))
    return beginner
turn = start()
board = [[0 for i in range(3)] for j in range(3)]

def full_board(board): 
    for i in board:
        for j in i:
            if j == 0:
                return False
    return True
def winner(board):
    for i in range(3):
        if board[i][0] != 0 and board[i][0] == board[i][1] and board[i][0] == board[i][2]: # checking for a winner in the horizontal line
            return board[i][0]
        if board[0][i] != 0 and board[0][i] == board[1][i] and board[0][i] == board[2][i]: # checking for a winner in the vertical line
            return board[0][i]
    if board[0][0] != 0 and board[0][0] == board[1][1] and board[0][0] == board[2][2] \
        or board[0][2] != 0 and board[0][2] == board[1][1] and board[0][2] == board[2][0]: # checking for a winner in the diagonals
        return board[1][1]
    if (full_board(board)):
        return 0
def print_board(board):
    for i in range(3):
        for j in range(3):
            
            if board[i][j] == -1:
                print('O', end="  ")
            elif board[i][j] == 1:
                print('X', end="  ")  
            else:
                print(i*3+j + 1, end="  ")
            
        print("")
def validating_entry(board, choice):
    if not choice.isdigit():
        return False
    choice = int(choice) -1
    if choice > 8 or choice < 0:
        return False
    if board[choice//3][choice%3] != 0:
        return False
    return True
def computers_choice(board, turn, choice = []):
    if winner(board) != None:
        return winner(board), choice
    if not turn:
        result = []
        for i in range(9):
            if board[i//3][i%3] == 0:
                new_board = deepcopy(board)
                new_board[i//3][i%3] = -1
                result.append(computers_choice(new_board, not turn, choice + [i]))
        result = sorted(result, key=lambda i: i[0])
    if turn:
        result = []
        for i in range(9):
            new_board = deepcopy(board)
            if new_board[i//3][i%3] == 0:
                new_board[i//3][i%3] = 1
                result.append(computers_choice(new_board, not turn, choice + [i]))
        result = sorted(result, key=lambda i: i[0], reverse=True)
    return result[0]
def place_token(board, turn):
    if turn:
        token = 1
        print_board(board)
        choice = input("At which number will you place your token? ")
        valid = validating_entry(board, choice)
        while not valid:
            print("Invalid choice, please choose a number between 1 and 9 of the available numbers")
            print_board(board)
            choice = input("At which number will you place your token? ")
            valid = validating_entry(board, choice)
        choice = int(choice) -1
    else:
        token = -1
        a = computers_choice(board, turn)
        choice = a[1][0]
    board[choice//3][choice%3] = token

while winner(board) == None:
    place_token(board, turn)
    turn = not turn

won = winner(board)
print_board(board)
if won == -1:
    print('\nThe winner is: the computer!\n')
elif won == 0:
    print('\nIt\'s a draw!\n')
else:
    print('\nYou are the winner! Wait a minute, that\'s imbossible against this computer???!!?\n')