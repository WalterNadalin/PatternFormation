# Routine to simulate the system that uses the `simulate` package

import simulation.utils as u
import numpy as np
import simulation.Models as PP
from simulation.plotting import heat_map, coefficients_plot
from simulation.coefficients import modality, power

c, s = 1, 1.2
h, L = 2e-1, 200
tau, T = 1e-2, 10
DeltaT = [i for i in np.arange(0, T, tau)]  # time instants
DeltaX = [i for i in np.arange(0, L, h)]  # space points
PP_system = PP.OtherModel(c, s)

eps, lam, gamma = 0.1, 10, 0.02
D = 0.05
u_init, v_init = PP_system.initial_conditions(eps, lam, L, h)
ev = u.solve_with_diffusion(PP_system, [D, 1], [u_init, v_init], DeltaT, DeltaX,
                           gamma=[gamma, gamma], STOCHASTICITY=True)
# Heatmap
heat_map('gigi', (0, L * h), (0, T), ev[:, :, 0])

# Modality coefficents
peaks = (9, 9.5, 10, 10.5, 11, 11.5, 12)
Ck = modality(ev[:, :, 0], peaks, h,  L * h)

coefficients_plot('gino', DeltaT, Ck, peaks)

# Modality power coefficents
print(power(Ck, tau, T))
