#pycards1.py
# basic deck of cards and some playing around
import CardClasses as cc
import random

def main():

    #make our deck
    deck=cc.buildDeck()

    #Shuffle the deck
    random.shuffle(deck)

    #Count the number of 5 card permutations
    #print (len(( list(itertools.combinations(deck,5)))))

    #take the first five cards
    hand=cc.dealCards(deck,5)
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
          print('File:',cc.getFileName(val,suit))

    print(cc.scoreHand(hand,None))

#Run the main function
main()
