#Chat.gpt was used as a resource to help create this code
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root

def equation1(x):
    """Define the first equation."""
    return x - 3 * np.cos(x)

def equation2(x):
    """Define the second equation."""
    return np.cos(2 * x) * x**3

def find_unique_roots_in_range(equation, x_range):
    """
    Find unique roots of an equation within a specific range.

    Parameters:
    :param equation: The equation for which roots are to be found.
    :param x_range: The range of x values to search for roots.
    :returns: A sorted list of unique roots rounded to 3 decimals.
    """
    roots = set()  # Use a set to store unique roots
    for x_guess in x_range:
        sol = root(equation, x_guess)
        if sol.success:
            roots.add(round(sol.x[0], 3))
    return sorted(list(roots))

# Find roots of each equation in the range -3 to 3
roots_equation1 = find_unique_roots_in_range(equation1, np.linspace(-3, 3, 1000))
roots_equation2 = find_unique_roots_in_range(equation2, np.linspace(-3, 3, 1000))

# Find intersection points in the range -3 to 3
def intersection_equations(x):
    """Define the system of equations for finding intersection points."""
    return equation1(x) - equation2(x)

# Use a larger range for initial guesses
all_guesses = np.linspace(-3, 3, 1000)
intersection_points = find_unique_roots_in_range(intersection_equations, all_guesses)

# Print the values of the roots and intersection points
print("Roots of Equation 1:", roots_equation1)
print("Roots of Equation 2:", roots_equation2)
print("Intersection Points:", intersection_points)

# Plot the equations and intersection points
x_values = np.linspace(-3, 3, 1000)
plt.plot(x_values, equation1(x_values), label='x - 3*cos(x)')
plt.plot(x_values, equation2(x_values), label='cos(2*x)*x^3')
plt.scatter(roots_equation1, np.zeros_like(roots_equation1), color='red', marker='o', label='Roots of Equation 1')
plt.scatter(roots_equation2, np.zeros_like(roots_equation2), color='blue', marker='x', label='Roots of Equation 2')
plt.scatter(intersection_points, equation1(intersection_points), color='green', marker='*', label='Intersection Points')
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
plt.title('Equations and Intersection Points')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
