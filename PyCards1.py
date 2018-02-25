#pycards1.py
# basic deck of cards and some playing around

import itertools
import random
from collections import Counter

vals=['2','3','4','5','6','7','8','9','10','jack','queen','king','ace']
suits=['spades','hearts','diamonds','clubs']
deck=list(itertools.product(vals,suits))

#Shuffle the deck
random.shuffle(deck)

#Count the number of 5 card permutations
print (len(( list(itertools.combinations(deck,5)))))

#Shuffle the deck
random.shuffle(deck)

#take the first five cards
hand=deck[0:5]

#list of all the cards
print ('#cards: ',len(deck))
for val,suit in hand:
      print('The %s of %s' %(val,suit))




#make two dictionaries to count the numbera and the suits after making lists of either vals or suits
print("Use a dictionary")
nums=[val for val,suit in hand]
suits=[suit for val,suit in hand]
print(dict((val, nums.count(val)) for val in nums))
print(dict((suit, suits.count(suit)) for suit in suits))

#count the number of vals and suits using collections counter
print("Use a Counter")
valList=Counter([val for val,suit in hand])
for k,v in valList.items():
    print(k,v)
suitList=Counter([suit for val,suit in hand])
for k,v in suitList.items():
    print(k,v)

