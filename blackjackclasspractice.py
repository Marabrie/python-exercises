import random

RANKS = [
    ('A',(1,11)),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
    (9,9),
    (10,10),
    ('J', 10),
    ('K', 10),
    ('Q', 10),
    ]

SUITS = [('hearts', '♥️'), ('diamonds', '♦️'), ('spades', '♠️'), ('clubs', '♣️')]


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def__str__(self):
        return f'{self.rank} {self.suit}'

class Deck:
    '''takes a list of suits and a list of ranks and generates one card of each combination'''
    def __init__(self, suits, ranks):
        self.cards = []
        suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit[1], rank[0]))

def shuffle(self):
    return random.shuffle(self.cards)

def deal(self, player, dealer):
    '''distributes two cards to each player's hand from the deck'''
    for person in [player, dealer]:
        while len(person.hand) < 2:
            person.hand.append(self.cards.pop())


class Player:
    def __init__(self, number, is_dealer=False):
        self.number = number
        self.hand = []
        self.is_dealer = is_dealer
        
        
    def__str__(self):
        if self.is dealer:
            return "Dealer"
        else: 
            return f'Player{self.number}' 
        
        
class Game:
    def__init__(self):
        self.winner = None
        self.rules =[]
        self.player= Player(1)
        self.dealer = Player(2, is_dealer = True)
        self.deck = Deck(SUITS, RANKS)
        self.deck.shuffle()
        self.deck.deal(self.player, self.dealer)

def play(self):
    while self.total_score(self.dealer) <= 17:
            self.hit(self.dealer)
            print("")
            for card in self.dealer.hand:
                print(card)
            print(self.total_score(self.dealer))

player_choice = None
while player_choice != 'S':
    player_choice = input("Would you like to Hit(H) or Stay(S)?")            
    if player_choice == 'H':
        self.hit(self.player)
    else:
        break

def hit(self,person):
    person.hand.append(self.deck.pop())

def total_score(self, person):
    total = 0
    for card in person.hand:
        if card.rank in ['J', 'Q', 'K']
            total += 10 
        elif card.rank in range(2,11):
            total += card.rank
        elif card.rank == 'A':
            total += 11
            if total > 21:
                total -= 10 
                
return total






# class Table:
#   pass

game = Game()
print("Player's hand")
for card in game.player.hand:
    print(card)

print("Dealer's hand")
for card in game.dealer.hand:
    print(card)

game.play 