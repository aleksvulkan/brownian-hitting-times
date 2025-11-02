import numpy as np

def simulate_brownian_paths(n_paths, n_steps, T):
    dt = T / n_steps
    dW = np.sqrt(dt) * np.random.randn(n_paths, n_steps)
    W = np.cumsum(dW, axis=1)
    W = np.hstack([np.zeros((n_paths, 1)), W])
    return W  # shape: (paths, steps+1)

def hitting_times(paths, barrier, T):
    n_paths, n_steps = paths.shape
    times = np.linspace(0, T, n_steps)

    hit_times = np.full(n_paths, np.inf)

    for i in range(n_paths):
        hit_idx = np.where(paths[i] >= barrier)[0]
        if len(hit_idx) > 0:
            hit_times[i] = times[hit_idx[0]]

    return hit_times