import random
import string
import words


class Hangman:
    def __init__(self):
        self.pickedWord = words.get_random_word().upper()  # Mot à deviner
        self._pickedWord_letters = set(self.pickedWord)  # Les lettres qui composent le mot
        self._alphabet = set(string.ascii_uppercase)
        self._used_letter = set()
        self._hangman_status = 0

    def get_hangman_status(self):
        return self._hangman_status

    def set_hangman_status(self, hangman_status):
        self._hangman_status = hangman_status

    def start_game(self):
        print(self.pickedWord)
        while len(self._pickedWord_letters) > 0 and self._hangman_status < 6:
            print('Status', self._hangman_status)
            print('User letter : ', ' '.join(self._used_letter))
            print('Current word : ', [letter if letter in self._used_letter else '-' for letter in self.pickedWord])

            user_letter = input('Guess a letter : ').upper()
            if user_letter in self._alphabet - self._used_letter:
                self._used_letter.add(user_letter)  # Ajoute la lettre utilisé
                if user_letter in self._pickedWord_letters:  # Vérifie si cette lettre est dans le mot à deviné
                    self._pickedWord_letters.remove(user_letter)
                else:
                    self._hangman_status = self._hangman_status + 1
                    print("Letter not in the word")
            elif user_letter in self._used_letter:
                print("Already used")
            else:
                print('Invalid letter')
        if self._hangman_status == 6:
            print("No more life")
        else:
            print("GG !")

        print("The word was " + self.pickedWord)

    @property
    def used_letter(self):
        return self._used_letter


if __name__ == '__main__':
    h = Hangman()
    h.start_game()
