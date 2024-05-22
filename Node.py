# tiles is called from the python file.

from tile import tile
# puzzleboard 
# puzzleboard called python. etc.
from PuzzleBoard import PuzzleBoard
# queue called from python,

from queue import Queue

#deepcopy, learned this from 2620 in c++ programming..etc.
from copy import deepcopy


#class node, 
class Node:
    # define inital boardgame, move, etc.

    def __init__(self, BoardGame, parent=None, move=""):
        
        self.Board = BoardGame
        
        self.parent = parent
        
        self.depth = 0
        
        #if statement for parent = none, initialize self depth at 0, self moves = move.
        if parent is None:

            self.depth = 0
            self.moves = move
        else:
            # if not, then else statement parent + 1, same thing for parent, parent +move
            self.depth = parent.depth+1
            self.moves = parent.moves + move
    # self called, stored as taker, which equals the queue.
    def taker(self):
        taker = Queue()
        # for looop m in moves
        #deepcopy self.board. move, 
        #if statement if h zero is not self board zero.
        for m in self.Board.moves:
            h = deepcopy(self.Board)
            h.move(m)
            #if statement.
            if h.zero is not self.Board.zero:
                taker.put(Node(h, self, m))
                #taker is returned after the loop, and if statement.
        return taker

#string, returned, self.moves.
    def __str__(self):
        return str(self.moves)
    