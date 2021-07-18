# Tic-tac-toe
# A very simple implementation

board = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"]]
player = "X"
won = False
winner = ""

class bcolors:
    HEADER = '\033[95m'
    Cyan = '\033[94m'
    O = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    X = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def switchplayer(player):
    if player == "X":
        return "O"
    return "X"

def getmove(player, board):
    '''Gets and checks for valid moves, returns x and y coordinates'''
    x, y = -1, -1
    print("Player: " + player)
    while x == -1:
        y, x = findpos(input("Enter your move:"), board)
        if x == -1:
            print("Position is not open.")
    print("X:" + str(x) + " Y:" + str(y))
    board[y][x] = player
    return board

def findpos(move, board):
    '''
    Given a move and the board, returns row and column of the position
    If none is found (spot is taken), then return -1, -1
    '''
    foundRow, foundCol = -1, -1
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == move:
                foundRow = y
                foundCol = x
    return foundRow, foundCol

def printboard(board):
    print(" _____________")
    output = ""
    for y in board:
        pline = " |"
        for x in y:
            if x == "X":
                output = bcolors.X + x + bcolors.ENDC
            elif x == "O":
                output = bcolors.O + x + bcolors.ENDC
            else:
                output = x
            pline += " " + output + " |"
        print(pline)
        print(" _____________")

def checkwin(board):
    # Return t/f if game is won and player letter if so
    # Check horizontal
    for row in board:
        if "".join(row) == "XXX":
            return True, "X"
        if "".join(row) == "OOO":
            return True, "O"
    # Check vertical
    for x in range(3):
        check = ""
        for y in range(len(board)):
            check += board[y][x]
        if check == "XXX":
            return True, "X"
        if check == "OOO":
            return True, "O"
    # Check diagonal
    lr = "" # left to right
    rl = "" # right to left
    for i in range(3):
        lr += board[i][i]
        rl += board[2-i][2-i]
    if lr == "XXX" or rl == "XXX":
        return True, "X"
    if lr == "OOO" or lr == "OOO":
        return True, "O"

    return False,""

def movesleft(board):
    # True or false if any moves left
    for row in board:
        for col in row:
            if col != "X" and col != "O":
                return True
    return False

# Game loop
while not won and movesleft(board):
    player = switchplayer(player)
    printboard(board)
    board = getmove(player, board)
    print(board)
    won, winner = checkwin(board)

if won:
    printboard(board)
    print(bcolors.WARNING + "Won by: "+ winner + bcolors.ENDC)
if not movesleft(board):
    print("No winner!")













