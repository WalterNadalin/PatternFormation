import matplotlib.pyplot as plt
import simulation.utils as u
import numpy as np
import simulation.Models as PP
from seaborn import heatmap


if __name__ == '__main__':
    c, s = 1, 1.2
    h, tau = 0.2, 0.01
    L, T = 40, 200
    DeltaT = [i for i in np.arange(0, T, tau)]  # time instants
    DeltaX = [i for i in np.arange(0, L, h)]  # space points
    PP_system = PP.OtherModel(c, s)
    D = 0.05
    eps, lam, gamma = 0.1, 12, 0.02
    u_init, v_init = PP_system.initial_conditions(eps, lam, L, h)
    ev = u.solve_with_diffusion(PP_system, [D, 1], [u_init, v_init], DeltaT, DeltaX,
                           gamma=[gamma, gamma], STOCHASTICITY=True)

    # Heatmap
    heatmap(ev[:, :, 0], cmap='jet')
    plt.xlabel('Space')
    plt.ylabel('Time')
    plt.show()
