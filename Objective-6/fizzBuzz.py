for _ in range(1, 101):
    fizz = "fizz" if _ % 3 == 0 else ""
    buzz = "buzz" if _ % 5 == 0 else ""
    print(f'{fizz}{buzz}' or _)
    