# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
import random
import time



class Ui_MainWindow_game(object):
    def __init__(self,complexity,player) -> None:
        self.player = player
        self.complexity = complexity
        if self.player == "X":
            self.computer = "O"
        else:
            self.computer = "X"
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
        self.step = 1
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        MainWindow.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(50, 50, 100, 100))
        self.pushButton_1.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_1.setText("")
        self.pushButton_1.setObjectName("pushButton")
        self.pushButton_1.setFont(font)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 50, 100, 100))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_2")
        self.pushButton_3.setFont(font)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 50, 100, 100))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_3")
        self.pushButton_2.setFont(font)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 150, 100, 100))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setFont(font)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 150, 100, 100))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 150, 100, 100))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setFont(font)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 250, 100, 100))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setFont(font)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 250, 100, 100))
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setFont(font)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(250, 250, 100, 100))
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setFont(font)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 400, 300, 40))
        self.label.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.label.setObjectName("label") 
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)  
        self.label.setFont(font)    
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(50, 500, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_10.setObjectName("pushButton_10")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.buttonList=[self.pushButton_1,self.pushButton_2, self.pushButton_3, self.pushButton_4,
                        self.pushButton_5,self.pushButton_6, self.pushButton_7, self.pushButton_8, 
                        self.pushButton_9]
        if self.player == "O":
            self.buttonList[4].setText(self.computer)
            self.step += 1
        
        
        self.pushButton_1.clicked.connect(lambda: self.clicker(0))
        self.pushButton_2.clicked.connect(lambda: self.clicker(1))
        self.pushButton_3.clicked.connect(lambda: self.clicker(2))
        self.pushButton_4.clicked.connect(lambda: self.clicker(3))
        self.pushButton_5.clicked.connect(lambda: self.clicker(4))
        self.pushButton_6.clicked.connect(lambda: self.clicker(5))
        self.pushButton_7.clicked.connect(lambda: self.clicker(6))
        self.pushButton_8.clicked.connect(lambda: self.clicker(7))
        self.pushButton_9.clicked.connect(lambda: self.clicker(8))
        self.pushButton_10.clicked.connect(self.clicker_play_again)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TicTacToe"))
        #self.pushButton_5.setText(_translate("MainWindow", "X"))
        self.pushButton_10.setText(_translate("MainWindow", "Play again"))
    
    # def computer_step(self):
    #     if self.player == "X":
    #         self.computer = "O"
    #     else:
    #         self.computer =  "X"
        
    def myvar(self):
        print(self.player,self.computer,self.complexity,self.row_triples,self.step)
    
    def clicker_play_again(self):
        for i in self.buttonList:
            i.setText("")
        self.label.setText("")
        self.step = 1
        if self.player == "O":
            self.buttonList[4].setText(self.computer)
            self.step += 1
    
    def clicker(self, b):
        if self.buttonList[b].text() == "":
            font = QtGui.QFont()
            font.setPointSize(50)
            font.setBold(True)
            font.setWeight(75)
            self.buttonList[b].setFont(font)
            self.buttonList[b].setText(self.player)
            if self.checkifwin() or self.checkIfTie():
                return 
            else:
                print(self.step)
                if self.complexity == "easy":
                    self.computer_step_easy()
                    self.checkifwin()
                    self.checkIfTie()
                elif self.player == "X" and self.complexity == "hard":
                    self.computer_step_hard_O()
                    self.checkifwin()
                    self.checkIfTie()
                elif self.player == "O" and self.complexity == "hard":
                    self.computer_step_hard_X()
                    self.checkifwin()
                    self.checkIfTie()
        self.step += 1

    
    def checkIfTie(self):
        btn_text_list = []
        for i in self.buttonList:
            btn_text_list.append(i.text())
        
        if "" not in btn_text_list:
            self.label.setText("It is a tie!")
            # time.sleep(3)
            # self.clicker_play_again()
            return True
        return False


    def checkifwin(self):
        for triple in self.row_triples:
            x, y, z = triple
            if self.buttonList[x].text() == self.buttonList[y].text() and self.buttonList[y].text() == self.buttonList[z].text() and self.buttonList[x].text() != '':
                self.label.setText(f"The winner is {self.buttonList[y].text()}")
                # time.sleep(3)
                # self.clicker_play_again()
                return True
        return False

    def computer_step_easy(self):
        while True:
            position = random.randint(0, 8)
            if self.buttonList[position].text() == "":
                self.buttonList[position].setText(self.computer)
                break
        

    def check_computer_win(self):
        for triple in self.row_triples:
            x, y, z = triple
            vals = sorted([self.buttonList[x].text(), self.buttonList[y].text(), self.buttonList[z].text()])
            if vals[0] == '' and vals[1] == vals[2] == self.computer:
                if self.buttonList[y].text() == '':
                    x = y
                if self.buttonList[z].text() == '':
                    x = z
                self.buttonList[x].setText(self.computer)
                return True
        return False
    
    def check_player_win(self):
        for triple in self.row_triples:
            x, y, z = triple
            vals = sorted([self.buttonList[x].text(), self.buttonList[y].text(), self.buttonList[z].text()])
            if vals[0] == '' and vals[1] == vals[2] == self.player:
                if self.buttonList[y].text() == '':
                    x = y
                if self.buttonList[z].text() == '':
                    x = z
                if self.buttonList[x].text() == "":
                    self.buttonList[x].setText(self.computer)
                    return True
        return False

    #computer plays hard with X
    def computer_step_hard_X(self):
        if self.check_computer_win():
            return True
        elif self.check_player_win():
            return True

        
        #step 1
        if self.step == 1:
            self.buttonList[4].setText("X")
            return True

        #step 2
        if self.step == 2:
            corners = [0, 2, 6, 8]
            for corner in corners:
                if self.buttonList[corner].text() == 'O':
                    self.buttonList[8 - corner].setText('X')
                    return True

            if self.buttonList[1].text() == "O" or self.buttonList[7].text() == 'O':
                x = random.choice([3,5])
                self.buttonList[x].setText('X')
                return True
            elif self.buttonList[3].text() == "O" or self.buttonList[5].text() == "O":
                x = random.choice([1,7])
                self.buttonList[x].setText('X')
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
                if self.buttonList[x].text() == "X" and self.buttonList[y].text() == "X" and self.buttonList[z].text() == "":
                    self.buttonList[z].setText('X')
                    return True
                
                if self.buttonList[x].text() == "X" and self.buttonList[z].text() == "X" and self.buttonList[y].text() == "":
                    self.buttonList[y].setText('X')
                    return True
                
        #step 4 
        if self.step == 4:
            for i in range(len(self.buttonList)):
                if self.buttonList[i].text() == "":
                    self.buttonList[i].setText('X')
                    break
            # self.step += 1
            return True
        
        
        #step 5
        if self.step == 5:
            for i in range(len(self.buttonList)):
                if self.buttonList[i].text() == "":
                    self.buttonList[i].setText('X')
                    break
            return True

    def computer_step_hard_O(self):
        if self.check_computer_win():
            return True
        elif self.check_player_win():
            return True

        #step 1
        if self.step == 1:
            if self.buttonList[4].text() == "":
                self.buttonList[4].setText('O')
                return True
            else:
                x = random.choice([0, 2, 6, 8])
                self.buttonList[x].setText('O')
                return True

        #step 2
        if self.step == 2:
            corners = [0, 2, 6, 8]
            for corner in corners:
                if self.buttonList[corner].text() == '':
                    self.buttonList[corner].setText('O')
                    return True
            
        #step 3 or 4
        if self.step >= 3:
            for i in range(len(self.buttonList)):
                if self.buttonList[i].text() == "":
                    self.buttonList[i].setText('O')
                    break
            return True
    


class logic:
    def __init__(self,player,computer,complexity,buttonList):
        self.player = player
        self.computer = computer
        self.complexity = complexity
        self.buttonList = buttonList
        

    def easyGame(self, gameOrder):
        if gameOrder:
            if self.player == "O":
                self.computer_step_hard_X()
                self.checkifwin()
            else:
                self.computer_step_hard_O()
                self.checkifwin()

        else:
            self.computer_step_easy()
            self.checkifwin()


    def clicker_play_again(self):
        for i in self.buttonList:
            i.setText("")
        self.label.setText("")
        self.step = 1

    def checkIfTie(self):
        btn_text_list = []
        for i in self.buttonList:
            btn_text_list.append(i.text())
            
        if "" not in btn_text_list:
            self.label.setText("It is a tie!")
            #QtCore.QCoreApplication.processEvents()

            # time.sleep(3)
            #self.clicker_play_again()

    def checkifwin(self):

        for triple in self.row_triples:
            x, y, z = triple
            if self.buttonList[x].text() == self.buttonList[y].text() and self.buttonList[y].text() == self.buttonList[z].text() and self.buttonList[x].text() != '':
                self.label.setText(f"The winner is {self.buttonList[y].text()}")
                #QtCore.QCoreApplication.processEvents()
                # time.sleep(3)
                #self.clicker_play_again()
                return True
        self.checkIfTie()
        return False

    def computer_step_easy(self):
        while True:
            position = random.randint(0, 8)
            if self.buttonList[position].text() == "":
                self.buttonList[position].setText(self.computer)
                break

    def check_computer_win(self):
        for triple in self.row_triples:
            x, y, z = triple
            vals = sorted([self.buttonList[x].text(), self.buttonList[y].text(), self.buttonList[z].text()])
            if vals[0] == '' and vals[1] == vals[2] == self.computer:
                if self.buttonList[y].text() == '':
                    x = y
                if self.buttonList[z].text() == '':
                    x = z
                self.buttonList[x].setText(self.computer)
                return True
        return False

    def check_player_win(self):
        for triple in self.row_triples:
            x, y, z = triple
            vals = sorted([self.buttonList[x].text(), self.buttonList[y].text(), self.buttonList[z].text()])
            if vals[0] == '' and vals[1] == vals[2] == self.player:
                if self.buttonList[y].text() == '':
                    x = y
                if self.buttonList[z].text() == '':
                    x = z
                print(self.buttonList[x].text())
                if self.buttonList[x].text() == "":
                    print(self.buttonList[x].text())
                    self.buttonList[x].setText(self.computer)
                    return True
        return False
        
    def computer_step_hard_X(self):
        if self.check_computer_win():
            self.step += 1
            return True
        elif self.check_player_win():
            self.step+=1
            return True

        
        #step 1
        if self.step == 1:
            self.buttonList[4].setText("X")
            self.step+=1
            #QtCore.QCoreApplication.processEvents()

            return True

        #step 2
        if self.step == 2:
            corners = [0, 2, 6, 8]
            for corner in corners:
                if self.buttonList[corner].text() == 'O':
                    self.buttonList[8 - corner].setText('X')
                    self.step += 1
                    #QtCore.QCoreApplication.processEvents()
                    return True

            if self.buttonList[1].text() == "O" or self.buttonList[7].text() == 'O':
                x = random.choice([3,5])
                self.buttonList[x].setText('X')
                self.step+=1
                #QtCore.QCoreApplication.processEvents()

                return True
            elif self.buttonList[3].text() == "O" or self.buttonList[5].text() == "O":
                x = random.choice([1,7])
                self.buttonList[x].setText('X')
                self.step+=1
                #QtCore.QCoreApplication.processEvents()

                return True
            elif self.buttonList[0].text() == "" and self.buttonList[8].text() == "":
                self.buttonList[0].setText('X')
                self.step+=1
                #QtCore.QCoreApplication.processEvents()

                return True
            elif self.buttonList[2].text() == "" and self.buttonList[6].text() == "":
                self.buttonList[2].setText('X')
                self.step+=1
                #QtCore.QCoreApplication.processEvents()

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
                if self.buttonList[x].text() == "X" and self.buttonList[y].text() == "X" and self.buttonList[z].text() == "":
                    self.buttonList[z].setText('X')
                    self.step += 1
                    #QtCore.QCoreApplication.processEvents()

                    return True
                
                if self.buttonList[x].text() == "X" and self.buttonList[z].text() == "X" and self.buttonList[y].text() == "":
                    self.buttonList[y].setText('X')
                    self.step += 1
                    #QtCore.QCoreApplication.processEvents()

                    return True
                
        #step 4 
        if self.step == 4:
            for i in range(len(self.buttonList)):
                if self.buttonList[i].text() == "":
                    self.buttonList[i].setText('X')
                    #QtCore.QCoreApplication.processEvents()

                    break
            self.step += 1
            return True
        
        
        #step 5
        if self.step == 5:
            for i in range(len(self.buttonList)):
                if self.buttonList[i].text() == "":
                    self.buttonList[i].setText('X')
                    #QtCore.QCoreApplication.processEvents()

                    break
            return True


    def computer_step_hard_O(self):
        if self.check_computer_win():
            self.step += 1
            return True
        elif self.check_player_win():
            self.step += 1
            return True

        #step 1
        if self.step == 1:
            if self.buttonList[4].text() == "":
                self.buttonList[4].setText('O')
                self.step += 1
                #QtCore.QCoreApplication.processEvents()
                return True
            else:
                x = random.choice([0, 2, 6, 8])
                self.buttonList[x].setText('O')
                self.step += 1
                #QtCore.QCoreApplication.processEvents()
                return True

        #step 2
        if self.step == 2:
            corners = [0, 2, 6, 8]
            for corner in corners:
                if self.buttonList[corner] == '':
                    self.buttonList[corner].setText('O')
                    self.step += 1
                    #QtCore.QCoreApplication.processEvents()
                    return True
            
        #step 3 or 4
        if self.step >= 3:
            for i in range(len(self.buttonList)):
                if self.buttonList[i].text() == "":
                    self.buttonList[i].setText('O')
                    #QtCore.QCoreApplication.processEvents()
                    break
            self.step += 1
            return True
    

    

