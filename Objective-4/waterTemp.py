temp = float(input("What is the temperature of the water: "))
print("Frozen" if temp <= 0 else "Boiling" if temp >= 100 else "Not boiling or frozen")