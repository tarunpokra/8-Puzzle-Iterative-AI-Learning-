# TARUN POKRA
# ASSIGNMENT 1, QUESTION 4, 8-PUZZLE PROGRAM.
# MAY 19TH 2024
# note: this main python file is what you use to run the program. so for example, if you type "DEFAULT" values you'll see the space, and the..
# .. direction needed to to complete it. for example, "D", for Down.

from PuzzleBoard import PuzzleBoard # puzzleboard python file is called

# search python file is called.

from Search import Search

print("Hello there, this is the 8-Puzzle program!")
input_string = input("Enter elements of a list separated by spaces or Enter DEFAULT in all caps to set list as 1, 2, 3, 4, 5, 0, 7, 8, 6: ")

# if statement if user types in default in all caps.

# if statement input string if its not default, then the user inputs own numbers.

if(input_string != "DEFAULT") :
  title = list(map(int, input_string.split()))
  
else :
    title = [1,2,3,4,5,0,7,8,6] # else statement

# puzzleboard title called and stored as board, same thing search1 = board.

board = PuzzleBoard(title)
#search1
Search1 = Search(board)

print(" ")
print("space added above...")

print("Moves that are required to reach the goal. D, down, R, right, U, up, L, left: ", Search1.iterativeDeepening())
#iterative deepening, search1. etc.

board.printBoard()
#board print.
