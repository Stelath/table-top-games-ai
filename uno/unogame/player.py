class Player():
    def __init__(self, p_id) -> None:
        self.p_id = p_id
        self.hand = []
    
    def new_card(self, card):
        self.hand.append(card)
    
    def play_card(self, card):
        self.hand.remove(card)
    
    def get_hand(self):
        return self.hand