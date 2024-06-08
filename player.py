import random
from string import ascii_uppercase

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.rack = []
        self.initialize_rack()

    def initialize_rack(self, num_tiles=7):
        """
        Initialize the player's rack with random tiles from the tile bag.
        """
        tile_bag = list(ascii_uppercase) * 2
        self.rack = random.sample(tile_bag, num_tiles)

    def refill_rack(self, num_tiles):
        """
        Refill the player's rack with new tiles from the tile bag.
        """
        tile_bag = list(ascii_uppercase) * 2
        available_tiles = [tile for tile in tile_bag if tile not in self.rack]
        new_tiles = random.sample(available_tiles, num_tiles)
        self.rack.extend(new_tiles)

    def remove_tiles(self, tiles):
        """
        Remove tiles from the player's rack.
        """
        for tile in tiles:
            if tile in self.rack:
                self.rack.remove(tile)

    def display_rack(self):
        """
        Display the current tiles on the player's rack.
        """
        print(f"{self.name}'s Rack: {', '.join(self.rack)}")

    def update_score(self, word_score):
        """
        Update the player's score based on the points earned from a word.
        """
        self.score += word_score

    def get_score(self):
        """
        Get the player's current score.
        """
        return self.score