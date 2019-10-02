#!/usr/bin/env python3
import sys, string

# The shared mutable data
data = []
words = []
word_freqs = []

def read_file(path_to_file):
    """ Takes file path and assigns contents to global variable data"""
    global data
    with open(path_to_file) as f:
        data = data + list(f.read())


def scan():
    """ Scan file for words, filling global variable words"""
    global data
    global words
    data_str = ''.join(data)
    words = words + data_str.split()


def frequencies():
    """ Creates a list of pairs associating words with frequencies"""
    global words
    global word_freqs
    for w in words:
        keys = wd[0] in word_freqs
        if word in keys:
            word_freqs[keys.index(word)][1] += 1
        else:
            word_freqs.append([word, 1])

# Main function

read_file(sys.argv[1])
scan()
frequencies()

for tf in word_freqs[0:25]:
    print(tf[0], ' - ', tf[1])
