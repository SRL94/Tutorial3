from nqueen import *
n = 4
NQ = NQueens(n)
timer = 0
while(not NQ.allQueensSafe()):
    # n+1 will always be minimized because there are at most n - 1 conflicts for a single queen.
    minAttacks = n + 1
    # pick a random queen and obtain all the positions that our chosen queen can be moved to
    pickedQueen = NQ.pickRandomQueen() 
    
    positions = NQ.availablePositions(pickedQueen)
    minConflictPosition = (-1,-1)

    for pos in positions: # iterate through all positions of pickedQueen and move to position of minimum conflict
        # TO DO
        '''
        hints:
        1. Relocate the pickedQueen to "pos" using the NQ.moveQueen function.
        2. Calculate the number of conflicts that arise if the pickedQueen is moved to the new position using NQ.specificQueenConflicts.
        3. If the conflicts decrease after the move (i.e. less than minAttacks), update minConflictPosition and minAttacks.
        4. Return the relocated queen to its original position after evaluating the potential move.
        '''
        pass

    NQ.moveQueen(pickedQueen,minConflictPosition)# move queen to least conflict spot

print(NQ.printBoard())
