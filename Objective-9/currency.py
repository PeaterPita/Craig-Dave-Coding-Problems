conversion = [["USD", 1.34], ["EURO", 1.17], ["AUS", 1.83], ["YEN", 152.84]]
while True:
    gbp, conv = str(input("Avalible currency: USD, EURO, AUS, YEN\nHow much money do you have in GBP followed by the currency to convert too\n>£")).split(" ")
    for _ in range(len(conversion)):
        if conv.upper() == conversion[_][0]: index = _ ;break
    if index >= 0: break
print(f'£{gbp} is worth {float(gbp) * conversion[index][1]} {conv} with an exchange rate of {str(conversion[index][1])}')