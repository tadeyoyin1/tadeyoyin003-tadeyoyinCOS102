import numpy as np

A = int(input("what is your value for A:"))
B = int(input("What is your value for B:"))
C = int(input("What is your value for c:"))
D= int(input("What is your value for D:"))
coefficients = [A, B, C, D]


roots = np.roots(coefficients)

print("The roots of the equation are:", roots)

