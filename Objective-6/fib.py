from math import sqrt
def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

for _ in range(20): print(f'Term {_+1}: {int(F(_))}')