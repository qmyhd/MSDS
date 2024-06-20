import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print(f"matplotlib version: {matplotlib.__version__}")
print(f"numpy version: {np.__version__}")
print(f"pandas version: {pd.__version__}")

# Solution for Problem 1
def problem_1():
    return sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
print("Problem 1 solution:", problem_1())

# Solution for Problem 2
def problem_2():
    a, b = 1, 2
    total = 0
    while a <= 4000000:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total
print("Problem 2 solution:", problem_2())

# Solution for Problem 3
def problem_3():
    def largest_prime_factor(n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
        return n
    return largest_prime_factor(600851475143)
print("Problem 3 solution:", problem_3())

# Generate and plot Binomial distribution
binom_dist = np.random.binomial(n=10, p=0.5, size=1000)
plt.hist(binom_dist, bins=10, alpha=0.7, color='blue')
plt.title('Binomial Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Generate and plot Poisson distribution
poisson_dist = np.random.poisson(lam=3.0, size=1000)
plt.hist(poisson_dist, bins=10, alpha=0.7, color='green')
plt.title('Poisson Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Generate and plot Normal distribution
normal_dist = np.random.normal(loc=0.0, scale=1.0, size=1000)
plt.hist(normal_dist, bins=30, alpha=0.7, color='red')
plt.title('Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

