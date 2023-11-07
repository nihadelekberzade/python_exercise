import random

number = random.randint(1, 9)
print('num' + str(number))
guessed = False
num_of_guesses = 0
while not guessed:
    num_of_guesses+=1
    guess = int(input('Your guess ?'))
    if guess < number:
        print('Try higher')
    elif guess > number:
        print('Try lower')
    else:
        guessed = True
        print('You won')
        print('Number of guesses:' + str(num_of_guesses))
