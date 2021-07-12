from random_word import *

r = RandomWords()
words_list = r.get_random_words()

print(words_list)


def loadWordsToFile(filename):
    with open(filename, 'w') as f:
        f.write('\n'.join(words_list))


def clearWordFile(filename):
    open(filename,"w").close()


loadWordsToFile("words.txt")
#clearWordFile("words.txt")
