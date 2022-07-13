from numpy import pi, cos, array

def modality(values: list, peaks: list, spacestep: float, length: float) -> list:
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
  const = 2 * spacestep * pi / length
  n, m = values.shape
  Ck = [[0 for _ in peaks] for _ in values]

  for i in range(n):
    for k in range(len(peaks)):
      temp = const * peaks[k]

      for j in range(m):
        Ck[i][k] += values[i][j] * cos(temp * j)

      Ck[i][k] *= spacestep

  return array(Ck)

def power(modality: list, timestep: float, length: float) -> list:
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
  n, m = modality.shape
  Wk = [0 for _ in range(m)]

  for j in range(m):
    for i in range(n):
      Wk[j] += modality[i][j] * modality[i][j]

    Wk[j] *= timestep / length

  return array(Wk)

