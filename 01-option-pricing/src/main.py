import numpy as np
import pandas as pd
from black_scholes import BlackScholesCall
from numerical_integration import NumericalIntegrationCall
from montecarlo import MonteCarloCall

def main():
    # Shared parameters
    S0 = 100.0
    K = 100.0
    T = 1.0
    r = 0.05
    sigma = 0.20

    bs = BlackScholesCall(K=K, sigma=sigma, T=T, r=r)
    ni = NumericalIntegrationCall(K=K, sigma=sigma, T=T, r=r)
    mc = MonteCarloCall(K=K, sigma=sigma, T=T, r=r)

    reference_price = float(bs.forward(S0))
    integration_price = float(ni.forward(S0))
    mc_price = float(mc.forward(S0, steps=1_000_000))

    results = pd.DataFrame({
        "Method": [
            "Black-Scholes",
            "Numerical Integration",
            "Monte Carlo",
        ],
        "Option Price": [
            reference_price,
            integration_price,
            mc_price,
        ],
    })

    results["Absolute Error"] = np.abs(
        results["Option Price"] - reference_price
    )

    print(results)

if __name__ == "__main__":
    main()