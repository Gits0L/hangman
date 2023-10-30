#%%
import random
#%%
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list 
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_"for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, word_guessed):
        self.word_guessed = self.word_guessed.lower()
        if self.word_guessed in self.word:
            print(f"Good guess! {self.word_guessed} is in the word")
        
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
                    print(f"Word guessed so far: {' '.join(self.word_guessed)}")
            self.num_letters -= 1
       
        else:
            self.num_letters -= 1
            print(f" sorry {letter} is not in the word")
            print(f"You have {self.num_lives} left")
    


    def ask_for_input(self):
        while True:
            guess = input("Guess a letter")
            if len(guess) != 1 and not self.letter_guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character")
            elif self.guess in self.list_of_guesses:
                print("You already tried that letter!")
            else: 
                check_guess(self.word_guessed)
                self.list_of_guesses.append(guess)

# %%
