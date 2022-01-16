bottles = int(input("How many bottles are there on the wall: "))
for n in range(bottles,0, -1): print(f"{n} green" + (" bottles " if n >= 2 else " bottle ") + "sitting on the wall") 