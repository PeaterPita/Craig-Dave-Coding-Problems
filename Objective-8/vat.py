while True:
    def VATcalc(price): return price * 0.2
    
    price = float(input("What is the price of the item youre buying: £"))
    print(f"The price of the item is: £{price}\nVAT is: £{VATcalc(price)}")