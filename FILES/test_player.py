import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("TestPlayer")

    def test_initialize_rack(self):
        self.assertEqual(len(self.player.rack), 7)

    def test_refill_rack(self):
        self.player.rack = ['A', 'B', 'C']
        self.player.refill_rack()
        self.assertEqual(len(self.player.rack), 7)

if __name__ == '__main__':
    unittest.main()
