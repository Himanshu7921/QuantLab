import numpy as np
from quantlab import QuantLab

class MonteCarloCall(QuantLab):
    """
    A very basic Implementation of Numerical Integration method
    """
    def __init__(self, K: float, sigma: float, T: float, r: float):
        """
        K: Strike price
        sigma: volatility in the asset
        T: Remaining Time period in years
        r: risk free interest rate
        """
        super().__init__()
        self.K = K
        self.r = r
        self.sigma = sigma
        self.T = T

    def forward(self, S0: np.ndarray, steps: int):
        """
        S0: current price of the asset
        Given any current price and the model's parameter, we can estimate the Price of European call option, using Numerical Integration
        """
        S0 = np.asarray(S0, dtype=np.float64)
        z = np.random.randn(steps) # Z drawn from Stand Normal Gaussian
        ST = S0 * np.exp((self.r - 0.5 * (self.sigma**2) )* self.T + self.sigma * np.sqrt(self.T) * z)
        payoff = np.maximum(ST - self.K, 0)

        expected_payoff = np.mean(payoff)
        C0 = np.exp(-self.r * self.T) * expected_payoff
        return C0


if __name__ == "__main__":
    model = MonteCarloCall(
        K=100,
        sigma=0.20,
        T=1.0,
        r=0.05,
    )

    price = model.forward(S0=100, steps = 1000000)
    print(f"Monte carlo's Option Price: {price:.6f}")
