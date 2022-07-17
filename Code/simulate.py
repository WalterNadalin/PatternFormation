# Routine to simulate the system that uses the `simulate` package
from simulation.solver import solve, generate_init
from simulation.coefficients import modality, power
from simulation.plotting import heat_map, coefficients_plot, confidence_plot
from simulation.analysis import confidence_intervals
from numpy import sqrt, zeros

# Initialization
a, b = 3, 9
Du, Dv = 2, 10
h, n = 2e-1, 200
eps, l = 2, 3
tau, T = 1e-4, 5
f = lambda u, v : a - (b + 1) * u + u ** 2 * v
g = lambda u, v : b * u - u ** 2 * v
init = generate_init(eps, l, n, a = a, b = b, uniform = False)

# Solving the equations
t, x, u, v = solve(f, g, init, (0, T), (0, n * h), Du = Du, Dv = Dv, step = tau, h = h, gamma = 0.02, stochasticity = False)

# Heatmap
heat_map('heat_map', (0, T), (0, n * h), u, x_n = 5, y_n = 3)

# Modality coefficents
peaks = (3, 3.5, 4, 4.5, 5)
Ck = modality(u, peaks, h, n * h)

# Coefficents plot
coefficients_plot('modality_coefficents', t, Ck, peaks)

'''
# Modality power coefficents
simulations = 100

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
'''
