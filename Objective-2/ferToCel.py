while True:
    temp = float(input("Enter the degrees in fahrenheit: "))
    print(f'{temp}F = {str((temp - 32) * (5/9))[:5]}')