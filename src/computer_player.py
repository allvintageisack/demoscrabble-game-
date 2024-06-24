from src.player import Player
import random
from src.word import Word

class ComputerPlayer(Player):

    def generate_move(self, board, word_dictionary):
        valid_word = False

        while not valid_word:
            word_to_play = random.choice(list(word_dictionary))
            word_length = len(word_to_play)

            if len(Word.played_words) == 0:
                direction = random.choice(["right", "down"])
                row, col = 7, 7

                if (direction == "right" and col + word_length <= 15) or (direction == "down" and row + word_length <= 15):
                    valid_word = True
            else:
                for row in range(15):
                    for col in range(15):
                        if board.board[row][col] != "   ":
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

            if word_to_play in Word.played_words:
                valid_word = False

        return word_to_play, [row, col], direction

    def can_place_word(self, board, word, row, col, direction):
        word_length = len(word)

        if direction == "right":
            if col + word_length > 15:
                return False
            for j in range(word_length):
                if not (board.board[row][col + j] == "   " or board.board[row][col + j] == f" {word[j]} "):
                    return False
            if not any(board.board[row][col + j] != "   " for j in range(word_length)):
                return False
        elif direction == "down":
            if row + word_length > 15:
                return False
            for j in range(word_length):
                if not (board.board[row + j][col] == "   " or board.board[row + j][col] == f" {word[j]} "):
                    return False
            if not any(board.board[row + j][col] != "   " for j in range(word_length)):
                return False

        return True
