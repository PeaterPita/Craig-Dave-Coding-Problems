
while True:
    marks = []
    for _ in range(3):
        marks.append(int(input(f'Enter in test {_+1} marks: ')))
    print(f'The adverage of all 3 tests is: {sum(marks) / 3}')