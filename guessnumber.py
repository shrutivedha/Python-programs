# this guess the num game

import random

print('Hello, name?')
name = input()
print('Well,'+ name + ', I am thinking of num between 1 nand 20')
secret  = random.randint(1, 20)
print('numsecret' + str(secret))

for i in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secret:
        print('your guess is low')
    elif guess > secret:
        print('guess is too high')
    else:
        break

if guess == secret:
   print('Good job,' + name +', you guessed my num',+ str(guess) + ',guesses')
else:
    print('Nope the num i was thinking of was,' + str(secret))

print('you took,' + str(guess) + ',guesses')
