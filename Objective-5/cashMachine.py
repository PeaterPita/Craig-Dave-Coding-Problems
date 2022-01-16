print("You have a balance of £231")
while True:
    withdraw = int(input("How much do you want to withdraw: £"))
    if withdraw <= 230 and withdraw >= 10:
        if withdraw % 10 == 0:
            print(f'You have withdrew £{withdraw} from your account.')
        else:
            print("This machine only has £10 and £20 notes, please select a withdraw amount suitable.")
            
    else:
        print("You cant withdraw more than you have in your account, and you cant withdraw <£10")
        