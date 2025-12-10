import math

# Valores de a, b y c
a = 2
b = -7
c = 3

# Fórmula general
x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

print("Solución 1:", x1)
print("Solución 2:", x2)
