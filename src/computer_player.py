from src.player import Player
import random
from src.word import Word

class ComputerPlayer(Player):

    def generate_move(self, board, word_dictionary):
        word_to_play = ""
        col = 0
        row = 0
        direction = ""
        valid_word = False

        while not valid_word: 
            # Step 1: Extract and shuffle the list of words
            play_words = list(word_dictionary)
            random.shuffle(play_words)

            # Step 2: Iterate through the shuffled list to find a valid word
            for word in play_words:
                if word not in Word.played_words:
                    word_to_play = word
                    for row in range(15):
                        for col in range(15):
                            if board.board[row][col] != "":
                                if self.can_place_word(board, word_to_play, row, col, "right"):
                                    direction = "right"
                                    valid_word = True
                                    break
                                if self.can_place_word(board, word_to_play, row, col, "down"):
                                    direction = "down"
                                    valid_word = True
                                    break
                        if valid_word:
                            break
                if valid_word:
                    break

        return word_to_play, [col, row], direction

    def can_place_word(self, board, word, row, col, direction):
        word_length = len(word)

        if direction == "right":
            if col + word_length > 15:  # Ensure word fits horizontally
                return False
            for j in range(word_length):
                if not (board.board[row][col + j] == "   " or board.board[row][col + j] == f" {word[j]} "):
                    return False
            if not any(board.board[row][col + j] != "   " for j in range(word_length)):
                return False
        elif direction == "down":
            if row + word_length > 15:  # Ensure word fits vertically
                return False
            for j in range(word_length):
                if not (board.board[row + j][col] == "   " or board.board[row + j][col] == f" {word[j]} "):
                    return False
            if not any(board.board[row + j][col] != "   " for j in range(word_length)):
                return False

        return True
