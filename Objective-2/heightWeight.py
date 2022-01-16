while True:
    hW = str(input("Enter your height (in inches) and your weight (in stones) seperated by a space: ")).split(' ')
    print(f'Height: {hW[0]}inches To {str(float(hW[0]) * 2.54)[:5]}cm\nWeight: {hW[1]} stone To {str(float(hW[1]) * 6.346)[:5]}Kg')