from unogame import Deck
import unittest
import logging


class TestDeck(unittest.TestCase):
    def test_new_deck(self):
        deck = Deck()
        new_deck = deck.new_deck(shuffle=False)
        print(f"Deck String: {new_deck}")
        self.assertEqual(len(new_deck), 108)
    
    def test_draw_card(self):
        deck = Deck()
        for card in deck.deck:
            deck.draw_card()
        
        self.assertEqual(deck.draw_card(), 54)
        
        deck.new_deck()
        self.assertEqual(deck.deck[0], deck.draw_card())

if __name__ == '__main__':
    level = logging.DEBUG
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)
    unittest.main()
