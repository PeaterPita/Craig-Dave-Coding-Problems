import math
while True:
    dia = float(input("What is the diameter of the circle:  "))
    arc = float(input("What is the size of the arc angle:  "))
    
    print(f'Based on user input:\nRadius: {dia / 2}\nArea: {str(math.pi * (dia/2)**2)[0:6]}\nCircumference: {str(math.pi * dia)[0:6]}\nArc Length: {str((math.pi * dia * arc) / 360)[0:6]}')