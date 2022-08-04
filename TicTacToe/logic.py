
import random
# from choose_he import Ui_MainWindow1
# from choose_xo import Ui_MainWindow2
# from game import Ui_MainWindow3

class TicTacToe:
    def __init__(self,player,complexitygame,board):
        self.gameRunning = True
        self.toys = ["X","O"]
        self.player = player
        self.complexitygame = complexitygame
        self.board = board
        self.step = 1
        self.toys.remove(player)
        self.computer = self.toys[0]
        self.row_triples = [
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
    def printBoard(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("---------")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("---------")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    # check if there is a winner or not
    def checkIfWin(self):
        for triple in self.row_triples:
            x, y, z = triple
            if self.board[x] == self.board[y] and self.board[y] == self.board[z] and self.board[x] != '-':
                self.printBoard()
                print(f"The winner is {self.board[x]}!")
                self.gameRunning = False
                return self.board[x] 
        
        self.checkIfTie()

    # the game is broken to a draw
    def checkIfTie(self):
        if "-" not in self.board:
            self.printBoard()
            print("It is a tie!")
            self.gameRunning = False
            return "Tie"

    #
    def playerInput(self):
        is_valid = False
        while not is_valid:
            inp = int(input("Select a spot 1-9: "))
            if self.board[inp-1] == "-":
                self.board[inp - 1] = self.player
                is_valid = True
            else:
                print("Oops player is already at that spot. Try again.")

    #camputer plays easy  
    def computer_step_easy(self):
        have_played = False
        while not have_played:
            position = random.randint(0, 8)
            if self.board[position] == "-":
                self.board[position] = self.computer
                have_played = True

    
    #there is a chance for the computer to win
    def check_computer_win(self):
        for triple in self.row_triples:
            x, y, z = triple
            vals = sorted([self.board[x], self.board[y], self.board[z]])
            if vals[0] == '-' and vals[1] == vals[2] == self.computer:
                if self.board[y] == '-':
                    x = y
                if self.board[z] == '-':
                    x = z
                self.board[x] = self.computer
                return True
        return False

    
    #there is a chance for the player to win
    def check_player_win(self):
        for triple in self.row_triples:
            x, y, z = triple
            vals = sorted([self.board[x], self.board[y], self.board[z]])
            if vals[0] == '-' and vals[1] == vals[2] == self.player:
                if self.board[y] == '-':
                    x = y
                if self.board[z] == '-':
                    x = z
                self.board[x] = self.computer
                return True
        return False

    #computer plays hard with X
    def computer_step_hard_X(self):
        if self.check_computer_win():
            self.step+=1
            return True
        elif self.check_player_win():
            self.step+=1
            return True
        
        #step 1
        if self.step == 1:
            self.board[4] = "X"
            self.step+=1
            return True

        #step 2
        if self.step == 2:
            corners = [0, 2, 6, 8]
            for corner in corners:
                if self.board[corner] == 'O':
                    self.board[8 - corner] = 'X'
                    self.step += 1
                    return True

            if self.board[1] == "O" or self.board[7] == 'O':
                x = random.choice([3,5])
                self.board[x] = 'X'
                self.step+=1
                return True
            elif self.board[3] == "O" or self.board[5] == "O":
                x = random.choice([1,7])
                self.board[x] = "X"
                self.step+=1
                return True
            elif self.board[0] == "-" and self.board[8] == "-":
                self.board[0] = "X"
                self.step+=1
                return True
            elif self.board[2] == "-" and self.board[6] == "-":
                self.board[2] = "X"
                self.step+=1
                return True
        
        #step 3
        if self.step == 3:
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
                if self.board[x] == "X" and self.board[y] == "X" and self.board[z] == "-":
                    self.board[z] = "X"
                    self.step += 1
                    return True
                
                if self.board[x] == "X" and self.board[z] == "X" and self.board[y] == "-":
                    self.board[y] = "X"
                    self.step += 1
                    return True
                
        #step 4 
        if self.step == 4:
            for i in range(len(self.board)):
                if self.board[i] == "-":
                    self.board[i] = "X"
                    break
            self.step += 1
            return True
        
        
        #step 5
        if self.step == 5:
            for i in range(len(self.board)):
                if self.board[i] == "-":
                    self.board[i] = "X"
                    break
            return True

            
    #computer plays hard with O
    def computer_step_hard_O(self):
        if self.check_computer_win():
            self.step += 1
            return True
        elif self.check_player_win():
            self.step += 1
            return True

        #step 1
        if self.step == 1:
            if self.board[4] == "-":
                self.board[4] = "O"
                self.step += 1
                return True
            else:
                x = random.choice([0, 2, 6, 8])
                self.board[x] = 'O'
                self.step += 1
                return True

        #step 2
        if self.step == 2:
            corners = [0, 2, 6, 8]
            for corner in corners:
                if self.board[corner] == '-':
                    self.board[corner] = 'O'
                    self.step += 1
                    return True
            
        #step 3 or 4
        if self.step >= 3:
            for i in range(len(self.board)):
                if self.board[i] == "-":
                    self.board[i] = "O"
                    break
            self.step += 1
            return True

'''
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

player = "-"

while player not in ['X', 'O']:
    player = input("Would you like to be X or O?\n")
complexitygame = '-'
while complexitygame not in ['easy', 'hard']:
    complexitygame = input("What mode do you want to play, easy or hard?\n")
'''

# if Ui_MainWindow1.radioButton_easy.isChecked():
#     complexitygame = "easy"
# else:
#     complexitygame = "hard"

# if Ui_MainWindow2.radioButton_x.isChecked():
#     player = "X"
# else:
#     player = "O"



#tictactoe = TicTacToe(player,complexitygame,board)

'''

if tictactoe.player == 'X' and tictactoe.complexitygame == "easy":
    while tictactoe.gameRunning:
        tictactoe.printBoard()
        tictactoe.playerInput()
        tictactoe.checkIfWin()
        if tictactoe.gameRunning == False:
            break
        tictactoe.checkIfTie()
        if tictactoe.gameRunning == False:
            break
        tictactoe.computer_step_easy()
        tictactoe.checkIfWin()
        if tictactoe.gameRunning == False:
            break
        tictactoe.checkIfTie()
elif tictactoe.player == 'O' and tictactoe.complexitygame == "easy":
    while tictactoe.gameRunning:
        tictactoe.computer_step_easy()
        tictactoe.printBoard()
        tictactoe.checkIfWin()
        if tictactoe.gameRunning == False:
            break
        tictactoe.checkIfTie()
        if tictactoe.gameRunning == False:
            break
        tictactoe.playerInput()
        tictactoe.checkIfWin()
        if tictactoe.gameRunning == False:
            break
        tictactoe.checkIfTie()
elif tictactoe.player == 'X' and tictactoe.complexitygame == "hard":
    while tictactoe.gameRunning:
        tictactoe.printBoard()
        tictactoe.playerInput()
        tictactoe.checkIfWin()
        if tictactoe.gameRunning == False:
            break
        tictactoe.checkIfTie()
        if tictactoe.gameRunning == False:
            break
        tictactoe.computer_step_hard_O()
        tictactoe.checkIfWin()
        if tictactoe.gameRunning == False:
            break
        tictactoe.checkIfTie()
elif tictactoe.player == 'O' and tictactoe.complexitygame == "hard":
    while tictactoe.gameRunning:
        tictactoe.computer_step_hard_X()
        tictactoe.printBoard()
        tictactoe.checkIfWin()
        if tictactoe.gameRunning == False:
            break
        tictactoe.checkIfTie()
        if tictactoe.gameRunning == False:
            break
        tictactoe.playerInput()
        tictactoe.checkIfWin()
        if tictactoe.gameRunning == False:
            break
        tictactoe.checkIfTie()

'''

