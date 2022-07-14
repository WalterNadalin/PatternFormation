# Routine to simulate the system that uses the `simulate` package

from simulation.solver import solve, generate_init
from simulation.coefficients import modality, power
from simulation.plotting import heat_map, coefficients_plot
from matplotlib.pyplot import show, style, xlabel, ylabel, plot, legend, savefig, close
from numpy import sqrt, linspace, floor

style.use('default')

c, s = 1, 1.2
h, n = 2e-1, 200
eps, l = 0.1, 10
tau, T = 1e-2, 10
f = lambda u, v : u * (1 - u) - v * sqrt(u)
g = lambda u, v : c * v * sqrt(u) - s * v ** 2
init = generate_init(eps, l, n, c = c, s = s)

t, x, u, v = solve(f, g, init, (0, T), (0, n * h), step = tau, h = h)

# Heatmap
heat_map('gigi', (0, n * h), (0, T), u)

# Modality coefficents
peaks = (9, 9.5, 10, 10.5, 11, 11.5, 12)
Ck = modality(u, peaks, h,  n * h)

coefficients_plot('gino', t, Ck, peaks)

# Modality power coefficents
print(power(Ck, tau, T))
