import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"
winner = None
gameRunning = True

def printBoard(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def playerInput(board):
    try:
        inp = int(input("Enter a number 1-9: "))  # User input
        if 1 <= inp <= 9 and board[inp-1] == "-":
            board[inp-1] = current_player
        else:
            print("Invalid move, try again.")
            playerInput(board)
    except ValueError:
        print("Invalid input! Enter a number between 1 and 9.")
        playerInput(board)

def checkHorizontals(board):
    global winner
    for i in [0, 3, 6]:  # Check rows
        if board[i] == board[i+1] == board[i+2] and board[i] != "-":
            winner = board[i]
            return True
    return False

def checkRows(board):
    global winner
    for i in range(3):  # Check columns
        if board[i] == board[i+3] == board[i+6] and board[i] != "-":
            winner = board[i]
            return True
    return False

def checkDiagonals(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checkWin():
    global gameRunning
    if checkHorizontals(board) or checkRows(board) or checkDiagonals(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

def checkTie():
    global gameRunning
    if "-" not in board and winner is None:
        printBoard(board)
        print("It's a tie!")
        gameRunning = False

def switchPlayer():
    global current_player
    current_player = "O" if current_player == "X" else "X"

def computer(board):
    if gameRunning:  # Only let the computer play if the game is still running
        while current_player == "O":
            inp = random.randint(0, 8)
            if board[inp] == "-":
                board[inp] = "O"
                switchPlayer()
                break  # Stop after placing one move

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie()
    
    if gameRunning:
        switchPlayer()
        computer(board)
        checkWin()
        checkTie()
