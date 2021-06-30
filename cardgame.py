# Make a card game in Python like the cardgame War

# cards
# deck
# 2 players
player1 = "Dolly"
player2 = "Miley"

# - Make a deck 
deck = []

# - in that deck, put 52 cards, 2 - A of each suit ♥️ ♦️ ♠️ ♣️
ranks = [2,3,4,5,6,7,8,9, "J", "Q", "K", "A"]
suits = ['♥️', '♦️', '♠️', '♣️']

for suit in suits:
    for rank in ranks:
        deck.append((rank.suit))

for card in deck:
    print(card)

# - deal cards out to each player, one at time until all are gone 
# - players throw down top card face up
# - if cards are the same value
# deal out three more cards then one more face up, compare again
# - If not the same, player with the higher card value gets the pile
# - play stops when one pplayer runs out of cards, other player wins
