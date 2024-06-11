import random
from collections import Counter

# Assuming WORD_DICTIONARY is a global variable containing valid words or letters
WORD_DICTIONARY = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.rack = []
        self.initialize_rack()

    def initialize_rack(self, num_tiles=7):
        # Use letters from the dictionary and shuffle them
        tile_bag= list("".join(WORD_DICTIONARY))
        random.shuffle(tile_bag)
        self.rack = random.sample(tile_bag, num_tiles)

    def refill_rack(self, num_tiles):
        tile_bag = list("".join(WORD_DICTIONARY))
        available_tiles = [tile for tile in tile_bag if tile not in self.rack]
        new_tiles = random.sample(available_tiles, num_tiles)
        self.rack.extend(new_tiles)

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