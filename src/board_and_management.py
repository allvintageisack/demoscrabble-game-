class Board:
    def __init__(self):
        self.board = [["   " for _ in range(15)] for _ in range(15)]
         #we initialize a board with empty spaces
        self.add_cells()
        #adds scoring cells to the board
        self.board[7][7] = " X "
        # set the center cell to indicate the starting point

    def add_cells(self): # Define coordinates  for tws,dws,tls & dls
        triple_word_score = [(0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14)]
        double_word_score = [(1, 1), (2, 2), (3, 3), (4, 4), (1, 13), (2, 12), (3, 11), (4, 10),
                             (13, 1), (12, 2), (11, 3), (10, 4), (13, 13), (12, 12), (11, 11), (10, 10)]
        triple_letter_score = [(1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5),
                               (9, 9), (9, 13), (13, 5), (13, 9)]
        double_letter_score = [(0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2),
                               (6, 6), (6, 8), (6, 12), (7, 3), (7, 11), (8, 2), (8, 6), (8, 8),
                               (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8), (14, 3), (14, 11)]
        # place tws,dws,tls & dls on the board 
        for co in triple_word_score:
            self.board[co[0]][co[1]] = 'TWS'
        for co in double_word_score:
            self.board[co[0]][co[1]] = 'DWS'
        for co in triple_letter_score:
            self.board[co[0]][co[1]] = 'TLS'
        for co in double_letter_score:
            self.board[co[0]][co[1]] = 'DLS'

    def get_board(self): #creates the top header of the board display with column numbers
        board_str = "   |  " + "  |  ".join(str(item) for item in range(10)) + "  | " + "  | ".join(str(item) for item in range(10, 15)) + " |"
        
        #add the top bordr of the board display
        board_str += ("\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ "
                      "_\n")

        formatted_rows = []
        for i, row in enumerate(self.board):# format each row of the board for display
            row_str = " | ".join(str(item) for item in row)

            #add row number with proper spacing 
            if i < 10:
                formatted_rows.append(f"{i}  | {row_str} |")
            else:
                formatted_rows.append(f"{i} | {row_str} |")

        row_separator = ("\n   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ "
                         "_ _|\n")
        board_str += row_separator.join(formatted_rows)
        board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
        return board_str

    def update_board(self, word, orientation, x, y):
        if orientation == "right":
            for i, char in enumerate(word):
                self.board[y][x + i] = f" {char} "
        elif orientation == "down":
            for i, char in enumerate(word):
                self.board[y + i][x] = f" {char} "

    def display_board(self):
        print(self.get_board())

    def is_cell_available(self, word, orientation, x, y):
        if orientation == "right":
            return all(self.board[y][x + i] == "   " or self.board[y][x + i] == f" {word[i]} " for i in range(len(word)))
        elif orientation == "down":
            return all(self.board[y + i][x] == "   " or self.board[y + i][x] == f" {word[i]} " for i in range(len(word)))
        return False




    def check_intersection(self, word, direction, col, row):
        word_length = len(word)
        if direction == "right":
            for i in range(word_length):
                if self.board[row][col + i] != "   ":
                    return True
        elif direction == "down":
            for i in range(word_length):
                if self.board[row + i][col] != "   ":
                    return True
        return False



    # TODO: check the existing word in the board and ensure that if the new word intersects with an existing word,
    #  the new word is valid and is  in the dictionary
