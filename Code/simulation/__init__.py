__all__ = ['solver', 'analysis', 'coefficents', 'plotting']

from .solver import solve, generate_init
from .analysis import confidence_interval
from .coefficients import power, modality
from .plotting import heat_map
