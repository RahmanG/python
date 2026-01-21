# Brownian Motion in Finance

Brownian motion, specifically **Geometric Brownian Motion (GBM)**, is the standard mathematical model used to describe the evolution of stock prices and other financial assets over time. It forms the foundation of the Black-Scholes option pricing model.

## Key Concepts

### 1. Standard Brownian Motion (Wiener Process)
A Standard Brownian Motion, denoted as $W_t$, is a continuous-time stochastic process with the following properties:
- $W_0 = 0$
- It has independent increments: $W_{t+u} - W_t$ is independent of past values.
- It has Gaussian increments: $W_{t+u} - W_t \sim N(0, u)$ (normally distributed with mean 0 and variance $u$).
- It has continuous paths.

### 2. Geometric Brownian Motion (GBM)
Stock prices cannot be negative, so we model the *logarithm* of the stock price using Brownian motion. The Stochastic Differential Equation (SDE) for a stock price $S_t$ is:

$$ dS_t = \mu S_t dt + \sigma S_t dW_t $$

Where:
- **$S_t$**: Stock price at time $t$
- **$\mu$ (mu)**: Drift coefficient (expected return)
- **$\sigma$ (sigma)**: Volatility (standard deviation of returns)
- **$dt$**: Small time step
- **$dW_t$**: Increment of a Wiener process (random shock)

### 3. Solution to the SDE
The analytical solution to the GBM equation is:

$$ S_t = S_0 \exp\left( (\mu - \frac{1}{2}\sigma^2)t + \sigma W_t \right) $$

This equation allows us to simulate future stock price paths.

## Why is it important?
- **Option Pricing**: It is the underlying assumption for the Black-Scholes formula.
- **Risk Management**: Used to calculate Value at Risk (VaR) and simulate portfolio scenarios.
- **Algorithmic Trading**: Helps in modeling price movements and mean reversion strategies (using related processes like Ornstein-Uhlenbeck).
