import numpy as np
from quantlab import QuantLab

from scipy.integrate import quad

class NumericalIntegrationCall(QuantLab):
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

    def forward(self, S0: np.ndarray):
        """
        S0: current price of the asset
        Given any current price and the model's parameter, we can estimate the Price of European call option, using Numerical Integration
        """
        S0 = np.asarray(S0, dtype=np.float64)

        def integrand(z):
            """
            calculates the integrand, and i'll use scipy's integrate.quad to eval to this integrand
            """
            ST = S0 * np.exp((self.r - 0.5 * (self.sigma**2))* self.T + self.sigma * np.sqrt(self.T) * z)
            payoff = max(ST - self.K, 0.0)
            pdf = np.exp(-0.5 * z**2) / (np.sqrt(2 * np.pi)) # Standard normal probability density
            return payoff * pdf

        expected_payoff, _ = quad(
            integrand,
            -np.inf,
            np.inf,
        )

        C0 = np.exp(-self.r * self.T) * expected_payoff
        return C0


if __name__ == "__main__":
    model = NumericalIntegrationCall(
        K=100,
        sigma=0.20,
        T=1.0,
        r=0.05,
    )

    price = model.forward(S0=100)
    print(f"Numerical Integration's Option Price: {price:.6f}")
