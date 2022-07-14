from numpy import arange, sqrt, zeros, cos, pi
from numpy.random import normal
from tqdm import tqdm

def update(u: list, v: list, i: int, j: int, fu: callable, fv: callable, Du: float, Dv: float, gamma: float, step: float):
    '''
    ...
    '''
    # Numerical solutions of the partial differential equations
    u[j + 1][i] = u[j][i] + step * fu(u[j][i], v[j][i])
    u[j + 1][i] += Du * (u[j][i - 1] - 2 * u[j][i] + u[j][i + 1])
    v[j + 1][i] = v[j][i] + step * fv(u[j][i], v[j][i])
    v[j + 1][i] += Dv * (v[j][i - 1] - 2 * v[j][i] + v[j][i + 1])

    if gamma:
      xi = normal(0, 1, 2) # Normal samples
      u[j + 1][i] += gamma * xi[0] # Stochastic term
      v[j + 1][i] += gamma * xi[1] 

def solve(fu: callable, fv: callable, init: list, time: tuple, domain: tuple, *, \
          Du: float = 0.05, Dv: float = 1, gamma: float = 0.03, step: float = 1e-2, \
          h: float = 2e-1, diffusion: bool = True, stochasticity: bool = True) -> list:
  '''
  ...
  '''
  t, x = arange(time[0], time[1] + step, step), arange(domain[0], domain[1] + h, h)
  n, k = t.shape[0], x.shape[0]
  u, v = zeros((n, k)), zeros((n, k))
  u[0], v[0] = init
  Du *= step / (h ** 2) if diffusion == True else 0
  Dv *= step / (h ** 2) if diffusion == True else 0
  gamma *= sqrt(step) if stochasticity == True else 0

  print('\nSolving the equations...')
  for j in tqdm(range(n - 1)):
    for i in range(1, k - 1):
      # Sometimes we could get something which is similar to zero from the
      # right, we can just put it to 0 to void problem with the square root
      u[j][i] = 0 if u[j][i] < 0 else u[j][i] 
      v[j][i] = 0 if v[j][i] < 0 else v[j][i]
      update(u, v, i, j, fu, fv, Du, Dv, gamma, step)


    # Boundary conditions
    u[j + 1][0], u[j + 1][-1] = u[j + 1][1], u[j + 1][-2]
    v[j + 1][0], v[j + 1][-1] = v[j + 1][1], v[j + 1][-2]

  return t, x, u, v

def generate_init(eps: float, l: float, n: int, *, \
                  c: float = 1, s: float = 1.2, uniform: bool = False) -> tuple:
  '''
  Generates the spatial initial conditions.
  ...
  '''
  u_bar = (s - c) / s
  v_bar = c * sqrt(s - c) / sqrt(s ** 3)

  if uniform:
    return ([u_bar for _ in range(n + 1)], [v_bar for _ in range(n + 1)])

  u_init = [u_bar + eps * cos(2 * pi * l * i / n) for i in range(n + 1)]
  v_init = [v_bar + eps * cos(2 * pi * l * i / n) for i in range(n + 1)]

  return (u_init, v_init)

if __name__ == '__main__':
  c, s = 1, 1.2
  h, n = 2e-1, 200
  eps, l = 0.1, 10
  tau, T = 1e-2, 50
  f = lambda u, v : u * (1 - u) - v * sqrt(u)
  g = lambda u, v : c * v * sqrt(u) - s * v ** 2
  init = generate_init(eps, l, n, c = c, s = s)

  stochasticity = input('Diffusion (True/False): ')
  diffusion = input('Stochasticity (True/False): ')
  t, x, u, v = solve(f, g, init, (0, T), (0, n * h), step = tau, h = h)
