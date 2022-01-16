file = "db.txt"
def addProduct():
    with open(file, "a") as f:
        while True:
            item = str(input("Enter the product name with thr price seperated by a comma, (speaker,49.99). \"EXIT\" To quit:    "))
            if item.upper() != "EXIT":
                f.write(item + "\n")
            else:
                break
            
            
def outPutAll():
    with open(file, "r") as f:
        for _ in f.readlines():
            print(f'{(_.split(","))[0]}:    £{(_.split(","))[1]}')

def findProduct():
    with open(file, "r") as f:
        while True:
            item = str(input("Enter the name of the product you want to search for: "))
            for _ in f.readlines():
                if item in _:
                    print(f'The price of /{item}\\ is £{_.split(",")[1]}')
                    exit()
                    
            
            else:
                print("That isnt an item in the databse")
                exit()
    


while True:
    choice = int(input("1.Add product to database\n2.Output all products\n3.Find a product price by name\nUser: "))
    addProduct() if choice == 1 else outPutAll() if choice == 2 else findProduct() if choice == 3 else print("Please pick either option 1,2 or 3\n\n\n")
    