while True:
    stats = ["name", "attack", "defense"]
    for _ in range(3): stats[_] = str(input(f"Enter the {stats[_]} of the character: "))
    with open("rpg.txt", "a") as f: 
        for i in stats: f.write(i + "|")
        f.write("\n")