from numpy import pi, cos

def compute(values: list, peaks: list, spacestep: float, length: float) -> list:
  const = 2 * pi / length
  n, m = values.shape
  Ck = [[0 for _ in peaks] for _ in values]
  x = lambda i : spacestep * i

  for i in range(n):
    for k in range(len(peaks)):
      Ck[i][k] = sum([values[i][j] * cos(const *  x(j) * peaks[k]) * spacestep for j in range(m)])

  return Ck
