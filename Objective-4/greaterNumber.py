nums = []
for _ in range(2):
    nums.append(int(input(f"Enter number {_+1}:  ")))
print('The greater of the 2 numbers entered is', "neither, they are the same" if nums[0] == nums[1] else f"{nums[0]}" if nums[0] > nums[1] else f"{nums[1]}")