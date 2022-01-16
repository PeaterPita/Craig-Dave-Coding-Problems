nums = int(input("How many numbers do you want to input?: "))
numbers = []
for _ in range(nums): numbers.append(int(input(f"number {_+1}: ")))
print(f'Total: {sum(numbers)}\nAdverage: {sum(numbers) / nums}')