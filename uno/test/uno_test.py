from unogame import Uno
import unittest
import logging


class TestDeck(unittest.TestCase):
    def test_turns(self):
        uno = Uno(2)
        cards = uno.get_current_cards()
        print(cards)
        # uno.next_turn()
        # self.assertEqual(len(new_deck), 108)
    
    def test_convert_card(self):
        uno = Uno(2)
        self.assertEqual(uno.convert_card(0), 16)
        self.assertEqual(uno.convert_card(4), 20)
        self.assertEqual(uno.convert_card(12), 28)
        self.assertEqual(uno.convert_card(16), 35) # Green 3
        self.assertEqual(uno.convert_card(32), 70) # Blue 6

if __name__ == '__main__':
    level = logging.DEBUG
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)
    unittest.main()
