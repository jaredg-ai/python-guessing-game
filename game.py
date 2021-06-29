import random
secret=random.randint(1,100)

hello = "Hello"
name = input("What is your name?\n")
thinking = "I'm thinking of a number between 1 and 100."
greeting = hello + ' ' + name + ', ' + thinking
print(greeting)

for guesstaken in range(1,100):
    print("\ntry to guess my number.")
    guess=int(input())
    if (guess < secret):
        print("your guess is too low")
    elif (guess > secret):
        print("your guess is too high")
    else:
        break

if (guess == secret):
    print("you win!")
    print("your guess is correct " + str(guess))
    print("you took " +str(guesstaken) +" guesses")
