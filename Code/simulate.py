# Routine to simulate the system that uses the `simulate` package
from simulation.solver import solve, generate_init
from simulation.coefficients import modality, power
from simulation.plotting import heat_map, coefficients_plot, confidence_plot
from simulation.analysis import confidence_intervals
from numpy import sqrt, zeros

# Initialization
c, s = 1, 1.2
h, n = 2e-1, 200
eps, l = 0.1, 5
tau, T = 1e-2, 500
f = lambda u, v : u * (1 - u) - v * sqrt(u)
g = lambda u, v : c * v * sqrt(u) - s * v ** 2
init = generate_init(eps, l, n, c = c, s = s, uniform = True)

# Solving the equations
t, x, u, v = solve(f, g, init, (0, T), (0, n * h), Du = 0.13, step = tau, h = h, gamma = 0.02)

# Heatmap
heat_map('heat_map', (0, n * h), (0, T), u)

# Modality coefficents
peaks = (4, 4.5, 5, 5.5, 6)
Ck = modality(u, peaks, h, n * h)

# Coefficents plot
coefficients_plot('modality_coefficents', t, Ck, peaks)

# Modality power coefficents
simulations = 60

gammas = [0.00, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08]
n_peaks, n_gammas = len(peaks), len(gammas)
CIs = zeros((n_gammas, n_peaks, 3))

for j in range(n_gammas):
  Wks = zeros((simulations, n_peaks))

  for i in range(simulations):
    print(f'\nSimulation {j * simulations + i + 1}/{simulations * n_gammas}')
    *_, u, _ = solve(f, g, init, (0, T), (0, n * h), step = tau, gamma = gammas[j], h = h)
    Cks = modality(u, peaks, h, n * h)
    Wks[i] = power(Cks, tau, T)

  CIs[j] = confidence_intervals(Wks, 0.95)

# Power plot
confidence_plot('average_power', CIs, peaks, gammas)
