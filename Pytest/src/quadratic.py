import math

def solve_quadratic_formula(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("All coefficients must be of type float or int!")
    if a == 0:
        raise ValueError("Cannot solve quadratic formula with a = 0!")
    
    D = b**2 - 4 * a * c
    if D < 0:
        raise ValueError("Cannot solve quadratic formula with negative discriminant!")
    
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    return x1, x2