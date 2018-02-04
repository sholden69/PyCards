#pycards1.py
# basic deck of cards and some playing around

import itertools
import random

vals=['2','3','4','5','6','7','8','9','10','jack','queen','king','ace']
suits=['spades','hearts','diamonds','clubs']
deck=list(itertools.product(vals,suits))
random.shuffle(deck)
print ('#cards: ',len(deck))
for val,suit in deck:
      print('The %s of %s' %(val,suit))
