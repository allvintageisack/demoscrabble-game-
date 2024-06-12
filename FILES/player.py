from tile_and_bag import WORD_DICTIONARY
import random
from string import ascii_uppercase
from collections import Counter
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.rack = []
        self.initialize_rack()

    def initialize_rack(self, num_tiles=7):
        while len(self.rack) < num_tiles:
            word = random.choice(list(WORD_DICTIONARY))
            scrambled_word = list(word)
            random.shuffle(scrambled_word)
            self.rack.extend(scrambled_word)
            self.rack = self.rack[:num_tiles]  # Ensure rack has exactly num_tiles

    def refill_rack(self):
        self.initialize_rack()

    def remove_tiles(self, tiles):
        for tile in tiles:
            if tile in self.rack:
                self.rack.remove(tile)

    def display_rack(self):
        rack_counter = Counter(self.rack)
        rack_display = ", ".join(f"{letter}({count})" for letter, count in rack_counter.items())
        return f"{self.name}'s Rack: {rack_display}"

    def update_score(self, word_score):
        self.score += word_score

    def get_score(self):
        return self.score

    def shuffle_rack(self):
        random.shuffle(self.rack)

    def set_rack(self, rack):
        self.rack = rack