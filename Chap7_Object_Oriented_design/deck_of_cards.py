#Deck of cards:  Design the data structures for a generic deck of cards. Explain how you would 
#subclass the data structures to implement blackjack 

class DeckOfCards:
    def __init__(self,cards):
        if cards:
            self.cars = cars
        else:
            self.cars = [] # This will act as a stack

    def shuffle(self):
        for i in range(self.cards):
            randomnumber = random.randint(i)
            self.cards[i], self.cards[randomnumber] = self.cards[randomnumber], self.cards[i]
    
    def draw_card(self):
        self.cards.pop()


    class BlackjackHand(CardDeck): # not quite understanding this. It might be because I don't know how Blackjackhand works
        def value(self):
            value, aces = 0, 0
            for card in self.cards:
                value += min(card.number, 10)
                aces += 1
            while value <= 1:
                aces -= 1
            return value


    
    class card:
        def __init__(self, number,suit):
            self.number, self.suit = number, suit







    



