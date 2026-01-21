import numpy as np
import matplotlib.pyplot as plt

def simulate_gbm(S0, mu, sigma, T, dt):
    """
    Simulate a Geometric Brownian Motion path.
    
    Parameters:
    S0    : Initial stock price
    mu    : Drift coefficient (expected return)
    sigma : Volatility (standard deviation)
    T     : Time horizon (in years)
    dt    : Time step
    
    Returns:
    t     : Array of time steps
    S     : Array of stock prices
    """
    N = int(T / dt)
    t = np.linspace(0, T, N)
    
    # Standard Brownian Motion (Wiener Process)
    # dW ~ N(0, dt) => W is cumulative sum of dW
    # We generate N-1 increments because S[0] is fixed
    dW = np.random.normal(0, np.sqrt(dt), N-1)
    W = np.insert(np.cumsum(dW), 0, 0) # W_0 = 0
    
    # Geometric Brownian Motion Solution:
    # S_t = S_0 * exp((mu - 0.5 * sigma^2) * t + sigma * W_t)
    
    # We can also compute it iteratively:
    # S_{t+1} = S_t * exp((mu - 0.5 * sigma^2) * dt + sigma * dW_t)
    
    # Using the exact solution formula for vectorization:
    drift = (mu - 0.5 * sigma**2) * t
    diffusion = sigma * W
    S = S0 * np.exp(drift + diffusion)
    
    return t, S

def main():
    # Parameters
    S0 = 100      # Initial price
    mu = 0.05     # 5% expected return
    sigma = 0.2   # 20% volatility
    T = 1.0       # 1 year
    dt = 0.001    # Daily steps (roughly)
    
    # Simulate
    np.random.seed(42) # For reproducibility
    t, S = simulate_gbm(S0, mu, sigma, T, dt)
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(t, S, label=f'GBM (mu={mu}, sigma={sigma})')
    plt.axhline(S0, color='r', linestyle='--', label='Initial Price')
    plt.title('Geometric Brownian Motion Simulation')
    plt.xlabel('Time (Years)')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.grid(True)
    
    output_file = 'gbm_simulation.png'
    plt.savefig(output_file)
    print(f"Simulation complete. Plot saved to {output_file}")
    print(f"Initial Price: {S0:.2f}")
    print(f"Final Price: {S[-1]:.2f}")

if __name__ == "__main__":
    main()
