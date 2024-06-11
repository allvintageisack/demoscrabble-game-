import unittest
from unittest.mock import patch
from player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("John")

    def test_initialize_player(self):
        self.assertEqual(self.player.name, "John")
        self.assertEqual(len(self.player.rack), 7)
        self.assertEqual(self.player.score, 0)

    def test_remove_tiles(self):
        original_rack = self.player.rack[:]
        tiles_to_remove = ['A', 'B']
        tiles_in_rack = [tile for tile in tiles_to_remove if tile in self.player.rack]
        self.player.remove_tiles(tiles_to_remove)
        for tile in tiles_in_rack:
            self.assertNotIn(tile, self.player.rack)
        expected_rack_len = len(original_rack) - len(tiles_in_rack)
        self.assertEqual(len(self.player.rack), expected_rack_len)

    @patch('player.random.sample')
    def test_refill_rack(self, mock_sample):
        mock_sample.return_value = ['X', 'Y', 'Z']
        original_rack_len = len(self.player.rack)
        self.player.refill_rack(3)
        self.assertEqual(len(self.player.rack), original_rack_len + 3)
        self.assertIn('X', self.player.rack)
        self.assertIn('Y', self.player.rack)
        self.assertIn('Z', self.player.rack)

    def test_update_score(self):
        self.player.update_score(10)
        self.assertEqual(self.player.score, 10)
        self.player.update_score(15)
        self.assertEqual(self.player.score, 25)

if __name__ == '__main__':
    unittest.main()