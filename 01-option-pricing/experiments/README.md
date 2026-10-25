# Experimental Notebook:  European Option Pricing

This notebook investigates and validates three numerical approaches for pricing European call options: numerical integration, the Black–Scholes closed-form solution, and Monte Carlo simulation.

### Experimental Objectives

1. **Model Comparison:** Compare numerical integration, Black–Scholes analytical pricing, and Monte Carlo estimates under identical market parameters.
2. **Convergence Analysis:** Investigate how Monte Carlo estimation error decreases as the number of simulations increases.
3. **Sensitivity Analysis:** Study the effect of underlying asset price, strike price, volatility, risk-free rate, and time to expiration on option prices.
4. **Error Quantification:** Measure absolute error and relative error between numerical estimates and the Black–Scholes reference price.
5. **Convergence Visualization:** Plot Monte Carlo estimates against simulation count, including the analytical reference price.
6. **Parameter-Space Exploration:** Generate option price curves and surface plots to examine pricing behavior across multiple parameter combinations.
7. **Numerical Stability:** Investigate the effects of floating-point precision, extreme parameter values, and numerical integration tolerances.
8. **Computational Performance:** Benchmark execution time and computational cost across the three pricing methods.
9. **Statistical Reliability:** Examine Monte Carlo estimate variability across independent runs and compare observed errors with theoretical sampling behavior.
10. **Financial Consistency Checks:** Verify properties such as non-negative call prices, upper and lower bounds, and monotonicity with respect to key parameters.

### Expected Outcome

A reproducible experimental comparison of analytical and numerical option pricing methods, supported by quantitative error metrics, visualizations, and computational benchmarks.