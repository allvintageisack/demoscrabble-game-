import random

# These are the points for the letters that are included in the tile bag
letter_points = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1,
    'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
    'Y': 4, 'Z': 10, ' ': 0
}

# Tile frequency - handles the appearance of each letter in the tile bag
tile_frequencies = {
     'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4,
     'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1,
    'Y': 2, 'Z': 1, ' ': 2
 }


class Tile:
    def __init__(self, letter, letter_point):
        self.letter = letter
        self.points = letter_point.get(letter, 0)


tiles = [Tile(letter, letter_points) for letter in letter_points.keys()]


class TileBag:
    def __init__(self):
        self.bag = []
        self.initialize_bag()

    def initialize_bag(self):
        for letter, frequency in tile_frequencies.items():
            for _ in range(frequency):
                self.bag.append(Tile(letter, letter_points))

    def draw_tiles(self, num_of_tiles):
        drawn_tiles = random.sample(self.bag, num_of_tiles)
        for tile in drawn_tiles:
            self.bag.remove(tile)
        return drawn_tiles

    def return_tiles(self, returned_tiles):
        self.bag.extend(returned_tiles)
