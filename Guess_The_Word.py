import random

#variable that holds a list of secret words
words = ["something", "better", "other", "random", "python", "eggplant", "supercalifragilisticexpialidocious"]

#a function that randomly choses a word in the words variable list and returns it
def choice():
    return random.choice(words)

#variable that holds the secret word the user has to guess and its list variant for dashes
secret_word = choice()
secret_word_list = list(secret_word)
secret_list = ["-" for i in secret_word]    

#printing the inital dashes
dashes = "".join(secret_list)
print(dashes)

#function that asks the user for a guess. it must be a lowercase letter and anything other than that will 
#make you reinput a guess until it is a lowercase letter
def get_guess():
    while True:
        user_guess = input("Guess: ")
        if len(user_guess) != 1:
            print("Your guess must have exactly one character!")
        elif user_guess.isdigit():
            print("Your guess must be a letter!")
        elif not user_guess.islower():
            print("Your guess must be a lowercase letter!")
        elif len(user_guess) == 1 and user_guess.lower() == user_guess:
            break
    return user_guess

def update_dashes(word, dash_now, user_guess):
    if user_guess in secret_word:
        for index, character in enumerate(secret_word):
            if character == user_guess:
                secret_list[index] = character
            dashes = "".join(secret_list)
        return dashes
    if user_guess not in secret_word:
        for index, character in enumerate(secret_word):
            if character == user_guess:
                secret_list[index] = character
            dashes = "".join(secret_list) 
        return dashes

#vairables that lets the user keep on guessing
user_still_guessing = True
guesses_left = 10
new_guess_list = []

#while statement that gets a guess equal to the amount of the guesses_left variable and if the 
#user_still_guessing variable is still guessing. If the user
#inputted a letter thats in the word, it goes into the letter and saves it. If all the letters
#have been guessed or if there are no more guesses left, then the guesses end.
while user_still_guessing and guesses_left > 0:
    guess = get_guess()
    print(str(guesses_left) + " incorrect guesses left.")
    if guess in secret_word:
        new_guess_list = update_dashes(secret_word, dashes, guess)
        print("That letter is in the word!")
        print(new_guess_list)
    else:
        print("That letter is not in the word.")
        new_guess_list = update_dashes(secret_word, dashes, guess)
        print(new_guess_list)
        guesses_left = guesses_left - 1
    if secret_word == new_guess_list:
        user_still_guessing = False

#guess that turns the guesses the user has made into one single string
final_guess = "".join(new_guess_list)

#if statement that checks if the user didn't get the secret word right
if final_guess == secret_word:
    print("Congrats! You win. The word was: " + secret_word + ".")
else:
    print("You lose. The word was: " + secret_word + ".")