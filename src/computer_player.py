from src.player import Player

import random

from src.word import Word




class Computer (Player):

    def generate_move(self,board,word_dictionary):


        word_to_play = ""

        col = 0

        row = 0

        direction = ""



        valid_word=False

        while not valid_word:

           

            word_to_play= random.choice(list(word_dictionary))#randomly selects a word from the wor_dictionary


            for row in range (15):

                for column in range(15):

                    if  board.board [row][column] != "" : #checks if the place on the board is empty

                        if self.can_place_word(board,word_to_play, row,column,"right"): #checks if the word can be placed to the right from the current position

                       

                            direction = "right"

                            valid_word = True

                            break

                        if self.can_place_word(board,word_to_play, row,column,"down"): #checks if the word can be placed down from the current position

                       

                            direction = "down"

                            valid_word = True

                            break

           

            if valid_word:

                break


        if word_to_play in Word.played_words: #checks if the word had been played do vali

            valid_word = False

            return word_to_play,[row, column],direction

       

    def can_place_word (self,board,direction,word,row,column):

        length_of_chosen_word= len(word) #checkks the length of the chosen word


        if direction == "right":                      

            if column + length_of_chosen_word > 15:

                return False

            for i in range (length_of_chosen_word): #checks cells avaialabilty

                if not (board.board)[row][column + i] == " " or (board.board)[row][column + i] == f" {word[i]} " :

                    return False

                if not any(board.board[row+1][column] != ""

                    for i in range (length_of_chosen_word)):

                    return False


   

        elif direction == "down":

              if row + length_of_chosen_word > 15:

                return False

              for i in range(length_of_chosen_word):  # checks cells availability

                if not (board.board)[row + i][column] == " " or (board.board)[row + i][column] == f" {word[i]} ":

                 return False

              if not any(board.board[row + i][column] != ""

               for i in range(length_of_chosen_word)):

                  return False