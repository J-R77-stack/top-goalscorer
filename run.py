#------------ Global variables-------------

# Variable containing a list to hold the board game data.
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

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

  board[place] = player
 
def see_if_game_over():
  """
  Fuction to see if game is over by a win or a draw
  """
  see_if_winner()
  see_if_draw()

def see_if_winner():
  global winner

  row_winner = check_rows()

  column_winner = check_columns()

  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return  

def check_rows():
  global game_still_running
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  if row_1 or row_2 or row_3:
    game_still_going = False
  if row_1:
    return board[0]
  elif row_2:   
    return board[3] 
  elif row_3:
    return board[6] 
  else:
    return None

def check_columns():
  # Set global variables
  global game_still_running
  # Check if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  # Return the winner
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  # Or return None if there was no winner
  else:
    return None

def check_diagonals():
  # Set global variables
  global game_still_running
  # Check if any of the columns have all the same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  # Return the winner
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[6]
  # Or return None if there was no winner
  else:
    return None  

def see_if_draw():
  return

def change_player(): 
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player =="O":
    current_player = "X"
  return 
  """
  Fuction to change the player from X to O and inform the user whose turn it is
  """  

play_game()