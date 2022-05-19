import random, sys

BLANK = "  "

def main():
    """The main loop for the game"""
    try:

        print("{0:>50}".format("SLIDING TILE PUZZLE"))
        print("""Use the WASD keys to move the tiles back into their original order:
        *--*--*--*--*
        |1 |2 |3 |4 |
        *--*--*--*--*
        |5 |6 |7 |8 |
        *--*--*--*--*
        |9 |10|11|12|
        *--*--*--*--* 
        |13|14|15|  |
        *--*--*--*--* """)
        input("Press Enter to begin\n > ")

        gameboard = getnewpuzzle()

        while True:
            displayboard(gameboard)
            playermove = askforplayermove(gameboard)
            makemove(gameboard, playermove)

            if gameboard == getnewboard():
                print("You Won!")
                sys.exit()
    except KeyboardInterrupt:
        print("\nThanks for playing! Try to finish the game the next time you play")

def getnewboard():
    """Return a list of lists that represents a new tile puzzle."""
    return [["1","5","9","13"],["2","6","10","14"],
            ["3","7","11","15"],["4","8","12",BLANK]]

def displayboard(board):
    """Display the board onto the screen."""
    labels = [board[0][0],board[1][0],board[2][0],board[3][0],
              board[0][1],board[1][1],board[2][1],board[3][1],
              board[0][2],board[1][2],board[2][2],board[3][2],
              board[0][3],board[1][3],board[2][3],board[3][3]]

    boardtodraw = """
    +---------+---------+---------+---------+
    |         |         |         |         |
    |    {}   |    {}   |    {}   |    {}   |
    |         |         |         |         |
    +---------+---------+---------+---------+ 
    |         |         |         |         |
    |    {}   |    {}   |    {}   |    {}   |
    |         |         |         |         |
    +---------+---------+---------+---------+ 
    |         |         |         |         |
    |    {}   |    {}   |    {}   |    {}   |
    |         |         |         |         |
    +---------+---------+---------+---------+ 
    |         |         |         |         |
    |    {}   |    {}   |    {}   |    {}   |
    |         |         |         |         |
    +---------+---------+---------+---------+ 
    
    """.format(*labels)
    print(boardtodraw)

def findblankspace(board):
    """Return an (x,y) tuple of the blank spaces location"""
    for x in range(4):
        for y in range(4):
            if board[x][y] == "  ":
                return (x,y)

def askforplayermove(board):
    """Let the player select a tile to slide."""
    blankx, blanky = findblankspace(board)

    w = "W" if blanky != 3 else " "
    a = "A" if blankx != 3 else " "
    s = "S" if blanky != 0 else " "
    d = "D" if blankx != 0 else " "

    while True:
        print("                          ({})".format(w))
        print("Enter WASD (or Quit): ({}) ({}) ({})".format(a,s,d))

        response = input("> ").upper()
        if response == "QUIT":
            sys.exit()

        if response in (w + a + s + d).replace(" ",""):
            return response
        else:
            print("INVALID MOVE! (TRY AGAIN)")

def makemove(board,move):
    """Carry out the given move on the board"""
    bx, by = findblankspace(board)

    if move == "W":
        board[bx][by],board[bx][by+1] = board[bx][by+1],board[bx][by]
    elif move == "A":
        board[bx][by], board[bx+1][by] = board[bx+1][by], board[bx][by]
    elif move == "S":
        board[bx][by], board[bx][by-1] = board[bx][by-1], board[bx][by]
    elif move  == "D":
        board[bx][by], board[bx-1][by] = board[bx-1][by], board[bx][by]

def makerandommove(board):
    """Perform a slide in a random direction"""
    blankx, blanky = findblankspace(board)
    validmoves = []
    if blanky != 3:
        validmoves.append("W")
    if blankx != 3:
        validmoves.append("A")
    if blanky != 0:
        validmoves.append("S")
    if blankx != 0:
        validmoves.append("D")

    makemove(board, random.choice(validmoves))

def getnewpuzzle(moves=200):
    """Get a new puzzle by making random slides from a solved state"""
    board = getnewboard()

    for i in range(moves):
        makerandommove(board)
    return board

main()

