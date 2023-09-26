import random 

def guess_the_number():
    guess = 0
    attempts = 0

    print("Welcome to Guess The Number")
    print("from 1 to 10")

    while True:
        number = random.randint(1,10)
        if (attempts == 3):
            break
        guessedNumber = int(input('Guess a number between [1-10]: '))
        # Check for correct answer and increment the attempt counter by one
        if (guessedNumber > number or guessedNumber < number ):
            print ("Wrong! Try again!")
        else :
            print ('Correct!')
guess_the_number()