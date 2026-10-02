import random
suits = ['Spades','Clubs','Hearts','Diamonds']
ranks = ['A', 'K', 'Q', 'J','2', '3', '4' , '5', '6', '7', '8', '9', '10']
#cardsV1 = []
cards = []
threshold = 21

#for rank in ranks:
#    for suit in suits:
#        cardsV1.append(suit + " of " + rank )

for rank in ranks:
    for suit in suits:
        cards.append([suit , rank])

#print(cardsV1)
#print("Number of cards in the deck are ", len(cardsV1))
print(cards)
print("Number of cards in the deck are ", len(cards))

def shuffle(self):
    random.shuffle(self)

def deal(number):
    cards_dealt = []
    for i in range(number):
        cards_dealt.append(cards.pop())
    return cards_dealt
    

shuffle(cards)
print("shuffled deck =" ,cards)
cards_dealt = deal(2)
print("\n the cards dealt are ", cards_dealt)

card1 = cards_dealt[0]
card2 = cards_dealt[1]

face1 = card1[0]
value1 = card1[1]

face2 = card2[0]
value2 = card2[1]
calculatedvalue1 = 0
calculatedvalue2 = 0
if value1 == "A":
    calculatedvalue1 = 11
elif value1 == "K" or value1 == "Q" or value1 == "J":
    calculatedvalue1 = 10
else:
    calculatedvalue1 = value1
if value2 == "A":
    calculatedvalue2 = 11
elif value2 == "K" or value2 == "Q" or value2 == "J":
    calculatedvalue2 = 10    
else:
    calculatedvalue2 = value2


calculated_rank_dict_1 ={"value" :value1, "calculation" : calculatedvalue1}
calculated_rank_dict_2 ={"value" :value2, "calculation" : calculatedvalue2}


print( value1,calculatedvalue1)
print( value2,calculatedvalue2)

total1 = calculatedvalue1 + calculatedvalue2

if total1 >= 21:
    print("you lost value exceeds 21", total1)

ask = print( input("do you wish to add another card y/n?")) 

if ask == "Y":
    added_card = deal(1)




#print(card1, card2)

#suit = suits[2]

#rank = "K"
#value = 10
#suits.append("snakes")

#print("Your card is : "+ rank + " of " + suit)

#for suit in suits:
#    print(suit)

