from numpy import arange, sqrt, array, ones, diag, fill_diagonal, identity, zeros, cos, pi, linspace, append
from matplotlib.pyplot import plot, show, style, legend, xlabel, ylabel, imshow
from seaborn import heatmap

style.use('dark_background')

def solve(f: callable, g: callable, alpha: float, beta: float, init: list, time: list, step: float, domain: list, h: int) -> list:
  '''
  ...
  '''
  t, x = arange(time[0], time[1] + step, step), arange(domain[0], domain[1] + h, h)
  n, k = t.shape[0], x.shape[0]
  u, v = zeros((n, k)), zeros((n, k))
  u[0], v[0] = init
  alpha *= step / (h ** 2)
  beta *= step / (h ** 2)

  for j in range(n - 1):
    for i in range(1, k - 1):
      u[j][i] = 0 if u[j][i] < 0 else u[j][i]
      v[j][i] = 0 if v[j][i] < 0 else v[j][i]
      u[j + 1][i] = u[j][i] + step * f(u[j][i], v[j][i])
      u[j + 1][i] += alpha * (u[j][i - 1] - 2 * u[j][i] + u[j][i + 1])
      v[j + 1][i] = v[j][i] + step * g(u[j][i], v[j][i])
      v[j + 1][i] += beta * (v[j][i - 1] - 2 * v[j][i] + v[j][i + 1])

    u[j + 1][0], u[j + 1][-1] = u[j + 1][1], u[j + 1][-2]
    v[j + 1][0], v[j + 1][-1] = v[j + 1][1], v[j + 1][-2]

  return t, x, u, v

if __name__ == '__main__':
  D = 0.05
  c = 1
  s = 1.2
  tau = 1e-3
  h = 2e-1
  n = 200
  eps = 0.1
  l = 2
  f = lambda u, v : u * (1 - u) - v * sqrt(u)
  g = lambda u, v : c * v * sqrt(u) - s * v ** 2
  u_bar = (s - c) / s
  v_bar = c * sqrt(s - c) / sqrt(s ** 3)
  u_init = [u_bar + eps * cos(2 * pi * l * i / n) for i in range(n + 1)]
  v_init = [v_bar + eps * cos(2 * pi * l * i / n) for i in range(n + 1)]

  t, x, u, v = solve(f, g, D, 1, (u_init, v_init), (0, 300), tau, (0, n * h), h)

  heatmap(u, cmap = 'jet')
  xlabel('Space')
  ylabel('Time')
  show()
