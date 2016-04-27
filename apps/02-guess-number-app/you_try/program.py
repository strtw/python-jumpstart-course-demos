
import random

the_number = random.randint(0, 100)
print(the_number)

def guessmake():

    while True:
        try:
            guess = int(input("Guess a number between 0 and 100"))
            break
        except ValueError:
            print("Please enter a number")
    if guess == the_number:
        print( "You guessed correctly!" )
        return True
    if guess >= 100 or guess <= 0:
        print("Please choose a number between 0 and 100")
    elif guess < the_number :
        print("Your guess is lower than the number")
    elif guess > the_number:
        print("Your guess is higher than the number")

    guessmake()

guessmake()
