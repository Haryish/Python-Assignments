# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 13:23:48 2023

@author: haryi
"""

import string
from collections import Counter


def paragraph_stats(paragraph):
    # remove special characters except apostrophe and hyphen
    special_chars = string.punctuation.replace("'", "").replace("-", "")
    paragraph = paragraph.translate(str.maketrans("", "", special_chars))

    # count vowels, consonants, digits and special symbols
    vowels = sum([1 for char in paragraph.lower() if char in "aeiou"])
    consonants = sum([1 for char in paragraph.lower() if char.isalpha() and char not in "aeiou"])
    digits = sum([1 for char in paragraph if char.isdigit()])
    symbols = sum([1 for char in paragraph if char in special_chars])

    # count words and sentences
    words = len(paragraph.split())
    sentences = len(paragraph.split("."))

    # count word frequency and palindrome words
    word_count = Counter(paragraph.split())
    palindrome_count = sum([1 for word in word_count if word == word[::-1]])

    # count anagrams
    def get_char_counts(word):
        return tuple(sorted(Counter(word.lower()).items()))

    anagram_count = sum([1 for word, count in word_count.items() if count > 1 and get_char_counts(word) in get_char_counts_anagrams])

    return {
        "vowels": vowels,
        "consonants": consonants,
        "digits": digits,
        "symbols": symbols,
        "words": words,
        "sentences": sentences,
        "frequency": word_count,
        "palindrome": palindrome_count,
        "anagrams": anagram_count,
    }


# precompute character count tuples for each anagram group
get_char_counts_anagrams = {}
for word in set(paragraph.split()):
    char_counts = get_char_counts(word)
    if char_counts not in get_char_counts_anagrams:
        get_char_counts_anagrams[char_counts] = []
    get_char_counts_anagrams[char_counts].append(word)


paragraph = "There is no strife, no prejudice, no national conflict in outer space as yet. Its hazards are hostile to us all. Its conquest deserves the best of all mankind, and its opportunity for peaceful cooperation many never come again. But why, some say, the moon? Why choose this as our goal? And they may well ask why climb the highest mountain? Why, 35 years ago, fly the Atlantic? Why does Rice play Texas? We choose to go to the moon. We choose to go to the moon in this decade and do the other things, not because they are easy, but because they are hard, because that goal will serve to organise and measure the best of our energies and skills, because that challenge is one that we are willing to accept, one we are unwilling to postpone, and one which we intend to win, and the others, too. -- John F Kennedy"

stats = paragraph_stats(paragraph)
print(stats)
