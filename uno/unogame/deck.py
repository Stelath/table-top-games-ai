import numpy as np

class Deck():
    def __init__(self) -> None:
        self.deck = np.zeros(108)
        self.new_deck()
        # self.card_colors = {'red': 16, 'green': 32, 'blue': 64, 'yellow': 128}
    
    def new_deck(self, cards_in_play = [], shuffle = True):
        new_deck = []
        # for key, color in self.card_colors.items(): 
        for i in range(4):
            new_deck.append(i * 13)
            for j in range(2):
                for n in range(1, 13):
                    new_deck.append((i * 13) + n)
        for i in range(4):
            new_deck.append(52)
        for i in range(4):
            new_deck.append(53)
        
        for card in cards_in_play:
            new_deck.remove(card)
        
        self.deck = np.array(new_deck)
        if shuffle: np.random.shuffle(self.deck)
        
        return self.deck
    
    def draw_card(self):
        if len(self.deck):
            card = self.deck[0]
            self.deck = np.delete(self.deck, 0)
        else:
            card = 54
        return card