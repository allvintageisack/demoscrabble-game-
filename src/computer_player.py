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
            word_to_play = self.find_valid_word(word_dictionary)
            if not word_to_play:
                print(f"{self.name} cannot find a valid word to play.")
                return None, None,None
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

            if word_to_play in Word.played_words:
                valid_word = False

        return word_to_play, [col, row], direction
    
    def word_from_rack(self,word,letters):
        rack = letters.copy()
        for i in word:
                
                if i in rack:
                    rack.remove(i)
                else:
                    return False
        return True    

    def find_valid_word(self,word_dictionary):
        letters_on_rack = [tile.letter for tile in self.rack]
        random.shuffle (letters_on_rack)

        for word in word_dictionary:
            if self.word_from_rack(word,letters_on_rack):
                return word
            elif word.strip() == "":
                break

        return " "    
            


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
