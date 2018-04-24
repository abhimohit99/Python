def welcome():
  print("Welcome to Tic-Tac-Toe!")

def clear_board():
  print("\n"*100) #couldn't find a better universal solution to refresh console output

def display_board(board):
  row,col = 0,0 #keep track of rows and columns
  
  for x in board:
    col+=1
    print(f" {board.get(x)} ",end=' ')
    if(col==3): #if you've reached the third and final column:
      print("\n",end='') #get ready to print on a new line
      col=0
      row+=1
      if(row!=3):#and if you've not reached the last row:
        print("----|-----|----")

    else:
      print("|", end=' ',flush=True)

def player_input():
  global player1, player2
  player1 = input("Please pick a marker 'X' or 'O':").upper()
  while(player1!='X' and player1!='O'): #if input isn't valid:
    player1 = input("Please type 'X' or 'O':").upper()
  if(player1=='X'):
    print(f"Player 1 will be X and Player 2 will be O! Let's play!")
    player2='O'
  else:
    print(f"Player 1 will be O and Player 2 will be X! Let's play!")
    player2='X'

def error_check(board,position):
  if position not in ['1','2','3','4','5','6','7','8','9'] or board[position]== "X" or board[position]== "O": #if input position isn't valid:
    print("Please try again. Enter an available number:",end='')
    return False
  return True

def place_marker(board,marker):
  position = (input('Please enter a number:'))
  while not error_check(board,position):
    position = input()
  board[str(position)]=marker #put in the X or O in the position inputted.

def win_check(board,marker): #check if someone has gotten 3 in a row!
  if((board['7'] == board['8'] == board['9'] == marker) or (board['4'] == board['5'] == board['6'] == marker) or (board['1'] == board['2'] == board['3'] == marker) or (board['7'] == board['4'] ==  board['1'] == marker) or (board['8'] == board['5'] == board['2'] == marker) or (board['9'] == board['6'] == board['3'] == marker) or (board['7'] ==  board['5'] == board['3'] == marker) or (board['9'] == board['5'] == board['1'] == marker)):
    print(f"{marker} won!")
    return True

def draw_check(board): #check if the board is all full!
  return (set(board.values())=={'X','O'})

def replay(): #ask if user wants to play again
  return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

def do(board,marker):
  print(f"{marker}'s turn!")
  place_marker(board,marker)
  clear_board()
  display_board(board)

def play():
  player_input() #get initial setup inputs
  board={'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9'} #create board
  display_board(board)
  
  while True:
    #All the stuff to do for Player 2:
    do(board,player1)
    if(win_check(board,player1)): #check for a win!
      if(not replay()): #if user doesn't want to play again:
        break
      else:
        clear_board()
        play()
    
    #Checking for a draw in between inputs from Players 1 and 2:
    if(draw_check(board)):#check for a draw!
      print("It's a draw!")
      if(not replay()): #check for replaying, as above
        break
      else:
        clear_board()
        play()
    
    #All the stuff to do for Player 2:
    do(board,player2)
    if(win_check(board,player2)): #check for a win!
      if(not replay()): #check for replaying, as above
        break
      else:
        clear_board()
        play()

welcome()
play()
