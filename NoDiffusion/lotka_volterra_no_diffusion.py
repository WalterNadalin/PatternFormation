from matplotlib.pyplot import plot, show, style, legend, xlabel, ylabel
import utils as u
from scipy.integrate import odeint
import numpy as np
import Models as PP

style.use('dark_background')

if __name__ == '__main__':
  # Example taken from the implementation of the Lotka - Volterra model of
  # the numerical analysis course (without diffusion)

  # definition of the parameter
  a, b, c, d = 0.08, -0.004, -0.06, 0.002

  # generation of the model
  PP_system = PP.PredatorPrey(a, b, c, d)

  # computation of time-evolution
  DeltaT = np.linspace(0, 120, 120)  # time instants
  # evolution = odeint(PP_system, [40, 20], DeltaT ) # alternatively
  evolution = u.fe(PP_system, [40, 20], DeltaT)
  # plotting
  plot(np.linspace(0, 120, 120), evolution[:, 0], label = 'Predators')
  plot(np.linspace(0, 120, 120), evolution[:, 1], label='Preys')
  xlabel('Time')
  ylabel('Number of individuals')
  legend()
  show()
