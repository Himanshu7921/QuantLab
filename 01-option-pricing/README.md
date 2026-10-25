# European Option Pricing from Scratch

A mathematical implementation and experimental comparison of European call option pricing using numerical integration, the Black–Scholes closed-form solution, and Monte Carlo simulation.

## 1. Numerical Integration

Compute the risk-neutral expected discounted payoff by integrating over the standard normal distribution.

$$
C_0=e^{-rT}\int_{-\infty}^{\infty}
\max\left(S_0e^{(r-\frac12\sigma^2)T+\sigma\sqrt{T}z}-K,0\right)
\phi(z)\,dz
$$

where $\phi(z)$ is the standard normal probability density function.

## 2. Black–Scholes Closed-Form Solution

The analytical solution provides a theoretical reference price under the model's assumptions.

$$
d_1=\frac{\ln(S_0/K)+(r+\frac12\sigma^2)T}{\sigma\sqrt{T}}
$$

$$
d_2=d_1-\sigma\sqrt{T}
$$

$$
C_0=S_0N(d_1)-Ke^{-rT}N(d_2)
$$

## 3. Monte Carlo Simulation

Approximate the risk-neutral expected payoff using $M$ independently simulated standard normal random variables $Z_i\sim\mathcal{N}(0,1)$.

$$
\widehat C_0=\frac{e^{-rT}}{M}
\sum_{i=1}^{M}
\max\left(S_0e^{(r-\frac12\sigma^2)T+\sigma\sqrt{T}Z_i}-K,0\right)
$$

## Experimental Objectives

- Compare numerical integration, analytical pricing, and Monte Carlo estimates.
- Investigate Monte Carlo convergence and estimation error.
- Analyze sensitivity to volatility, strike price, and time to expiration.
- Visualize pricing behavior and computational performance.
- Validate numerical results against theoretical properties.

## Model Parameters

| Symbol | Description |
|---|---|
| $S_0$ | Initial underlying asset price |
| $K$ | Strike price |
| $T$ | Time to expiration, in years |
| $r$ | Continuously compounded risk-free rate |
| $\sigma$ | Annualized volatility |
| $N(x)$ | Standard normal cumulative distribution function |
| $M$ | Number of Monte Carlo simulations |

**Assumptions:** European exercise, no dividends, constant volatility, constant risk-free rate, frictionless markets, and geometric Brownian motion under the risk-neutral measure.

**Technology:** Python, NumPy, SciPy, Matplotlib, and PyTorch.

## Results and Experimental Analysis

This section evaluates the numerical behavior, convergence characteristics, and parameter sensitivity of the three European call option pricing methods. All experiments use the Black–Scholes model assumptions, with the analytical solution serving as the reference for numerical validation.

### 1. Pricing Method Comparison

![Comparison of Black-Scholes, Numerical Integration, and Monte Carlo option prices](results/Method%20Comparision.png)

**Objective:** Verify whether all three methods produce consistent option prices under identical parameters.

**Observations:**

- The Black–Scholes closed-form solution provides the analytical reference price.
- Numerical integration evaluates the risk-neutral expected payoff through deterministic quadrature and closely reproduces the analytical result.
- Monte Carlo estimates the same expected payoff using random samples, introducing sampling error.
- In the baseline experiment, the analytical and numerical integration prices are approximately \(10.450584\), while the Monte Carlo estimate is approximately \(10.45618\).

**Analysis:** The agreement between the three methods supports the correctness of the implementations. The small difference in the Monte Carlo estimate is expected because a finite number of random samples only approximates the theoretical expectation.

### 2. Numerical Error Analysis

![Absolute numerical error relative to the Black-Scholes reference](results/Error%20Analysis.png)

**Objective:** Quantify the discrepancy between the numerical methods and the analytical reference.

The absolute error is defined as

$$
E_{\mathrm{abs}}=
\left|\widehat{C}_0-C_{\mathrm{BS}}\right|
$$

where \(\widehat{C}_0\) is the estimated price and \(C_{\mathrm{BS}}\) is the Black–Scholes reference price.

**Observations:**

- Numerical integration exhibits an error close to floating-point and quadrature precision.
- Monte Carlo exhibits a larger error because its estimate depends on a finite random sample.
- The logarithmic vertical axis makes differences across several orders of magnitude visible.

**Analysis:** Numerical integration is highly accurate for this one-dimensional expectation. Monte Carlo trades this deterministic precision for a sampling-based method that generalizes naturally to higher-dimensional problems.

The observed Monte Carlo error is not guaranteed to decrease with every additional simulation batch; convergence is statistical rather than strictly monotonic.

### 3. Monte Carlo Convergence

![Monte Carlo estimate as a function of simulation count](results/Monte%20Carlo%20convergence.png)

**Objective:** Investigate how the number of simulations affects the stability and accuracy of the Monte Carlo estimator.

For \(M\) independent simulations, the estimator is

$$
\widehat{C}_0=
\frac{e^{-rT}}{M}
\sum_{i=1}^{M}
\max(S_T^{(i)}-K,0)
$$

The standard error of the Monte Carlo estimator typically scales as

$$
\operatorname{SE}(\widehat{C}_0)
=
\frac{\sigma_{\mathrm{payoff,disc}}}{\sqrt{M}}
$$

where \(\sigma_{\mathrm{payoff,disc}}\) is the standard deviation of the discounted simulated payoff.

**Observations:**

- Estimates based on very few simulations fluctuate substantially.
- As the simulation count increases, the estimate generally stabilizes around the analytical reference.
- Increasing the sample count reduces typical sampling uncertainty at a rate proportional to \(M^{-1/2}\).

**Analysis:** Reducing the standard error by approximately a factor of two generally requires four times as many simulations. This illustrates the computational cost of improving Monte Carlo precision.

The convergence plot illustrates one realization of the simulation process. It does not, by itself, establish a confidence interval or guarantee monotonic convergence.

### 4. European Call Option Price Surface

![European call option price surface over underlying asset price and volatility](results/option%20price%20surface.png)

**Objective:** Examine how the underlying asset price and volatility jointly affect the theoretical option price.

The price surface is generated by evaluating the Black–Scholes equation over a grid of parameter values:

$$
C_0=C(S_0,\sigma;K,T,r)
$$

**Observations:**

- The call price increases as the underlying asset price increases.
- Greater volatility generally increases the value of a European call option under the model assumptions.
- The surface is nonlinear, particularly around the strike price, where the probability of finishing in the money changes materially.

**Analysis:** The surface reveals interactions between model parameters that are difficult to identify from a single baseline calculation. It also provides a useful foundation for later experiments involving option Greeks and sensitivity analysis.

### 5. Volatility Sensitivity

![European call option price as a function of annualized volatility](results/Volatility%20sensitivity.png)

**Objective:** Measure the sensitivity of the European call price to changes in annualized volatility while keeping the other parameters fixed.

The volatility sensitivity, known as *vega*, is

$$
\frac{\partial C_0}{\partial \sigma}
=
S_0\phi(d_1)\sqrt{T}
$$

where \(\phi\) is the standard normal probability density function.

**Observations:**

- The option price increases with volatility across the displayed parameter range.
- Higher volatility increases the range of possible terminal asset prices.
- For a call option, the additional upside potential increases the value of the right to purchase the asset at the fixed strike price, while the holder's loss remains limited to the premium paid.

**Analysis:** This experiment validates an important qualitative property of the Black–Scholes model. The slope of the price curve represents vega and is not constant across all volatility levels.

### 6. Model Validation Summary

The experiments demonstrate three complementary ways to calculate the same theoretical European call price:

| Method | Numerical approach | Main characteristic |
|---|---|---|
| Black–Scholes | Closed-form analytical solution | Fast reference price |
| Numerical Integration | Deterministic quadrature | High accuracy for this one-dimensional expectation |
| Monte Carlo | Random sampling of terminal payoffs | Sampling error decreases as simulation count increases |

**Overall conclusion:** The analytical and numerical integration results agree closely, while the Monte Carlo estimate approaches the same reference as the number of simulations increases. The sensitivity experiments also reproduce the expected qualitative relationship between call option value, underlying asset price, and volatility.

**Limitations:** These experiments validate the implementations under the assumed Black–Scholes framework. They do not establish that the model accurately predicts traded option prices in real markets, where volatility smiles, transaction costs, discrete dividends, and other market effects may matter.