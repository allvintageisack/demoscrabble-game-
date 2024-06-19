import random

with open('dict.txt', 'r') as file:
    words = [word.strip().upper() for word in file.readlines()]

WORD_DICTIONARY = set(words)

LETTER_POINTS = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1,
    'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
    'Y': 4, 'Z': 10
}

class Tile:
    def __init__(self, letter, LETTER_POINTS={}):
        self.letter = letter
        self.LETTER_POINTS = LETTER_POINTS.get(letter, 0)

tiles = [Tile(letter, LETTER_POINTS) for letter in LETTER_POINTS.keys()]

class Tile_bag:
    def __init__(self, bag):
        self.bag = bag.copy()

    def refill(self):
        self.bag = tiles.copy()

    def draw_tiles(self, num_of_tiles):
        drawn_tiles = random.sample(self.bag, num_of_tiles)
        for tile in drawn_tiles:
            self.bag.remove(tile)
        return drawn_tiles

    def return_tiles(self, returned_tiles):
        self.bag.extend(returned_tiles)
