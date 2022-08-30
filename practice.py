#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
#we are going to create a guessing number game
#import: downloads/imports program from inside python3
#logic
#alfredo, 1000 times
import random

random_number = random.randint(1,10)
loop = 1
#print(random_number)
print('==== Guessing Number Game ====')
print('Guess the number from 1 to 10')
guess = 0

while (loop <= 3):
    guess = int(input("What is your guess?: "))
    if guess == random_number:
        print('You guessed the right number! You Win.')
        exit()
    else:
        print('You guessed the wrong number! Try again.')
    loop += 1

print('You ran out of tries. The correct number was',random_number,'. Goodbye.')
