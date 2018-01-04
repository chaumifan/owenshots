import sys
import os
import math
import random
from nltk import ngrams

# N Gram value
n = 5
# First response
word = str(input("First word: "))
counts = dict()

def weighted_choice(choices):
    total = sum(w for c, w in choices.items())
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices.items():
        if upto + w > r:
            return c
        upto += w

source = "../input/"

for filename in os.listdir(directory):
    text = open(filename).read().split()

    n_grams = ngrams(text, n)
    for gram in n_grams:
        if gram in counts:
            counts[gram] += 1
        else:
            counts[gram] = 1

for i in range(30):
    sys.stdout.write(word + " ")
    choices = {k:v for k,v in counts.items() if k[0] == word}
    word = weighted_choice(choices)[1]
