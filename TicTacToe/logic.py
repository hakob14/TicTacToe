
import random

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

winner = None
gameRunning = True
toys = ["X","O"]
player = '-'
while player not in ['X', 'O']:
    player = input("Would you like to be X or O?\n")
complexitygame = '-'
while complexitygame not in ['easy', 'hard']:
    complexitygame = input("What mode do you want to play, easy or hard?\n")

toys.remove(player)
computer = toys[0]
row_triples = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]

# game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def checkIfWin(board):
    global gameRunning
    for triple in row_triples:
        x, y, z = triple
        if board[x] == board[y] and board[y] == board[z] and board[x] != '-':
            printBoard(board)
            print(f"The winner is {board[x]}!")
            gameRunning = False
            break


def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False


def playerInput(board):
    is_valid = False
    while not is_valid:
        inp = int(input("Select a spot 1-9: "))
        if board[inp-1] == "-":
            board[inp - 1] = player
            is_valid = True
        else:
            print("Oops player is already at that spot. Try again.")


def computer_step_easy(board):
    have_played = False
    while not have_played:
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = computer
            have_played = True

   

def check_computer_win():
    for triple in row_triples:
        x, y, z = triple
        vals = sorted([board[x], board[y], board[z]])
        if vals[0] == '-' and vals[1] == vals[2] == computer:
            if board[y] == '-':
                x = y
            if board[z] == '-':
                x = z
            board[x] = computer
            return True
    return False

 

def check_player_win():
    for triple in row_triples:
        x, y, z = triple
        vals = sorted([board[x], board[y], board[z]])
        if vals[0] == '-' and vals[1] == vals[2] == player:
            if board[y] == '-':
                x = y
            if board[z] == '-':
                x = z
            board[x] = computer
            return True
    return False


step = 1
def computer_step_hard_X(board):
    global step
    if check_computer_win():
        step+=1
        return True
    elif check_player_win():
        step+=1
        return True
    
    #step 1
    if step == 1:
        board[4] = "X"
        step+=1
        return True

    #step 2
    if step == 2:
        corners = [0, 2, 6, 8]
        for corner in corners:
            if board[corner] == 'O':
                board[8 - corner] = 'X'
                step += 1
                return True

        if board[1] == "O" or board[7] == 'O':
            x = random.choice([3,5])
            board[x] = 'X'
            step+=1
            return True
        elif board[3] == "O" or board[5] == "O":
            x = random.choice([1,7])
            board[x] = "X"
            step+=1
            return True
        elif board[0] == "-" and board[8] == "-":
            board[0] = "X"
            step+=1
            return True
        elif board[2] == "-" and board[6] == "-":
            board[2] = "X"
            step+=1
            return True
    
    #step 3
    if step == 3:
        combinatios = [
            (4, 3, 0),
            (4, 3, 6),
            (4, 1, 0),
            (4, 1, 2),
            (4, 5, 2),
            (4, 5, 8),
            (4, 7, 8),
            (4, 7, 6)
        ]
        for (x, y, z) in combinatios:
            if board[x] == "X" and board[y] == "X" and board[z] == "-":
                board[z] = "X"
                step += 1
                return True
            
    #step 4 
    if step == 4:
        for i in range(len(board)):
            if board[i] == "-":
                board[i] = "X"
                break
        step += 1
        return True
    
    
    #step 5
    if step == 5:
        for i in range(len(board)):
            if board[i] == "-":
                board[i] = "X"
                break
        return True

        

step = 1
def computer_step_hard_O(board):
    global step
    if check_computer_win():
        step += 1
        return True
    elif check_player_win():
        step += 1
        return True

    #step 1
    if step == 1:
        if board[4] == "-":
            board[4] = "O"
            step += 1
            return True
        else:
            x = random.choice([0, 2, 6, 8])
            board[x] = 'O'
            step += 1
            return True

    #step 2
    if step == 2:
        corners = [0, 2, 6, 8]
        for corner in corners:
            if board[corner] == '-':
                board[corner] = 'O'
                step += 1
                return True
        
    #step 3 or 4
    if step >= 3:
        for i in range(len(board)):
            if board[i] == "-":
                board[i] = "O"
                break
        step += 1
        return True



if player == 'X' and complexitygame == "easy":
    while gameRunning:
        printBoard(board)
        playerInput(board)
        checkIfWin(board)
        if gameRunning == False:
            break
        checkIfTie(board)
        if gameRunning == False:
            break
        computer_step_easy(board)
        checkIfWin(board)
        if gameRunning == False:
            break
        checkIfTie(board)
elif player == 'O' and complexitygame == "easy":
    while gameRunning:
        computer_step_easy(board)
        printBoard(board)
        checkIfWin(board)
        if gameRunning == False:
            break
        checkIfTie(board)
        if gameRunning == False:
            break
        playerInput(board)
        checkIfWin(board)
        if gameRunning == False:
            break
        checkIfTie(board)
elif player == 'X' and complexitygame == "hard":
    while gameRunning:
        printBoard(board)
        playerInput(board)
        checkIfWin(board)
        if gameRunning == False:
            break
        checkIfTie(board)
        if gameRunning == False:
            break
        computer_step_hard_O(board)
        checkIfWin(board)
        if gameRunning == False:
            break
        checkIfTie(board)
elif player == 'O' and complexitygame == "hard":
    while gameRunning:
        computer_step_hard_X(board)
        printBoard(board)
        checkIfWin(board)
        if gameRunning == False:
            break
        checkIfTie(board)
        if gameRunning == False:
            break
        playerInput(board)
        checkIfWin(board)
        if gameRunning == False:
            break
        checkIfTie(board)