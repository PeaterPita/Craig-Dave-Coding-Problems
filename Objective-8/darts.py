points, total = 501, 0
for _ in range(3): total += int(input("How many points did you get from dart throw {_}: "))
if points - total == 0: print("Player 1 wins the game")
elif points - total >= 1: points - total; print(f"New Score: {points - total}")
