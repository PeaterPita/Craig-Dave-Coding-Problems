import random
numToGuess, guesses = random.randint(1,100), 1
while True:
    guess = int(input("What is your guess?: "))
    if guess == numToGuess: break
    else: print("You guessed too high" if guess > numToGuess else "You guessed too low")
    guesses += 1
print(f'Well done you guessed the number correctly. In {guesses} guesses')