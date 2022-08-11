from .deck import Deck
from .player import Player

class Uno():
    def __init__(self, p_count=4) -> None:
        self.deck = Deck()
        
        self.pile = []
        
        self.draw_num = 0
        self.change_color = False
        self.reverse = False
        
        
        self.current_player = 0
        self.players = []
        for p in range(p_count):
            self.players.append(Player(p))
        
        self.deck.new_deck()
        
        for i in range(7):
            for player in self.players:
                player.new_card(self.deck.draw_card())
    
    def reset_deck(self):
        cards_in_play = []
        for player in self.players:
            for card in player.get_hand():
                cards_in_play.append(card)
        self.deck.new_deck(cards_in_play)
    
    def get_pile(self):
        return self.pile
    
    def get_players(self):
        return self.players
    
    def get_current_cards(self):
        current_player = self.players[self.current_player]
        return current_player.get_hand()
    
    def convert_card(self, num):
        """
        Card Type Dict:
        Red - 00010000 - 16
        Green - 00100000 - 32
        Blue - 01000000 - 64
        Yellow - 10000000 - 128
        
        Number Cards: 0-9
        Skip: 10
        Reverse: 11
        Draw 2: 12
        Wild: 13
        Draw 4 Wild: 14
        """
        
        # if num in [13,14]:
        #     card = num - 39
        # else:
        card_types = [16, 32, 64, 128]
        card_type = card_types[int(num / 13)]
        card = (num % 13) + card_type
        return card
            
    def play_card(self, played_card, current_player):
        current_player.play_card(played_card)
        self.pile.insert(0, played_card)
        
        card_num = self.convert_card(played_card) & 15
        
        if card_num == 11:
            self.draw_num += 2
        elif card_num == 12:
            self.reverse = not self.reverse
        elif played_card == 52:
            self.change_color = True
        elif played_card == 53:
            self.change_color = True
            self.draw_num = 4
        
        if len(current_player.get_hand()) <= 0:
            return 3
        
        self.current_player += 1
        
        return 2
    
    def next_turn(self, played_card):
        current_player = self.players[self.current_player]
        
        bin_played_card = self.convert_card(played_card)
        bin_pile_card = self.convert_card(self.pile[0])
        
        if self.change_color and played_card > 54:
            self.pile.insert(0, [16, 32, 64, 128][played_card - 55])
            return 2
        elif played_card > 54 or (self.change_color and played_card <= 54):
            return 0
        
        
        if played_card == 54:
            card = self.deck.draw_card()
            if card == 54:
                self.reset_deck()
                card = self.deck.draw_card()
            current_player.new_card(card)
            return 1
        elif played_card in current_player.hand and (not len(self.pile) or bin_played_card & bin_pile_card >= 16 or bin_played_card & 15 == bin_pile_card & 15 or played_card in [52,53]):
            return self.play_card(played_card, current_player)
        
        return 0
    