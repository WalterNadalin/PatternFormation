import numpy as np
from tqdm import tqdm

# Forward Euler: to improve with Runge-Kutta or an implicit method eventually
def solve_no_diffusion(model: callable, init: list, t: list):
    '''
    Forward Euler applied to a bidimensional non-linear system of first order
    ordinary differential equations.

    Parameters
    ----------
    f : callable
      Class object of the system considered
      (provided with __call__ method).
    init : int
      Initial conditions of the two variables.
    t : list
      ...

    Returns
    -------
    out : np.array
      ...
    '''
    n = len(t)
    dim = len(init)
    dt = (t[-1] - t[0])/n
    evolution = np.zeros((n, dim))
    evolution[0] = init

    for i in tqdm(range(1, n)):
        evolution[i] = evolution[i - 1] + dt * model(evolution[i - 1], t[i])
    return evolution


def solve_with_diffusion(model: callable, D: list, init: list, t: list, x: list, gamma=[0], STOCHASTICITY=False):
    '''
    ...
    '''
    n, m, dim = len(t), len(x), len(init)
    if STOCHASTICITY:
        assert len(gamma) == dim, "gamma must have length equal to the " \
                                  "number of dimensions"
    rand = np.zeros(dim)
    dt, dx = (t[-1] - t[0])/n, (x[-1] - x[0])/m
    ev = np.zeros((n, m, dim))
    ev[0] = np.array(init).T
    for i in tqdm(range(1, n)):  # for each time instant
        for j in range(1, m - 1):  # for each space point
            if STOCHASTICITY:
                rand = np.random.normal(0, 1, dim)
            ev[i, j] = (ev[i - 1, j] + dt*model(ev[i - 1, j], t[i]) +
                        dt * np.array(D)/dx**2 * np.array(ev[i - 1, j + 1] -
                                                          2 * ev[i - 1, j] +
                                                          ev[i - 1, j - 1])
                        + np.array(gamma) * rand * np.sqrt(dt))
            for k in range(dim):
                ev[i, j, k] = 0 if ev[i, j, k] < 0 else ev[i, j, k]
        # boundary conditions
        ev[i, 0] = ev[i, 1]
        ev[i, -1] = ev[i, -2]

    return ev
