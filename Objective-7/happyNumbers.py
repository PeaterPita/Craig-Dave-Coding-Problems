num = int(input("Enter a 2 digit number"))
while True:
    print(num)
    if num == 1:
        print("That number was a happy number")
        break
    elif num == 4:
        print("That number is a sad number as it is stuck in an infinite loop")
        break
    numtemp = 0
    for _ in range(len(str(num))):
        numtemp += [int(digit) for digit in str(num)][_]**2
    num = numtemp
    
