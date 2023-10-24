#%%
import random
#%%
my_fruit_list = ["Mango", "Pineapple", "Grape", "Melon", "Apple"]

random_fruit_choice = random.choice(my_fruit_list) 

#%%
def check_guess(random_fruit_choice):
    random_fruit_choice = random_fruit_choice.lower()
    if letter_guess in random_fruit_choice:
        print(f"Good guess! {letter_guess} is in the word")
    else:
        print(f"Sorry, {letter_guess} is not in the word. Try again")

#%%
def ask_for_input():
    letter_guess = input("Enter a letter")
    if len(letter_guess) == 1 and letter_guess.isalpha():
        print("Good guess bro!")
    else:
        print("Uh oh! That is not a valid input, please try again")



#%%
while True:
    guess_a_letter = input("Guess a letter")
    if len(guess_a_letter) == 1 and guess_a_letter.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character")

    
# %%
ask_for_input()
# %%
