#pycards1.py
# basic deck of cards and some playing around

import itertools
import random
from collections import Counter


def buildDeck():
#create a new 52 deck from vals * suits
   return list(itertools.product(vals,suits))

def dealCards (deck, numCards):
#return the first numCards cards from the top of the deck
    hand=deck[0:numCards]
    deck=deck[numCards:len(deck)]  #drop numCards from the deck
    return (hand)

def getFileName( val,suit):
# Given a {val,suit} tuple, spit out the PNG filename
  return val+"_of_"+suit+".png"

def scoreHand( communityCards,holeCards):
# Returns the best 5 card hand from a set of hand + hole cards
    # make two dictionaries to count the numbers and the suits after making lists of either vals or suits
    nums = [val for val, suit in communityCards]   #make a list of vals only
    numsDict = dict((val, nums.count(val)) for val in nums)

    suits = [suit for val, suit in communityCards]  #make a list of suits only
    suitsDict = dict((suit, suits.count(suit)) for suit in suits)

    # count the number of vals and suits using collections counter
    # valList=Counter([val for val,suit in hand])
    # for k,v in valList.items():
    #    print(k,v)
    # suitList=Counter([suit for val,suit in hand])
    # for k,v in suitList.items():
    #    print(k,v)

    # count how many combos we have - max four of a kind
    cardCount = [0, 0, 0, 0]  #count of 1 of kind, 2 of kind etc
    for n in range(4): # look for 1s first, then 2s etc
        for i, cnt in numsDict.items(): #now check each item in the list of counts
            if cnt == n + 1:   #if the count matches what we are looking for then increment the result array
                cardCount[n] += 1

    # sequence test. Nice use of map + join to convert each digit to a string and look for 5 in a row
    seqDict = dict((val, 0) for val in vals)  #Make a dict for each value and initialise to zero
    for n in nums:  # where we have a number set the seqDict to 1
        seqDict[n] = 1
    # look for 5 adjacent 1's ie a sequence of 5 in a row
    # join the empty string to str applied via map to all of seqDict to make a string.
    isSeq = '11111' in ''.join(map(str, seqDict.values()))

    # Now work out what hand we've got
    if cardCount[3] == 1:  # I've got four of a kind
        return "*** four of a kind"
    elif cardCount[2] == 1:  # I've got at least three of a kind
        if cardCount[1] == 1:
            return"*** full house"
        else:
            return "*** three of a kind"
    else:
        if cardCount[1] == 2:
            return "*** two pairs"
        elif cardCount[1] == 1:
            return "*** one pair"
        elif isSeq:
            if len(suitsDict) == 1:
                return "*** straight flush"
            else:
                return "straight"
        else:
            return "*** a high"


def main():
    global vals
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    global suits
    suits = ['spades', 'hearts', 'diamonds', 'clubs']

    #make our deck
    deck=buildDeck()

    #Shuffle the deck
    random.shuffle(deck)

    #Count the number of 5 card permutations
    #print (len(( list(itertools.combinations(deck,5)))))

    #take the first five cards
    hand=dealCards(deck,5)
    print("deck length",len(deck))

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
          print('File:',getFileName(val,suit))

    print(scoreHand(hand,None))

#Run the main function
main()
