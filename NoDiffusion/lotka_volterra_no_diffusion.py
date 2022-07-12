from numpy import zeros, arange
from matplotlib.pyplot import plot, show, style, legend, xlabel, ylabel

style.use('dark_background')


# Forward Euler: to improve with Runge-Kutta or an implicit method eventually
def fe(f: callable, g: callable, init: list, begin: float, end: float, step: float) -> list:
  '''
  Forward Euler applied to a bidimensional non-linear system of first order
  ordinary differential equations.

  Parameters
  ----------
  f : callable
    Forcing term of the first variable.
  g : callable
    Forcing term of the second variable.
  init : int
    Initial conditions of the two variables.
  begin : float
    ...

  Returns
  -------
  out : list, list, list
    ...
  '''
  timesteps = arange(begin, end, step)
  n = timesteps.shape[0]
  u = zeros(n)
  v = zeros(n)
  u[0], v[0] = init

  for i in range(1, n):
    u[i] = u[i - 1] + step * f(u[i - 1], v[i - 1])
    v[i] = v[i - 1] + step * g(u[i - 1], v[i - 1])

  return u, v, timesteps

if __name__ == '__main__':
  # Example taken from the implementation of the Lotka - Volterra model of
  # the numerical analysis course (without diffusion)
  a, b, c, d = 0.08, -0.004, -0.06, 0.002
  f = lambda u, v : a * u + b * u * v
  g = lambda u, v : c * v + d * u * v

  u, v, time = fe(f, g, (40, 20), 0, 120, 0.5)
  plot(time, u, label = 'Preys')
  plot(time, v, label = 'Predators')
  xlabel('Time')
  ylabel('Number of individuals')
  legend()
  show()
