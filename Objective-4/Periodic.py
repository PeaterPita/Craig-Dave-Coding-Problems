   ## ["LI", "LITHIUM", "ALKALI METALS", 6.94]
##      symbol name     group           weight
elements = [["LI", "LITHIUM", "ALKALI METALS", 6.94], ["NA", "SODIUM", "ALKALI METALS", 22.99], ["K", "POTASSIUM", "ALKALI METALS", 39.0], ["RB", "RUBIDIUM", "ALKALI METALS", 85.46], ["CS", "CAESIUM", "ALKALI METALS", 132.91], ["FR", "FRANCIUM", "ALKALI METALS", 223], 
            ["HE", "HELIUM", "NOBLE GASES", 4.00], ["NE", "NEON", "NOBLE GASES", 20.18], ["AR", "ARGON", "NOBLE GASES", 39.94], ["KR", "KRYPTON", "NOBLE GASES", 83.79], ["XE", "XENON", "NOBLE GASES", 131.29], ["RN", "RADON", "NOBLE GASES", 222]]



while True:
    userElement = input("Enter the name, symbol, group or atomic weight of the element you want.")
    for _ in range(len(elements)):
        if userElement.upper() in elements[_]:
            print(f'Name: {elements[_][1]}\nWeight: {elements[_][3]}')