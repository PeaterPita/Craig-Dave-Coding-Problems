import random
while True:
    roll = int(input("What number sided dice do you wanna roll?: "))
    print("Roll: ", random.randint(1, roll))