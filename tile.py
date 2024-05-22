# I quickly created a class tile for the numbers, intialized, 
# as well as the value of the tiles, and the change, so for example 
# .. directions, up, down, right, left.

class tile:

    def __init__(self, num):
        self.localnum = num
          
    def value(self):

        
        return self.localnum

    def change(self,valu):
        
         self.localnum= valu
# done.
# 
