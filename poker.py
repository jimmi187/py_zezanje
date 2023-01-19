from random import shuffle

class Card:
    def __init__(self, suit, value):
        self.suit=suit
        self.value=value
    
    def __repr__(self) -> str:
        return("{} of {}".format(self.value,self.suit))
    
class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = sum([map(lambda x: [map(lambda y: Card(x, y),values)],suits)],[])
    
    def _deal(self, num):
        num_of_cards=len(self.cards)
        if num_of_cards == 0:
            raise ValueError("All cards have been dealt")
        if num_of_cards<num:
            cards = self.cards[num_of_cards-num:]
            self.cards = self[:num_of_cards-num]
            return cards

    def deal_card(self):
        self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)
    
    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")

        shuffle(self.cards)
        return self

