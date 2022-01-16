while True:
    hoursToys = str(input("Enter the number of hours you worked (rounded up to nearest whole number) and the number of toy cars you made seperated by a space: ")).split(' ')
    print(f'You should be paid: £{str( ((int(hoursToys[0]) * 1200) + (int(hoursToys[1]) * 60)) /100 )}')
    
    
    ##             
