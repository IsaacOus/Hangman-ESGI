# import random
#
# WORDS = ("python", "froid", "empreinte", "difficile", "animal",  "douche", "dire", "canard", "voiture", "voler",
#          "habiter", "saluer", "habitation", "jouer", "vieillir", "animer", "carabine", "sorcier", "bougie",
#          "contenir", "commentaire", "discuter", "gouter", "vendeuse", "tremblement", "aribitre", "loto", "location",
#          "Engagement", "Quinze", "Incertain", "Acupuncture", "Cargaison", "Province", "Buffle", "Kamikaze")
# word = random.choice(WORDS)
#
# def loadWordsToFile():
#     with open("words.txt", 'w') as f:
#         f.write(word)
#
#
# def clearWordFile():
#     open("words.txt", "w").close()
#
#
# def get_random_word():
#     with open("words.txt", "r") as f:
#         allText = f.read()
#         words = list(map(str, allText.split()))
#         return random.choice(words)
#
#
# loadWordsToFile()
import urllib.request, random
import unidecode

def get_random_word():
    page = urllib.request.urlopen('http://www.pallier.org/extra/liste.de.mots.francais.frgut.txt')
    liste_mots = page.readlines()
    mot = random.choice(liste_mots)
    word = mot.decode('UTF-8').split()[0]
    page.close()
    with open("words.txt", 'a') as f:
        f.write(word)

    print(mot.decode('UTF-8').split()[0])
    mot_sans_accent = unidecode.unidecode(word)
    return mot_sans_accent