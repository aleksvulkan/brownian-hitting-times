import numpy as np
import matplotlib.pyplot as plt
from simulation import simulate_brownian_paths, hitting_times
from plots import plot_hist_vs_theory

def main():
    n_paths = 5000        # number of Brownian paths
    n_steps = 1000        # steps per path
    T = 1.0               # time horizon
    barrier = 1.0         # hitting level a > 0

   
    print(f"Simulating {n_paths} paths...")
    paths = simulate_brownian_paths(n_paths, n_steps, T)

    
    plt.figure(figsize=(8,4))
    time_grid = np.linspace(0, T, n_steps + 1)
    for i in range(100):
        plt.plot(time_grid, paths[i])
    plt.axhline(barrier, color='red', linestyle='--', label='Barrier')
    plt.title("Sample Brownian Motion Paths")
    plt.xlabel("t")
    plt.ylabel("B(t)")
    plt.legend()
    plt.show()

    
    hit_times = hitting_times(paths, barrier, T)
    finite_hits = hit_times[np.isfinite(hit_times)]
    hit_ratio = len(finite_hits) / n_paths

    print(f"Fraction of paths that hit barrier: {hit_ratio:.4f}")

    
    plot_hist_vs_theory(hit_times, barrier)

if __name__ == "__main__":
    main()