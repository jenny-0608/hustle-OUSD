# guessing game, Jannfier Calmo Ranmirez

# allows library to be added for python to know to randomize a number
import random

# generates random number to try and guess
def generate_random_number():
    return random.randint (1, 100)

 # print(generate_random_number())

# gets the users guess on what the randomly generted number is.
def get_user_guess():

# gives the user 3 tries to input a guess that fits the range 
# of 1 through 100 each time the question is asked
    for user_input in range(3):
        guess = int(input("enter your number guess!:"))
        if guess >= 1 and guess <= 100:
            return guess
        else:
            print("guess is not in range of 1 through 100")

# actual function for playing the game
def play_guessing_game():
    secret_number = generate_random_number()
    guess = get_user_guess()
    attempts = 0
    number = False
    while number == False:

# checks how close your guess is from the actual number as well as
# the amount of tries it takes you to get the number
# each false allows for the user to input new guesses and try again
# break ensures that the game_loop function can run
        if guess > secret_number:
            attempts = attempts +1
            print("your guess is too high, try again.")
            number = False
            guess = get_user_guess()
        elif guess < secret_number:
            attempts = attempts +1
            print("your guess is too low, try again.")
            number = False
            guess = get_user_guess()
        else:
            print("you got it!")
            print (f"it took you {attempts} attempt/s before you got the right answer!")
            number = True
            break

#function to start up the game as well as asks if user wants to play again 
# or quit after completing a round.
def game_loop():
    while True:
        play_guessing_game()
        loop = input("do you want to play again? yes/no: ")
        if loop == "yes":
            continue
        elif loop == "no":
            print("thank you for playing!")
            break
        else:
            print ("uh oh, invalid word, press control + c, type clear, and run again to play.\nTo stop dont do the last part!")

#starts up
if __name__ == "__main__": 
    game_loop()