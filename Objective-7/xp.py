xp, rank = 0, 1
while True:
    xp +=  int(input("How much xp did you earn last game?: "))
    print(f'Your total xp now is: {xp}')
    rank = 2 if xp >= 200 and rank == 1 else rank
    print("You have reached Corporal" if rank == 2 else "")
    