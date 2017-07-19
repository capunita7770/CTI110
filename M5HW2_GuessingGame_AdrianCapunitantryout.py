# Guessing Game
# 6/26
# CTI-110 M5HW2 - Random Number Guessing Game
# Adrian Capunitan
#

import random

guessesTaken = 0



def main():
    number = random.randint(1, 100)
    print('Hello! What is your name?')
    myName = input()

print('Well, ' + myName + ', I am thinking of a number between 1 and 100.')

while guessesTaken < 10:
    print('Please take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Too low, try again.') # There are eight spaces in front of print.
    elif guess > number:
        print('Too high, try again.')
    elif guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
