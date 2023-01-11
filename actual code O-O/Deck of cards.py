from random import shuffle
suits = ["♥", "♦", "♣", "♠"]
deck=[]
for suit in suits:
    for i in range(1,14):
        deck.append(str(i)+suit)
deck.append("Joker")
deck.append("King")
deck.append("Queen")
print(shuffle(deck))