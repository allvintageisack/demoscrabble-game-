class Board:
    def __init__(self):
        self.board = [["   " for _ in range(15)] for _ in range(15)] 
        self.add_board()
        self.board[7][7]=" * "
        
        #Added Board class with constructor to initialize the game board
        
    def add_board(self):
        TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
        DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
        TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
        DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))
        #coordinates To indicate the locations of special scoring squares on game board. 
        
        for co in TRIPLE_WORD_SCORE:
            self.board[co[0]][co[1]] = 'TWS'
        for co in DOUBLE_WORD_SCORE:
            self.board[co[0]][co[1]] = 'DWS'
        for co in TRIPLE_LETTER_SCORE:
            self.board[co[0]][co[1]] = 'TLS'
        for co in DOUBLE_LETTER_SCORE:
            self.board[co[0]][co[1]] = 'DLS'
            
        #The loops are for marking specific squares on the game board with their corresponding special scoring types: 
        # Triple Word Score (TWS), 
        # Double Word Score (DWS), 
        # Triple Letter Score (TLS), and Double Letter Score (DLS).
    
    def get_board(self):
        board_str= " | " + " | ".join(str(i) for i in range(10)) + " | " + " | ".join(str(i) for i in range(10, 15)) + " | "
        board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n" #This line creates a visual separation between the header and the board content.
        for i, row in enumerate(self.board):
            row_str = " | ".join(item for item in row)    
            if i < 10:
             board_str += f"{i} | {row_str} | \n"
            else:
                board_str += f"{i} | {row_str} | \n"
        
        board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
        return board_str 
    
        #The get_board method generates a string representation of the board 
        # that includes row and column indices, as well as the content of each cell. 
    
