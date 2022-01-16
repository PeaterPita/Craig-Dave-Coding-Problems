while True:
    num = []
    for i in range(2):
        num.append ( int(input(f'Enter number {i+1}: ')) )
    print(f'{num[0]} + {num[1]} = {sum(num)}')