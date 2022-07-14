from numpy import pi, cos, array
from tqdm import tqdm

def modality(values: list, peaks: list, spacestep: float, length: float) -> list:
  '''
  Computes the modality coefficents.

  Parameters
  ----------
  ...
  '''
  const = 2 * spacestep * pi / length
  n, m = values.shape
  Ck = [[0 for _ in peaks] for _ in values]

  print('\Computing the modality coefficents...')
  for i in tqdm(range(n)):
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
  '''
  n, m = modality.shape
  Wk = [0 for _ in range(m)]

  print('Computing the power modality coefficents...')
  for j in tqdm(range(m)):
    for i in range(n):
      Wk[j] += modality[i][j] * modality[i][j]

    Wk[j] *= timestep / length

  return array(Wk)

