
def cmToin():
    cm = float(input("Cm To Inches: "))
    print(f'{cm}cm is {cm / 2.54:.2f}in')
def litersToGallons():
    liters = float(input("Liters To Gallons: "))
    print(f'{liters}l is {liters / 4.5:.2f}Gallons')
def kMToM():
    km = float(input("Kilometers To Miles: "))
    print(f'{km}Km is {km * (5/8):.2f}miles')
def litersToPints():
    liters = float(input("Liters To Pints: "))
    print(f'{liters}l is {liters * 1.75:.2f}Pints')
def kGToLbs():
    kg = float(input("Kg To Lbs: "))
    print(f'{kg}kg is {kg * 2.2:.2f}Lbs')


while True:
    choice = int(input("1. cm to in\n2. liters to gallons\n3. Km to m\n4. litre to pints\n5. Kg to lbs\nWhat do you want to do?: "))
    if choice in range(1,6): 
        if choice == 1: cmToin()
        elif choice == 2: litersToGallons()
        elif choice == 3: kMToM()
        elif choice == 4: litersToPints()
        elif choice == 5: kGToLbs()
