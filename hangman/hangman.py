import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-'in word or ' 'in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # keep track of the letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # keep track of what user have guessed

    lives = 6

    while len(word_letters) > 0 and lives > 0:   # Stop iteration if len(word_letters) == 0 or lives > 0
        # letters used
        print('You have ', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is:
        answer_letters = [letter if letter in used_letters else '-' for letter in word]
        print('The answer: ', ' '.join(answer_letters))

        user_guess = input("\nGuess a letter: ").upper()
        if user_guess in alphabet - used_letters:
            used_letters.add(user_guess)
            if user_guess in word_letters:
                word_letters.remove(user_guess)
            else:
                lives -= 1
                print("Letter is not in the word.")
        elif user_guess in used_letters:
            print("You've used this letter already. Guess another one.")
        else:
            print("Invalid letter. Try again.")
    if lives == 0:
        print("Sorry you\'re dead. The answer is ", word, "...")
    else: 
        print("Yay! You guessed the answer, ", word, "!!")

hangman()