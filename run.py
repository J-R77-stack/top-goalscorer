#------------ Global variables-------------

# Variable containing a list to hold the board game data.
board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

# Variable to inform the users if the game is finished yet.
game_still_running = True        

# Variable to1
# inform the users who the winner is.
winner = None

# Variable to inform the users whose go it is, starts with player X.
current_player = "X"


def show_board():
  """
  Function to print the game board to the screen in every round
  """
  print("\n")
  print(" Welcome to Noughts and Crosses")
  print("\n")
  print(" | " + board[0] + " | " + board[1] + " | " + board[2]+ " | ")
  print(" | " + board[3] + " | " + board[4] + " | " + board[5]+ " | ")
  print(" | " + board[6] + " | " + board[7] + " | " + board[8]+ " | ")
  print("\n")

def play_game(): 

   show_board()

   while game_still_running:
    """
    While loop to loop through which players turn it is and 
    to then change the player and check to see if game is over.
    """

    game_turn(current_player)

    see_if_game_over()

    change_player()

   if winner == "X" or winner == "O":
     print(winner + "is the winner.")
   elif winner == None:
     print("Its a Draw")  

def game_turn(player):
  place = input("Please select a number from 1 to 9:")
  place = int(place) - 1

  board[place] = "X"
 
def see_if_game_over():
  """
  Fuction to see if game is over by a win or a draw
  """
  see_if_winner()
  see_if_draw()

def see_if_winner():

  row_winner = check_rows()

  column_winner = check_columns()

  diagonal_winner = check_diagonals()
  if row_winner:
    # There was a win
  elif column_winner:
    # There was a win
  elif diagonal_winner:
    # There was a win 
  else:
    # No win  
  return  

def check_rows():
  return
  

def see_if_draw():
  return

def change_player(): 
  return 
  """
  Fuction to change the player from X to O and inform the user whose turn it is
  """  

play_game()