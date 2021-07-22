import random

from random_word import *

r = RandomWords()
words_list = r.get_random_words()


def loadWordsToFile():
    with open("words.txt", 'w') as f:
        f.write(' '.join(words_list))


def clearWordFile():
    open("words.txt", "w").close()


def get_random_word():
    with open("words.txt", "r") as f:
        allText = f.read()
        words = list(map(str, allText.split()))
        return random.choice(words)


loadWordsToFile()
