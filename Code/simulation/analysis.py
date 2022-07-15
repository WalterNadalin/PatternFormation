from numpy import mean, var, array, sqrt, zeros
from scipy.stats import norm

def confidence_intervals(measures: list, alpha: float):
  '''
  Computes the confidence interval of a real function computed on a given trajectory.

  Parameters
  ----------
  function : callable
  ...
  '''
  n, m = measures.shape
  z = norm.ppf((1 + alpha) / 2)
  result = zeros((m, 3))
  averages = mean(measures, axis = 0)
  variances = var(measures, ddof = 1, axis = 0)

  for i in range(m):
    average = averages[i]
    term = z * sqrt(variances[i] / n)
    result[i] = array([average - term, average, average + term])

  return result
