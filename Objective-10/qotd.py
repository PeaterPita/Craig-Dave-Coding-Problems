import random 
with open("quotes.txt", "r") as f: print(random.choice(f.readlines())) 