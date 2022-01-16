import itertools
bal = ["Current Balance", "Desired Amount"]
for i in range(2): bal[i] = float(input(f"Enter your {bal[i]}: £"))


for i in itertools.count():
    if bal[0] >= bal[1]:
        break
    else:
        bal[0] *= 1.04
        print(f"After {i+1} years your balnce will be £{bal[0]:.2f}")