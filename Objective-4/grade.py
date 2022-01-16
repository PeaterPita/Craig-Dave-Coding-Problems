grade = float(input("Enter the grade out of 100: "))
print("DISTINCTION" if grade >= 80 else "MERIT" if grade >= 60 else "PASS" if grade >= 40 else "FAIL")