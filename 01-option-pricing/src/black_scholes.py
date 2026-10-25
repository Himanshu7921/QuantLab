import numpy as np
from scipy.stats import norm
from quantlab import QuantLab

class BlackScholesCall(QuantLab):
    """
    A very basic Implementation of Black Scholes Equation
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
        Given any current price and the model's parameter, we can estimate the Price of European call option, using Black Scholes Call Equation
        """
        S0 = np.asarray(S0, dtype=np.float64)

        d1 = (np.log(S0 / self.K) + self.T * (self.r + (self.sigma ** 2) / 2)) / (self.sigma * np.sqrt(self.T))
        d2 = d1 - self.sigma * np.sqrt(self.T)

        C0 = S0 * norm.cdf(d1) - self.K * np.exp(-self.r * self.T) * norm.cdf(d2)

        # 1st term is, Expected value of the asset over time period T, where the call option makes money, i.e S_T > K
        # 2nd term is, weighted average of Strike Price where the call option makes the money, i.e S_T > K
        return C0



if __name__ == "__main__":
    S0 = 100
    K = 100
    T = 1.0
    r = 0.05
    sigma = 0.20

    black_scholes_model = BlackScholesCall(K = K, T = T, r = r, sigma = sigma)
    price = black_scholes_model(S0)

    print(f"Black Scholes Option Price = INR {price:.4f}")