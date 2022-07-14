from numpy import mean, var, array
from scipy.stats import norm


def confidence_interval(measures: list, alpha: float):
  '''
  Computes the confidence interval of a real function computed on a given trajectory.

  Parameters
  ----------
  function : callable
  ...
  '''
  n = measures.shape[0]
  z = norm.ppf((1 + alpha) / 2)
  average = mean(measures)
  variance = var(measures, ddof = 1)
  return average + z * sqrt(variance / N) * array([-1., 1.])
