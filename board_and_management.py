class Board:
    def __init__(self):
        self.board = [["   " for _ in range(15)] for _ in range(15)] 
        self.add_board()
        
        #Added Board class with constructor to initialize the game board