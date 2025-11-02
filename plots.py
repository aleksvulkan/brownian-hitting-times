import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import levy

def plot_hist_vs_theory(hit_times, barrier):
    hit_times = hit_times[np.isfinite(hit_times)]
    t = np.linspace(1e-4, max(hit_times), 500)
    pdf = levy.pdf(t, scale=barrier**2)

    plt.hist(hit_times, bins=50, density=True, alpha=0.5)
    plt.plot(t, pdf, linewidth=2)
    plt.title(f"Hitting time distribution for barrier = {barrier}")
    plt.xlabel("t")
    plt.ylabel("Density")
    plt.show()