import matplotlib.pyplot as plt
import simulation.utils as u
import numpy as np
import simulation.Models as PP
from seaborn import heatmap

if __name__ == '__main__':
    c, s = 1, 1.2
    h, tau = 0.2, 0.01
    L, T = 40, 400
    DeltaT = [i for i in np.arange(0, T, tau)]  # time instants
    DeltaX = [i for i in np.arange(0, L, h)]  # space points
    PP_system = PP.OtherModel(c, s)

    # SPACE EVOLUTION GRAFICS
    ev_05 = []
    D = 0.05
    for eps, lam in [[0.05, 6.5], [0.1, 4.5], [0.05, 12]]:
        u_init, v_init = PP_system.initial_conditions(eps, lam, L)
        evolution = u.solve_with_diffusion(PP_system, [D, 1], [u_init, v_init], DeltaT, DeltaX)
        ev_05.append(evolution[-1, :, 0])

    ev_1 = []
    D = 0.1
    for eps, lam in [[0.1, 4], [0.1, 5.5], [0.05, 8]]:
        u_init, v_init = PP_system.initial_conditions(eps, lam, L)
        evolution = u.solve_with_diffusion(PP_system, [D, 1], [u_init, v_init], DeltaT, DeltaX)
        ev_1.append(evolution[-1, :, 0])

    plt.plot(ev_05[0], label="epsilon=0.05, lambda=6.5", color="blue")
    plt.plot(ev_05[1], label="epsilon=0.1, lambda=4.5", color="red", linestyle="--")
    plt.plot(ev_05[2], label="epsilon=0.05, lambda=12", color="green", linestyle="--")
    plt.xlabel("x")
    plt.title("D=0.05")
    plt.legend()
    plt.show()
    #plt.savefig("D_005_x.png")

    plt.plot(ev_1[0], label="epsilon=0.1, lambda=4", color="blue")
    plt.plot(ev_1[1], label="epsilon=0.1, lambda=5.5", color="red", linestyle="--")
    plt.plot(ev_1[2], label="epsilon=0.05, lambda=8", color="green", linestyle="--")
    plt.xlabel("x")
    plt.title("D=0.1")
    plt.legend()
    plt.savefig("D_01_x.png")
    plt.show()


    # HEATMAP GRAFICS
    eps, lam = 0.1, 2
    u_init, v_init = PP_system.initial_conditions(eps, lam, L, h)
    D = 0.05
    evolution = u.solve_with_diffusion(PP_system, [D, 1], [u_init, v_init], DeltaT, DeltaX)

    heatmap(evolution[:, :, 0], cmap='jet')
    plt.xlabel('Space')
    plt.ylabel('Time')
    plt.show()

    # MODALITY COEFFICIENTS
    peaks = (8, 9, 10, 11, 12)
    Ck = u.modality(evolution[:, :, 0], peaks, h, L)
    plt.plot(DeltaT, Ck, label=peaks)
    plt.legend()
    plt.show()

    # MODALITY POWER COEFFICIENTS
    print(u.power(Ck, tau, T))


