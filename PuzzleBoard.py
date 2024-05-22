#called tile from the python files.

from tile import tile

# class puzzleboard, 
class PuzzleBoard:

# define the initilization self, and the tiles that are given.
    def __init__(self, tilesgiven):
       # self initalized at 0.

       self.i = 0
       
       self.key1 = None
       #similar code form node python file.

       self.key2 = None
       
       self.zero=(self.key1,self.key2)
       

       # these are moves, that were displayed in a string in node file.
       self.moves=['U','D','L','R']
       # up, down, left, right.

       #ranges for the tiles, 3 by 3, etc.

       self.tiles = [[0 for _ in range(3)] for _ in range(3)]
       
       # for loop
       for x in range(3):
            # x-axis tiles for loop.
            for y in range(3):
                # for loop for y-axis tiles
                self.n=tile(tilesgiven[self.i]) 

                
                self.tiles[x][y] = self.n
                
                self.i += 1
                # stored and equals 1
                
    def printBoard(self):
     # print board, self, tiles, etc.
     print("Space, ignore this. ")

     for i in range(3):
        # for i in range 3, 
        for j in range(3):
            # for loop j range of 3.

            if self.tiles[i][j].value() == 0:
                print("SPACE  ", end = "")
                # printing blank space.
            else:
                print(f"{self.tiles[i][j].value():2d}", end = "")
                # print f, self tiles i, and j values 2D.

            if j != 2:
                # if j does not equal 2, print out vertical separators, etc.

                print(" | ", end="")  # Print vertical separators between tiles
        print()  # Move to the next line
        # blank line again.
        if i != 2:
            print("--------------")  # Print horizontal separator between rows
            # visually adding a line, etc.

       
    
    def move(self,direction):
        
        # moving, direction, etc.
        for x in range(3):
             # x range of 3, similar code above.
             for y in range(3):
                 # y range of 3, similar code above.
                 # if statement tiles of both x and y, intialize at 0.

                 if (self.tiles[x][y]).value() == 0:
                     # keys 1 and 2, equals x, y.
                     key1 = x
                     key2 = y

                     self.key1=key1
                     self.key2=key2
                     # self key1, key2, 
                     self.zero=(self.key1,self.key2)
                     # zero = self, key1, key2, etc.

        if self.key1 != None and self.key2 != None:
         # if statement key 1, and key 2 equals not, then equal none.

         if direction == 'R':
                # right direction
                self.temp = None
                if key2 == 2:
                    return 0
                else :
                    self.temp =self.tiles[key1][key2+1]
                    self.tiles[key1][key2+1]=self.tiles[key1][key2]
                    self.key2=key2+1
                    self.tiles[key1][key2]=self.temp
                    self.zero=(self.key1,self.key2)
  
         elif direction == 'L':
                # L direction, similar code as R, above, copy-paste, edit.
                self.temp = None

                # if statement if key2 is 0, then terminate.

                if key2 == 0:
                    return 0
                # else statement, temp variables, 
                else :
                    self.temp =self.tiles[key1][key2-1]
                    self.tiles[key1][key2-1]=self.tiles[key1][key2]
                    self.key2=key2-1
                    self.tiles[key1][key2]=self.temp
                    self.zero=(self.key1,self.key2)
         elif direction == 'U':
                self.temp = None
                # U direction, up.
                if key1 == 0:
                    return 0
                else :
                    self.temp =self.tiles[key1-1][key2]
                    self.tiles[key1-1][key2]=self.tiles[key1][key2]
                    self.key1=key1-1
                    self.tiles[key1][key2]=self.temp
                    # similar code, as R, L, etc.
                    self.zero=(self.key1,self.key2)
         elif direction == 'D':
                self.temp = None
                # similar code, this time for D, as in Down for the tiles.
                if key1 == 2:
                    return 0
                else :
                    self.temp =self.tiles[key1+1][key2]
                    self.tiles[key1+1][key2]=self.tiles[key1][key2]
                    self.key1=key1+1
                    self.tiles[key1][key2]=self.temp
                    self.zero=(self.key1,self.key2)
         else: 
                print("Sorry the direction is wrong, oh well.")
                return 0
         
        else:
            # print and display these statements.

            print("Sorry, not working")
            return 0

    def checkPuzzle(self):
      # intialize count 1, 0, 3, j range, 0, 3.
      count=1
      for i in range(0,3):
          # for loop for i in range
          for j in range(0,3):
              # j loop for i in range, count, 3,3, etc.
              if self.tiles[i][j].value()!=(count%(3*3)):
                  return False
              # return false if count % 3 * 3.

              count+=1
              # store and equal count + 1.
      return True
    