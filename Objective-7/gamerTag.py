while True:
    gamerTag = str(input("Enter in your desired gamertag. It must be less than 15 characters buy longer than 3: "))
    if len(gamerTag) in range(3,16): break
    else: print("Your gamertag must be longer than 3 characters and less than 15")
print("That is a valid gamer tag")