# QuantLab

**A mathematical laboratory for quantitative finance, numerical methods, and computational modelling.**

QuantLab is an open-source collection of quantitative projects exploring the mathematical foundations of financial models through first-principles implementations, numerical experiments, simulation, and visualization.

The objective is to understand not only how a model works, but also why its mathematics is valid, how it can be implemented computationally, and how its theoretical properties behave under experimentation.

**Maintainer & Developer:** Himanshu Singh

---

## Mathematical Foundations

QuantLab begins with the mathematical formulation of a problem and implements multiple approaches to solving it. The first project investigates European call option pricing using analytical mathematics, deterministic numerical integration, and stochastic simulation.

### 1. Black–Scholes Closed-Form Solution

Under the Black–Scholes assumptions, the price of a European call option is

$$
C_0=S_0N(d_1)-Ke^{-rT}N(d_2)
$$

where

$$
d_1=
\frac{\ln(S_0/K)+(r+\frac{1}{2}\sigma^2)T}
{\sigma\sqrt{T}}
$$

$$
d_2=d_1-\sigma\sqrt{T}
$$

Here, \(N(x)\) denotes the standard normal cumulative distribution function. This analytical solution serves as the reference price for validating the numerical methods.

### 2. Numerical Integration

The option price can also be expressed as the discounted risk-neutral expectation of its terminal payoff:

$$
C_0=e^{-rT}\int_{-\infty}^{\infty}
\max\left(
S_0e^{(r-\frac12\sigma^2)T+\sigma\sqrt{T}z}-K,
0
\right)\phi(z)\,dz
$$

where

$$
\phi(z)=\frac{1}{\sqrt{2\pi}}e^{-z^2/2}
$$

The integral is evaluated numerically using deterministic quadrature. This provides an independent computational validation of the closed-form solution.

### 3. Monte Carlo Simulation

Monte Carlo estimates the same risk-neutral expectation using independently sampled standard normal random variables:

$$
Z_i\overset{\mathrm{i.i.d.}}{\sim}\mathcal{N}(0,1)
$$

The simulated terminal asset price is

$$
S_T^{(i)}=S_0
\exp\left[
\left(r-\frac{\sigma^2}{2}\right)T
+\sigma\sqrt{T}Z_i
\right]
$$

The resulting option price estimate is

$$
\widehat C_0=
\frac{e^{-rT}}{M}
\sum_{i=1}^{M}\max(S_T^{(i)}-K,0)
$$

For independent samples with finite payoff variance, the estimator converges to the theoretical price as \(M\to\infty\), with standard error proportional to \(M^{-1/2}\).

---

## Project Portfolio

| Project | Focus | Status |
|---|---|---|
| [01 — European Option Pricing](01-option-pricing/README.md) | Analytical pricing, numerical integration, Monte Carlo simulation, and experimental validation | Implemented; experiments ongoing |
| Future projects | Portfolio optimization, time-series modelling, statistical arbitrage, and other quantitative methods | Planned |

The portfolio will expand as additional mathematical models and computational experiments are implemented.

---

# European Option Pricing

**Project 01 — European Call Option Pricing from Scratch**

This project implements three approaches to pricing European call options and compares their outputs under identical model assumptions.

The purpose is to investigate the relationship between analytical solutions, numerical approximation, and stochastic estimation, supported by reproducible experiments and visual analysis.

## Methods Implemented

| Method | Implementation | Purpose |
|---|---|---|
| Black–Scholes | Closed-form equation | Analytical reference price |
| Numerical Integration | SciPy quadrature | Deterministic integration of the expected payoff |
| Monte Carlo | NumPy vectorized simulation | Stochastic estimation of the expected payoff |

All three methods calculate the same theoretical quantity. Their differences arise from their computational approaches rather than different financial models.


## Model Parameters

| Symbol | Description |
|:---|:---|
| S₀ | Initial underlying asset price |
| K | Option strike price |
| T | Time to expiration, in years |
| r | Continuously compounded risk-free interest rate |
| σ | Annualized volatility |
| M | Number of Monte Carlo simulations |
| N(x) | Standard normal cumulative distribution function |
| φ(x) | Standard normal probability density function |


### Model Assumptions

The implementation assumes European exercise, no dividends, constant volatility, a constant risk-free interest rate, frictionless markets, and geometric Brownian motion for the underlying asset under the risk-neutral measure.

These assumptions define the mathematical model; real market option prices may deviate from its theoretical predictions.

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/Himanshu7921/QuantLab.git
cd QuantLab
pip install numpy scipy pandas matplotlib seaborn
```

## Usage

### 1. Black–Scholes

```python
from src.black_scholes import BlackScholesCall

model = BlackScholesCall(
    K=100.0,
    sigma=0.20,
    T=1.0,
    r=0.05,
)

price = model.forward(S0=100.0)

print(f"Call price: {price:.6f}")
```

Expected output:

```text
Call price: 10.450584
```

### 2. Numerical Integration

```python
from src.numerical_integration import NumericalIntegrationCall

model = NumericalIntegrationCall(
    K=100.0,
    sigma=0.20,
    T=1.0,
    r=0.05,
)

price = model.forward(S0=100.0)

print(f"Call price: {price:.6f}")
```

Numerical integration should reproduce the analytical result to within numerical integration and floating-point error for this example.

### 3. Monte Carlo

```python
from src.monte_carlo import MonteCarloCall

model = MonteCarloCall(
    K=100.0,
    sigma=0.20,
    T=1.0,
    r=0.05,
)

price = model.forward(
    S0=100.0,
    steps=1_000_000,
)

print(f"Monte Carlo price: {price:.6f}")
```

The result will generally differ slightly between runs unless the random number generator is seeded. With sufficiently many simulations, the estimate should approach the analytical price.

**Note:** These imports are illustrative until the module filenames are finalized. The examples assume the classes can be imported from the project root and that the `QuantLab` base class is available.

---

## Experimental Results

The experiments investigate model agreement, numerical error, Monte Carlo convergence, and parameter sensitivity.

All figures below are stored in `01-option-pricing/results/` and are linked relative to the repository root.

### 1. Pricing Method Comparison

![Black–Scholes, Numerical Integration, and Monte Carlo price comparison](01-option-pricing/results/Method%20Comparision.png)

**Objective:** Verify that all three implementations return consistent option prices.

The Black–Scholes closed-form solution provides the reference value. Numerical integration should closely match it, while Monte Carlo introduces sampling error because it estimates the expected payoff from a finite number of simulations.

For the baseline configuration \(S_0=100\), \(K=100\), \(T=1\), \(r=0.05\), and \(\sigma=0.20\), the analytical price is approximately \(10.450584\).

**Interpretation:** Agreement between the methods supports the consistency of their implementations under the assumed model.

### 2. Numerical Error Analysis

![Absolute numerical error relative to Black–Scholes](01-option-pricing/results/Error%20Analysis.png)

**Objective:** Quantify deviations from the analytical reference.

The absolute error is

$$
E_{\mathrm{abs}}=
\left|\widehat C_0-C_{\mathrm{BS}}\right|
$$

Numerical integration exhibits very small error for this one-dimensional integral. Monte Carlo error is typically larger because of random sampling.

**Interpretation:** The comparison demonstrates the difference between deterministic quadrature accuracy and stochastic estimation uncertainty. The observed errors depend on numerical tolerances, floating-point precision, and the particular Monte Carlo sample.

### 3. Monte Carlo Convergence

![Monte Carlo convergence as simulation count increases](01-option-pricing/results/Monte%20Carlo%20convergence.png)

**Objective:** Study the relationship between simulation count and estimation stability.

The estimator's standard error decreases proportionally to \(1/\sqrt{M}\), assuming independent samples and finite payoff variance.

**Interpretation:** Larger simulation counts generally produce more stable estimates, but convergence is not necessarily monotonic. Reducing typical sampling error by half requires approximately four times as many simulations.

### 4. European Call Option Price Surface

![European call option price surface across underlying price and volatility](01-option-pricing/results/option%20price%20surface.png)

**Objective:** Visualize the joint effect of underlying asset price and volatility on the theoretical call price.

The surface evaluates

$$
C_0=C(S_0,\sigma;K,T,r)
$$

over a grid of underlying prices and volatility levels.

**Interpretation:** The option price increases with the underlying asset price and is non-decreasing in volatility under the model assumptions. The surface reveals the nonlinear structure of option valuation across parameter combinations.

### 5. Volatility Sensitivity

![European call price versus annualized volatility](01-option-pricing/results/Volatility%20sensitivity.png)

**Objective:** Measure how the option price changes as volatility varies while the other parameters remain fixed.

The sensitivity of the call price to volatility is known as vega:

$$
\frac{\partial C_0}{\partial \sigma}
=S_0\phi(d_1)\sqrt{T}
$$

**Interpretation:** Greater volatility increases the value of the right to purchase the underlying asset at the fixed strike price, under the standard Black–Scholes assumptions.

### 6. Experimental Conclusions

The experiments demonstrate that:

- The analytical solution and numerical integration produce consistent prices.
- Monte Carlo approximates the same expected payoff and exhibits sampling variability.
- Increasing the simulation count generally improves estimation precision.
- The call price responds systematically to changes in underlying asset price and volatility.
- Numerical validation and sensitivity analysis help identify implementation errors and verify theoretical properties.

These results validate the computational implementations under the specified assumptions. They do not establish that Black–Scholes accurately predicts real market quotes, where effects such as volatility smiles, transaction costs, and discrete dividends may be relevant.

---

## Repository Structure

```text
QuantLab/
├── README.md
├── 01-option-pricing/
│   ├── README.md
│   ├── math formulation/
│   ├── experiments/
│   ├── results/
│   │   ├── Error Analysis.png
│   │   ├── Method Comparison.png
│   │   ├── Model agreement.png
│   │   ├── Monte Carlo convergence.png
│   │   ├── option price surface.png
│   │   └── Volatility sensitivity.png
│   └── src/
└── LICENSE
```

This is a conceptual overview of the current project layout. Exact source filenames and additional files may differ as development continues.

## Development Philosophy

QuantLab follows a mathematics-first approach:

1. Formulate the problem mathematically.
2. Derive or identify the governing equations.
3. Implement the methods from first principles where practical.
4. Validate outputs against analytical results or independent numerical methods.
5. Design experiments to test convergence, sensitivity, and computational performance.
6. Document observations, assumptions, and limitations.

The objective is not merely to produce a numerical answer, but to understand why the result is valid and when the underlying assumptions matter.

## Ownership and Open Source

QuantLab is owned, maintained, and developed by **Himanshu Singh**.

The repository is intended to be open source, enabling others to study the implementations, reproduce the experiments, suggest improvements, and contribute additional quantitative projects.

Contributions, mathematical corrections, bug reports, and suggestions for new experiments are welcome.

---

*QuantLab — Mathematics, Models, and Experiments in Quantitative Finance.*