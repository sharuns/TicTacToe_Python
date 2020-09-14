#from IPython.display import clear_output
print("####################################################################################################")
#Function to display the board
def display_board(board):
    print(board[7:10],"  7    8    9  ") #print("  7    8    9  ")
    print(board[4:7],"  4    5    6  ") #print("  4    5    6  ")
    print(board[1:4],"  1    2    3  ") #print("  1    2    3  ")
    
def player_input():
    pla[0] = 0
    pla[0]  = input ("Choose your marker Player1 (X or O)")
    while pla[0] not in ["X","O","x","o"]: 
        pla[0]  = input ("Choose a valid marker Player1 (X or O)")
    if pla[0] == "x":
        pla[1] = "O"
    else :
        pla[1] = "x"


def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark)or
    (board[1] == mark and board[5] == mark and board[9]== mark) or
    (board[2] == mark and board[5] == mark and board[8]== mark) or
    (board[1] == mark and board[2] == mark and board[3]== mark) or
    (board[3] == mark and board[5] == mark and board[7]== mark) or
    (board[4] == mark and board[5] == mark and board[6]== mark) or
    (board[3] == mark and board[6] == mark and board[9]== mark) or
    (board[7] == mark and board[8] == mark and board[9]== mark))


def space_check(board, position):
    return board[position] == ' '



def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            print("HI")
            return False
    return True
def player_choice(board):
    position = int (input('Enter your choice (1-9):'))
    while position not in [1,2,3,4,5,6,7,8,9]:
        position = int (input('Please enter a valid choice (1-9):'))
    if space_check(board,position):
        return position
    else:
        return 0 


def replay():
    choice  = input("Do you want to play again ? (y/n):")
    return choice == 'y'


print('Welcome to Tic Tac Toe!')
while True:
    # Set the game up here
    #pass
    Tic = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    CurPla = 0
    pla = [2,2]
    players = [0,0]
    player_input()
    #print("Marker of Player 1 : " + pla[0] + "\nMarker of Player 2 : " + pla[1] + "\n")
    print(f"Marker of Player 1 : {pla[0]}\nMarker of Player 2 : {pla[1]}\n")
    players[0] = input("Enter Name for player 1 : ")
    players[1] = input("Enter Name for player 2 : ")
    display_board(Tic)
    game_on = True
    while game_on:
        if full_board_check(Tic):
            print("Sadly its a draw")
            break
        #Player 1 Turn
        #print(players[CurPla]+"'s chance, your marker is "+ pla[CurPla])
        print(f"{players[CurPla]}'s chance, your marker is {pla[CurPla]}")
        pos = 0
        while pos==0:
            pos = player_choice(Tic)
            if not pos:
	            print("Already occupied ,choose some other position!")
        
        place_marker(Tic,pla[CurPla],pos)
        display_board(Tic)
        if win_check(Tic, pla[CurPla]):
            game_on = False
            #print("Congrats!!!, " + players[CurPla] + " has won!")	
            print(f"Congrats!!!,{players[CurPla]} has won!")
        CurPla = not CurPla
    if not replay():
        break

