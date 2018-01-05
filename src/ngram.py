import sys
import os
import random
from nltk import ngrams

def weighted_choice(choices):
    total = sum(w for c, w in choices.items())
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices.items():
        if upto + w > r:
            return c
        upto += w


def ngram_init():
    # N Gram value
    n = 5
    counts = {}
    
    directory = "../input/"
    filename = "../input/test.txt"
    text = open(filename).read().split()
    
    n_grams = ngrams(text, n)
    for gram in n_grams:
        if gram in counts:
            counts[gram] += 1
        else:
            counts[gram] = 1
    return counts
    
    #for filename in os.listdir(directory):
    #    text = open(filename).read().split()
    #
    #    n_grams = ngrams(text, n)
    #    for gram in n_grams:
    #        if gram in counts:
    #            counts[gram] += 1
    #        else:
    #            counts[gram] = 1

def ngram(counts, word):
    result = ""
    for i in range(random.randint(5,15)):
        result = result + " " + word
        choices = {k:v for k,v in counts.items() if k[0] == word}
        word = weighted_choice(choices)[1]
    return result
