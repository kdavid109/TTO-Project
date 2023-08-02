#all the functions for Tic Tac Toe
from random import shuffle
import random
#Displaying the board Fix
def displayBoard(boardings):
    
    count = 0
    showing =''
    for spot in boardings:
        showing = showing + spot + " "
        count += 1
        if count == 3:
            print(showing)
            showing = ''
            count = 0

# Choosing the players character
def whoGoesFirst():
    global board
    finished = False
    global first, second, player1Char, player2Char
    while finished != True:
        x = random.randint(1,2)
        goingFirst = input('Player 1, choose a number 1 or 2: ')

        if x == int(goingFirst):
            pickMark = input("Player 1 is going first! would you like to be X or O? : ")
            first = 'Player 1'
            second = 'Player 2'
            if(pickMark.upper() == 'X'):
                player1Char = 'X'
                player2Char = 'O'

                return player1Char, player2Char
                
            else:
                player1Char = 'O'
                player2Char = 'X'
                return player2Char, player1Char
        else:
            
            pickMark = input("Player 2 is going first! would you like to be X or O?: ")
            first = 'Player 2'
            second = 'Player 1'
            if(pickMark.upper() == 'X'):
                player2Char = 'X'
                player1Char = 'O'
                return player1Char, player2Char
            else:
                player2Char = 'O'
                player1Char = 'X'
                return player1Char, player2Char
        finished = True  

#Method to check if board is filled, return a boolean value
def boardFilled(boardings):
    count = 0
    for spot in boardings:
        if spot == '':
            return False
            
        else:
            continue
        count += 1
    return True
#Function to return True if a spot is empty
def spotEmpty(boardings,ptr):
    
    if boardings[ptr] == '':
        return True
    else:
        return False

#Function to check who won
def gameWon(boardings, char):
    
    clst = [char, char, char]
    count = 0
    straightAcross = 0 # checking 
    endOfAcross = 3 
    while count < 3:
        if boardings[count::3] == clst:
            return True
        if boardings[straightAcross:endOfAcross:] == clst:
            return True
        count += 1
        straightAcross += 3
        endOfAcross += 3

    if boardings[::4] == clst:
        return True
    if boardings[2:7:2] == clst:
        return True
    return False

#starting the game
def startGame(board):
   someoneWon = False
   whoGoesFirst()
   global first
   while boardFilled(board) == False and someoneWon == False:
       displayBoard(board)
       theChoice = input(f'%s pick a spot from 0 - 8  : ' %(first))
       if isinstance(theChoice, int):
           theChoice = int(theChoice)

       if (0 <= theChoice < 9) and spotEmpty(board, theChoice) == True:
           
           if first == 'Player 1':
               board[theChoice] = player1Char
               first = 'Player 2'
           elif first == 'Player 2':
                board[theChoice] = player2Char
                first = 'Player 1'
       else:
           print('Choose another spot')
       #pla1Wins = gameWon(board, player1Char)
       if gameWon(board,player1Char) == True:
           print('Player 1 Wins!')
           displayBoard(board)
           someoneWon = True
       elif gameWon(board, player2Char) == True:
           print('Player 2 Wins!')
           displayBoard(board)
           someoneWon = True
           
   if boardFilled(board) == True and someoneWon == False:
       print('Sorry No Winner!')

   global repeat
   repeat = input('Do you wanna play again? Y or N: ')
   if repeat.upper() == 'Y':
       board = ['','','','','','','','','']
       someoneWon = False
       startGame(board)
   else:
       return
    