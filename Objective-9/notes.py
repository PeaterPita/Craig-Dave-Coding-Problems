notes = ["-" for i in range(10)]
def menu():
    while True:
        for i, _ in enumerate(notes): print(f'{i+1}. {_}')
        choice = int(input("Enter the number of the note that you want to change: "))
        if choice in range(1, 11): return choice
        else: print("Please enter a number 1-10")
def editNote(note):
    notes[note - 1] = str(input(f"Edit note {note}:\n>>>"))
        
while True:
    editNote(menu())