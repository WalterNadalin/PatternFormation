import numpy as np
from tqdm import tqdm

# Forward Euler: to improve with Runge-Kutta or an implicit method eventually
def fe(model: callable, init: list, t: list):
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


def solve(model: callable, D: list, init: list, t: list, x: list):
    '''
    ...
    '''
    n, m, dim = len(t), len(x), len(init)
    dt, dx = (t[-1] - t[0])/n , (x[-1] - x[0])/m
    ev = np.zeros((n, m, dim))
    ev[0] = np.array(init).T
    for i in tqdm(range(1, n)):  # for each time instant
        for j in range(1, m - 1):  # for each space point
            ev[i, j] = (ev[i - 1, j] + dt*model(ev[i - 1, j], t[i]) +
                        dt * np.array(D)/dx**2 * np.array(ev[i - 1, j + 1] -
                                                          2 * ev[i - 1, j] +
                                                          ev[i - 1, j - 1]))
            for k in range(dim):
                ev[i, j, k] = 0 if ev[i, j, k] < 0 else ev[i, j, k]
        # boundary conditions
        ev[i, 0] = ev[i, 1]
        ev[i, -1] = ev[i, -2]

    return ev


def modality(values: list, peaks: list, spacestep: float, length: float):
    '''
    Computed the modality coefficents.
    Parameters
    ----------
    values : list
        ...
    Returns
    -------
    out : list
        ...
    '''
    const = 2 * spacestep * np.pi / length
    n, m = len(values)
    Ck = [[0 for _ in peaks] for _ in values]

    for i in range(n):
        for k in range(len(peaks)):
        temp = const * peaks[k]

        for j in range(m):
            Ck[i][k] += values[i][j] * np.cos(temp * j)

        Ck[i][k] *= spacestep

    return np.array(Ck)

def power(modality: list, timestep: float, length: float):
    '''
    Computes the modality power coefficents given the modality coefficents.
    Parameters
    ----------
    modality : list
        The modality coefficents of which to compute the power.
    timestep : float
        ...
    Returns
    -------
    out : list
        ...
    '''
    n, m = len(modality)
    Wk = [0 for _ in range(m)]

    for j in range(m):
        for i in range(n):
            Wk[j] += modality[i][j] * modality[i][j]

        Wk[j] *= timestep / length

    return np.array(Wk)
