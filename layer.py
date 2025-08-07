from card import Card

class Layer:
    def __init__(self):
        self.cards = []
        self.layer_behind = None
        self.layer_ahead = None

    def add_card(self,title):
        card = Card(title)
        self.cards.append(card)
        return True