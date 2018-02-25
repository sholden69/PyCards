#pycards1.py
# basic deck of cards and some playing around

import itertools
import random
from collections import Counter

#make our deck
vals=['2','3','4','5','6','7','8','9','10','jack','queen','king','ace']
suits=['spades','hearts','diamonds','clubs']
deck=list(itertools.product(vals,suits))

#Shuffle the deck
random.shuffle(deck)

#Count the number of 5 card permutations
#print (len(( list(itertools.combinations(deck,5)))))

#take the first five cards
hand=deck[0:5]

#some test data
# Straight flush
#hand=[('6', 'clubs'), ('7', 'clubs'), ('8', 'clubs'), ('9', 'clubs'), ('10', 'clubs')]
# Straight
#hand=[('6', 'clubs'), ('7', 'hearts'), ('8', 'clubs'), ('9', 'spades'), ('10', 'diamonds')]
#four of a kind
#hand=[('6', 'clubs'), ('6', 'hearts'), ('6', 'spades'), ('6', 'diamonds'), ('10', 'clubs')]
#three of a kind
#hand=[('6', 'clubs'), ('6', 'hearts'), ('6', 'spades'), ('7', 'diamonds'), ('10', 'clubs')]
#full house
#hand=[('6', 'clubs'), ('6', 'hearts'), ('6', 'spades'), ('7', 'diamonds'), ('7', 'clubs')]
#two pairs
#hand=[('6', 'clubs'), ('6', 'hearts'), ('ace', 'spades'), ('7', 'diamonds'), ('7', 'clubs')]



#list of all the cards
#print ('#cards: ',len(deck))
print("Here are your cards:")
for val,suit in hand:
      print('The %s of %s' %(val,suit))

#make two dictionaries to count the numbera and the suits after making lists of either vals or suits
nums=[val for val,suit in hand]
suits=[suit for val,suit in hand]
numsDict=dict((val, nums.count(val)) for val in nums)
suitsDict=dict((suit, suits.count(suit)) for suit in suits)

#count the number of vals and suits using collections counter
#print("Use a Counter")
#valList=Counter([val for val,suit in hand])
#for k,v in valList.items():
#    print(k,v)
#suitList=Counter([suit for val,suit in hand])
#for k,v in suitList.items():
#    print(k,v)

#count how many combos we have - max four of a kind
cardCount=[0,0,0,0]
for n in range (4):
    for i,cnt in numsDict.items():
       if cnt==n+1:
           cardCount[n]+=1

#sequence test. Nice use of map + join to coonvert each digit to a string and look for 5 in a row
seqDict=dict((val,0) for val in vals)
for n in nums:
    seqDict[n]=1
isSeq='11111' in ''.join(map(str,seqDict.values()))


# Now work out what hand we've got
if cardCount[3]==1:  #I've got four of a kind
    print("*** four of a kind")
elif cardCount[2]==1:  #I#ve got at least three of a kind
    if cardCount[1]==1:
        print("*** full house")
    else:
        print("*** three of a kind")
else:
    if cardCount[1]==2:
        print("*** two pairs")
    elif cardCount[1]==1:
        print("*** one pair")
    elif isSeq:
        if len(suitsDict)==1:
            print("*** straight flush")
        else:
            print("straight")
    else:
          print("*** a high")

