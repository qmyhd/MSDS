import numpy as np
import matplotlib.pyplot as plt

# Parameters
p = 0.5
Ns = [10, 50, 100, 1000]

# Plotting
for N in Ns:
    binom_dist = np.random.binomial(n=N, p=p, size=10000)
    mean = N * p
    stddev = np.sqrt(N * p * (1 - p))
    normal_dist = np.random.normal(loc=mean, scale=stddev, size=10000)
    
    plt.figure(figsize=(10, 6))
    
    plt.hist(binom_dist, bins=50, alpha=0.5, label=f'Binomial (N={N}, p={p})', density=True)
    plt.hist(normal_dist, bins=50, alpha=0.5, label=f'Normal (mean={mean}, stddev={stddev})', density=True)
    
    plt.title(f'Binomial vs Normal Distribution for N={N}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    
    plt.savefig(f'binomial_vs_normal_N{N}.png')
    plt.show()