import random
while True:
    num1, num2 = random.randint(1,10), random.randint(1,10)
    answer = num1 + num2
    print("Correct" if int(input()) == answer else "Incorrect")
    