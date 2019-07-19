import random

number = random.randint(1,10)
tries = 0

user = input("What is your username: ")

print("Hello %s" % user)

question = input("Do you want to play a game? ")

if question == 'no':
    print("oh. okay")
if question == 'yes':
    guess = int(input("Guess a number between 1 through 10: "))
    while guess != number:
        if guess < 1 or guess > 10:
            guess = int(input("You are out of range. Please try again. "))
        if guess < number:
            guess = int(input("too low, try again. "))
        if guess > number:
           guess = int(input("too high, try again. "))
        tries += 1
    if guess == number:
        tries += 1
        print("You're right! The number was %d" % number + " and it only took you %d tries" % tries)

