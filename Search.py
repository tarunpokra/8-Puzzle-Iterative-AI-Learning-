# puzzleboard is imported from puzzleboard python, etc.


from PuzzleBoard import PuzzleBoard

# node, node is imported from node.

from Node import Node

# queue is needed for life of queue.
from queue import LifoQueue

# class search created for the self board, node, 
class Search:
   def __init__(self, BoardA):
        self.start = Node(BoardA)
    
    # this is iterative deepening, self, intialized = 0.
   def iterativeDeepening(self):
        self.depth = 0
        result = None
        # result = none, 

        while result == None:
            # while loop result initialized none, 

            result = self.depthLimited(self.depth)
            # result self, depth limited, depth, stored and equal + 1.

            self.depth +=1
            
        return result
   # return result 


   def depthLimited(self, depth):
        
        levels = LifoQueue()
        # these are levels, start, stop, if needed.

        levels.put(self.start)
        while True:

            # while true, the levels empty.
            # if levels empty returning none.
            if levels.empty():
                return None
            actual = levels.get()
            # if statement, now if the board.checkpuzzle drew, then return the actual one.
            if (actual.Board).checkPuzzle():
                
                return actual
            
            elif actual.depth is not depth:

                # else if take 1 equals actual.
                taker1 = actual.taker()
                while not taker1.empty():
                    # while loop for not, under if the taker equals empty.
                    levels.put(taker1.get())
                    # done.