import random

print 'Hello. What is your name?'
name = input()

print 'Well', + name + ', I am thinking of a # between 1 and 20'
secretNumber = random.randint(1, 20)

for guesses in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print 'Your guess is too low.'
    elif guess > secretNumber:
        print 'Your guess is too high.'
    else:
        break  # This condition for correct guess

if guess == secretNumber:
    print 'Dope!, ' + name + 'You guessed my number in ' + str(guesses) + ' guesses'
else:
    print 'Nope. The number I was thinking of was ' + int(secretNumber)

