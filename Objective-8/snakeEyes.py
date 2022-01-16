import random
curPlayer = 1 ## play 1 = 1, player 2 = -1
bank = [99,0,0]
runningTot = [99,0,0]


def swapPlayer(curPlayer):
    print("\n\n\n")
    rollDice(curPlayer * -1)

def gambleOrBank(curPlayer, rollTot):
    while True:
        choice = int(input("You didnt roll a 1, would you like to roll the dice again? Or bank your total. \n1. Roll Again\n2. Bank total"))
        if choice == 1 or choice == 2:
            if choice == 1:
                print("You have chosen to roll again")
                print()
                rollDice(curPlayer)
            elif choice == 2:
                bank[curPlayer] += rollTot
                print(f'You have chosen to bank your total, this means your bank now has {bank[curPlayer]}')
                swapPlayer(curPlayer)
                
                
        else:
            print("Pick either option 1 to gamble, or option 2 to bank")
            continue

def rollDice(curPlayer):
    if curPlayer == -1:
        print("Players 2 turn")
    else:
        print("Players 1 turn")
    roll1, roll2 = random.randint(1,6), random.randint(1,6)
    print(f'Played rolled a {roll1} and a {roll2}, for a total of {roll1 + roll2}')
    if roll1 == 1 or roll2 == 1:
        if roll1 == 1 and roll2 == 1:
            bank[curPlayer] = 0
            print(f'Players bank has been reset as a double 1 was rolled.')
        runningTot[curPlayer] = 0
        print(f'Players running total was reset as 1 was rolled.')
        swapPlayer(curPlayer)
    else:
        print(f'THis now means that the running total is {runningTot[curPlayer] + roll1 + roll2}')
        gambleOrBank(curPlayer, roll1 + roll2)
            
            
            
rollDice(curPlayer)
        
    
