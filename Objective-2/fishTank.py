from functools import reduce
dimension = ["length","depth","height"]
while True:
    for _ in range(3):
        dimension[_] = int(input(f'Enter the {dimension[_]} of the fishtank to the nearest cm: '))
    liters = reduce(lambda x, y: x*y, dimension)
    print(f'To fill the tank you will need:\nLiters: {liters}\nGallons: {liters * 0.264172}')