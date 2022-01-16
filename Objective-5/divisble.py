while True:
    fn, sn = str(input("Enter two numbers to see if they are exactly divisble. Numbers should be seperated ny a space: ")).split(' ')
    print("Error 0 is not allowed" if fn == "0" or sn == "0" else "Number 2 is exactly divisible by number 1" if int(sn) % int(fn) == 0 else f"The numbers have a reminder off {int(sn) // int(fn)}")