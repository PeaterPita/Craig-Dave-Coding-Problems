marks = ["analysis", "design", "implementation", "evaluation"]
grades = [2,4,13,22,31,41,54,67,80]

def findNearest(num):
    for _ in range(len(grades)):
        if num - grades[_] <= 0: return _

for i in range(4):
    marks[i] = int(input(f"Enter the marks awarded for {marks[i]}: "))
totmarks = sum(marks)
print(f'''The total marks awarded was: {sum(marks)}
      This means your grade is: {"U" if totmarks < 2 else findNearest( totmarks )}
      Needed marks to get next grade: {grades[findNearest( totmarks )] - totmarks}''')

    
    
      
      